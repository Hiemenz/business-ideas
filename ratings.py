"""Store the user's own 1-5 ratings of ideas, and compare them against
Gemini's composite scores to see whether the automated scoring actually
predicts what the user finds interesting.

Ratings live in ratings.parquet (one row per rating). If the rated idea also
exists in the main log, its user_rating column is updated there too.
"""
import hashlib
from datetime import datetime
from pathlib import Path

import pandas as pd

RATINGS_PATH = Path("ratings.parquet")
LOG_PATH     = Path("money_making_ideas_log.parquet")


def idea_hash(idea_text: str) -> str:
    return hashlib.md5(idea_text.encode()).hexdigest()


def save_rating(idea_text: str, rating: int, user_id: int, gemini_score: float | None = None):
    """Persist a 1-5 rating. Returns the idea hash."""
    if not 1 <= rating <= 5:
        raise ValueError("rating must be 1-5")

    h = idea_hash(idea_text)
    row = pd.DataFrame([{
        "hash":         h,
        "user_id":      str(user_id),
        "rating":       rating,
        "gemini_score": gemini_score if gemini_score is not None else float("nan"),
        "idea_snippet": idea_text.split("\n")[0][:200],
        "timestamp":    datetime.now().isoformat(),
    }])

    if RATINGS_PATH.exists():
        df = pd.read_parquet(RATINGS_PATH)
        # One rating per user per idea — newest wins
        df = df[~((df["hash"] == h) & (df["user_id"] == str(user_id)))]
        df = pd.concat([df, row], ignore_index=True)
    else:
        df = row
    df.to_parquet(RATINGS_PATH, index=False)

    # Mirror into the main log if this idea was logged there
    if LOG_PATH.exists():
        log = pd.read_parquet(LOG_PATH)
        if "user_rating" in log.columns and (log["hash"] == h).any():
            log.loc[log["hash"] == h, "user_rating"] = float(rating)
            log.to_parquet(LOG_PATH, index=False)

    return h


def calibration_report() -> str:
    """How well does Gemini's composite score track the user's ratings?"""
    if not RATINGS_PATH.exists():
        return "No ratings yet. Rate ideas with !rate 1-5 in Discord."

    df = pd.read_parquet(RATINGS_PATH)
    scored = df.dropna(subset=["gemini_score"])
    lines = [f"Ratings collected: {len(df)}"]

    if len(scored) >= 5:
        corr = scored["rating"].corr(scored["gemini_score"])
        lines.append(f"Correlation between your rating and Gemini score: {corr:.2f} "
                     f"(n={len(scored)}; 1.0 = perfect, 0 = no relationship)")
        by_bucket = scored.groupby(scored["gemini_score"].round())["rating"].mean()
        lines.append("Avg your-rating by Gemini score bucket:")
        for bucket, avg in by_bucket.items():
            lines.append(f"  Gemini {bucket:.0f}/10 -> you rate {avg:.1f}/5")
    else:
        lines.append(f"Need ~5+ rated ideas with Gemini scores for a correlation "
                     f"(have {len(scored)}). Keep rating!")

    return "\n".join(lines)


if __name__ == "__main__":
    print(calibration_report())
