"""Single source of truth for the idea log schema.

Every script reads the parquet through load_log() so schema migration
happens in exactly one place — older files (which may lack score/status/
timestamp columns entirely) upgrade automatically no matter which script
touches them first.

Idea lifecycle: generated -> onepager -> poc -> launched | killed
"""
from pathlib import Path

import numpy as np
import pandas as pd

LOG_PATH = Path("money_making_ideas_log.parquet")

DEFAULTS = {
    "idea": "", "industry": "", "business_model": "", "hash": "",
    "score": 0.0, "market_size": 0, "feasibility": 0,
    "novelty": 0, "competition": 0, "trend_context": "",
    "displayed": False, "timestamp": "",
    "status": "generated", "status_note": "",
    "user_rating": np.nan,
    "validation_score": np.nan, "validation_summary": "",
}

STATUSES = ["generated", "unscored", "onepager", "poc", "launched", "killed"]


def load_log(path=LOG_PATH):
    """Read the idea log, adding any missing columns with defaults.
    Returns an empty (but fully-columned) DataFrame if the file doesn't exist."""
    if Path(path).exists():
        df = pd.read_parquet(path)
        for col, default in DEFAULTS.items():
            if col not in df.columns:
                df[col] = default
    else:
        df = pd.DataFrame(columns=list(DEFAULTS.keys()))
    return df


def save_log(df, path=LOG_PATH):
    df.to_parquet(path, index=False)


def idea_title(idea_text, width=90):
    """First meaningful line of an idea — for lists, digests, dashboards."""
    for line in str(idea_text).split("\n"):
        line = line.strip()
        if line and not line.startswith("#"):
            return line[:width]
    return str(idea_text)[:width]
