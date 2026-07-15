#!/usr/bin/env python3
"""Generate a static HTML portfolio dashboard from the idea log.

Shows the pipeline at a glance: totals, status funnel, score distribution,
industry yield, stale high-scorers, and a full idea table. Pure HTML/CSS —
no JS dependencies — so it renders anywhere (including scp'd to the Pi).

Usage:
    python dashboard.py               # writes dashboard.html
    python dashboard.py --out /tmp/x.html
"""
import argparse
import html
import sys
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd

from idea_log import LOG_PATH, STATUSES as STATUS_ORDER, load_log, idea_title


def e(x):
    return html.escape(str(x))


def hbar_rows(counts, max_count):
    """Horizontal magnitude bars: single hue, direct value labels in ink."""
    rows = []
    for label, count in counts.items():
        pct = (count / max_count * 100) if max_count else 0
        rows.append(
            f'<div class="hbar-row" title="{e(label)}: {count}">'
            f'<span class="hbar-label">{e(label)}</span>'
            f'<span class="hbar-track"><span class="hbar-fill" style="width:{pct:.1f}%"></span></span>'
            f'<span class="hbar-value">{count}</span></div>'
        )
    return "\n".join(rows)


def build_html(df):
    total = len(df)
    avg_score = df["score"].mean() if total else 0
    status_counts = df["status"].value_counts()

    launched = int(status_counts.get("launched", 0))
    killed   = int(status_counts.get("killed", 0))
    pursued  = launched + killed + int(status_counts.get("poc", 0))

    # Stale winners: scored well, never pursued, older than 30 days
    cutoff = (datetime.now() - timedelta(days=30)).isoformat()
    stale = df[(df["score"] >= 7.5)
               & (df["status"].isin(["generated", "onepager"]))
               & (df["timestamp"] < cutoff)]

    # Status funnel in lifecycle order
    funnel = {s: int(status_counts.get(s, 0)) for s in STATUS_ORDER if status_counts.get(s, 0)}

    # Score distribution (0.5-wide buckets from threshold-ish range)
    bins = [round(b * 0.5, 1) for b in range(8, 21)]  # 4.0 .. 10.0
    hist = {}
    for lo in bins:
        n = int(((df["score"] >= lo) & (df["score"] < lo + 0.5)).sum())
        if n:
            hist[f"{lo:.1f}"] = n

    # Industry yield: which inputs produce keepers
    industry_counts = df["industry"].value_counts().head(10).to_dict()

    tiles = f"""
    <div class="tiles">
      <div class="tile"><div class="tile-value">{total}</div><div class="tile-label">ideas logged</div></div>
      <div class="tile"><div class="tile-value">{avg_score:.1f}</div><div class="tile-label">avg score /10</div></div>
      <div class="tile"><div class="tile-value">{pursued}</div><div class="tile-label">pursued (poc+)</div></div>
      <div class="tile"><div class="tile-value">{launched}</div><div class="tile-label">launched</div></div>
      <div class="tile"><div class="tile-value">{len(stale)}</div><div class="tile-label">stale 7.5+ scorers</div></div>
    </div>"""

    stale_section = ""
    if not stale.empty:
        rows = "".join(
            f"<tr><td><code>{e(r['hash'][:8])}</code></td><td>{e(idea_title(r['idea']))}</td>"
            f"<td class='num'>{r['score']}</td><td>{e(r['timestamp'][:10])}</td></tr>"
            for _, r in stale.sort_values("score", ascending=False).head(10).iterrows()
        )
        stale_section = f"""
    <section>
      <h2>⚠️ High scorers gathering dust</h2>
      <p class="hint">Scored ≥7.5 over 30 days ago, never taken past a one-pager.
      Validate or kill them: <code>python validate.py --hash &lt;hash&gt;</code></p>
      <table><thead><tr><th>hash</th><th>idea</th><th class="num">score</th><th>generated</th></tr></thead>
      <tbody>{rows}</tbody></table>
    </section>"""

    recent_rows = "".join(
        f"<tr><td><code>{e(r['hash'][:8])}</code></td><td>{e(idea_title(r['idea']))}</td>"
        f"<td class='num'>{r['score']}</td>"
        f"<td class='num'>{'' if pd.isna(r.get('validation_score')) else r['validation_score']}</td>"
        f"<td>{e(r['status'])}</td><td>{e(r['industry'])}</td><td>{e(r['timestamp'][:10])}</td></tr>"
        for _, r in df.sort_values("timestamp", ascending=False).head(40).iterrows()
    )

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Idea Portfolio</title>
<style>
  .viz-root {{
    color-scheme: light;
    --surface-1: #fcfcfb; --page: #f9f9f7;
    --text-primary: #0b0b0b; --text-secondary: #52514e; --muted: #898781;
    --grid: #e1e0d9; --border: rgba(11,11,11,0.10);
    --bar: #2a78d6; --track: #f0efec;
  }}
  @media (prefers-color-scheme: dark) {{
    :root:where(:not([data-theme="light"])) .viz-root {{
      color-scheme: dark;
      --surface-1: #1a1a19; --page: #0d0d0d;
      --text-primary: #ffffff; --text-secondary: #c3c2b7; --muted: #898781;
      --grid: #2c2c2a; --border: rgba(255,255,255,0.10);
      --bar: #3987e5; --track: #262624;
    }}
  }}
  :root[data-theme="dark"] .viz-root {{
    color-scheme: dark;
    --surface-1: #1a1a19; --page: #0d0d0d;
    --text-primary: #ffffff; --text-secondary: #c3c2b7; --muted: #898781;
    --grid: #2c2c2a; --border: rgba(255,255,255,0.10);
    --bar: #3987e5; --track: #262624;
  }}
  * {{ margin: 0; box-sizing: border-box; }}
  body.viz-root {{ font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
    background: var(--page); color: var(--text-primary);
    max-width: 960px; margin: 0 auto; padding: 2rem 1.25rem; line-height: 1.5; }}
  h1 {{ font-size: 1.5rem; margin-bottom: .25rem; }}
  .sub {{ color: var(--text-secondary); margin-bottom: 1.5rem; }}
  h2 {{ font-size: 1.05rem; margin-bottom: .75rem; }}
  section {{ background: var(--surface-1); border: 1px solid var(--border);
    border-radius: 12px; padding: 1.25rem; margin-bottom: 1.25rem; }}
  .hint {{ color: var(--muted); font-size: .85rem; margin-bottom: .75rem; }}
  .tiles {{ display: grid; gap: 1rem; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    margin-bottom: 1.25rem; }}
  .tile {{ background: var(--surface-1); border: 1px solid var(--border);
    border-radius: 12px; padding: 1rem 1.25rem; }}
  .tile-value {{ font-size: 1.9rem; font-weight: 650; }}
  .tile-label {{ color: var(--text-secondary); font-size: .85rem; }}
  .hbar-row {{ display: grid; grid-template-columns: 130px 1fr 3.5ch; align-items: center;
    gap: .6rem; padding: .22rem 0; }}
  .hbar-row:hover .hbar-fill {{ opacity: .85; }}
  .hbar-label {{ font-size: .85rem; color: var(--text-secondary);
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
  .hbar-track {{ background: var(--track); border-radius: 4px; height: 14px; display: block; }}
  .hbar-fill {{ background: var(--bar); border-radius: 0 4px 4px 0; height: 100%; display: block; }}
  .hbar-value {{ font-size: .85rem; color: var(--text-primary);
    font-variant-numeric: tabular-nums; text-align: right; }}
  table {{ width: 100%; border-collapse: collapse; font-size: .85rem; }}
  th {{ text-align: left; color: var(--muted); font-weight: 500;
    border-bottom: 1px solid var(--grid); padding: .35rem .5rem; }}
  td {{ border-bottom: 1px solid var(--grid); padding: .35rem .5rem; vertical-align: top; }}
  td.num, th.num {{ text-align: right; font-variant-numeric: tabular-nums; }}
  tr:hover td {{ background: var(--track); }}
  code {{ font-size: .8rem; color: var(--text-secondary); }}
  .table-wrap {{ overflow-x: auto; }}
</style>
</head>
<body class="viz-root">
<h1>Idea Portfolio</h1>
<p class="sub">Generated {datetime.now():%Y-%m-%d %H:%M} · {total} ideas ·
regenerate with <code>python dashboard.py</code></p>
{tiles}
<section>
  <h2>Pipeline status</h2>
  {hbar_rows(funnel, max(funnel.values()) if funnel else 0)}
</section>
<section>
  <h2>Score distribution</h2>
  {hbar_rows(hist, max(hist.values()) if hist else 0)}
</section>
<section>
  <h2>Ideas by industry</h2>
  {hbar_rows(industry_counts, max(industry_counts.values()) if industry_counts else 0)}
</section>
{stale_section}
<section>
  <h2>Recent ideas</h2>
  <div class="table-wrap">
  <table><thead><tr><th>hash</th><th>idea</th><th class="num">score</th>
  <th class="num">validation</th><th>status</th><th>industry</th><th>date</th></tr></thead>
  <tbody>{recent_rows}</tbody></table>
  </div>
</section>
</body>
</html>
"""


def main():
    parser = argparse.ArgumentParser(description="Generate the idea portfolio dashboard.")
    parser.add_argument("--out", default="dashboard.html")
    args = parser.parse_args()

    if not LOG_PATH.exists():
        sys.exit("No idea log yet. Run main.py first.")

    df = load_log()
    Path(args.out).write_text(build_html(df))
    print(f"Dashboard written to {args.out}")


if __name__ == "__main__":
    main()
