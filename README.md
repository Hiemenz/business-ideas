# Business Idea Generator

Generates, scores, deduplicates, and expands business ideas using Google Gemini.
Optionally renders the top ideas to a Waveshare 7.5" e-ink display on a Raspberry Pi.

## Pipeline at a glance

```
main.py          — generate 5 ideas, dedupe via embeddings, score, log to parquet
validate.py      — external validation signals (Reddit pain-mining, Hacker News)
onepager.py      — expand top-scored ideas into full one-pager markdown
landing.py       — generate a static waitlist landing page for an idea
status.py        — track idea outcomes (generated → onepager → poc → launched|killed)
digest.py        — weekly top-ideas digest (stdout + Discord webhook)
dashboard.py     — static HTML portfolio dashboard from the parquet log
display.py       — render the next pending idea to e-ink (Pi only)
discord_bot.py   — interactive idea generation + !rate over Discord
ratings.py       — your 1-5 ratings vs Gemini's scores (calibration report)
```

Shared modules: `gemini_client.py` (all Gemini calls, rate-limited),
`idea_log.py` (parquet schema + migration), `trends.py` (trend/Reddit/arXiv
context), `render.py` (e-ink PNG).

### The idea lifecycle

1. `main.py` generates and scores ideas (cron-friendly).
2. `validate.py` adds outside evidence — are people complaining about this
   problem? Is anyone shipping in this space?
3. `onepager.py` expands winners (now includes **First 10 Customers** and
   **Cost to Validate** sections).
4. `landing.py` builds a waitlist page — signups are the real market test.
5. `status.py set <hash> poc|launched|killed --note "why"` records what
   happened; killed/launched outcomes are fed back into the generation
   prompt so the generator learns from real results.
6. `digest.py` (cron, Mondays) surfaces the week's top ideas plus stale
   high-scorers; `dashboard.py` shows the whole portfolio.

---

## Prerequisites

