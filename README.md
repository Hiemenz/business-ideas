# Business Idea Generator

Generates, scores, validates, and expands business ideas using Google Gemini.
Optionally renders the top ideas to a Waveshare 7.5" e-ink display on a Raspberry Pi.

## Pipeline at a glance

```
main.py          — generate ideas, dedupe via embeddings, score, log to parquet
validate.py      — external validation signals (Reddit pain-mining, Hacker News)
onepager.py      — expand top-scored ideas into full one-pager markdown
landing.py       — generate a static waitlist landing page for an idea
status.py        — track idea outcomes (generated → onepager → poc → launched|killed)
digest.py        — weekly top-ideas digest (stdout + Discord webhook)
dashboard.py     — static HTML portfolio dashboard from the parquet log
ratings.py       — calibration report: your ratings vs Gemini's scores
discord_bot.py   — interactive idea generation + rating over Discord
display.py       — render the next pending idea to e-ink (Pi only)
```

Shared modules: `gemini_client.py` (all Gemini calls, rate-limited + retried),
`idea_log.py` (parquet schema + migration), `trends.py` (trend/Reddit/arXiv context).

### The idea lifecycle

```
main.py → validate.py → onepager.py → landing.py
                                           ↓
                                     status.py set <hash> poc|launched|killed
                                           ↓
                              digest.py / dashboard.py (review + surface)
```

1. `main.py` generates and scores ideas; outcome feedback from past runs is injected into the prompt so the generator learns from what worked and what didn't.
2. `validate.py` adds outside evidence — are people complaining about this problem on Reddit? Is anyone shipping in this space on HN?
3. `onepager.py` expands winners into a full business plan with revenue projections, roadmap, and risks.
4. `landing.py` builds a static waitlist page — signups are the real market test.
5. `status.py set <hash> poc|launched|killed --note "why"` records what happened.
6. `digest.py` (cron, Mondays) surfaces the week's top ideas plus stale high-scorers; `dashboard.py` shows the whole portfolio.

---

## Prerequisites

