# PoC 07 — "Win the Money You're Leaving on the Table" — Grant & RFP Proposal Writing Service for Small Businesses/Nonprofits

**Date:** 2026-07-08
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Small businesses, nonprofits, and local governments leave enormous amounts of grant and RFP funding unclaimed every year simply because writing a competitive proposal is time-consuming, formulaic, and intimidating — not because the funding doesn't exist. Federal, state, local, and foundation grant programs (SBIR/STTR, small business innovation grants, community development block grants, arts/nonprofit foundation grants) and public-sector RFPs are published on a predictable schedule with clear eligibility criteria, but most eligible applicants either don't apply or submit weak proposals because they lack a dedicated grant writer. This is a research + writing service with a strong, provable ROI story (funding won vastly exceeds your fee), and it scales cleanly with LLM-assisted drafting since proposals are highly structured, template-driven documents.

## Who It's For

- Small businesses eligible for SBIR/STTR or state economic-development grants (especially tech/manufacturing/R&D-adjacent).
- Nonprofits applying to foundation and government grants (arts, community services, education).
- Small agencies/contractors responding to public-sector RFPs (local government IT, construction, consulting) who don't have a proposal team.

Best entry point: organizations that have clearly won at least one grant/RFP before (proven eligibility + credibility) but haven't applied again recently — momentum plus an obvious re-engagement opener.

## How It Makes Money

- Flat project fee per proposal: $500–$2,500 depending on complexity and grant size (a 2-page LOI is cheaper than a full SBIR Phase I narrative).
- Contingency/success-fee hybrid: reduced upfront fee ($300–$500) + 5–10% of awarded funding if the application succeeds — mirrors PoC 02's risk-reversal structure and is a strong closer for cash-strapped nonprofits.
- Retainer for organizations that apply to grants regularly: $500–$1,000/mo for ongoing pipeline management (tracking open opportunities, drafting on a rolling basis) rather than one-off engagements.
- Research-only tier: $150–$300 for a "here are the 5 grants/RFPs you're eligible for and their deadlines" opportunity report, sold as a low-friction entry before the full writing engagement.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Pick one niche to start (recommend: local nonprofits, since grants.gov, foundation directories, and local community foundation sites are all free and searchable, and nonprofit decision-makers are generally more reachable than corporate procurement).
   - Manually search free databases (grants.gov, Candid/Foundation Directory free listings, state economic development sites, SAM.gov for federal contracts/RFPs) for open opportunities matching a prospect's profile.
   - Draft the proposal using an LLM prompted with the funder's stated evaluation criteria + the client's mission/track record/budget details gathered in an intake call, then edit for accuracy and voice before submission.
