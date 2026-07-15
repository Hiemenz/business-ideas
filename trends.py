"""Fetches current industry trends via Gemini.
Falls back gracefully if GEMINI_API_KEY is not set.
"""
import os
import xml.etree.ElementTree as ET
import requests
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL   = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"


def fetch_trends(industry):
    """Return a short summary of current trends for the given industry."""
    if not GEMINI_API_KEY:
        return f"No trend data available (GEMINI_API_KEY not set). Focus on general {industry} opportunities."

    prompt = (
        f"Name 2 current trends in {industry} as of early 2026. "
        f"One sentence each. No headers."
    )

    try:
        resp = requests.post(
            GEMINI_URL,
            params={"key": GEMINI_API_KEY},
            headers={"Content-Type": "application/json"},
            json={
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {"maxOutputTokens": 150},
            },
            timeout=15,
        )
        resp.raise_for_status()
        data = resp.json()
        candidates = data.get("candidates", [])
        if not candidates:
            return f"No trend data retrieved. Focus on general {industry} opportunities."
        return candidates[0]["content"]["parts"][0]["text"].strip()
    except Exception as e:
        print(f"  Trends fetch failed for {industry}: {e}")
        return f"No trend data retrieved. Focus on general {industry} opportunities."


def fetch_reddit_ideas(subreddits, posts_per_sub=3):
    """Pull top posts from business-focused subreddits this week.

    Uses Reddit's public JSON endpoint — no API key or auth required.
    Returns a newline-joined list of titles + short snippets.
    """
    headers   = {"User-Agent": "BusinessIdeaGenerator/1.0"}
    collected = []

    for sub in subreddits:
        try:
            resp = requests.get(
                f"https://www.reddit.com/r/{sub}/top.json",
                params={"t": "week", "limit": posts_per_sub},
                headers=headers,
                timeout=10,
            )
            resp.raise_for_status()
            for post in resp.json()["data"]["children"]:
                title   = post["data"]["title"]
                snippet = post["data"].get("selftext", "")[:100].strip()
                collected.append(f"- {title}: {snippet}" if snippet else f"- {title}")
        except Exception as e:
            print(f"  Reddit fetch failed for r/{sub}: {e}")

    return "\n".join(collected) if collected else "No Reddit data available."


# ==== ARXIV ====
# Map config.yml industries to arXiv category prefixes.
# A query like "cat:cs.AI" fetches papers in the AI sub-category of CS.
INDUSTRY_TO_ARXIV = {
    "education":        ["cs.CY", "cs.AI"],
    "gaming":           ["cs.GR", "cs.AI", "cs.HC"],
    "finance":          ["q-fin.TR", "q-fin.GN", "q-fin.CP", "q-fin.ST", "cs.CE"],
    "wellness":         ["cs.CY", "q-bio.QM"],
    "real estate":      ["econ.GN", "cs.CE"],
    "e-commerce":       ["cs.IR", "cs.AI"],
    "cryptocurrency":   ["cs.CR", "q-fin.CP"],
    "content creation": ["cs.MM", "cs.CL", "cs.AI"],
    "healthcare":       ["cs.AI", "q-bio.QM", "cs.CY"],
    "travel":           ["cs.IR", "cs.CY"],
}


def fetch_arxiv_papers(industry, max_results=5):
    """Fetch recent arXiv papers relevant to an industry.

    Uses the public arXiv Atom API — no API key required.
    Returns a newline-joined list of paper titles + abstract snippets.
    """
    categories = INDUSTRY_TO_ARXIV.get(industry, ["cs.AI"])
    cat_query = "+OR+".join(f"cat:{c}" for c in categories)
    url = (
        f"https://export.arxiv.org/api/query"
        f"?search_query={cat_query}"
        f"&sortBy=submittedDate&sortOrder=descending"
        f"&max_results={max_results}"
    )

    try:
        resp = requests.get(url, timeout=15)
        resp.raise_for_status()
        root = ET.fromstring(resp.text)
        ns = {"atom": "http://www.w3.org/2005/Atom"}

        papers = []
        for entry in root.findall("atom:entry", ns):
            title = entry.find("atom:title", ns).text.strip().replace("\n", " ")
            abstract = entry.find("atom:summary", ns).text.strip().replace("\n", " ")[:120]
            papers.append(f"- {title}: {abstract}")

        return "\n".join(papers) if papers else "No arXiv papers found."
    except Exception as e:
        print(f"  arXiv fetch failed for {industry}: {e}")
        return "No arXiv data available."
