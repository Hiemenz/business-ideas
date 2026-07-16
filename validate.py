#!/usr/bin/env python3
"""External validation signals for scored ideas.

Gemini scoring is one model grading its own homework. This adds cheap
outside evidence per idea:

  1. Pain demand   — Reddit search for people complaining about the problem
  2. Market buzz   — Hacker News (Algolia API) stories about the space
  3. Competitors   — HN + Reddit mentions of existing products doing this

Signals are combined into a 0-10 validation_score and a human-readable
summary, both written back to the parquet log.

Usage:
    python validate.py                # top 3 unvalidated ideas by score
    python validate.py --top 5
    python validate.py --hash ab12    # one specific idea
"""
import argparse
import logging
import sys

import requests

from gemini_client import call_gemini, parse_json_block
from idea_log import LOG_PATH, load_log, save_log

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger(__name__)

HEADERS  = {"User-Agent": "BusinessIdeaValidator/1.0"}


# ==== SIGNAL FETCHERS ====

def extract_queries(idea_text):
    """Ask Gemini for the search queries this idea should be validated with."""
    prompt = (
        "Given this business idea, produce search queries to validate it.\n\n"
        f"{idea_text[:1500]}\n\n"
        "Return ONLY compact JSON:\n"
        '{"problem_query": "<how a frustrated person would describe the problem, 3-6 words>",'
        ' "market_query": "<the product category / space, 2-4 words>"}'
    )
    raw = call_gemini(prompt, max_tokens=128, temperature=0.2)
    parsed = parse_json_block(raw)
    return parsed["problem_query"], parsed["market_query"]


def reddit_pain_search(query, limit=8):
    """People complaining about the problem = real demand. Returns (count, engagement, titles)."""
    try:
        resp = requests.get(
            "https://www.reddit.com/search.json",
            params={"q": query, "sort": "relevance", "t": "year", "limit": limit},
            headers=HEADERS, timeout=15,
        )
        resp.raise_for_status()
        posts = resp.json()["data"]["children"]
    except Exception as e:
        logger.warning("Reddit search failed: %s", e)
        return None

    titles = [p["data"]["title"][:90] for p in posts[:3]]
    engagement = sum(p["data"].get("score", 0) + p["data"].get("num_comments", 0) for p in posts)
    return {"count": len(posts), "engagement": engagement, "titles": titles}


def hn_search(query, limit=10):
    """HN stories about the space: demand + competitor signal. Free Algolia API."""
    try:
        resp = requests.get(
            "https://hn.algolia.com/api/v1/search",
            params={"query": query, "tags": "story", "hitsPerPage": limit},
            headers=HEADERS, timeout=15,
        )
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        logger.warning("HN search failed: %s", e)
        return None

    hits = data.get("hits", [])
    titles = [h.get("title", "")[:90] for h in hits[:3]]
    points = sum(h.get("points") or 0 for h in hits)
    # "Show HN" / "Launch HN" posts in the space = direct competitors shipping
    competitors = sum(
        1 for h in hits
        if any(tag in (h.get("title") or "") for tag in ("Show HN", "Launch HN"))
    )
    return {"total": data.get("nbHits", len(hits)), "points": points,
            "titles": titles, "competitors": competitors}


# ==== SCORING ====

def compute_validation(reddit, hn):
    """Blend signals into a 0-10 score + summary. Crude but consistent —
    the point is comparing ideas against each other, not absolute truth.
    The score is normalized to the sources that actually responded, so an
    idea isn't penalized because e.g. Reddit blocked the request."""
    score, available_max, parts = 0.0, 0.0, []

    if reddit is None:
        parts.append("Reddit: unavailable (blocked or down — not counted)")
    else:
        available_max += 5.0
        # Demand: complaints exist and people engage with them (max 5 pts)
        demand = min(5.0, reddit["count"] * 0.3 + min(reddit["engagement"], 2000) / 500)
        score += demand
        parts.append(f"Reddit pain demand {demand:.1f}/5 "
                     f"({reddit['count']} posts, {reddit['engagement']} engagement)")

    if hn is None:
        parts.append("HN: unavailable (not counted)")
    else:
        available_max += 5.0
        # Buzz: the space is alive (max 3 pts)
        buzz = min(3.0, min(hn["total"], 100) / 33 + min(hn["points"], 1500) / 1000)
        # Competition: some competitors = validated market; a pile = crowded (max 2 pts)
        comp = 2.0 if 1 <= hn["competitors"] <= 3 else (1.0 if hn["competitors"] == 0 else 0.5)
        score += buzz + comp
        parts.append(f"HN buzz {buzz:.1f}/3 ({hn['total']} stories, {hn['points']} points)")
        parts.append(f"Competition signal {comp:.1f}/2 ({hn['competitors']} Show/Launch HN posts)")

    evidence = []
    if reddit and reddit["titles"]:
        evidence.append("Reddit: " + " | ".join(reddit["titles"]))
    if hn and hn["titles"]:
        evidence.append("HN: " + " | ".join(hn["titles"]))

    summary = "; ".join(parts)
    if evidence:
        summary += "\n" + "\n".join(evidence)

    if available_max == 0:
        return float("nan"), summary  # nothing responded — stays unvalidated
    return round(score / available_max * 10, 1), summary


def validate_idea(idea_text):
    problem_q, market_q = extract_queries(idea_text)
    logger.info("  problem query: '%s'  |  market query: '%s'", problem_q, market_q)
    reddit = reddit_pain_search(problem_q)
    hn     = hn_search(market_q)
    return compute_validation(reddit, hn)


# ==== CLI ====

def main():
    parser = argparse.ArgumentParser(description="Fetch external validation signals for ideas.")
    parser.add_argument("--top", type=int, default=3, help="Validate top N unvalidated ideas by score")
    parser.add_argument("--hash", default="", help="Validate one idea by hash prefix")
    args = parser.parse_args()

    if not LOG_PATH.exists():
        sys.exit("No idea log yet. Run main.py first.")

    df = load_log()

    if args.hash:
        targets = df[df["hash"].str.startswith(args.hash)]
        if targets.empty:
            sys.exit(f"No idea with hash starting '{args.hash}'.")
    else:
        targets = (df[df["validation_score"].isna()]
                   .sort_values("score", ascending=False)
                   .head(args.top))
        if targets.empty:
            print("All ideas already validated.")
            return

    logger.info("Validating %d idea(s)...", len(targets))
    for idx, row in targets.iterrows():
        title = str(row["idea"]).split("\n")[0][:80]
        logger.info("%s", title)
        try:
            vscore, summary = validate_idea(row["idea"])
        except Exception as e:
            logger.error("Validation failed: %s", e)
            continue
        df.loc[idx, "validation_score"]   = vscore
        df.loc[idx, "validation_summary"] = summary
        logger.info("  validation score: %s/10 (Gemini score: %s/10)", vscore, row["score"])

    save_log(df)
    logger.info("Saved to %s.", LOG_PATH)


if __name__ == "__main__":
    main()
