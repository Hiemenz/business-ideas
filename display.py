#!/usr/bin/env python3
"""Raspberry Pi e-ink display driver.

Pulls the highest-scored pending idea from the parquet log, renders it,
and pushes to a Waveshare 7.5" v2 e-ink display.

--- Pi setup ---
    pip install pandas pyarrow Pillow
    pip install waveshare-epd          # Waveshare driver

--- Sync the parquet from your main machine ---
    scp money_making_ideas_log.parquet pi@<ip>:/path/to/project/

--- Run manually ---
    python display.py

--- Run on a schedule (crontab -e) ---
    0 8 * * * /path/to/venv/bin/python /path/to/project/display.py
"""
import sys
from pathlib import Path

import pandas as pd
from render import render_idea

LOG_PATH  = Path("money_making_ideas_log.parquet")
OUTPUT_IMG = Path("/tmp/current_idea.png")


def get_next_idea():
    """Return (idea_text, score, hash) for the highest-scored pending idea."""
    if not LOG_PATH.exists():
        return None, None, None

    df      = pd.read_parquet(LOG_PATH)
    pending = df[df["displayed"] == False].sort_values("score", ascending=False)

    if pending.empty:
        return None, None, None

    row = pending.iloc[0]
    return row["idea"], row["score"], row["hash"]


def mark_displayed(idea_hash):
    """Flip displayed=True for the idea with this hash."""
    df = pd.read_parquet(LOG_PATH)
    df.loc[df["hash"] == idea_hash, "displayed"] = True
    df.to_parquet(LOG_PATH, index=False)


def push_to_display(image_path):
    """Push the rendered PNG to the e-ink panel. Graceful fallback if driver missing."""
    try:
        from waveshare_epd import epd7in5_v2
        from PIL import Image

        epd = epd7in5_v2.EPD()
        epd.Init()
        epd.Clear()

        img = Image.open(image_path).convert("1")
        epd.display(epd.getbuffer(img))
        epd.sleep()
        print("Pushed to e-ink display.")

    except ImportError:
        print(f"waveshare_epd not installed — image saved to: {image_path}")
        print("On Pi: pip install waveshare-epd")


def main():
    idea_text, score, idea_hash = get_next_idea()

    if idea_text is None:
        print("No pending ideas in the log. Run main.py to generate more.")
        sys.exit(0)

    print(f"Rendering idea (score {score}/10)...")
    render_idea(idea_text, str(OUTPUT_IMG), score=score)

    push_to_display(str(OUTPUT_IMG))
    mark_displayed(idea_hash)
    print("Done.")


if __name__ == "__main__":
    main()
