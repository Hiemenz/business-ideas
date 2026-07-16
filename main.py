import json
import logging
import random
import hashlib
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
import yaml
from dotenv import load_dotenv

from trends import fetch_trends, fetch_reddit_ideas, fetch_arxiv_papers, load_trend_cache, save_trend_cache
import gemini_client
from gemini_client import (
    build_prompt, score_ideas, call_gemini, embed_text,
    composite_score, EMBED_MODEL,
)
from idea_log import LOG_PATH, load_log, save_log

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger(__name__)

# ==== CONFIGURATION ====
YAML_PATH      = Path("config.yml")
EMBEDDING_PATH = Path("embeddings.json")

if not gemini_client.GEMINI_API_KEY:
    raise SystemExit("GEMINI_API_KEY environment variable is not set.")

# ==== LOAD YAML CONFIG ====
with open(YAML_PATH) as f:
    config = yaml.safe_load(f)

settings             = config.get("settings", {})
BATCH_SIZE           = settings.get("batch_size", 5)
SCORE_THRESHOLD      = settings.get("score_threshold", 6.0)
SIMILARITY_THRESHOLD = settings.get("similarity_threshold", 0.85)
ROTATION_WINDOW      = settings.get("rotation_window", 30)
TREND_CACHE_TTL_HOURS = settings.get("trend_cache_ttl_hours", 24)

gemini_client.set_rpm_limit(settings.get("gemini_rpm_limit", 14))

industries      = config["industries"]
business_models = config["business_models"]
audiences       = config["audiences"]
technologies    = config["technologies"]
problems        = config["problems"]
platforms       = config["platforms"]
monetization    = config["monetization"]
subreddits      = config.get("subreddits", [])

# ==== LOAD & MIGRATE LOG ====
log_df          = load_log()
used_industries = log_df["industry"].tolist()[-ROTATION_WINDOW:]
used_models     = log_df["business_model"].tolist()[-ROTATION_WINDOW:]

# Load persisted embeddings — JSON format, migrate from legacy pkl if present
_pkl_path = Path("embeddings.pkl")
if EMBEDDING_PATH.exists():
    with open(EMBEDDING_PATH) as f:
        stored_embeddings = json.load(f)
elif _pkl_path.exists():
    import pickle
    with open(_pkl_path, "rb") as f:
        _legacy = pickle.load(f)
    stored_embeddings = {
        k: (v if isinstance(v, dict) else {"model": "legacy-unknown", "vec": v})
        for k, v in _legacy.items()
    }
    logger.info("Migrated embeddings.pkl → embeddings.json")
else:
    stored_embeddings = {}

trends_cache = load_trend_cache(ttl_hours=TREND_CACHE_TTL_HOURS)


# ==== HELPERS ====

def pick_combo():
    """Pick a random parameter combo, avoiding recently used industries/models."""
    avail_industries = [i for i in industries if i not in used_industries]
    avail_models     = [m for m in business_models if m not in used_models]
    return {
        "industry":       random.choice(avail_industries or industries),
        "business_model": random.choice(avail_models or business_models),
        "audience":       random.choice(audiences),
        "technology":     random.choice(technologies),
        "problem":        random.choice(problems),
        "platform":       random.choice(platforms),
        "monetization":   random.choice(monetization),
    }


def is_duplicate(embedding, model=EMBED_MODEL):
    """True if this embedding is too close to any previously seen idea (cosine sim).

    Only compares against stored vectors from the same model AND with the same
    dimensionality — mixed-dimension history would otherwise build a ragged
    array and crash.
    """
    dim = len(embedding)
    stored_vecs = [
        v["vec"] for v in stored_embeddings.values()
        if isinstance(v, dict) and v.get("model") == model and len(v.get("vec", [])) == dim
    ]
    if not stored_vecs:
        return False
    stored_vecs = np.array(stored_vecs)
    vec         = np.array(embedding)
    sims        = (stored_vecs @ vec) / (np.linalg.norm(stored_vecs, axis=1) * np.linalg.norm(vec))
    return float(sims.max()) > SIMILARITY_THRESHOLD


