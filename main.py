import os
import json
import random
import hashlib
from datetime import datetime
import pickle
from pathlib import Path
import time

import numpy as np
import pandas as pd
import requests
import yaml
from dotenv import load_dotenv
from tenacity import retry, wait_exponential, stop_after_attempt

from trends import fetch_trends, fetch_reddit_ideas, fetch_arxiv_papers
from gemini_client import build_prompt, score_ideas

load_dotenv()

# ==== CONFIGURATION ====
LOG_PATH             = Path("money_making_ideas_log.parquet")
YAML_PATH            = Path("config.yml")
EMBEDDING_PATH        = Path("embeddings.pkl")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL   = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")

if not GEMINI_API_KEY:
    raise SystemExit("GEMINI_API_KEY environment variable is not set.")

# ==== LOAD YAML CONFIG ====
with open(YAML_PATH) as f:
    config = yaml.safe_load(f)

settings             = config.get("settings", {})
BATCH_SIZE           = settings.get("batch_size", 5)
SCORE_THRESHOLD      = settings.get("score_threshold", 6.0)
SIMILARITY_THRESHOLD = settings.get("similarity_threshold", 0.85)
ROTATION_WINDOW      = settings.get("rotation_window", 30)
GEMINI_RPM_LIMIT     = settings.get("gemini_rpm_limit", 14)
TREND_CACHE_TTL_HOURS = settings.get("trend_cache_ttl_hours", 24)

industries     = config["industries"]
business_models = config["business_models"]
audiences      = config["audiences"]
technologies   = config["technologies"]
problems       = config["problems"]
platforms      = config["platforms"]
monetization   = config["monetization"]
subreddits     = config.get("subreddits", [])

# ==== LOAD & MIGRATE LOG ====
# New columns have defaults so existing parquet files upgrade automatically.
DEFAULTS = {
    "idea": "", "industry": "", "business_model": "", "hash": "",
    "score": 0.0, "market_size": 0, "feasibility": 0,
    "novelty": 0, "competition": 0, "trend_context": "",
    "displayed": False, "timestamp": "",
}

if LOG_PATH.exists():
    log_df = pd.read_parquet(LOG_PATH)
    for col, default in DEFAULTS.items():
        if col not in log_df.columns:
            log_df[col] = default
    used_industries = log_df["industry"].tolist()[-ROTATION_WINDOW:]
    used_models     = log_df["business_model"].tolist()[-ROTATION_WINDOW:]
else:
    log_df          = pd.DataFrame(columns=DEFAULTS.keys())
    used_industries = []
    used_models     = []

# Load persisted idea embeddings for semantic dedup
if EMBEDDING_PATH.exists():
    with open(EMBEDDING_PATH, "rb") as f:
        stored_embeddings = pickle.load(f)
else:
    stored_embeddings = {}

# Migrate old flat-list format to versioned dict format
for k, v in list(stored_embeddings.items()):
    if isinstance(v, list):
        stored_embeddings[k] = {"model": "gemini-embedding-001", "vec": v}


# ==== TREND CACHE ====
TREND_CACHE_PATH = Path("trends_cache.json")

def load_trend_cache():
    if not TREND_CACHE_PATH.exists():
        return {}
    try:
        with open(TREND_CACHE_PATH) as f:
            raw = json.load(f)
        cutoff = datetime.now().timestamp() - TREND_CACHE_TTL_HOURS * 3600
        return {k: v for k, v in raw.items() if v.get("ts", 0) > cutoff}
    except Exception:
        return {}

def save_trend_cache(cache):
    with open(TREND_CACHE_PATH, "w") as f:
        json.dump(cache, f)

trends_cache = load_trend_cache()


# ==== ADAPTIVE RATE LIMITER ====
_last_gemini_call = 0.0
_MIN_GEMINI_INTERVAL = 60.0 / GEMINI_RPM_LIMIT  # seconds between calls

def gemini_throttle():
    global _last_gemini_call
    elapsed = time.monotonic() - _last_gemini_call
    if elapsed < _MIN_GEMINI_INTERVAL:
        time.sleep(_MIN_GEMINI_INTERVAL - elapsed)
    _last_gemini_call = time.monotonic()


# ==== HELPERS ====
@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=2, min=4, max=60))
def call_gemini(prompt, max_tokens=1024, temperature=0.85):
    gemini_throttle()
    resp = requests.post(
        f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent",
        params={"key": GEMINI_API_KEY},
        headers={"Content-Type": "application/json"},
        json={
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "temperature":   temperature,
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


def pick_combo():
    """Pick a random parameter combo, avoiding recently used industries/models."""
    avail_industries = [i for i in industries if i not in used_industries]
    avail_models     = [m for m in business_models if m not in used_models]
    return {
        "industry":      random.choice(avail_industries or industries),
        "business_model": random.choice(avail_models or business_models),
        "audience":      random.choice(audiences),
        "technology":    random.choice(technologies),
        "problem":       random.choice(problems),
        "platform":      random.choice(platforms),
        "monetization":  random.choice(monetization),
    }


@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=2, min=4, max=60))
def embed_text(text):
    """Embed a single text via Gemini gemini-embedding-001."""
    resp = requests.post(
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-001:embedContent",
        params={"key": GEMINI_API_KEY},
        headers={"Content-Type": "application/json"},
        json={"content": {"parts": [{"text": text}]}},
    )
    resp.raise_for_status()
    return resp.json()["embedding"]["values"]


