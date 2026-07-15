# PoC 24 — "Your Menu Is Losing You Money" — Menu Engineering & Pricing Optimization Service for Restaurants

**Date:** 2026-07-11
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Independent restaurant owners set their menu prices once, tweak them occasionally for inflation, and rarely analyze which items are actually profitable versus which are popular-but-margin-losing, or how menu layout/psychology (item placement, description language, price anchoring) influences what customers order. "Menu engineering" — classifying items by profitability and popularity into a simple matrix, then redesigning the menu to nudge orders toward high-margin items — is a well-established restaurant consulting discipline, but traditional menu consultants charge enterprise rates and independent restaurants (the majority of the market) rarely have access to it. This is a fresh vertical for this folder (food service) and a genuinely data-driven service: with basic sales-mix data from the restaurant's POS system, the profitable-item analysis itself is a straightforward, well-defined calculation, not a subjective judgment call.

## Who It's For

Independent restaurant owners (not chains, which typically have in-house menu strategy) who've had their menu largely unchanged for 6+ months and use a modern POS system (Square, Toast, Clover) that can export sales-by-item data — a near-universal setup for independent restaurants today, making the required data readily available.

## How It Makes Money

- Flat project fee: $400–$1,200 depending on menu size and complexity, covering a full menu engineering analysis (profitability × popularity classification per item) plus a redesigned menu layout with repositioned/rewritten high-margin items and pricing adjustment recommendations.
- Menu redesign/copywriting add-on: $200–$500 to actually rewrite item descriptions using appetite-appeal language techniques (proven to measurably lift orders of specific items) and redesign layout for visual hierarchy.
- Quarterly re-analysis retainer: $150–$400/quarter to re-run the analysis as seasonal menus rotate or ingredient costs shift — a natural, justified recurring cadence given how often independent restaurants seasonally refresh offerings.
- Multi-location package for small local restaurant groups (2-5 locations): a bundled rate per additional location, since much of the analytical framework/copy technique carries over with location-specific tuning.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Client exports sales-by-item data from their POS (units sold and revenue per item over a recent period, typically available as a standard report in Square/Toast/Clover) along with each item's known food cost (or a rough estimate if exact costing isn't tracked).
   - Calculate contribution margin per item (price minus food cost) and classify each into the standard menu-engineering matrix: high-margin/high-popularity ("stars" to feature prominently), high-margin/low-popularity ("puzzles" to reposition or rename), low-margin/high-popularity ("plow-horses" to subtly reprice or pair with higher-margin add-ons), low-margin/low-popularity ("dogs" — candidates to cut).
   - Deliver a findings report with the classification, specific repositioning/pricing recommendations per item, and a redesigned menu layout draft.
2. **Software layer (build once 2–3 clients are live, funded by early project fees):**
   - Spreadsheet-based calculation template (Google Sheets formulas) that automates the margin/popularity classification once sales data is pasted in — the core analytical engine of the service, reusable across every client with minimal per-engagement rework.
   - LLM-assisted description rewriting using proven appetite-appeal copywriting patterns (sensory language, provenance/quality cues) applied consistently to whichever items the analysis flags for repositioning.
   - Reusable layout-principle checklist (eye-tracking-informed placement zones, price presentation without dollar signs, strategic use of boxes/highlighting for target items) applied per client's menu format.

## Tools/Stack

- Client's existing POS system export (Square, Toast, Clover all support sales-by-item reporting, no new tooling cost).
- Google Sheets for the margin/popularity classification calculation.
- Claude/Gemini API for menu description copywriting.
- Basic design tool (Canva free tier) for redesigned menu layout mockups.
- Stripe/invoice for fee collection.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify prospects among independent restaurants with menus that look visibly unchanged/dated (no recent specials, same layout for a long time, visible on their website or a recent visit) — combined with restaurants openly discussing thin margins or rising food costs, a strong and timely pain signal.
2. Free-sample hook: pick 2-3 items from a prospect's publicly posted menu and offer a quick, free take based on general menu-engineering principles and observable pricing: "Looked at your menu — [item] is priced in a way that's probably underperforming its margin potential compared to [item]. Happy to run the full analysis with your actual sales data." A lighter-weight version of the free-sample tactic used throughout this folder, since full analysis requires the restaurant's own sales data but a directional observation can be made from the public menu alone.
3. Local restaurant owner associations, independent restaurant Facebook/community groups, and food-service supplier relationships (a supplier rep who visits many independent restaurants could be a strong referral partner, similar to the CPA referral channel in PoC 22) are strong outreach venues.
4. Position the ROI math concretely: "shifting 10% of orders toward your highest-margin items, even without raising a single price, is real found money" — reframes the service as margin recovery rather than a cost.
5. A single "average ticket went up $2.50 after the redesign" result, especially with a before/after visual of the menu, is a highly concrete and shareable case study for local restaurant community outreach.

## Time to First Dollar

- Day 1–3: identify 15-20 independent restaurant prospects, review public menus for directional free-sample observations on the first 8-10.
- Day 3–5: send outreach (or visit in person — restaurant owners are often more reachable face-to-face during off-peak hours) with the specific menu observation.
- Day 5–10: close 2–3 clients on the flat project fee ($400–$1,200), collected upfront or split between deposit and delivery.
- **First dollar within 1–2 weeks** — no build dependency, the spreadsheet-based analysis engine is fast to run once sales data is in hand, and turnaround per engagement can be just a few days.

## Why This, Why Now

- Zero build required to start — the analytical method (margin × popularity classification) is a well-established, straightforward calculation doable in a spreadsheet from day one.
- Fresh vertical (food service) diversifies this folder further while reusing the same core research/analysis/copywriting/outreach skill set applied throughout.
- Restaurants are a high-volume, easily identifiable local prospect pool with a genuinely universal pain point (thin, pressured margins) that makes the pitch resonate without needing much education.
- In-person outreach is unusually viable for this vertical (restaurant owners are physically locatable and often reachable during off-peak hours), giving you a channel beyond pure digital outreach that many other ideas in this folder don't have.

## Risks / Open Questions

- **Food cost data accuracy varies:** not every independent restaurant tracks precise ingredient costing — where cost data is rough/estimated, be transparent that recommendations carry corresponding uncertainty, and offer to help set up basic cost tracking as part of the engagement if it's missing entirely.
- **Implementation dependent on the client actually changing the menu:** unlike some services in this folder where you implement the fix directly, menu printing/redesign implementation typically requires the restaurant's own action (or your design handoff to their printer) — clarify scope (recommendations plus design mockup vs. full physical menu production) upfront.
- **Results take a full menu cycle to measure:** unlike faster-feedback services elsewhere in this folder, proving the average-ticket-increase claim requires weeks of post-implementation sales data — set expectations about measurement timeline honestly.
- **In-person sales approach requires different logistics** (visiting during off-peak hours, no email response infrastructure to lean on) — allocate outreach time accordingly if leaning into face-to-face prospecting for this vertical.

## Validation Signal to Watch

If 3+ of your first 10 outreach attempts (digital or in-person) generate genuine interest in the free directional observation, the hook and vertical are working — scale outreach across more independent restaurants in your area. If early clients' post-implementation sales data shows a measurable average-ticket or item-mix shift toward the repositioned high-margin items, that becomes a strong, concrete proof point both for the quarterly retainer upsell and for future outreach in this vertical.
