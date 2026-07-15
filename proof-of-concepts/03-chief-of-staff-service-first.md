# PoC 03 — "Chief of Staff as a Service" — Service-First, Productize Later

**Date:** 2026-07-08
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Frequent travelers (executives, entrepreneurs, high earners with complex lives) lose track of the unglamorous logistics that keep a life running: passport/visa renewals, insurance deadlines, anniversary/birthday gifts, kids' school forms, subscription renewals, car registration, tax deadlines. These aren't hard problems individually — they're death by a thousand small misses, each one embarrassing or costly (a missed passport renewal cancels a trip; a forgotten anniversary has social cost far beyond its dollar cost). No one currently owns this in their life. This PoC sells the human-plus-lightweight-tooling version first, so you validate exactly what a client needs tracked before ever building a product around it.

## Who It's For

Busy people with disposable income and a demonstrated travel/complexity signal: frequent flyers, founders, consultants who travel weekly, dual-career households with kids. Best entry point is people already paying for adjacent concierge services (travel agents, EAs, meal kits, personal trainers) — they've already proven willingness to outsource life admin.

## How It Makes Money

- Flat monthly retainer: $500–$1,500/mo depending on complexity (single person vs. family, one household vs. multiple properties).
- Tiered onboarding fee ($250–$500) covering the initial "life audit" — cataloging every recurring deadline, document, and relationship (family birthdays, gift preferences) into the system.
- Natural upsell path once trusted: travel booking coordination, holiday/gift purchasing on their behalf (small commission or flat fee per event), household bill-pay oversight.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Client onboarding call: extract every recurring deadline (passport/visa expiry, driver's license, car registration, insurance renewals, domain/subscription renewals) and every relationship-based date (birthdays, anniversaries, gift preferences for each) that matters to them.
   - Log everything in a free-tier Notion database or Airtable base — one row per item, with date, recurrence, and a note on what "handled" looks like (e.g., "book restaurant + order flowers" vs. "just remind me").
   - Weekly human check-in (15-min call or async voice memo/Slack message) reviewing what's coming up in the next 2–4 weeks and confirming action items.
2. **Software layer (build once 2–3 clients are live, funded by retainer cash):**
   - LLM-generated weekly digest: script pulls the Notion/Airtable data via API, has an LLM draft a plain-English "here's what's coming up and what I need from you" summary, sent via email/SMS — same pattern as this repo's existing `discord_notify.py`/notification scripts.
   - Auto-reminders at multiple lead times (90/30/7 days before a deadline) rather than relying on manual review each week.
   - Simple recurrence logic (annual, biennial for passports, custom) so you're not manually recalculating renewal dates.

## Tools/Stack

- Notion or Airtable (free tier) as the system of record.
- Claude/Gemini API for digest generation and drafting gift/event suggestions.
- Zapier/Make free tier (or a simple scheduled Python script, consistent with this repo's cron-driven scripts) to trigger weekly digests automatically.
- Calendly or similar free tool for booking the recurring check-in call.

## Go-to-Market — First 3-5 Customers, Zero Ad Spend

1. Network first: ask people you know who travel heavily or run households with a lot of moving parts whether they'd pay for someone to make sure nothing falls through the cracks — this is a very easy "yes, that sounds amazing" conversation because everyone has a story about a missed deadline.
2. Free "life audit" hook: offer a free 30-minute call where you catalog their next 90 days of deadlines/events for free, then pitch the ongoing retainer to keep it maintained — mirrors the free-sample pattern used in PoC 01 and PoC 02.
3. Target via warm referral chains from people in relevant orbits: travel agents, EAs who are overloaded and want to offload the "small stuff," estate/wealth planning professionals whose clients already pay for concierge services.
4. Position explicitly as "the thing your EA doesn't have time for" rather than competing with a full EA — cheaper, narrower scope, easier yes.

## Time to First Dollar

- Day 1–3: run 3–5 free life-audit calls with warm network contacts.
- Day 4–7: convert 1–2 into paid retainers ($500–$1,500/mo + onboarding fee), collected via Stripe invoice upfront.
- **First dollar within 1–2 weeks**, since the entire MVP is a spreadsheet/database and a phone call — there is no build dependency blocking revenue.

## Why This, Why Now

- Zero software build required to start selling — validates real demand and exact feature needs before writing a line of code.
- High stickiness: once a client hands over their full life logistics picture, switching cost is high (a new provider has to relearn everything) — this is a genuinely durable recurring-revenue business, not a one-off gig.
- Plays to sales/ops strength for the close and onboarding; software skill compounds margin later without gating the first sale.

## Risks / Open Questions

- **Time-intensive per client at first:** manual tracking and weekly check-ins don't scale past a handful of clients without the software layer — cap manual-only client count at ~5 before investing build time.
- **Trust threshold is high:** you're being handed sensitive personal/family info (document numbers, family relationship details) — be explicit about data handling from day one.
- **Scope creep:** clients may push toward "just do everything for me" (full EA replacement) — hold the line on scope (tracking + reminding + light coordination) unless pricing reflects full EA-level service.

## Validation Signal to Watch

If 2+ of your first 5 free life-audit calls convert to paid retainers within a week, and clients naturally start asking "can you also handle X" (a strong stickiness signal), this is worth investing in the software layer. Track exactly which fields/reminders clients act on vs. ignore during the manual phase — that becomes your future product's feature list, informing [[04-chief-of-staff-app-first]].
