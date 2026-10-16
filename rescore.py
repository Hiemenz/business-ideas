#!/usr/bin/env python3
"""Rescore ideas that landed with score=0 or status='unscored'.

Usage:
    python rescore.py           # rescore all score=0 / unscored ideas
    python rescore.py --all     # rescore every idea in the log
"""
import argparse
import logging

from dotenv import load_dotenv

from gemini_client import score_ideas, composite_score
from idea_log import load_log, save_log, idea_title, LOG_PATH

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Rescore ideas with missing scores.")
    parser.add_argument("--all", action="store_true", help="Rescore every idea, not just score=0")
    args = parser.parse_args()

    if not LOG_PATH.exists():
        print("No idea log found. Run 'ideas generate' first.")
        return

    df = load_log()
    if df.empty:
        print("Idea log is empty.")
        return

    targets = df if args.all else df[(df["score"] == 0.0) | (df["status"] == "unscored")]

    if targets.empty:
        print("No ideas need rescoring.")
        return

    logger.info("Rescoring %d idea(s)...", len(targets))
    scores = score_ideas(targets["idea"].tolist())

    updated = 0
    for (idx, _), score in zip(targets.iterrows(), scores):
        if score is None:
            logger.warning("Score unavailable for '%s' — skipping", idea_title(df.loc[idx, "idea"], 60))
            continue
        c = composite_score(score)
        df.loc[idx, "score"] = c
        df.loc[idx, "market_size"] = score["market_size"]
        df.loc[idx, "feasibility"] = score["feasibility"]
        df.loc[idx, "novelty"] = score["novelty"]
        df.loc[idx, "competition"] = score["competition"]
        if df.loc[idx, "status"] == "unscored":
            df.loc[idx, "status"] = "generated"
        logger.info("%.1f/10 — %s", c, idea_title(df.loc[idx, "idea"], 60))
        updated += 1

    save_log(df)
    print(f"Rescored {updated}/{len(targets)} idea(s).")


if __name__ == "__main__":
    main()