- Python 3.10+
- A Google Gemini API key (free tier at [ai.google.dev](https://ai.google.dev))

No other API keys are needed. Trends and idea generation both use the same key.

---

## Mac Setup

### 1. Clone or download the project

```bash
git clone <your-repo-url>
cd business_ideas
```

### 2. Install dependencies (Poetry)

```bash
poetry install
```

Run any script with `poetry run python <script>.py` (or `poetry shell` once).

### 3. Set your API key

Copy the template and fill in your key — scripts auto-load `.env` via
python-dotenv:

```bash
cp .env.example .env
# edit .env and set GEMINI_API_KEY
```

The default model is `gemini-2.5-flash` (Google zeroed out free-tier quota
for `gemini-2.0-flash`; override with `GEMINI_MODEL` in `.env` if needed).

### 4. Run the pipeline

Generate and score ideas:

```bash
poetry run python main.py
```

Fetch external validation signals for the top unvalidated ideas:

```bash
poetry run python validate.py --top 3
```

Expand the top ideas into one-pagers (saved to `onepagers/`):

```bash
poetry run python onepager.py --top 3
```

Build a waitlist landing page for the best idea (saved to `landing_pages/`;
set `FORM_ENDPOINT` in `.env` to a free formspree.io form to collect emails):

```bash
poetry run python landing.py
```

Track outcomes and review the portfolio:

```bash
poetry run python status.py list
poetry run python status.py set ab12cd34 killed --note "no search demand"
poetry run python dashboard.py     # writes dashboard.html
poetry run python digest.py        # weekly summary; posts to Discord if configured
```

Note: Reddit blocks unauthenticated API access from some networks (you'll
see 403s). Validation scores normalize to the sources that respond, so this
degrades gracefully.

---

## Raspberry Pi Setup

The Pi runs `display.py` to push ideas to a Waveshare 7.5" e-ink display.
You can either run the full pipeline on the Pi or just the display driver
(syncing the parquet file from your Mac).

### 1. Flash Raspberry Pi OS

Use the [Raspberry Pi Imager](https://www.raspberrypi.com/software/) to write
Raspberry Pi OS (Desktop or Lite) to your SD card. During setup:

- Set a hostname, username, and password.
- Configure Wi-Fi.
- Enable SSH if you plan to work headless.

### 2. Enable SPI (required for the e-ink display)

```bash
sudo raspi-config
```

Navigate to **Interface Options > SPI** and enable it. Reboot.

### 3. Install system dependencies

The Waveshare driver needs the GPIO and SPI libraries:

```bash
sudo apt update
sudo apt install -y python3-pip python3-venv python3-dev lgpio
```

### 4. Create a virtual environment and install packages

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pyaml numpy pandas pyarrow requests Pillow waveshare-epd
```

`waveshare-epd` is the official Waveshare Python driver. If your display is a
different model, check the driver package name on the
[Waveshare wiki](https://www.waveshare.com/wiki/Main_Page).

### 5. Set your API key (if running the full pipeline on the Pi)

Same as Mac — export `GEMINI_API_KEY` in your shell or `.env`.

If you're only running `display.py` and syncing the parquet from your Mac,
no API key is needed on the Pi.

### 6. Wire the e-ink display

Connect the Waveshare 7.5" v2 to the Pi's GPIO header using the cable that
ships with the display. Pin mapping (BCM):

| Display pin | Pi GPIO |
|---|---|
| RST  | 17 |
| CE   | 8  |
| DC   | 24 |
| DIN  | 10 |
| CLK  | 11 |
| VCC  | 3.3V |
| GND  | GND  |

### 7. Sync the parquet file (if not running the pipeline on the Pi)

From your Mac, copy the log file to the Pi:

```bash
scp money_making_ideas_log.parquet pi@<pi-ip>:/path/to/project/
```

### 8. Run the display driver

```bash
python display.py
```

It picks the highest-scored idea that hasn't been displayed yet, renders it
to a 1304x975 B&W PNG, and pushes it to the e-ink panel.

### 9. Automate with cron

To refresh the display every morning at 8 AM:

```bash
crontab -e
```

Add this line (adjust the paths to match your setup):

```
0 8 * * * /path/to/.venv/bin/python /path/to/project/display.py
```

If you want to run the full pipeline on the Pi on a schedule as well (e.g.
generate new ideas every 6 hours), add another entry:

```
0 */6 * * * GEMINI_API_KEY=AIza... /path/to/.venv/bin/python /path/to/project/main.py
```

---

## Migrating from OpenAI

If you previously ran this project with OpenAI, the embedding vectors stored
in `embeddings.pkl` are incompatible — OpenAI used 1536 dimensions,
Gemini `text-embedding-004` uses 768. Delete the file before your first run:

```bash
rm embeddings.pkl
```

The dedup store will rebuild from scratch on the next run. Previously logged
ideas in the parquet file are unaffected.

---

## Future Improvements

### Foundations

- [x] **Make it a git repo** — done, with `.gitignore` covering secrets and caches.
- [x] **Add a `.env.example`** — done.
- [x] **Sync the README with reality** — done (Poetry install, all scripts documented).

### Code quality

- [ ] **Real tests** — replace the lone `test_gem.py` script with a `pytest`
  suite in `tests/` covering `is_duplicate` cosine-similarity behavior,
  `pick_combo` rotation-window logic, parquet column migration, and
  trend-cache TTL expiry.
- [x] **Extract shared code** — done: `gemini_client.py` owns all API calls +
  throttling; `idea_log.py` owns the parquet schema and migration.
- [ ] **Replace pickle with JSON for embeddings** — `embeddings.pkl` is
  unversioned binary; the stored `{"model": ..., "vec": ...}` dicts
  serialize trivially to JSON, which diffs better and is safe to load.
- [ ] **Structured logging** — use the `logging` module with levels instead of
  bare `print`, so failures in unattended cron runs on the Pi don't vanish.

### Features / workflow

- [ ] **CLI entry point** — `argparse` or `typer` with subcommands
  (`generate`, `score`, `onepager --top 3`, `display`) wired up via Poetry's
  `[project.scripts]`.
- [ ] **Index for `proof-of-concepts/`** — a generated `INDEX.md` (or a
  parquet column linking idea → one-pager → POC status) to make the ~38
  numbered markdown files browsable and track which ideas are being pursued.
- [ ] **CI** — GitHub Actions running `pytest` + `ruff` on push, once the
  repo is on GitHub.
- [x] **Score-drift guard** — done: malformed scores are validated, missing
  ones retried per-idea, still-unscored ideas logged with status `unscored`.
- [ ] **Reddit OAuth** — Reddit blocks anonymous JSON from many networks;
  registering a free script app and using OAuth would restore the Reddit
  signals in `trends.py` and `validate.py` everywhere.
- [ ] **Calibrated score weights** — once `!rate` has collected ~50 ratings,
  use `python ratings.py` correlation output to reweight the four sub-scores.
