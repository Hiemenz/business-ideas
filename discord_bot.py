import os
import random
import asyncio
import functools

import yaml
import discord
from dotenv import load_dotenv

from trends import fetch_trends, fetch_reddit_ideas, fetch_arxiv_papers
from onepager import generate_onepager
from gemini_client import call_gemini, build_prompt, score_ideas
from pi_terminal import TerminalManager

load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Discord user IDs allowed to open terminal sessions on this machine.
# Empty by default (fail closed) — set TERMINAL_ADMIN_IDS="123,456" in .env to enable.
TERMINAL_ADMIN_IDS = {
    int(uid) for uid in os.getenv("TERMINAL_ADMIN_IDS", "").split(",") if uid.strip()
}
TERMINAL_WORKDIR = os.getenv("TERMINAL_WORKDIR")  # defaults to this process's cwd if unset

terminals = TerminalManager(command=["claude"], cwd=TERMINAL_WORKDIR)

# Load config
with open("config.yml") as f:
    CONFIG = yaml.safe_load(f)

STEPS = [
    "industry", "business_model", "audience",
    "technology", "problem", "platform", "monetization",
]

STEP_LABELS = {
    "industry":       "Industry",
    "business_model": "Business model",
    "audience":       "Audience",
    "technology":     "Technology",
    "problem":        "Problem to solve",
    "platform":       "Platform",
    "monetization":   "Monetization",
}

CONFIG_KEYS = {
    "industry":       "industries",
    "business_model": "business_models",
    "audience":       "audiences",
    "technology":     "technologies",
    "problem":        "problems",
    "platform":       "platforms",
    "monetization":   "monetization",
}

sessions: dict  = {}   # user_id -> {"step": int, "choices": dict}
last_idea: dict = {}   # user_id -> (idea_text, score) for !onepager

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


# ==== CONVERSATION HELPERS ====

def options_for_step(step):
    return CONFIG[CONFIG_KEYS[step]]


def build_question(step):
    options = options_for_step(step)
    label   = STEP_LABELS[step]
    numbered = "\n".join(f"{i+1}. {v}" for i, v in enumerate(options))
    return f"**{label}?** Reply with a number:\n{numbered}\n*(or type `random` to skip)*"


def parse_choice(text, options):
    """
    Returns the chosen value or None if the input is not valid.
    Accepts a 1-based digit string or 'random'.
    """
    if text.lower() == "random":
        return random.choice(options)
    if text.isdigit():
        n = int(text)
        if 1 <= n <= len(options):
            return options[n - 1]
    return None


# ==== ASYNC GENERATION ====

async def generate_idea(channel, combo):
    loop    = asyncio.get_running_loop()
    industry    = combo["industry"]
    subreddits  = CONFIG.get("subreddits", [])

    trends, reddit_ideas, arxiv_papers = await asyncio.gather(
        loop.run_in_executor(None, fetch_trends, industry),
        loop.run_in_executor(None, fetch_reddit_ideas, subreddits),
        loop.run_in_executor(None, fetch_arxiv_papers, industry),
    )

    prompt    = build_prompt(combo, trends, reddit_ideas, arxiv_papers)
    idea_text = await loop.run_in_executor(None, functools.partial(call_gemini, prompt))

    scores = await loop.run_in_executor(None, score_ideas, [idea_text])
    if scores:
        s = scores[0]
        composite = round(
            (s["market_size"] + s["feasibility"] + s["novelty"] + s["competition"]) / 4, 1
        )
    else:
        composite = 0.0

    return idea_text, composite


async def send_in_chunks(channel, text, code_block=False):
    """Send long text split into ≤1900-char messages."""
    wrap_open  = "```markdown\n" if code_block else ""
    wrap_close = "\n```"         if code_block else ""
    limit = 1900 - len(wrap_open) - len(wrap_close)
    for i in range(0, len(text), limit):
        chunk = text[i:i + limit]
        await channel.send(f"{wrap_open}{chunk}{wrap_close}")


