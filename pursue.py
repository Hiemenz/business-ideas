#!/usr/bin/env python3
"""Rank proof-of-concepts and surface the best ones to pursue next.

Reads all 'poc'-status ideas from the log, ranks them by a weighted composite
of score, feasibility, and market_size, and prints a decision table.

Usage:
    python pursue.py                    # top 10 PoCs by default ranking
    python pursue.py --top 5            # show top N
    python pursue.py --sort feasibility # rank by a single sub-score
    python pursue.py --all-statuses     # include generated/onepager too
"""
import argparse
import sys
from pathlib import Path

from idea_log import load_log, LOG_PATH, idea_title

SORT_KEYS = ("score", "feasibility", "market_size", "novelty", "competition")


def _pursuit_score(row):
    """Weighted ranking: feasibility and market_size matter most for 'what to build'."""
    return (
        row["score"] * 0.4
        + row["feasibility"] * 0.35
        + row["market_size"] * 0.25
    )


def main():
    parser = argparse.ArgumentParser(description="Rank PoCs by pursuit priority.")
    parser.add_argument("--top", type=int, default=10, metavar="N")
    parser.add_argument("--sort", choices=SORT_KEYS, default=None,
                        help="Sort by a single sub-score instead of weighted composite")
    parser.add_argument("--all-statuses", action="store_true",
                        help="Include all statuses, not just 'poc'")
    args = parser.parse_args()

    if not LOG_PATH.exists():
        sys.exit("No idea log found. Run 'ideas ingest' first.")

    df = load_log()

    if not args.all_statuses:
        df = df[df["status"] == "poc"]

    if df.empty:
        sys.exit(
            "No PoC-status ideas found.\n"
            "Run 'ideas ingest' to load proof-of-concepts, or use --all-statuses."
        )

    if args.sort:
        df = df.sort_values(args.sort, ascending=False)
    else:
        df = df.copy()
        df["_pursuit"] = df.apply(_pursuit_score, axis=1)
        df = df.sort_values("_pursuit", ascending=False)

    top = df.head(args.top).reset_index(drop=True)

    # Header
    col_w = 62
    print(f"\n{'Rank':<5} {'Score':>5}  {'Feasib':>6}  {'Market':>6}  {'Novelty':>7}  {'Title'}")
    print("-" * (col_w + 40))

    for i, (_, row) in enumerate(top.iterrows(), 1):
        title = idea_title(row["idea"], col_w)
        file_hint = ""
        if row.get("source_file"):
            file_hint = f"\n       → {Path(row['source_file']).name}"
        print(
            f"{i:<5} {row['score']:>5.1f}  {row['feasibility']:>6.1f}  "
            f"{row['market_size']:>6.1f}  {row['novelty']:>7.1f}  {title}{file_hint}"
        )

    print()

    # Actionable footer
    best = top.iloc[0]
    best_hash = best["hash"][:8]
    best_title = idea_title(best["idea"], 55)
    print(f"Top pick: {best_title}")
    if best.get("source_file"):
        print(f"File:     {best['source_file']}")
    print(f"\nTo mark as launched:  ideas status set {best_hash} launched")
    print(f"To kill:              ideas status set {best_hash} killed --note \"reason\"")
    print()


if __name__ == "__main__":
    main()
