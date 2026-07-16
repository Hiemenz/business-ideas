import logging
import os
import re
import json
import time
import threading

import requests
from dotenv import load_dotenv
from tenacity import retry, wait_exponential, stop_after_attempt

load_dotenv()

logger = logging.getLogger(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# gemini-2.0-flash free-tier quota was retired (limit: 0) — 2.5-flash is current
GEMINI_MODEL   = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
EMBED_MODEL    = "gemini-embedding-001"

REQUEST_TIMEOUT = 60  # seconds

# ==== RATE LIMITER ====
# Shared across call_gemini and embed_text so the free-tier RPM cap applies
# to every Gemini request, not just text generation.
_throttle_lock = threading.Lock()
_last_call = 0.0
_min_interval = 60.0 / float(os.getenv("GEMINI_RPM_LIMIT", "14"))


def set_rpm_limit(rpm):
    """Override the requests-per-minute cap (e.g. from config.yml settings)."""
    global _min_interval
    _min_interval = 60.0 / float(rpm)


def _throttle():
    global _last_call
    with _throttle_lock:
        elapsed = time.monotonic() - _last_call
        if elapsed < _min_interval:
            time.sleep(_min_interval - elapsed)
        _last_call = time.monotonic()


@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=2, min=4, max=60))
def call_gemini(prompt, max_tokens=1024, temperature=0.85):
    _throttle()
    resp = requests.post(
        f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent",
        params={"key": GEMINI_API_KEY},
        headers={"Content-Type": "application/json"},
        json={
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "temperature":     temperature,
                "maxOutputTokens": max_tokens,
                # 2.5-series models spend "thinking" tokens out of the same
                # budget — with small max_tokens the visible answer starves.
                # These are formatting/copy tasks; thinking adds nothing.
                "thinkingConfig":  {"thinkingBudget": 0},
            },
        },
        timeout=REQUEST_TIMEOUT,
    )
    resp.raise_for_status()
    data = resp.json()
    candidates = data.get("candidates", [])
    if not candidates:
        raise ValueError(f"Gemini returned no candidates. Response: {data}")
    parts = candidates[0].get("content", {}).get("parts", [])
    text = "".join(p.get("text", "") for p in parts if not p.get("thought")).strip()
    if not text:
        raise ValueError(f"Gemini returned no text (finishReason="
                         f"{candidates[0].get('finishReason')}). Raise max_tokens?")
    return text


@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=2, min=4, max=60))
def embed_text(text):
    _throttle()
    resp = requests.post(
        f"https://generativelanguage.googleapis.com/v1beta/models/{EMBED_MODEL}:embedContent",
        params={"key": GEMINI_API_KEY},
        headers={"Content-Type": "application/json"},
        json={"content": {"parts": [{"text": text}]}},
        timeout=REQUEST_TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json()["embedding"]["values"]


def parse_json_block(raw):
    """Extract the first JSON array or object from an LLM response."""
    raw = re.sub(r"```(?:json)?\s*", "", raw).strip()
    raw = raw.rstrip("`").strip()
    starts = [i for i in (raw.find("["), raw.find("{")) if i != -1]
    if not starts:
        raise ValueError(f"No JSON found in response: {raw[:200]}")
    start = min(starts)
    end = raw.rindex("]" if raw[start] == "[" else "}") + 1
    return json.loads(raw[start:end])


def build_prompt(combo, trends, reddit_ideas, arxiv_papers, outcome_feedback=""):
    feedback_block = (
        f"Lessons from previously pursued ideas (avoid repeating failures, "
        f"lean toward what worked):\n{outcome_feedback}\n\n"
    ) if outcome_feedback else ""
    return (
        f"Generate an original business idea using these parameters:\n"
        f"Platform: {combo['platform']} | Audience: {combo['audience']} | Problem: {combo['problem']}\n"
        f"Industry: {combo['industry']} | Tech: {combo['technology']} | Model: {combo['business_model']} | Monetization: {combo['monetization']}\n\n"
        f"Trends:\n{trends}\n\n"
        f"Reddit signals:\n{reddit_ideas}\n\n"
        f"arXiv research:\n{arxiv_papers}\n\n"
        f"{feedback_block}"
        "Combine signals into an original idea (do not restate existing content).\n\n"
        "## Business Idea\n[Name + 2-sentence description]\n\n"
        "## Research Insight\n[Which paper/trend inspired this and what problem it solves]\n\n"
        "## Outline\n- Core functionality\n- Who benefits\n- 3-5 key features\n- Tech stack\n- Unique advantage\n\n"
        "## Revenue Feasibility\n- Revenue streams\n- Market size\n- Monthly revenue (early/scaled)\n- Key risks\n- Time-to-first-revenue\n"
    )


SCORE_KEYS = ("market_size", "feasibility", "novelty", "competition")


def _clean_scores(parsed, expected):
    """Validate/coerce the parsed score list. Bad entries become None."""
    if not isinstance(parsed, list):
        return [None] * expected
    cleaned = []
    for item in parsed[:expected]:
        if isinstance(item, dict) and all(isinstance(item.get(k), (int, float)) for k in SCORE_KEYS):
            cleaned.append({k: float(item[k]) for k in SCORE_KEYS})
        else:
            cleaned.append(None)
    cleaned += [None] * (expected - len(cleaned))
    return cleaned


def score_ideas(ideas, max_retries=1):
    """Score ideas via Gemini. Returns a list the same length as `ideas`;
    entries are score dicts, or None where scoring failed. Missing/invalid
    scores are retried individually up to `max_retries` times."""
    def ask(batch):
        ideas_text = "\n---\n".join(f"[{i+1}] {t[:300]}" for i, t in enumerate(batch))
        prompt = (
            f"Score {len(batch)} business ideas (1-10 each):\n"
            "market_size, feasibility, novelty, competition (10=low competition)\n"
            "Return ONLY compact JSON array:\n"
            '[{"market_size":7,"feasibility":8,"novelty":6,"competition":5},...]\n\n'
            f"{ideas_text}"
        )
        raw = call_gemini(prompt, max_tokens=max(256, 64 * len(batch)), temperature=0.2)
        try:
            return _clean_scores(parse_json_block(raw), len(batch))
        except (ValueError, json.JSONDecodeError) as e:
            logger.warning("Failed to parse scores from Gemini: %s", e)
            return [None] * len(batch)

    scores = ask(ideas)

    # Retry only the ideas that came back missing or malformed
    for _ in range(max_retries):
        missing = [i for i, s in enumerate(scores) if s is None]
        if not missing:
            break
        logger.info("Retrying scoring for %d idea(s)...", len(missing))
        retried = ask([ideas[i] for i in missing])
        for idx, s in zip(missing, retried):
            scores[idx] = s

    return scores


def composite_score(score):
    """Average the four sub-scores into one 0-10 composite."""
    return round(sum(score[k] for k in SCORE_KEYS) / len(SCORE_KEYS), 1)
