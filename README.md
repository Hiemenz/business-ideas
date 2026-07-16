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

## Notes

- **Reddit 403s** — Reddit blocks unauthenticated requests from some networks. Validation scores normalize to the sources that responded, so this degrades gracefully.
- **Embeddings** — `embeddings.pkl` stores embedding vectors for semantic dedup. If you switch embedding models, delete this file and let it rebuild.
- **Schema migration** — `idea_log.py` handles parquet column migration automatically; older log files are upgraded on first load, no manual steps needed.
