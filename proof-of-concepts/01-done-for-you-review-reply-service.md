# PoC 01 — "Never Miss a Review" — Done-for-You Google/Yelp Review Response Service for Local Service Businesses

**Date:** 2026-07-07
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Local service businesses (dentists, HVAC, salons, auto shops, property managers) get Google/Yelp reviews constantly but rarely respond — especially to negative ones — which hurts local SEO ranking and conversion. They know they should respond but don't have time or the right words. This is a well-known pain point with proven willingness to pay ($150–$500/mo per location on tools like Podium/Birdeye), but those tools are expensive and impersonal. A cheap, fast, human-plus-AI-assisted service undercuts them badly.

## Who It's For

Local businesses with 1–5 locations, 20+ reviews/month, no dedicated marketing person. Target verticals with high review volume and reputational sensitivity: dental/medical practices, home services (HVAC, plumbing, roofing), restaurants, auto repair, property management.

## How It Makes Money

- Flat monthly retainer: $199–$399/mo per business (per Google Business Profile location).
- Optional setup fee ($99) to review tone/brand voice.
- Upsell: monthly review-volume report + "get more 5-star reviews" SMS/QR campaign ($99/mo add-on) once trust is built.

## MVP — Buildable in Days, ~$0 Cost

1. **Manual/semi-automated v0 (week 1, no code needed to start selling):**
   - Client shares Google Business Profile owner access (or forwards review notification emails).
   - You draft replies using an LLM (Claude) with a per-client tone/style prompt, review manually, post via the Business Profile dashboard.
   - Turnaround promise: replies posted within 24 hours.
2. **Software layer (build in parallel, once you have 2–3 paying clients to fund your time):**
   - Python script (you already have `gemini_client.py`/similar patterns in this repo) that pulls new reviews via the Google Business Profile API, drafts responses with an LLM using a per-client voice profile, and either auto-posts or queues for one-click approval (Slack/email).
   - Store client voice/tone configs in a simple YAML/JSON file per client — same pattern as `config.yml` in this repo.
   - Flag negative reviews (<=3 stars) for manual review before posting — never auto-post to a 1-star review.

## Tools/Stack

- Google Business Profile API (free) for pulling reviews once you're past the manual-access phase.
- Claude/Gemini API for draft generation (near-$0 at this volume — pennies per review).
- Simple cron or scheduled script (Poetry env already set up in this repo) to poll for new reviews every few hours.
- Stripe for recurring billing.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Pull a list of 50 local businesses in your city with 4.0–4.6 star ratings and 10+ unanswered reviews in the last 90 days (visible on Google Maps — free, manual research, ~2 hrs).
2. Cold outreach (email/DM/walk-in) with a **free sample**: reply drafts for their 3 most recent unanswered reviews, unsolicited, in the message. "I noticed you haven't responded to some reviews — here's what I'd post, free. If you like it, I'll do this every week for $199/mo."
3. Close via a 15-minute call; no contract, month-to-month, cancel anytime — removes friction for fast yes.
4. Ask every client for 2 referrals after week 2 once they've seen a reply posted.

## Time to First Dollar

- Day 1–2: build outreach list, draft 3 free samples for 10 prospects.
- Day 3–5: send outreach, book calls.
- Day 5–10: close 2–3 clients at $199–$399/mo → **$400–$1,200 MRR within the first two weeks**, collected via Stripe invoice/first payment upfront.

## Why This, Why Now

- Zero build required to start selling (you're doing the LLM drafting by hand on day 1).
- Sales/marketing skill is the actual bottleneck, not software — plays directly to stated strengths.
- Software automation is a pure margin/time upgrade you layer in once cash is flowing, not a prerequisite to start.
- Recurring revenue model — unlike one-off gigs, this compounds.

## Risks / Open Questions

- Access/trust: getting write access to a client's Google Business Profile is a trust hurdle — mitigate by offering to draft-only (client posts themselves) for the first month.
- Churn risk if perceived value drops after the "wow" of the free sample — mitigate with a monthly report showing reply count/rating trend.
- Google API access approval can take time for automated posting — the manual/LLM-assisted workflow avoids blocking on this for revenue.

## Validation Signal to Watch

If 2+ of the first 10 cold outreach responses convert to a paid call within 5 days, this is worth building the automation layer. If response rate is near-zero, pivot the vertical (try restaurants or auto shops instead of dental) before abandoning the model.
