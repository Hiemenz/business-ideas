#!/usr/bin/env python3
"""Ingest proof-of-concept markdown files into the idea log.

Reads every *.md file in proof-of-concepts/, scores each one via Gemini,
and adds it to the parquet with status='poc'.  Already-ingested files
(matched by content hash) are skipped.

Usage:
    python ingest_pocs.py               # ingest all new PoC files
    python ingest_pocs.py --dry-run     # show what would be ingested
    python ingest_pocs.py --force       # re-ingest even if hash exists
"""
import argparse
import hashlib
import logging
import re
from datetime import datetime
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv

from gemini_client import score_ideas, composite_score
from idea_log import load_log, save_log

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger(__name__)

POC_DIR = Path(__file__).parent / "proof-of-concepts"

# Maps keywords in the PoC title/content to config.yml industries
_INDUSTRY_KEYWORDS = {
    "seo": "e-commerce", "shopify": "e-commerce", "ecommerce": "e-commerce",
    "airbnb": "real estate", "real estate": "real estate",
    "health": "healthcare", "medical": "healthcare", "dental": "healthcare",
    "saas": "software", "software": "software", "app": "software",
    "restaurant": "hospitality", "food": "hospitality",
    "hr": "hr", "hiring": "hr", "recruit": "hr",
    "finance": "finance", "bookkeeping": "finance", "invoice": "finance",
    "marketing": "marketing", "email": "marketing", "content": "content creation",
    "linkedin": "marketing", "podcast": "content creation",
}


def _extract_title(content: str) -> str:
    """Return the human-readable title from the PoC markdown header line."""
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("# PoC"):
            # '# PoC 01 — "Title" — Long description'
            # Drop the '# PoC N — ' prefix
            without_header = re.sub(r"^#\s*PoC\s+\d+\s*[—–-]+\s*", "", line).strip()
            return without_header
    return content.splitlines()[0].lstrip("# ").strip()


def _extract_date(content: str) -> str:
    m = re.search(r"\*\*Date:\*\*\s*(\S+)", content)
    return m.group(1) if m else datetime.now().date().isoformat()


def _infer_industry(title: str, content: str) -> str:
    combined = (title + " " + content[:500]).lower()
    for kw, industry in _INDUSTRY_KEYWORDS.items():
        if kw in combined:
            return industry
    return "service"


def main():
    parser = argparse.ArgumentParser(description="Ingest PoC markdown files into the idea log.")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    parser.add_argument("--force", action="store_true", help="Re-ingest even if already present")
    args = parser.parse_args()

    poc_files = sorted(POC_DIR.glob("*.md"))
    if not poc_files:
        print(f"No markdown files found in {POC_DIR}")
        return

    df = load_log()
    existing_hashes = set(df["hash"].tolist()) if not df.empty else set()

    new_rows = []
    skipped = 0

    for path in poc_files:
        content = path.read_text(encoding="utf-8")
        content_hash = hashlib.md5(content.encode()).hexdigest()

        if not args.force and content_hash in existing_hashes:
            logger.debug("Already ingested: %s", path.name)
            skipped += 1
            continue

        title = _extract_title(content)
        date_str = _extract_date(content)
        industry = _infer_industry(title, content)
        logger.info("Queued: %s", title[:80])
        new_rows.append({
            "_path": str(path),
            "_name": path.name,
            "_hash": content_hash,
            "_title": title,
            "_date": date_str,
            "_industry": industry,
            "_content": content,
        })

    if not new_rows:
        print(f"All {skipped} PoC file(s) already ingested. Use --force to re-ingest.")
        return

    if args.dry_run:
        print(f"Would ingest {len(new_rows)} PoC(s) (skipping {skipped} already present):")
        for r in new_rows:
            print(f"  {r['_name']}")
        return

    logger.info("Scoring %d PoC(s) via Gemini...", len(new_rows))
    idea_texts = [r["_content"] for r in new_rows]
    scores = score_ideas(idea_texts)

    ingested = 0
    records = []
    for row, score in zip(new_rows, scores):
        if score is None:
            logger.warning("Score failed for %s — ingesting unscored", row["_name"])
            composite, s = 0.0, {}
            status = "unscored"
        else:
            composite = composite_score(score)
            s = score
            status = "poc"

        records.append({
            "idea":               row["_title"] + "\n\n" + row["_content"],
            "industry":           row["_industry"],
            "business_model":     "service",
            "hash":               row["_hash"],
            "score":              composite,
            "market_size":        s.get("market_size", 0),
            "feasibility":        s.get("feasibility", 0),
            "novelty":            s.get("novelty", 0),
            "competition":        s.get("competition", 0),
            "trend_context":      "",
            "displayed":          False,
            "timestamp":          row["_date"] + "T00:00:00",
            "status":             status,
            "status_note":        "",
            "user_rating":        float("nan"),
            "validation_score":   float("nan"),
            "validation_summary": "",
            "source_file":        row["_path"],
        })
        logger.info("%.1f/10 [%s] %s", composite, status, row["_title"][:70])
        ingested += 1

    df = pd.concat([df, pd.DataFrame(records)], ignore_index=True)
    save_log(df)
    print(f"Ingested {ingested} PoC(s). Skipped {skipped} already present.")


if __name__ == "__main__":
    main()
