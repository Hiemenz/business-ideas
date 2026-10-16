#!/usr/bin/env python3
"""ideas — unified CLI for the business idea pipeline.

Usage:
    ideas generate              # generate + score ideas
    ideas validate [--top N]    # external validation signals
    ideas onepager [--top N]    # expand top ideas into one-pagers
    ideas landing [--hash H]    # build a waitlist landing page
    ideas status list           # review lifecycle
    ideas status set <hash> <status> [--note "..."]
    ideas digest [--days N]     # weekly summary
    ideas dashboard             # regenerate dashboard.html
    ideas ratings               # score calibration report
    ideas rescore [--all]       # rescore ideas with score=0 or status=unscored
    ideas ingest [--dry-run]    # load proof-of-concepts/*.md into the log
    ideas pursue [--top N]      # rank PoCs by pursuit priority
"""
import subprocess
import sys
from pathlib import Path

_ROOT = Path(__file__).parent

COMMANDS = {
    "generate":  "main.py",
    "validate":  "validate.py",
    "onepager":  "onepager.py",
    "landing":   "landing.py",
    "status":    "status.py",
    "digest":    "digest.py",
    "dashboard": "dashboard.py",
    "ratings":   "ratings.py",
    "rescore":   "rescore.py",
    "ingest":    "ingest_pocs.py",
    "pursue":    "pursue.py",
}


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        print("Commands:", ", ".join(COMMANDS))
        sys.exit(0)

    cmd = sys.argv[1]
    if cmd not in COMMANDS:
        print(f"Unknown command: {cmd!r}")
        print(f"Available: {', '.join(COMMANDS)}")
        sys.exit(1)

    script = _ROOT / COMMANDS[cmd]
    sys.exit(subprocess.call([sys.executable, str(script)] + sys.argv[2:]))


if __name__ == "__main__":
    main()
