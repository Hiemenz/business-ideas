# Business Idea Generator

Generates, scores, deduplicates, and expands business ideas using Google Gemini.
Optionally renders the top ideas to a Waveshare 7.5" e-ink display on a Raspberry Pi.

## Pipeline at a glance

```
main.py          — generate 5 ideas, dedupe via embeddings, score, log to parquet
onepager.py      — expand top-scored ideas into full one-pager markdown
display.py       — render the next pending idea to e-ink (Pi only)
```

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

### 2. Create a virtual environment and install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pyaml numpy pandas pyarrow requests Pillow
```

### 3. Set your API key

Option A — export it in your shell (lasts for the current session):

```bash
export GEMINI_API_KEY="AIza..."
```

Option B — create a `.env` file and source it before each run:

```bash
echo 'export GEMINI_API_KEY="AIza..."' > .env
source .env
```

Option C — if you use an IDE or tool that auto-loads `.env`, just put the
`export` line in that file and it will be picked up automatically.

### 4. Run the pipeline

Generate and score ideas:

```bash
python main.py
```

Expand the top ideas into one-pagers (all new ideas, or just the top N):

```bash
python onepager.py
python onepager.py --top 3
```

One-pagers are saved to `onepagers/`.

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

- [ ] **Make it a git repo** — `git init`, plus a `.gitignore` for `__pycache__/`,
  `.venv/`, `.env`, `embeddings.pkl`, `trends_cache.json`, and the parquet log.
  The `.env` file holds the Gemini API key and must never be committed.
- [ ] **Add a `.env.example`** documenting `GEMINI_API_KEY`, `GEMINI_MODEL`, and
  the Discord bot token, so setup is self-documenting without exposing secrets.
- [ ] **Sync the README with reality** — setup should say `poetry install`
  (the project uses Poetry, not manual `pip install`), and the README should
  cover `discord_bot.py`, `pi_terminal.py`, and the `proof-of-concepts/` folder.

### Code quality

- [ ] **Real tests** — replace the lone `test_gem.py` script with a `pytest`
  suite in `tests/` covering `is_duplicate` cosine-similarity behavior,
  `pick_combo` rotation-window logic, parquet column migration, and
  trend-cache TTL expiry.
- [ ] **Extract shared code** — consolidate config-loading, API-calling, and
  retry logic into `gemini_client.py` (owning `call_gemini`, `embed_text`,
  and throttling). Currently `embed_text` in `main.py` bypasses the rate
  limiter that `call_gemini` uses.
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
- [ ] **Score-drift guard** — when scoring returns fewer scores than ideas,
  retry the scoring call for the missing ones or log unscored ideas with a
  null score, instead of silently dropping generated (and paid-for) ideas.
