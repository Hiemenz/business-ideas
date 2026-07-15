#!/usr/bin/env python3
"""Generate a self-contained landing page for an idea — the cheapest real
market test: put it in front of people and count waitlist signups.

Gemini writes the copy; this renders it into a single static HTML file in
landing_pages/ that can be dropped onto any static host (GitHub Pages,
Netlify, Cloudflare Pages).

The waitlist form posts to FORM_ENDPOINT — create a free form at
https://formspree.io, then either set the FORM_ENDPOINT env var or edit
the generated file. Without it the button falls back to a mailto: link.

Usage:
    python landing.py                 # top-scored idea without a landing page
    python landing.py --hash ab12     # specific idea by hash prefix
"""
import argparse
import html
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

from gemini_client import call_gemini, parse_json_block
from idea_log import LOG_PATH, load_log

load_dotenv()

OUTDIR   = Path("landing_pages")
FORM_ENDPOINT = os.getenv("FORM_ENDPOINT", "")


def generate_copy(idea_text):
    prompt = (
        "Write landing-page copy for this business idea. Punchy, specific, "
        "benefit-led — no filler like 'revolutionary' or 'game-changing'.\n\n"
        f"{idea_text[:2000]}\n\n"
        "Return ONLY compact JSON:\n"
        "{"
        '"name": "<product name, 1-3 words>", '
        '"headline": "<outcome-focused headline, max 10 words>", '
        '"subhead": "<one sentence: what it is and who it is for>", '
        '"pains": ["<pain 1>", "<pain 2>", "<pain 3>"], '
        '"benefits": [{"title": "<benefit>", "desc": "<one sentence>"}, {"title": "...", "desc": "..."}, {"title": "...", "desc": "..."}], '
        '"cta": "<call to action button text, 2-4 words>"'
        "}"
    )
    return parse_json_block(call_gemini(prompt, max_tokens=512, temperature=0.7))


def render_page(copy, form_endpoint=""):
    e = html.escape
    pains = "".join(f"<li>{e(p)}</li>" for p in copy["pains"])
    benefits = "".join(
        f'<div class="card"><h3>{e(b["title"])}</h3><p>{e(b["desc"])}</p></div>'
        for b in copy["benefits"]
    )
    if form_endpoint:
        form = (
            f'<form action="{e(form_endpoint)}" method="POST" class="waitlist">'
            '<input type="email" name="email" placeholder="you@email.com" required>'
            f'<button type="submit">{e(copy["cta"])}</button></form>'
        )
    else:
        # No form backend configured — mailto fallback still counts interest
        form = (
            '<a class="waitlist-btn" href="mailto:?subject=Waitlist%20signup%20-%20'
            f'{e(copy["name"])}">{e(copy["cta"])}</a>'
            "<p class='hint'>Set FORM_ENDPOINT (e.g. a free formspree.io form) to collect emails properly.</p>"
        )

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(copy["name"])} — {e(copy["headline"])}</title>
<style>
  :root {{ color-scheme: light dark; }}
  * {{ margin: 0; box-sizing: border-box; }}
  body {{ font-family: system-ui, sans-serif; line-height: 1.6;
         max-width: 720px; margin: 0 auto; padding: 2rem 1.25rem; }}
  header {{ text-align: center; padding: 3rem 0 2rem; }}
  h1 {{ font-size: 2.4rem; line-height: 1.15; margin-bottom: 1rem; }}
  .subhead {{ font-size: 1.2rem; opacity: .8; }}
  section {{ margin: 2.5rem 0; }}
  h2 {{ font-size: 1.3rem; margin-bottom: 1rem; }}
  ul.pains {{ padding-left: 1.2rem; }}
  ul.pains li {{ margin: .5rem 0; }}
  .cards {{ display: grid; gap: 1rem; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); }}
  .card {{ border: 1px solid rgba(128,128,128,.35); border-radius: 10px; padding: 1rem; }}
  .card h3 {{ margin-bottom: .4rem; font-size: 1.05rem; }}
  .cta {{ text-align: center; padding: 2rem 0 3rem; }}
  .waitlist {{ display: flex; gap: .5rem; justify-content: center; flex-wrap: wrap; }}
  .waitlist input {{ padding: .75rem 1rem; border-radius: 8px; border: 1px solid rgba(128,128,128,.5);
                     font-size: 1rem; min-width: 240px; }}
  .waitlist button, .waitlist-btn {{ padding: .75rem 1.5rem; border-radius: 8px; border: none;
      background: #2563eb; color: #fff; font-size: 1rem; font-weight: 600;
      cursor: pointer; text-decoration: none; display: inline-block; }}
  .hint {{ font-size: .8rem; opacity: .6; margin-top: .75rem; }}
  footer {{ text-align: center; font-size: .85rem; opacity: .6; padding: 2rem 0; }}
</style>
</head>
<body>
<header>
  <h1>{e(copy["headline"])}</h1>
  <p class="subhead">{e(copy["subhead"])}</p>
</header>
<section class="cta">{form}</section>
<section>
  <h2>Sound familiar?</h2>
  <ul class="pains">{pains}</ul>
</section>
<section>
  <h2>What {e(copy["name"])} does</h2>
  <div class="cards">{benefits}</div>
</section>
<section class="cta">{form}</section>
<footer>© {e(copy["name"])} — early access coming soon.</footer>
</body>
</html>
"""


def main():
    parser = argparse.ArgumentParser(description="Generate a waitlist landing page for an idea.")
    parser.add_argument("--hash", default="", help="Idea hash prefix (default: top-scored without a page)")
    args = parser.parse_args()

    if not LOG_PATH.exists():
        sys.exit("No idea log yet. Run main.py first.")
    df = load_log()

    OUTDIR.mkdir(exist_ok=True)
    existing = {p.stem.split("-")[-1] for p in OUTDIR.glob("*.html")}

    if args.hash:
        matches = df[df["hash"].str.startswith(args.hash)]
        if matches.empty:
            sys.exit(f"No idea with hash starting '{args.hash}'.")
        row = matches.iloc[0]
    else:
        pending = df[~df["hash"].str[:8].isin(existing)].sort_values("score", ascending=False)
        if pending.empty:
            sys.exit("Every idea already has a landing page.")
        row = pending.iloc[0]

    print(f"Writing landing-page copy for: {str(row['idea']).split(chr(10))[0][:80]}")
    copy = generate_copy(row["idea"])
    page = render_page(copy, FORM_ENDPOINT)

    slug = "".join(c if c.isalnum() else "-" for c in copy["name"].lower()).strip("-")
    path = OUTDIR / f"{slug}-{row['hash'][:8]}.html"
    path.write_text(page)
    print(f"-> {path}\nOpen it locally or deploy to any static host; "
          "waitlist signups are your validation metric.")


if __name__ == "__main__":
    main()
