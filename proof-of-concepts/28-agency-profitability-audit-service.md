# PoC 28 — "Which Clients Are Secretly Losing You Money" — Project Profitability Audit for Freelancers & Small Agencies

**Date:** 2026-07-12
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Freelancers and small agencies quote a flat project fee, deliver the work, and move on — rarely stepping back to calculate actual profitability per client or per project once scope creep, revision rounds, and support time are factored in. It's extremely common for a business's "favorite," most time-consuming client to actually be their least profitable one, invisible until someone does the math. Most freelancers track time loosely (if at all) and invoice by project rather than by hour, meaning the data to see this exists but is never assembled into a clear picture. This is distinct from PoC 22 (which cleans up bookkeeping/reconciliation) and PoC 17 (which collects overdue invoices) — this audits business-model profitability itself: which clients/services are actually worth keeping, which need repricing, and which are quietly draining time that could go toward better-paying work.

## Who It's For

Freelancers, consultants, and small agencies (1-10 people) doing project-based or retainer work who track time in some form (even loosely, via calendar blocks, a time-tracking tool, or rough estimates) and have at least 6 months of client history across multiple clients/projects to analyze — best entry point: people openly expressing burnout or "working constantly but not making what I should be" frustration, a direct signal that the profitability picture likely has a real, findable problem in it.

## How It Makes Money

- Flat audit fee: $300–$700 to analyze a defined period of client/project history (time spent vs. revenue collected per client) and deliver a ranked profitability breakdown with specific repricing/scope recommendations.
- Repricing strategy add-on: $150–$300 to draft the actual client-facing communication for renegotiating scope or pricing with underpriced clients — bridges the gap between "here's the finding" and "here's how to actually act on it without an awkward conversation."
- Quarterly re-audit retainer: $150–$300/quarter for freelancers/agencies who want ongoing visibility as their client mix shifts — a natural, low-friction recurring service once the value of the first audit is proven.
- Pricing/proposal template upsell: a one-time fee to build a reusable project-scoping and pricing template that bakes in margin protection from the start, reducing future underpricing before it happens rather than only catching it after the fact.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Client shares whatever time-tracking data exists (a time-tracking tool export, rough calendar-based estimates, or even just a memory-based reconstruction for smaller client lists) plus invoicing/revenue data per client/project over a defined period.
   - Calculate effective hourly rate per client (total revenue collected ÷ total time spent, including scope-creep and support time often left uncounted) and rank clients from most to least profitable — a straightforward calculation that frequently produces a genuinely surprising result for the freelancer.
   - Identify patterns behind the least-profitable engagements (chronic scope creep, underpriced initial quote, excessive revision rounds, slow-paying clients compounding the problem) using an LLM to help synthesize qualitative notes about each client relationship alongside the raw numbers.
   - Deliver a ranked findings report with specific, per-client recommendations: reprice, renegotiate scope, or (for the worst offenders) consider parting ways.
2. **Software layer (build once 2–3 clients are live, funded by early audit fees):**
   - Spreadsheet-based calculation template (Google Sheets formulas) automating the effective-hourly-rate calculation once time and revenue data is entered — the core reusable analytical engine, same pattern as PoC 24's menu-engineering spreadsheet approach applied to a different domain.
   - Reusable scope-creep/repricing communication templates by scenario (a chronically over-scoping client vs. an initially underpriced retainer) so the repricing add-on can be delivered quickly once the pattern is identified.
   - Case tracker aggregating anonymized findings across clients (e.g., "average freelancer profitability audit finds 20-30% of clients below break-even effective rate") — both useful for your own service refinement and as a compelling, non-client-specific stat for marketing.

## Tools/Stack

