# PoC 02 — "Am I Being Overcharged?" — Fractional Bill/Contract Auditing Service for High-Net-Worth Households

**Date:** 2026-07-08
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Wealthy households and small businesses spend heavily on contractors, vendors, and recurring service providers (roofers, contractors, private jet/charter operators, medical billing, property management, landscaping, household staff agencies) — and rarely have time or expertise to verify they're paying fair market rates. Overcharging is common and often invisible because there's no one whose job it is to check. This is a pure trust/expertise-arbitrage service: you find money that's already being lost, and take a cut of what you recover. No product to build, no inventory, no capital — just research + negotiation skill, sold on a contingency basis that removes all buyer risk.

## Who It's For

Individuals and families with meaningful recurring spend and low price-sensitivity awareness:
- HNW households with home renovation, landscaping, property management, or private staff contracts
- Small business owners paying vendor/supplier invoices without a procurement function
- Anyone with recent large one-off purchases (roof replacement, HVAC install, remodel) who suspects but can't confirm they overpaid
- Medical billing review is a strong adjacent niche (notoriously error-prone, well-documented industry of "medical bill advocates" already proves willingness to pay)

## How It Makes Money

- **Contingency fee model (primary, removes sales friction):** 20–33% of any savings/overcharge identified and recovered — client pays nothing if you find nothing. This is the single biggest lever for cold-close conversion because it's a risk-free yes.
- **Flat audit fee alternative** for clients who prefer certainty: $500–$1,500 per contract/invoice reviewed, regardless of outcome — useful once you have case studies to justify a fixed price.
- **Ongoing retainer upsell:** once trust is established, $299–$999/mo to review all new vendor invoices/contracts before the client signs or pays — shifts you from reactive audit to proactive gatekeeper.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Client sends you an invoice, quote, or existing contract (PDF/photo).
   - You benchmark against market rate using public data: contractor licensing boards, Angi/HomeAdvisor/Thumbtack quote ranges, industry rate guides, competitor quotes you solicit anonymously, and LLM-assisted research to summarize typical pricing ranges for the service/region.
   - Deliver a one-page findings memo: "You paid $X, market rate is $Y–$Z, here's the itemized gap and how to dispute or renegotiate it." Optionally draft the dispute/renegotiation email or call script for them.
2. **Software layer (build once 2–3 cases are underway, funded by early contingency fees):**
   - Reusable prompt templates per vertical (roofing, HVAC, medical billing, private aviation, landscaping) that structure the LLM's market-rate research and flag common overcharge patterns (e.g., line-item duplication, inflated "emergency" surcharges, unbundled fees that should be bundled).
   - Simple intake form (Google Form/Typeform, free tier) + a tracking sheet (Airtable/Google Sheets, free tier) for case status, fee owed, recovery amount — same lightweight-tooling pattern as this repo's `config.yml`-driven scripts.
   - OCR/parsing step (e.g., simple Python script with a PDF text extractor) to pull line items out of scanned invoices automatically before LLM analysis, cutting manual data entry as volume grows.

## Tools/Stack

- Claude/Gemini API for market-rate research synthesis and drafting dispute letters — near-$0 per case.
- Free-tier Airtable/Google Sheets for case tracking and CRM.
- Public data sources: state contractor licensing boards, Angi/Thumbtack/HomeAdvisor quote ranges, CMS/Medicare fee schedules for medical billing comparisons.
- Stripe or simple invoicing for contingency fee collection once savings are confirmed.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Start in your own network: ask 10–15 people directly "Have you gotten any big contractor quotes, medical bills, or vendor invoices in the last 6 months you weren't 100% sure were fair?" — this alone often surfaces 2–3 warm leads.
2. Target Nextdoor/local Facebook groups and HOA/condo boards in higher-income neighborhoods — post offering a **free 10-minute overcharge check** on any recent invoice over $2,000, no obligation. This is the same "free sample" hook that worked in PoC 01.
3. Partner-referral angle: reach out to divorce attorneys, estate attorneys, and financial advisors who see client invoices/contracts regularly and would refer clients for a revenue share (they have zero downside — free value-add for their clients).
4. Medical billing niche is especially cold-outreach-friendly: hospital/ER bills over $5k are common, errors are well-documented (up to 80% of medical bills contain errors per widely cited industry stats), and "medical bill advocate" as a category already has proven demand — search local Facebook/Nextdoor for people complaining about a bill and DM them directly.
5. Close with the contingency pitch: "Send me the invoice, I'll tell you within 48 hours if you overpaid and by how much — you only pay if I find money."

## Time to First Dollar

- Day 1–3: build the intake form + market-rate research playbook for 2 verticals (start with medical billing + home services — highest volume of public complaints/leads).
- Day 3–7: source 8–10 real invoices via network ask + Nextdoor/Facebook free-check offer.
- Day 7–14: deliver findings memos, identify overcharges, close contingency agreements, initiate disputes/renegotiations on behalf of clients.
- **First dollar arrives when a dispute succeeds** — timeline depends on the counterparty (a vendor renegotiation can resolve in days; a medical billing dispute can take 2–6 weeks). To de-risk cash timing in weeks 1–2, prioritize cases where the "overcharge" can be recovered fast (e.g., disputing a not-yet-paid invoice or negotiating down inflated quote before signing) over already-paid bills requiring refund processes.

## Why This, Why Now

- Zero capital, zero inventory, zero build required to start — you can close your first case this week using nothing but research and negotiation skill.
- Contingency pricing means literally free to the customer to say yes, collapsing the sales cycle to nearly zero — this is the strongest structural advantage of any idea generated so far.
- Directly plays to sales/ops strength (negotiation, structured research, outreach) while software automation is a pure scaling lever, not a prerequisite.
- Recession/inflation-resistant: people become more price-sensitive to being overcharged, not less, when costs rise — demand doesn't depend on a booming economy.

## Risks / Open Questions

- **Recovery lag:** unlike a flat-fee service, contingency fees are only paid out once savings are actually realized — a vendor negotiation may take longer than a client expects, and a paid-invoice refund dispute can take weeks to months. Mitigate by offering the flat-fee option for clients who want speed/certainty, and by prioritizing pre-payment cases (quotes/contracts not yet signed) for your first cash-in-window.
- **Credibility gap on day one:** no track record yet. Mitigate with the free 10-minute check to build first case studies fast, and be transparent that you're new but confident in the research method.
- **Verticals require different expertise:** medical billing codes, contractor licensing rules, and private aviation contracts are each their own domain — don't try to cover all of them at once. Pick one vertical to prove the model (recommend: home services/contractor invoices, since it's the most universally relatable and has the most public comparison data), then expand.
- **Scope creep risk:** clients may expect you to fully manage the dispute/negotiation end-to-end rather than just deliver a memo — decide upfront whether you're selling "analysis only" or "analysis + I fight it for you" (the latter commands a higher fee but takes more time per case).

## Validation Signal to Watch

If 3+ of your first 10 free 10-minute checks reveal a real, defensible overcharge (>10% above market rate), the research methodology works and it's worth formalizing into the software layer. If free checks mostly come back "you paid a fair price," pivot toward the vertical with the most documented error rate (medical billing) rather than general contractor invoices.