def outcome_feedback(df, max_items=6):
    """Summarize launched/killed ideas so generation learns from outcomes."""
    if "status" not in df.columns or df.empty:
        return ""
    lines = []
    for status, verb in (("killed", "FAILED"), ("launched", "WORKED")):
        subset = df[df["status"] == status].tail(max_items // 2)
        for _, row in subset.iterrows():
            summary = str(row["idea"]).split("\n")[0][:150]
            note = f" (reason: {row['status_note']})" if row.get("status_note") else ""
            lines.append(f"- {verb}: {summary}{note}")
    return "\n".join(lines)


def main():
    logger.info("Generating %d ideas...", BATCH_SIZE)

    global log_df
    ideas, combos = [], []
    feedback = outcome_feedback(log_df)

    logger.info("Fetching Reddit ideas...")
    reddit_ideas = (
        fetch_reddit_ideas(subreddits, posts_per_sub=settings.get("posts_per_sub", 3))
        if subreddits else "No subreddits configured."
    )

    arxiv_cache = {}

    for i in range(BATCH_SIZE):
        combo    = pick_combo()
        industry = combo["industry"]

        if industry not in trends_cache:
            logger.info("Fetching trends for %s...", industry)
            trends_cache[industry] = {"text": fetch_trends(industry), "ts": datetime.now().timestamp()}

        if industry not in arxiv_cache:
            logger.info("Fetching arXiv papers for %s...", industry)
            arxiv_cache[industry] = fetch_arxiv_papers(industry, max_results=settings.get("arxiv_max_results", 5))

        try:
            idea_text = call_gemini(build_prompt(
                combo, trends_cache[industry]["text"], reddit_ideas,
                arxiv_cache[industry], outcome_feedback=feedback,
            ))
            embedding = embed_text(idea_text)
        except Exception as e:
            logger.error("[%d/%d] Skipped — API error: %s", i + 1, BATCH_SIZE, e)
            continue

        if is_duplicate(embedding):
            logger.info("[%d/%d] Skipped — too similar to an existing idea", i + 1, BATCH_SIZE)
            continue

        ideas.append(idea_text)
        combos.append(combo)
        stored_embeddings[hashlib.md5(idea_text.encode()).hexdigest()] = {
            "model": EMBED_MODEL,
            "vec": embedding,
        }
        logger.info("[%d/%d] Generated", i + 1, BATCH_SIZE)

    # ==== SCORE & LOG ====
    if not ideas:
        logger.info("No unique ideas generated this run.")
    else:
        logger.info("Scoring %d idea(s)...", len(ideas))
        scores = score_ideas(ideas)

        new_rows = []
        for idea, combo, score in zip(ideas, combos, scores):
            if score is None:
                logger.warning("Score unavailable — logged unscored (rescore later)")
                composite, kept = 0.0, True
            else:
                composite = composite_score(score)
                kept = composite >= SCORE_THRESHOLD
                logger.info("Score: %.1f/10 — %s", composite, "kept" if kept else "filtered out")

            if kept:
                s = score or {}
                new_rows.append({
                    "idea":               idea,
                    "industry":           combo["industry"],
                    "business_model":     combo["business_model"],
                    "hash":               hashlib.md5(idea.encode()).hexdigest(),
                    "score":              composite,
                    "market_size":        s.get("market_size", 0),
                    "feasibility":        s.get("feasibility", 0),
                    "novelty":            s.get("novelty", 0),
                    "competition":        s.get("competition", 0),
                    "trend_context":      trends_cache[combo["industry"]]["text"],
                    "displayed":          False,
                    "timestamp":          datetime.now().isoformat(),
                    "status":             "generated" if score else "unscored",
                    "status_note":        "",
                    "user_rating":        np.nan,
                    "validation_score":   np.nan,
                    "validation_summary": "",
                })

        if new_rows:
            log_df = pd.concat([log_df, pd.DataFrame(new_rows)], ignore_index=True)
            save_log(log_df)
            logger.info("%d idea(s) logged to %s", len(new_rows), LOG_PATH)
        else:
            logger.info("All ideas scored below %.1f/10 — nothing logged.", SCORE_THRESHOLD)

    save_trend_cache(trends_cache)

    with open(EMBEDDING_PATH, "w") as f:
        json.dump(stored_embeddings, f)


if __name__ == "__main__":
    main()
