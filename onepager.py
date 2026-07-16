#!/usr/bin/env python3
"""
Generate detailed markdown one-pagers from scored ideas in the parquet log.

Each one-pager is a full business plan lite: problem, solution, market,
revenue projections, roadmap, risks, and next steps.

Usage:
    python onepager.py            # one-pager for every new scored idea
    python onepager.py --top 3    # only the top 3 by score
"""
import os
import re
import sys
import argparse

from pathlib import Path
from dotenv import load_dotenv

from gemini_client import call_gemini
from idea_log import LOG_PATH, load_log, save_log

load_dotenv()

OUTDIR   = Path("onepagers")

OUTDIR.mkdir(exist_ok=True)


def slugify(text):
    """Idea name -> filesystem-safe slug."""
    return re.sub(r"[^a-z0-9_-]", "", text.lower().replace(" ", "_"))[:60]


def extract_name(idea_text):
    """Pull the idea name out of the ## Business Idea block."""
    in_section = False
    for line in idea_text.split("\n"):
        stripped = line.strip()
        if stripped == "## Business Idea":
            in_section = True
            continue
        if in_section and stripped.startswith("## "):
            break
        if in_section and stripped:
            # handles both "Name — description" and "Name. description"
            return stripped.split(" — ")[0].split(".")[0].strip()
    return "idea"


def existing_hashes():
    """Return set of idea hashes that already have a generated one-pager."""
    hashes = set()
    for md in OUTDIR.glob("*.md"):
        with open(md) as f:
            first_line = f.readline().strip()
        if first_line.startswith("<!-- id:"):
            hashes.add(first_line.split(":")[1].strip().rstrip(" -->"))
    return hashes


def generate_onepager(idea_text, score):
    """Send a scored idea to Gemini and get back a full one-pager."""
    prompt = (
        "You are a business strategist writing an executive one-pager for a potential startup.\n\n"
        f"The idea has been scored {score}/10 for viability.\n\n"
        f"Original idea:\n{idea_text}\n\n"
        "Expand this into a detailed, actionable one-pager. Use real numbers, concrete "
        "timelines, and specific next steps. Do not be vague.\n\n"
        "Use this EXACT markdown structure (keep every header exactly as shown):\n\n"
        "# [Idea Name]\n\n"
        "> **Viability Score:** [score]/10\n\n"
        "## Executive Summary\n"
        "2-3 sentences: what it is, who it's for, why it matters now.\n\n"
        "## Problem\n"
        "The specific pain point. Include real-world evidence or data where plausible.\n\n"
        "## Solution\n"
        "What the product or service does end-to-end. How it solves the problem.\n\n"
        "## Target Market\n"
        "Exact audience. Demographics, psychographics, estimated market size.\n\n"
        "## Business Model\n"
        "How revenue flows in. Include pricing tiers if applicable.\n\n"
        "## Revenue Projections\n"
        "A markdown table with 3 stages:\n"
        "| Stage | Timeline | Monthly Revenue | Key Assumption |\n"
        "|---|---|---|---|\n"
        "| Pre-revenue | ... | $0 | ... |\n"
        "| Early | ... | $X | ... |\n"
        "| Scaled | ... | $Y | ... |\n\n"
        "## Competitive Landscape\n"
        "Who else is in this space. Where the actual gap is.\n\n"
        "## Implementation Roadmap\n"
        "Broken into phases. Each phase has a clear milestone and deliverable.\n\n"
        "## Key Risks & Mitigations\n"
        "Top 3 risks. One concrete mitigation per risk.\n\n"
        "## First 10 Customers\n"
        "Name the exact communities, channels, or lists where the first 10 customers are. "
        "Include a 2-3 sentence outreach message tailored to them. No generic advice like "
        "'post on social media' — be specific enough to act on today.\n\n"
        "## Cost to Validate\n"
        "What a 2-week validation test costs in dollars and hours, what the test is, "
        "and the specific signal that means 'continue' vs 'kill'.\n\n"
        "## Next Steps\n"
        "The first 3 actions to take this week. Be specific and actionable.\n"
    )
    # A full one-pager overflows the 1024-token default and gets cut mid-sentence
    return call_gemini(prompt, max_tokens=4096)


def main():
    parser = argparse.ArgumentParser(description="Generate one-pagers from scored ideas.")
    parser.add_argument("--top", type=int, default=0,
                        help="Limit to top N ideas by score. 0 = all pending.")
    args = parser.parse_args()

    if not LOG_PATH.exists():
        print("No ideas logged yet. Run main.py first.")
        sys.exit(0)

    df      = load_log()
    done    = existing_hashes()
    pending = df[~df["hash"].isin(done) & (df["score"] > 0)].sort_values("score", ascending=False)

    if args.top:
        pending = pending.head(args.top)

    if pending.empty:
        print("No new ideas to expand. All scored ideas already have one-pagers.")
        sys.exit(0)

    print(f"\nGenerating one-pagers for {len(pending)} idea(s)...\n")

    for _, row in pending.iterrows():
        name = extract_name(row["idea"])
        # Hash suffix keeps same-named ideas from overwriting each other's files
        slug = f"{slugify(name)}-{row['hash'][:8]}"
        path = OUTDIR / f"{slug}.md"

        print(f"  {name} (score {row['score']}/10)...")
        content = generate_onepager(row["idea"], row["score"])

        # Hash comment at the top so we know this idea has been expanded
        path.write_text(f"<!-- id: {row['hash']} -->\n{content}\n")
        print(f"    -> {path}")

        # Advance lifecycle status (generated -> onepager); don't regress
        # ideas that are already further along (poc/launched/killed)
        if df.loc[row.name, "status"] in ("generated", "unscored", ""):
            df.loc[row.name, "status"] = "onepager"

    save_log(df)

    print(f"\nDone. One-pagers in {OUTDIR}/")


if __name__ == "__main__":
    main()