- Python 3.10+, Poetry
- A Google Gemini API key (free tier at [ai.google.dev](https://ai.google.dev))

No other API keys are required. Reddit and arXiv use public endpoints. Discord is optional.

---

## Setup

### 1. Clone and install

```bash
git clone https://github.com/Hiemenz/business-ideas
cd business-ideas
poetry install
```

### 2. Configure secrets

```bash
cp .env.example .env
# edit .env — set GEMINI_API_KEY at minimum
```

Scripts auto-load `.env` via python-dotenv. The default model is `gemini-2.5-flash`; override with `GEMINI_MODEL` in `.env` if needed.

### 3. Run the pipeline

Generate and score ideas:

```bash
poetry run python main.py
```

Fetch external validation for the top 3 unvalidated ideas:

```bash
poetry run python validate.py --top 3
```

Expand top ideas into one-pagers (saved to `onepagers/`):

```bash
poetry run python onepager.py --top 3
```

Build a waitlist landing page for the best idea (saved to `landing_pages/`):

```bash
poetry run python landing.py
```

Review and track the portfolio:

```bash
poetry run python status.py list
poetry run python status.py set ab12cd34 killed --note "no search demand"
poetry run python status.py set ab12cd34 poc

poetry run python dashboard.py      # writes dashboard.html
poetry run python digest.py         # weekly summary; posts to Discord if configured
poetry run python ratings.py        # score calibration report
```

### 4. Automate with cron

```cron
# Generate ideas every 6 hours
0 */6 * * * cd /path/to/project && /path/to/.venv/bin/python main.py

# Weekly digest on Monday at 9am
0 9 * * 1 cd /path/to/project && /path/to/.venv/bin/python digest.py
```

---

## Discord bot (optional)

Set `DISCORD_BOT_TOKEN` in `.env`, then:

```bash
poetry run python discord_bot.py
```

Commands: `!idea` (generate), `!rate <hash> <1-5>` (rate an idea), `!top` (top-scored), `!status <hash> <status>`.

---

## Raspberry Pi / e-ink display (optional)

`display.py` pushes the next pending idea to a Waveshare 7.5" v2 e-ink display.

### 1. Flash Raspberry Pi OS

Use the [Raspberry Pi Imager](https://www.raspberrypi.com/software/). During setup, configure Wi-Fi and enable SSH if working headless.

### 2. Enable SPI

```bash
sudo raspi-config
# Interface Options > SPI > Enable, then reboot
```

### 3. Install dependencies

```bash
sudo apt update && sudo apt install -y python3-pip python3-venv python3-dev lgpio
python3 -m venv .venv
source .venv/bin/activate
pip install pyaml numpy pandas pyarrow requests Pillow waveshare-epd
```

### 4. Wire the display

| Display pin | Pi GPIO (BCM) |
|---|---|
| RST  | 17 |
| CE   | 8  |
| DC   | 24 |
| DIN  | 10 |
| CLK  | 11 |
| VCC  | 3.3V |
| GND  | GND  |

### 5. Sync and run

If running ideas on your Mac and displaying on the Pi, sync the log file:

```bash
scp money_making_ideas_log.parquet pi@<pi-ip>:/path/to/project/
```

Then on the Pi:

```bash
python display.py
```

Cron to refresh the display every morning at 8am:

```cron
0 8 * * * /path/to/.venv/bin/python /path/to/project/display.py
```

---

## Configuration

`config.yml` controls batch size, score threshold, similarity threshold for dedup, RPM limits, and the pools of industries, business models, audiences, etc. that are randomly combined per idea.

---

## Idea-discovery loop (Claude Code)

Separate from the Python/Gemini pipeline above, this repo also accumulates freeform
idea-discovery markdown written by Claude Code itself, in three parallel series:

```
discovered-problems/   — broad business-problem discovery by sector, unscored
side-income-ideas/     — solo-buildable side income ideas, $500-3K/mo ceiling
main-income-ideas/     — solo-buildable ideas with a credible path to $8-15K+/mo,
                          i.e. ideas that could realistically replace a full-time salary
```

Each series runs as a **recurring local loop, every 5 hours** (`0 */5 * * *`), started
with the `CronCreate` tool inside a Claude Code session. These jobs are session-only —
they die when the session ends and auto-expire after 7 days regardless — so the loop
needs to be re-armed periodically. To restart the `main-income-ideas/` loop, start a
Claude Code session in this repo and ask it to schedule a recurring job with this prompt:

> Run the recurring main-income idea discovery session for the `business-ideas` repo.
>
> **Builder profile:** 29, software engineering + data analytics skills. Goal is
> different from the existing `side-income-ideas/` series: not "$500-3K/mo of side
> money" but a solo-buildable path that can realistically replace a full-time salary
> (**$8-15K+/mo**) within 12-24 months if it works. Still has to start small,
> evenings/weekends, no funding, no cofounder.
>
> **Steps:**
> 1. List `main-income-ideas/` and find the highest existing `vN` file and its date
>    (if the directory is empty, this is v1).
> 2. Skim filenames/titles in `main-income-ideas/`, `side-income-ideas/`, and
>    `discovered-problems/` to build a mental list of concepts already covered — every
>    idea in this run must be a genuinely new sector/concept, not a repeat.
> 3. Write a new file `main-income-ideas/YYYY-MM-DD-main-income-vN.md` (today's date,
>    next session number) with 4-6 ideas, in the same structural style as
>    `side-income-ideas/*.md`, but scored against main-income ground rules instead of
>    side-income ones:
>    - **Solo-buildable start.** One person, evenings/weekends, no funding, no
>      cofounder required to get the first version live.
>    - **Realistic path to $8-15K+/mo**, not a side-money ceiling — state what that
>      scale actually requires (customer count x price point) plainly, no TAM
>      hand-waving.
>    - **Time to first dollar < 90 days.** Long enterprise sales cycles are
>      disqualifying by default.
>    - **Named distribution channel** for the first 10 customers AND a credible path
>      to the next 10x (the part that turns "side" into "main").
>    - **Boring is fine.** Low-glamour, real-pain problems beat trendy ones.
>    - **No repeats** of anything already covered across `main-income-ideas/`,
>      `side-income-ideas/`, or `discovered-problems/`.
>    - Each idea needs: Problem, What to build, Skill fit, MVP scope, Time to first $,
>      Income ceiling (realistic, with the math), Why this can go beyond side money,
>      Biggest risk, Growth path (side project → replaces-salary stage by stage).
> 4. Add a scoring summary table and a "This session's pick" section explaining which
>    idea has the clearest path to full-time income and why.
> 5. End the file with a line: `Cron Loop: 0 */5 * * *` continues.
> 6. Do not touch `side-income-ideas/` or `discovered-problems/` — this is a separate
>    series. Do not commit or push (these files stay local/uncommitted like the rest
>    of the series unless the user asks otherwise).

If you'd rather it run unattended in the cloud (independent of this machine staying
on), commit and push these directories first, then create a claude.ai routine
(`/schedule`) pointed at this repo with the same prompt — cloud routines poll a fresh
GitHub checkout, so they can't see local uncommitted files.

---

## Notes

- **Reddit 403s** — Reddit blocks unauthenticated requests from some networks. Validation scores normalize to the sources that responded, so this degrades gracefully.
- **Embeddings** — `embeddings.pkl` stores embedding vectors for semantic dedup. If you switch embedding models, delete this file and let it rebuild.
- **Schema migration** — `idea_log.py` handles parquet column migration automatically; older log files are upgraded on first load, no manual steps needed.