# ==== DISCORD EVENTS ====

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    user_id    = message.author.id
    text       = message.content.strip()
    text_lower = text.lower()

    # ---- !status ----
    if text_lower == "!status":
        await message.channel.send("Pi is alive and running.")
        return

    # ---- !help ----
    if text_lower == "!help":
        help_text = (
            "**Commands:**\n"
            "`!status` — check if Pi is running\n"
            "`!explore` — guided business idea generator\n"
            "`!cancel` — cancel in-progress exploration\n"
            "`!onepager` — expand last idea into a full one-pager\n"
            "`!help` — show this message"
        )
        if user_id in TERMINAL_ADMIN_IDS:
            help_text += (
                "\n\n**Terminal (admin):**\n"
                "`!term start` — open a Claude terminal session on the Pi\n"
                "`!term stop` — end the session\n"
                "`!term clear` — send `/clear` to reset context, session stays alive\n"
                "`!term status` — check if a session is running\n"
                "`!t <text>` — send a line of input to the running session"
            )
        await message.channel.send(help_text)
        return

    # ---- !term ... (admin-only terminal sessions) ----
    if text_lower.startswith("!term"):
        if user_id not in TERMINAL_ADMIN_IDS:
            await message.channel.send("Not authorized to use terminal sessions.")
            return

        sub = text[len("!term"):].strip().lower()

        if sub == "start":
            if terminals.has_session(user_id):
                await message.channel.send("Session already running. Use `!term stop` first.")
                return

            async def on_output(chunk, channel=message.channel):
                await send_in_chunks(channel, chunk, code_block=True)

            terminals.start(user_id, on_output)
            await message.channel.send("Terminal session started. Send input with `!t <text>`.")
            return

        if sub == "stop":
            if not terminals.has_session(user_id):
                await message.channel.send("No active session.")
                return
            terminals.stop(user_id)
            await message.channel.send("Session stopped.")
            return

        if sub == "clear":
            try:
                terminals.clear(user_id)
            except RuntimeError:
                await message.channel.send("No active session.")
                return
            await message.channel.send("Sent `/clear` — context reset, session still running.")
            return

        if sub == "status":
            running = terminals.has_session(user_id)
            await message.channel.send("Session is running." if running else "No active session.")
            return

        await message.channel.send("Usage: `!term start|stop|clear|status`")
        return

    # ---- !t <text> — send input to an active terminal session ----
    if text.startswith("!t "):
        if user_id not in TERMINAL_ADMIN_IDS:
            await message.channel.send("Not authorized to use terminal sessions.")
            return
        try:
            terminals.send(user_id, text[len("!t "):])
        except RuntimeError:
            await message.channel.send("No active session. Use `!term start` first.")
        return

    # ---- !explore ----
    if text_lower == "!explore":
        sessions[user_id] = {"step": 0, "choices": {}}
        await message.channel.send(
            "Let's build a business idea tailored to you!\n\n" + build_question(STEPS[0])
        )
        return

    # ---- !cancel ----
    if text_lower == "!cancel":
        if user_id in sessions:
            del sessions[user_id]
            await message.channel.send("Exploration cancelled.")
        else:
            await message.channel.send("No active exploration session.")
        return

    # ---- !onepager ----
    if text_lower == "!onepager":
        if user_id not in last_idea:
            await message.channel.send("No idea to expand yet. Use `!explore` first.")
            return

        idea_text, score = last_idea[user_id]
        await message.channel.send("Generating one-pager... this takes ~15 seconds ⏳")
        loop = asyncio.get_running_loop()
        try:
            onepager = await loop.run_in_executor(
                None, functools.partial(generate_onepager, idea_text, score)
            )
        except Exception as e:
            await message.channel.send(f"One-pager generation failed: {e}")
            return

        await send_in_chunks(message.channel, onepager, code_block=True)
        return

    # ---- In-session reply ----
    if user_id not in sessions:
        return

    session  = sessions[user_id]
    step_idx = session["step"]
    step_name = STEPS[step_idx]
    options   = options_for_step(step_name)

    chosen = parse_choice(text, options)
    if chosen is None:
        # Not a valid number or "random" — ignore (user may be chatting in the same channel)
        return

    session["choices"][step_name] = chosen
    step_idx += 1
    session["step"] = step_idx

    if step_idx < len(STEPS):
        next_step = STEPS[step_idx]
        await message.channel.send(
            f"**{STEP_LABELS[step_name]}** locked in: *{chosen}*\n\n"
            + build_question(next_step)
        )
    else:
        # All steps done — run generation
        combo = dict(session["choices"])
        del sessions[user_id]

        summary = "\n".join(
            f"- **{STEP_LABELS[k]}:** {v}" for k, v in combo.items()
        )
        await message.channel.send(
            f"All choices locked in:\n{summary}\n\n"
            "Fetching market data and generating your idea... ⏳"
        )

        try:
            idea_text, score = await generate_idea(message.channel, combo)
        except Exception as e:
            await message.channel.send(f"Generation failed: {e}")
            return

        last_idea[user_id] = (idea_text, score)
        score_line = f"\n\n**Viability score: {score}/10**" if score else ""
        await send_in_chunks(message.channel, idea_text + score_line)
        await message.channel.send("Type `!onepager` to get the full business plan expansion.")


client.run(TOKEN)
