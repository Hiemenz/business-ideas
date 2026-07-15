#!/usr/bin/env python3
"""Weekly digest: the top ideas from the last 7 days, ranked and summarized.

Prints to stdout and, if DISCORD_WEBHOOK_URL is set, posts to Discord.
Ideas that arrive as a ranked weekly batch get acted on; a parquet file
nobody opens does not.

Usage:
    python digest.py               # last 7 days, top 3
    python digest.py --days 14 --top 5

Cron (Monday 9am):
    0 9 * * 1 /path/to/.venv/bin/python /path/to/project/digest.py
"""
import argparse
import sys
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd

from discord_notify import post
from idea_log import LOG_PATH, load_log, idea_title


def build_digest(days=7, top=3):
    if not LOG_PATH.exists():
        return None
    df = load_log()
    if df.empty:
        return None

    cutoff = (datetime.now() - timedelta(days=days)).isoformat()
    recent = df[df["timestamp"] >= cutoff].sort_values("score", ascending=False)

    lines = [f"**📋 Idea digest — last {days} days**"]
    if recent.empty:
        lines.append(f"No new ideas generated. ({len(df)} total in the log — "
                     "is the cron job still running?)")
        return "\n".join(lines)

    lines.append(f"{len(recent)} new idea(s); top {min(top, len(recent))}:\n")
    for rank, (_, row) in enumerate(recent.head(top).iterrows(), 1):
        lines.append(f"**{rank}. {idea_title(row['idea'])}**")
        detail = f"   Gemini score: {row['score']}/10"
        vs = row.get("validation_score")
        if pd.notna(vs):
            detail += f" | validation: {vs}/10"
        detail += f" | {row['industry']} / {row['business_model']} | hash `{row['hash'][:8]}`"
        lines.append(detail)

    # Nudge on stale winners: high scores that never went anywhere
    stale = df[(df["score"] >= 7.5) & (df["status"].isin(["generated", "onepager"]))]
    stale = stale[stale["timestamp"] < cutoff]
    if not stale.empty:
        lines.append(f"\n⚠️ {len(stale)} older idea(s) scored 7.5+ but were never pursued. "
                     "Run `python status.py list` to review.")

    lines.append("\nNext: `python validate.py` for signals, "
                 "`python onepager.py --top 3` to expand, "
                 "`python landing.py` to build a waitlist test.")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Weekly idea digest.")
    parser.add_argument("--days", type=int, default=7)
    parser.add_argument("--top", type=int, default=3)
    parser.add_argument("--no-discord", action="store_true", help="Print only, don't post")
    args = parser.parse_args()

    digest = build_digest(days=args.days, top=args.top)
    if digest is None:
        sys.exit("No idea log yet. Run main.py first.")

    print(digest)

    if not args.no_discord:
        if post(digest, username="Idea Digest"):
            print("\n(Posted to Discord.)")
        else:
            print("\n(Discord webhook not configured or post failed — printed only.)")


if __name__ == "__main__":
    main()