2. **Software layer (build once 2–3 engagements are underway, funded by early project fees):**
   - Scraper/monitor script (consistent with this repo's `trends.py` pattern) that checks grants.gov and state grant portals on a schedule and flags new opportunities matching saved client eligibility criteria — turns you from reactive searcher into proactive opportunity-spotter.
   - Reusable proposal-section template library (needs statement, methodology, budget narrative, evaluation plan) driven by structured client intake data, so each new proposal starts from a scaffold rather than a blank page — same reusable-template philosophy as `onepager.py`.
   - Per-client profile config (mission, past wins, budget ranges, team bios) stored once and reused across every future application for that client, cutting re-entry time on repeat engagements.

## Tools/Stack

- grants.gov, SAM.gov, Candid/Foundation Directory (free tier), state/local economic development sites — all free public data sources.
- Claude/Gemini API for first-draft generation against funder-specific evaluation criteria.
- Google Docs for collaborative drafting/client review.
- Simple scheduled script (same cron pattern used elsewhere in this repo) for opportunity monitoring once volume justifies it.
- Stripe/invoice for project fees; contract terms for success-fee arrangements should be simple and clearly written (flat % of awarded amount, paid on receipt of funds).

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Build a list of 20–30 local nonprofits or small businesses with a public track record of at least one past grant/award (visible in press releases, annual reports, or grants.gov award history — all free to search) — this filters for organizations who've already proven they're fundable.
2. Free-sample hook: identify one specific, currently-open, clearly-eligible grant or RFP for each prospect (real deadline, real amount) and lead outreach with that finding: "I found a $25k grant you're eligible for, deadline is in 5 weeks — want me to draft it?" — same specific-finding-as-opener tactic proven in PoC 05.
3. Local chamber of commerce, nonprofit association meetups, and small business development center (SBDC) events are natural low-cost/no-cost venues to meet this exact buyer in person — SBDCs in particular often maintain referral relationships and may send you clients directly once you're known to them.
4. Close with the research-only tier first if the full project fee is a stretch for a cash-strapped nonprofit, then upsell to the writing engagement once the opportunity report proves your research quality.
5. A single won grant is a powerful case study — ask for a reference/testimonial immediately upon award notification, while gratitude is highest.

## Time to First Dollar

- Day 1–3: pick the niche, build the prospect list, identify one real open opportunity per prospect for the first 10.
- Day 3–6: send outreach with the specific opportunity + deadline as the opener.
- Day 6–12: close 2–3 clients on either the research-only tier or a flat project fee, collected upfront via Stripe/invoice.
- **First dollar within 1–2 weeks** via the flat/research fee; **outsized payoff (potentially $5k–$50k+ in success fees) arrives later** on whatever timeline the funder's award cycle runs, so don't rely on success fees alone for near-term cash — price the base engagement to cover weeks-1-4 cash needs independent of award outcomes.

## Why This, Why Now

- Extremely low competition relative to demand: most small businesses/nonprofits don't know a dedicated grant-writing option exists at this price point (traditional grant writers often charge $5k+ per proposal or require a large retainer) — you're priced well below the traditional market with LLM-assisted drafting speed as the enabler.
- Public, free, well-organized data sources (grants.gov, SAM.gov, foundation directories) mean the research side of this business costs literally nothing and requires no special access.
- Extremely strong ROI story for the buyer — the ratio of funding won to your fee makes this one of the easiest "yes" pitches across all ideas generated so far, once you find a real, relevant, time-bound opportunity to lead with.
- Software skill compounds directly into a durable moat: opportunity-monitoring automation and a growing template library make you faster and cheaper than any human grant writer over time, without ever needing to raise prices.

## Risks / Open Questions

- **Award cycles are slow and uncertain** — grant/RFP decisions can take weeks to months, and success isn't guaranteed even for a strong proposal, so success-fee-only deals are a poor fit for urgent cash needs; lead with flat/upfront fees for near-term revenue.
- **Domain credibility matters:** funders and evaluators can tell when a proposal is generic — the LLM draft must be heavily grounded in the client's real track record, budget specifics, and the funder's actual stated criteria, not generic boilerplate; treat the LLM as a first-draft accelerator, not a finished-product generator.
- **Compliance/formatting requirements vary widely** by funder (page limits, required sections, specific forms) — a rejected proposal on a technicality is a completely avoidable and reputation-damaging failure mode; build a compliance checklist per funder type early.
- **Niche selection matters a lot:** nonprofits are more reachable and lower-friction to close than corporate/government procurement, but grant sizes and fees are correspondingly smaller — decide upfront whether you're optimizing for deal volume (nonprofits) or deal size (SBIR/public RFPs), since outreach and proposal complexity differ substantially between the two.

## Validation Signal to Watch

If 3+ of your first 10 "I found a specific grant you're eligible for" outreach messages get a reply within a week, the opener tactic and niche are working — scale outreach volume in that niche. If nonprofit outreach is slow, test the SBIR/small-business grant angle instead, where deal sizes are larger and the same specific-opportunity-opener tactic should work even harder given higher stakes per applicant.
