# PoC 43 — "Investors Stop Reading at Slide 3" — Pitch Deck Audit & Restructure Service for Early-Stage Founders

**Date:** 2026-07-15
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Early-stage founders raising their first pre-seed or seed round routinely send pitch decks that structurally undermine the fundraise before the content even gets a fair read: wrong slide order, missing key slides investors specifically look for (the "why now," the competitive moat, the ask with use of funds), too much text obscuring the core narrative, financials without context, or a team slide that doesn't address the obvious "why are you the right people for this?" question. Most founders have never raised money before and built their deck by looking at other decks they could find online — not by understanding what an investor is specifically trying to answer in the first 3 minutes of reviewing a cold deck. The audit + restructure service bridges that gap: an experienced review that identifies the specific structural and narrative problems (not just typos and font choices), explains why each is a problem from the investor's perspective, and provides a rewritten slide-by-slide brief the founder can implement in an afternoon. This is distinct from PoC 06 (LinkedIn ghostwriting) and PoC 09 (job search acceleration) — this is specifically investor fundraising, a high-stakes, time-compressed situation with a very specific and well-understood audience (early-stage investors) whose evaluation criteria are knowable.

## Who It's For

First-time founders actively preparing for or in the middle of a pre-seed or seed fundraise — best entry points: founders who've had a few investor meetings and gotten consistent "not for us" responses without useful feedback, founders who've been told to "work on the deck" without specifics, or founders who are about to start reaching out to investors for the first time and want a review before sending cold.

## How It Makes Money

- Flat audit fee: $300–$600 for a written, slide-by-slide audit identifying every structural, narrative, and framing problem in the current deck, with a specific fix brief for each issue and a 30-minute walkthrough call to discuss the findings.
- Restructure tier: $600–$1,200 for a full deck restructure — the audit plus a rewritten narrative outline (slide titles, key message per slide, bullet content structure) that the founder implements in their own design tool, saving them the cost of a designer while delivering the structural outcome they actually need.
- Investor narrative document add-on: $200–$400 for a one-page "investor narrative" distilling the deck's thesis into the 3-sentence hook a founder needs for cold email outreach to investors — a natural upsell since founders who've fixed their deck immediately need to start sending it.
- Fundraise readiness full package: $1,000–$2,500 combining the restructure, the investor narrative, a target investor list of 30-50 well-matched funds/angels based on the company's stage/sector (reusing the list-building skill from PoC 42), and a cold outreach email template — a complete "go raise" kit for a first-time founder.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Receive the deck (PDF or slides link) and a 2-paragraph brief from the founder: what the company does, who the target investor is (pre-seed angel vs. seed institutional vs. both), and what specific concern they have about the current deck.
   - Review against a structured audit framework: does the deck answer the 10 core investor questions in the right order (problem, solution, market size, traction, team, business model, competition, go-to-market, financials, ask + use of funds)? Is the market size framed credibly? Is the traction slide honest and specific? Does the ask include use of funds with a clear 18-24 month runway plan? Is the "why now" compelling or absent?
   - Use an LLM prompted with the audit framework and the specific slide content to generate the initial findings draft, then edit and sharpen from founder context — the LLM accelerates the structured analysis; the judgment about what matters most for this specific company and stage is yours.
   - Deliver the written audit as a structured Google Doc (one section per slide, findings + fix brief per slide) and a 30-minute walkthrough call within 48-72 hours of receipt.
2. **Software layer (build once 2–3 clients are live):**
   - Reusable audit framework document (the 10-question investor evaluation rubric, common structural problems by deck section, and a "red flag" checklist from known investor feedback patterns) — built once, updated after each engagement as new patterns emerge, and reused as the systematic input for every audit.
   - Structured LLM prompt template that takes slide-by-slide content as input and produces a first-pass findings draft in the correct audit format, reducing per-engagement audit drafting time from 3-4 hours to under 1 hour.
   - Library of before/after slide restructure examples (anonymized, with founder permission) that becomes a quality reference and a compelling marketing asset over time.

## Tools/Stack

