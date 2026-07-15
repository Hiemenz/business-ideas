# PoC 25 — "What's Actually Happening On Your Sales Calls" — Call Analysis & Coaching Insights Service for Small B2B Sales Teams

**Date:** 2026-07-12
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Small B2B sales teams (2-10 reps) at startups and small agencies routinely record their sales calls (Zoom/Google Meet recordings are standard now) but almost never systematically review them — founders and sales managers are too busy running the business to listen back to calls, so recurring objection patterns, weak pitch moments, and what actually separates won deals from lost ones go completely unanalyzed. Enterprise tools like Gong/Chorus solve this at a price point ($1,000s/mo) built for larger sales orgs, leaving small teams with either nothing or an unused enterprise trial. This is distinct from PoC 08 (which books meetings) and PoC 13 (which cleans CRM data) — this service analyzes what's actually said and done on calls that have already happened, turning existing recordings into a concrete coaching asset.

## Who It's For

Startup/small-agency founders or sales managers with 2+ reps making regular sales calls, recording those calls (even just via default Zoom/Meet recording, not a dedicated call-intelligence tool), and closing at a rate that suggests real room for improvement — visible via founders openly discussing close-rate frustration or lengthy sales cycles in founder communities.

## How It Makes Money

- Flat analysis project fee: $400–$1,000 to review a batch of 10-20 recent recorded calls, categorize recurring objections, flag specific weak moments (unclear pitch, poor discovery questions, weak close attempts), and deliver a findings report with concrete coaching recommendations.
- Ongoing weekly/biweekly call-review retainer: $300–$800/mo to continuously review new calls and deliver a rolling coaching digest — the natural recurring hook, since call volume is continuous for any active sales team.
- Win/loss pattern analysis add-on: a deeper-dive project ($300–$600) specifically comparing won vs. lost deal calls to identify what actually differentiates outcomes — a higher-value analytical product once the basic service has proven useful.
- Playbook creation upsell: once patterns are identified, a project fee ($500–$1,500) to codify findings into an actual call script/objection-handling playbook the team can use for onboarding new reps — converts insight into a durable, reusable asset.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Client shares a batch of recorded call links/files (Zoom recordings are commonly link-shareable) along with basic outcome data (which calls led to closed deals vs. lost/ghosted).
   - Transcribe using a free tool (Zoom's built-in transcription, or a free tier of a transcription service) if not already transcribed.
   - Review transcripts using an LLM to extract recurring themes: common objections raised, discovery question quality, moments where the rep talked over or missed a buying signal, and how effectively (or not) the call moved toward a next step/close.
   - Deliver a findings report: top 3-5 recurring patterns (both strengths to reinforce and weaknesses to coach), with specific quoted examples pulled directly from the transcripts for concreteness.
2. **Software layer (build once 2–3 clients are live, funded by early project fees):**
   - Reusable analysis prompt template categorizing calls by outcome and extracting structured findings (objection type, discovery quality, close attempt strength) consistently across every transcript — the core reusable engine of the service, same pattern used throughout this folder.
   - Simple script to batch-transcribe and pre-process call recordings (using a free/low-cost speech-to-text API) rather than manually running each file through a web tool individually, cutting turnaround time as volume grows.
   - Case tracker (Airtable/Google Sheets) logging recurring objection frequency and call-outcome correlation across a client's full call history over time, turning the retainer into a genuinely compounding data asset rather than a series of disconnected one-off reviews.

## Tools/Stack

- Client's existing call recording setup (Zoom, Google Meet) — no new tooling cost, working with recordings they already have.
- Free/low-cost transcription (Zoom's built-in feature, or a free-tier transcription API).
- Claude/Gemini API for transcript analysis, pattern extraction, and coaching-recommendation drafting.
- Google Docs for report delivery.
- Airtable/Google Sheets for ongoing pattern tracking.
- Stripe/invoice for fee collection.

## Go-to-Market — First 3-5 Customers, Zero Ad Spend

1. Identify prospects via founder/sales-leader communities where close-rate frustration, long sales cycles, or "why do deals keep stalling" questions are openly discussed — a direct, self-identifying pain signal.
2. Free-sample hook: ask for a single recorded call (even one that didn't close) and deliver a quick, free breakdown of 2-3 specific moments worth coaching — a low-effort ask for the prospect (just one call) that produces a genuinely useful, concrete artifact demonstrating real analytical value before any commitment.
3. Sales leadership and RevOps communities (overlapping somewhat with the audience in PoC 13/16/19) are a strong, on-topic venue, and cross-selling into any existing CRM cleanup (PoC 13) or candidate sourcing (PoC 16) client relationships is a natural same-buyer upsell.
4. Position pricing explicitly against the enterprise alternative — "the same kind of insight Gong gives $10k/mo sales orgs, sized and priced for a 3-person team" is an easy-to-understand value comparison.
5. A single "found the exact objection killing 40% of your calls and we fixed the response" result is a highly specific, credible case-study stat for founder/sales-leader community outreach.

## Time to First Dollar

- Day 1–3: identify 10-15 prospects showing visible close-rate/sales-cycle frustration signals.
- Day 3–5: request a single free-sample call from the first 6-8 responsive prospects and deliver a quick breakdown.
- Day 5–10: close 2–3 clients on the flat analysis project fee ($400–$1,000), collected upfront.
- **First dollar within 1–2 weeks** — no build dependency, and the free sample itself (one call, one breakdown) can be turned around within a day or two of receiving it, keeping the sales cycle short.

## Why This, Why Now

- Zero build required to start — transcript analysis is doable manually with LLM assistance from day one, using recordings the client already has sitting unused.
- Directly plays to both technical skill (structured pattern extraction from unstructured transcript data) and sales fluency (understanding what actually makes a sales call effective, which sharpens your own outreach in the process of doing this work for clients).
- Strong, easily understood price-vs-enterprise-alternative comparison makes the pitch land quickly without needing to educate on why call review matters — most sales leaders already know Gong-style tools exist, they just can't justify the price at small-team scale.
- Compounding data asset dynamic on retainer: the longer you work with a client, the more pattern history accumulates, making the ongoing service more valuable over time rather than static.

## Risks / Open Questions

- **Sensitive to being received as criticism:** call coaching feedback touches individual reps' performance directly — frame findings constructively and pattern-based ("this objection comes up in 60% of calls and the response varies widely," not "Rep X handled this call poorly") to keep the engagement collaborative rather than adversarial.
- **Transcription accuracy on multi-speaker calls:** free transcription tools can struggle with cross-talk or accented speech, similar to the risk noted in PoC 12 — budget review time to catch transcription errors before drawing conclusions from them.
- **Recording consent/compliance varies by jurisdiction:** call recording laws differ (some require all-party consent) — this is the client's existing practice and responsibility, but be aware of it and confirm the client's recordings are already compliant with their own state/local requirements before analyzing them.
- **Small sample sizes limit pattern confidence:** a batch of 10-20 calls may not be enough to confidently identify true patterns versus noise, especially for win/loss analysis — be appropriately calibrated in how confidently findings are presented, especially in early engagements before more data accumulates.

## Validation Signal to Watch

If 2+ of your first 6-8 free single-call breakdowns generate a genuinely surprised or valuable-feeling reaction from the prospect (not just polite acknowledgment), the analytical method and hook are validated — scale outreach into sales leadership/founder communities. If early paid engagements don't surface any consistent, actionable pattern across a client's calls, the sample size may be too small or the sales process too variable rep-to-rep — consider narrowing scope to a single rep's calls first to establish a clearer signal before analyzing the full team.
