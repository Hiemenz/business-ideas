"""Renders a business idea to a B&W PNG sized for a Waveshare 7.5" e-ink display
(1304x975 native resolution). Produces a clean card layout with title, outline,
and revenue feasibility sections.

Can be tested on any machine — no e-ink hardware required:
    python -c "from render import render_idea; render_idea(open('sample.txt').read(), score=7.8)"
"""
import textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Waveshare 7.5" v2 native resolution
WIDTH, HEIGHT = 1304, 975
MARGIN = 48

# Font search order: works on both Linux (Pi) and macOS
_FONT_PATHS = {
    "regular": [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ],
    "bold": [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ],
}


def _load_font(style, size):
    for path in _FONT_PATHS[style]:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def _parse_sections(text):
    """Split ## markdown headings into {name: body_text}."""
    sections, name, lines = {}, None, []
    for line in text.split("\n"):
        if line.startswith("## "):
            if name:
                sections[name] = "\n".join(lines).strip()
            name, lines = line[3:].strip(), []
        elif name is not None:
            lines.append(line)
    if name:
        sections[name] = "\n".join(lines).strip()
    return sections


def _chars_per_line(font, max_width):
    """Estimate how many characters fit in max_width pixels for this font."""
    sample = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 "
    bbox = font.getbbox(sample)
    avg_char_width = (bbox[2] - bbox[0]) / len(sample)
    return max(20, int(max_width / avg_char_width))


def _draw_wrapped(draw, text, x, y, font, max_width, max_y, line_height=26):
    """Draw text with bullet support and word-wrap. Returns new y position."""
    wrap_at = _chars_per_line(font, max_width - 20)  # leave room for bullets

    for line in text.split("\n"):
        if y >= max_y:
            break
        line = line.strip()
        if not line:
            y += 10
            continue

        indent = 0
        bullet = False
        if line.startswith("- ") or line.startswith("* "):
            line = line[2:]
            bullet = True
            indent = 20

        wrapped = textwrap.wrap(line, width=wrap_at)
        for i, segment in enumerate(wrapped):
            if y >= max_y:
                break
            if i == 0 and bullet:
                draw.ellipse([(x, y + 9), (x + 7, y + 16)], fill="black")
            draw.text((x + indent, y), segment, fill="black", font=font)
            y += line_height

    return y


def render_idea(idea_text, output_path="idea.png", score=None):
    """Render a business idea markdown string to a B&W PNG.

    Args:
        idea_text:   Full idea string with ## Business Idea / ## Outline / ## Revenue Feasibility
        output_path: Where to save the PNG
        score:       Optional composite score float to display on the card
    """
    img = Image.new("1", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(img)

    f_title  = _load_font("bold",    30)
    f_header = _load_font("bold",    22)
    f_body   = _load_font("regular", 19)
    f_score  = _load_font("bold",    24)

    sections       = _parse_sections(idea_text)
    x              = MARGIN
    y              = MARGIN
    content_width  = WIDTH - MARGIN * 2
    bottom         = HEIGHT - MARGIN

    # --- outer border ---
    draw.rectangle([(2, 2), (WIDTH - 3, HEIGHT - 3)], outline="black", width=3)

    # --- score badge (top-right) ---
    if score is not None:
        badge = f"Score: {score}/10"
        bbox  = draw.textbbox((0, 0), badge, font=f_score)
        draw.text((WIDTH - MARGIN - (bbox[2] - bbox[0]), y), badge, fill="black", font=f_score)

    # --- fallback: no recognized ## sections -> render the raw text ---
    # (older log entries predate the structured format; a blank card helps no one)
    if not sections:
        draw.text((x, y), "BUSINESS IDEA", fill="black", font=f_title)
        y += 52
        _draw_wrapped(draw, idea_text, x, y, f_body, content_width, bottom)
        img.save(output_path)
        return output_path

    # --- Business Idea: name + description ---
    # GPT often returns "Name — description" on one line; split so the name
    # stays big and the description wraps cleanly below it.
    idea_block = sections.get("Business Idea", "").strip()
    if " — " in idea_block:
        name, rest = idea_block.split(" — ", 1)
    elif "\n" in idea_block:
        name, rest = idea_block.split("\n", 1)
    else:
        name, rest = idea_block, ""

    draw.text((x, y), name.strip(), fill="black", font=f_title)
    y += 42

    desc = rest.strip()
    if desc:
        y = _draw_wrapped(draw, desc, x, y, f_body, content_width, y + 100)

    # --- divider ---
    y += 16
    draw.line([(x, y), (WIDTH - MARGIN, y)], fill="black", width=2)
    y += 20

    # --- Outline ---
    draw.text((x, y), "OUTLINE", fill="black", font=f_header)
    y += 32
    y = _draw_wrapped(draw, sections.get("Outline", ""), x, y, f_body, content_width, bottom - 220)

    # --- divider ---
    y += 16
    draw.line([(x, y), (WIDTH - MARGIN, y)], fill="black", width=1)
    y += 20

    # --- Revenue Feasibility ---
    draw.text((x, y), "REVENUE FEASIBILITY", fill="black", font=f_header)
    y += 32
    _draw_wrapped(draw, sections.get("Revenue Feasibility", ""), x, y, f_body, content_width, bottom)

    img.save(output_path)
    return output_path