def is_duplicate(embedding, model="gemini-embedding-001"):
    """True if this embedding is too close to any previously seen idea (cosine sim)."""
    matching = {k: v for k, v in stored_embeddings.items()
                if isinstance(v, dict) and v.get("model") == model}
    if not matching:
        return False
    stored_vecs = np.array([v["vec"] for v in matching.values()])
    vec         = np.array(embedding)
    sims        = (stored_vecs @ vec) / (np.linalg.norm(stored_vecs, axis=1) * np.linalg.norm(vec))
    return float(sims.max()) > SIMILARITY_THRESHOLD


def main():
    # ==== MAIN: generate batch ====
    print(f"\nGenerating {BATCH_SIZE} ideas...\n")

    ideas, combos = [], []

    # Reddit context is the same for every idea in the batch — fetch once
    print("  Fetching Reddit ideas...")
    reddit_ideas = fetch_reddit_ideas(subreddits, posts_per_sub=settings.get("posts_per_sub", 3)) if subreddits else "No subreddits configured."

    arxiv_cache = {}                              # cache arXiv results per industry

    for i in range(BATCH_SIZE):
        combo    = pick_combo()
        industry = combo["industry"]

        if industry not in trends_cache:
            print(f"  Fetching trends for {industry}...")
            trends_cache[industry] = {"text": fetch_trends(industry), "ts": datetime.now().timestamp()}

        if industry not in arxiv_cache:
            print(f"  Fetching arXiv papers for {industry}...")
            arxiv_cache[industry] = fetch_arxiv_papers(industry, max_results=settings.get("arxiv_max_results", 5))

        try:
            idea_text  = call_gemini(build_prompt(combo, trends_cache[industry]["text"], reddit_ideas, arxiv_cache[industry]))
            embedding  = embed_text(idea_text)
        except Exception as e:
            print(f"  [{i+1}/{BATCH_SIZE}] Skipped — API error: {e}")
            continue

        if is_duplicate(embedding):
            print(f"  [{i+1}/{BATCH_SIZE}] Skipped — too similar to an existing idea")
            continue

        ideas.append(idea_text)
        combos.append(combo)
        # Store immediately so later ideas in this batch can't duplicate each other
        stored_embeddings[hashlib.md5(idea_text.encode()).hexdigest()] = {
            "model": "gemini-embedding-001",
            "vec": embedding,
        }
        print(f"  [{i+1}/{BATCH_SIZE}] Generated")

    # ==== SCORE & LOG ====
    if not ideas:
        print("\nNo unique ideas generated this run.")
    else:
        print(f"\nScoring {len(ideas)} idea(s)...")
        scores = score_ideas(ideas)

        if scores is None:
            print("Scoring failed — ideas not logged.")
        else:
            if len(scores) != len(ideas):
                print(f"  WARNING: got {len(scores)} scores for {len(ideas)} ideas — {len(ideas) - len(scores)} idea(s) will be dropped silently")
            new_rows = []
            for idea, combo, score in zip(ideas, combos, scores):
                composite = round(
                    (score["market_size"] + score["feasibility"] +
                     score["novelty"]     + score["competition"]) / 4, 1
                )
                kept = composite >= SCORE_THRESHOLD
                print(f"  Score: {composite}/10 — {'kept' if kept else 'filtered out'}")

                if kept:
                    new_rows.append({
                        "idea":           idea,
                        "industry":       combo["industry"],
                        "business_model": combo["business_model"],
                        "hash":           hashlib.md5(idea.encode()).hexdigest(),
                        "score":          composite,
                        "market_size":    score["market_size"],
                        "feasibility":    score["feasibility"],
                        "novelty":        score["novelty"],
                        "competition":    score["competition"],
                        "trend_context":  trends_cache[combo["industry"]]["text"],
                        "displayed":      False,
                        "timestamp":      datetime.now().isoformat(),
                    })

            if new_rows:
                log_df = pd.concat([log_df, pd.DataFrame(new_rows)], ignore_index=True)
                log_df.to_parquet(LOG_PATH, index=False)
                print(f"\n  {len(new_rows)} idea(s) logged to {LOG_PATH}")
            else:
                print(f"\n  All ideas scored below {SCORE_THRESHOLD}/10 — nothing logged.")

    save_trend_cache(trends_cache)

    # Persist embeddings — includes ideas that failed the score filter
    # so they won't be regenerated next run.
    with open(EMBEDDING_PATH, "wb") as f:
        pickle.dump(stored_embeddings, f)


if __name__ == "__main__":
    main()