- Client's existing time-tracking data (Toggl, Harvest, a calendar, or rough estimates) and invoicing records (whatever system they already use) — no new tooling cost.
- Google Sheets for the effective-rate calculation engine.
- Claude/Gemini API for pattern synthesis and repricing-communication drafting.
- Google Docs for report delivery.
- Stripe/invoice for fee collection.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify prospects via freelancer/consultant communities where burnout, overwork, and "I'm busy but not making enough" frustration is openly discussed — the same general venues used in PoC 17 (invoice collections), since it's a closely related pain cluster and audience.
2. Free-sample hook: ask a prospect to share rough time/revenue estimates for just 2-3 of their clients, and calculate a quick effective-hourly-rate comparison for free: "Based on what you shared, Client A is netting you roughly $40/hr and Client B is closer to $12/hr once you count the revision rounds — want the full breakdown across all your clients?" A small, low-effort ask that produces a genuinely eye-opening, concrete finding.
3. Cross-sell directly into any existing PoC 17 (invoice collections) client relationship — a freelancer already working with you on getting paid what they're owed is a natural, warm next conversation about whether what they're charging in the first place is even sufficient.
4. Freelance/solopreneur-focused newsletters, podcasts, and community events are strong venues, since profitability-awareness is a widely and directly relatable pain point in this specific audience.
5. A single "found their most 'important' client was actually their least profitable, renegotiated, and recovered $15/hr in effective rate" story is a highly relatable, concrete case study for freelancer community outreach.

## Time to First Dollar

- Day 1–3: identify 15-20 prospects showing visible overwork/underearning frustration signals, request small rough-estimate samples from the first 8-10.
- Day 3–5: run free quick comparisons and share as the outreach hook.
- Day 5–10: close 2–3 clients on the flat audit fee ($300–$700), collected upfront.
- **First dollar within 1–2 weeks** — no build dependency, the spreadsheet-based calculation is fast once data is in hand, and the free sample requires only a small, low-effort data request from the prospect.

## Why This, Why Now

- Zero build required to start — the core calculation (revenue ÷ time = effective rate) is simple, well-defined, and immediately doable in a spreadsheet.
- Directly and unusually relatable to the target audience's actual lived pain (working hard but not seeing it reflected in income), making the pitch resonate without requiring buyer education about whether the underlying problem is real.
- Natural cross-sell chain with PoC 17 and PoC 22, all targeting overlapping freelancer/small-agency financial-health pain points — a single relationship can plausibly expand across multiple services in this folder over time.
- Concrete, memorable, easily-repeated finding format ("Client X nets you $12/hr, Client Y nets you $65/hr") makes the service's value immediately graspable and highly shareable within tight-knit freelancer communities.

## Risks / Open Questions

- **Data quality/completeness varies widely:** freelancers with poor or no time-tracking history will produce a less rigorous analysis — be transparent about how estimate-based inputs affect confidence in the findings, and consider offering a lightweight time-tracking setup as part of the engagement for clients starting from nothing.
- **Emotionally sensitive findings:** learning that a favorite or long-standing client relationship is actually unprofitable can be an uncomfortable realization — frame findings constructively and focus on actionable next steps (reprice, renegotiate) rather than framing it as a client the freelancer was foolish to keep.
- **Repricing/renegotiation execution risk sits with the client, not you:** you can identify the problem and draft the communication, but the freelancer still has to have the actual conversation with their client — be clear about this scope boundary and offer the repricing-communication add-on specifically to reduce (not eliminate) that friction.
- **Small sample sizes for newer freelancers:** someone with only 1-2 clients or a few months of history won't have enough data for a meaningful comparative analysis — this service works best for freelancers with an established, varied client history, and that should be screened for during initial outreach.

## Validation Signal to Watch

If 2+ of your first 8-10 free quick comparisons produce a genuinely surprising finding that generates a strong reaction, the analytical hook is validated — scale outreach into freelancer/consultant communities and consider the direct cross-sell into existing PoC 17 relationships. If findings consistently confirm what freelancers already suspected rather than surfacing anything new, the differentiated value may need to shift more toward the repricing-execution support (the "now what do I do about it" layer) rather than the diagnostic finding itself.
