#!/usr/bin/env python3
"""Track what actually happened to each idea.

Lifecycle: generated -> onepager -> poc -> launched | killed

Killed/launched outcomes are fed back into the generation prompt (see
outcome_feedback in main.py) so the generator learns from real results.

Usage:
    python status.py list                     # recent ideas with status
    python status.py list --status poc        # filter by status
    python status.py set <hash-prefix> poc
    python status.py set <hash-prefix> killed --note "no search demand"
"""
import argparse
import sys

from idea_log import LOG_PATH, STATUSES, load_log as _load, save_log, idea_title


def load_log():
    if not LOG_PATH.exists():
        sys.exit("No idea log yet. Run main.py first.")
    return _load()


def cmd_list(args):
    df = load_log()
    if args.status:
        df = df[df["status"] == args.status]
    if df.empty:
        print("No ideas match.")
        return
    df = df.sort_values("timestamp", ascending=False).head(args.limit)
    print(f"{'hash':<10} {'score':<6} {'status':<10} idea")
    print("-" * 100)
    for _, row in df.iterrows():
        note = f"  [{row['status_note']}]" if row.get("status_note") else ""
        print(f"{row['hash'][:8]:<10} {row['score']:<6} {row['status']:<10} "
              f"{idea_title(row['idea'])}{note}")


def cmd_set(args):
    if args.status not in STATUSES:
        sys.exit(f"Invalid status '{args.status}'. Choose from: {', '.join(STATUSES)}")

    df = load_log()
    matches = df[df["hash"].str.startswith(args.hash_prefix)]
    if matches.empty:
        sys.exit(f"No idea with hash starting '{args.hash_prefix}'. Try: python status.py list")
    if len(matches) > 1:
        sys.exit(f"Hash prefix '{args.hash_prefix}' matches {len(matches)} ideas — use more characters.")

    idx = matches.index[0]
    old = df.loc[idx, "status"]
    df.loc[idx, "status"] = args.status
    if args.note:
        df.loc[idx, "status_note"] = args.note
    save_log(df)
    print(f"{idea_title(df.loc[idx, 'idea'])}\n  {old} -> {args.status}"
          + (f"  ({args.note})" if args.note else ""))


def main():
    parser = argparse.ArgumentParser(description="Track idea outcomes.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_list = sub.add_parser("list", help="List ideas with their status")
    p_list.add_argument("--status", choices=STATUSES, help="Filter by status")
    p_list.add_argument("--limit", type=int, default=25)
    p_list.set_defaults(func=cmd_list)

    p_set = sub.add_parser("set", help="Set an idea's status by hash prefix")
    p_set.add_argument("hash_prefix", help="First few chars of the idea hash")
    p_set.add_argument("status", help=f"One of: {', '.join(STATUSES)}")
    p_set.add_argument("--note", default="", help="Why (especially for killed) — feeds the generator")
    p_set.set_defaults(func=cmd_set)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