- Google Docs / Slides for deck review and deliverable.
- Claude/Gemini API for structured audit drafting from the slide-by-slide content input.
- Loom (free tier) as an optional async walkthrough alternative to a live call for founders in different time zones.
- Calendly (free tier) for walkthrough call scheduling.
- Stripe/invoice for fee collection.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify prospects in founder and fundraising communities (Indie Hackers fundraising threads, r/startups, YC Hacker News "ask HN: fundraising advice," AngelList forums, founder Slack groups) where first-time fundraising anxiety is a constant, specific, openly-discussed topic — "how do I know if my deck is ready?" is essentially a recurring question in all of them.
2. Free-sample hook: offer a free "3-slide cold read" — look at only the first 3 slides of a founder's deck and give honest, specific written feedback on whether those 3 slides would keep an investor reading or not: "Your problem slide buries the insight in the third bullet — investors spend under 10 seconds on a problem slide and most will miss it. Here's how I'd restructure those three slides specifically." A limited but genuine, specific sample of the full audit that demonstrates depth without giving away the whole service.
3. YC application season and Demo Day periods are high-density prospecting windows — founders actively preparing for YC, Techstars, or other accelerator applications are in exactly the deck-building/refinement mindset and have clear, immovable deadlines that create urgency.
4. Warm intro through founder communities and startup networks: any founder you know who's raised or is raising is a natural referral source — fundraising is one of the most word-of-mouth-driven buying decisions in the startup ecosystem ("my friend used this person to prep their deck and got into YC" is extremely persuasive).
5. A single "founder sent revised deck, got first investor meeting within a week" story (with permission) is extremely high-signal in these communities because the outcome is specific, attributable, and aspirationally resonant.

## Time to First Dollar

- Day 1–2: build the audit framework document (10-question rubric + common problem patterns + red flag checklist) and run one full test audit on a publicly available sample deck to calibrate time and process.
- Day 2–4: identify 15-20 founders actively in or about to enter a raise in founder communities, prepare a 3-slide free read for the 8-10 most accessible decks.
- Day 4–7: send outreach with the 3-slide free read findings attached.
- Day 7–12: close 2–3 founders on the flat audit fee ($300–$600), collected upfront; deliver within 48-72 hours of receipt.
- **First dollar within 1–2 weeks** — no build dependency beyond the audit framework, LLM-assisted drafting makes each audit fast to produce, and founders in active fundraising mode have both urgency and available budget.

## Why This, Why Now

- High-stakes, time-sensitive situation (fundraising has real deadlines and enormous consequences) creates strong willingness to pay for expert review — similar in urgency framing to PoC 38's scholarship deadline structure but with larger dollar amounts on both sides of the transaction.
- The free-sample (3-slide cold read) gives a genuine taste of the service depth without requiring the founder to share their full deck with a stranger — a sensible barrier that the limited sample respects while still being a genuinely convincing demonstration.
- Investor evaluation criteria are well-documented and learnable — this is a knowledge-gap service where the expertise is real and acquirable, not proprietary access or insider connections.
- Fundraising-adjacent upsells (investor narrative, target investor list, outreach templates) create a natural progression from audit through the full fundraising workflow, increasing average engagement value significantly above the base audit fee.

## Risks / Open Questions

- **Outcome cannot be guaranteed:** a well-structured deck doesn't guarantee investor meetings or a close — be clear that the service improves the odds by removing structural and narrative barriers, not that it produces a specific fundraising outcome.
- **Sector-specific knowledge gaps:** some industries (deep tech, biotech, fintech) have sector-specific investor expectations that differ meaningfully from a generic SaaS pre-seed deck — be honest about where your sector knowledge is strong vs. where the audit is more structurally focused, and refer to sector specialists for domains outside your depth.
- **Founders can be emotionally attached to their current deck:** audit feedback can trigger defensiveness, especially when the finding is "the core narrative is wrong," not just "fix the formatting" — deliver findings as an investor's-eye-view observation, not a personal critique, and frame every problem with a specific, actionable fix.
- **Confidentiality matters:** pitch decks contain sensitive company information; be explicit about how you handle received decks (you review and delete, you don't share, you don't retain for training data) as this concern comes up frequently and proactively addressing it removes friction.

## Validation Signal to Watch

If the 3-slide free reads consistently generate strong, specific reactions from founders ("this is exactly the feedback I couldn't get from my accelerator application" or "I've sent this to 20 investors and no one told me this"), the audit framework is hitting the right level of specificity and depth. Once 3+ full audits are delivered, review which problem categories recur most frequently across decks — those are the patterns to turn into the highest-value, fastest-to-generate sections of the reusable audit prompt template.
