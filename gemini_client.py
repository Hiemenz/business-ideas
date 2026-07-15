import os
import re
import json
import requests
from dotenv import load_dotenv
from tenacity import retry, wait_exponential, stop_after_attempt

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL   = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")


@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=2, min=4, max=60))
def call_gemini(prompt, max_tokens=1024, temperature=0.85):
    resp = requests.post(
        f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent",
        params={"key": GEMINI_API_KEY},
        headers={"Content-Type": "application/json"},
        json={
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "temperature":     temperature,
                "maxOutputTokens": max_tokens,
            },
        },
    )
    resp.raise_for_status()
    data = resp.json()
    candidates = data.get("candidates", [])
    if not candidates:
        raise ValueError(f"Gemini returned no candidates. Response: {data}")
    return candidates[0]["content"]["parts"][0]["text"].strip()


@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=2, min=4, max=60))
def embed_text(text):
    resp = requests.post(
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-001:embedContent",
        params={"key": GEMINI_API_KEY},
        headers={"Content-Type": "application/json"},
        json={"content": {"parts": [{"text": text}]}},
    )
    resp.raise_for_status()
    return resp.json()["embedding"]["values"]


def build_prompt(combo, trends, reddit_ideas, arxiv_papers):
    return (
        f"Generate an original business idea using these parameters:\n"
        f"Platform: {combo['platform']} | Audience: {combo['audience']} | Problem: {combo['problem']}\n"
        f"Industry: {combo['industry']} | Tech: {combo['technology']} | Model: {combo['business_model']} | Monetization: {combo['monetization']}\n\n"
        f"Trends:\n{trends}\n\n"
        f"Reddit signals:\n{reddit_ideas}\n\n"
        f"arXiv research:\n{arxiv_papers}\n\n"
        "Combine signals into an original idea (do not restate existing content).\n\n"
        "## Business Idea\n[Name + 2-sentence description]\n\n"
        "## Research Insight\n[Which paper/trend inspired this and what problem it solves]\n\n"
        "## Outline\n- Core functionality\n- Who benefits\n- 3-5 key features\n- Tech stack\n- Unique advantage\n\n"
        "## Revenue Feasibility\n- Revenue streams\n- Market size\n- Monthly revenue (early/scaled)\n- Key risks\n- Time-to-first-revenue\n"
    )


def score_ideas(ideas):
    """Score all ideas in a single Gemini call. Returns list of score dicts or None on failure."""
    ideas_text = "\n---\n".join(f"[{i+1}] {t[:300]}" for i, t in enumerate(ideas))
    prompt = (
        f"Score {len(ideas)} business ideas (1-10 each):\n"
        "market_size, feasibility, novelty, competition (10=low competition)\n"
        "Return ONLY compact JSON array:\n"
        '[{"market_size":7,"feasibility":8,"novelty":6,"competition":5},...]\n\n'
        f"{ideas_text}"
    )
    raw = call_gemini(prompt, max_tokens=256, temperature=0.2)
    raw = re.sub(r"```(?:json)?\s*", "", raw).strip()
    raw = raw.rstrip("`").strip()
    try:
        start = raw.index("[")
        end   = raw.rindex("]") + 1
        return json.loads(raw[start:end])
    except (ValueError, json.JSONDecodeError) as e:
        print(f"  Failed to parse scores from Gemini: {e}")
        print(f"  Raw response: {raw[:300]}")
        return None
