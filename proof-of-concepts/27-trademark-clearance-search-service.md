# PoC 27 — "Don't Get Sued for Your Own Business Name" — Trademark Clearance Search Service for New Businesses/Products

**Date:** 2026-07-12
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Founders naming a new business, product, or app routinely pick a name, buy the domain, print materials, and launch — without ever checking whether that name conflicts with an existing trademark, only to discover months later (via a cease-and-desist letter) that they need to rebrand everything at real cost and disruption. A proper trademark clearance search before launch is standard advice from any startup lawyer, but full attorney-conducted searches cost $500-$1,500+ and most bootstrapped founders skip the step entirely, assuming (often wrongly) that a basic Google search or domain availability check is sufficient. This is distinct from PoC 11 (which reviews existing contracts before signature) — this is a proactive, pre-launch naming-risk check using entirely free public trademark databases, sold at a price point far below attorney rates while still delivering genuinely useful risk-flagging (explicitly not a substitute for formal legal clearance on higher-stakes launches).

## Who It's For

Early-stage founders naming a new business, product line, or app who haven't yet filed a trademark application or consulted an attorney — best entry point: people actively discussing a new venture name/branding decision in founder communities, or businesses about to invest in a rebrand/launch (visible via "landing page coming soon" or pre-launch social posts).

## How It Makes Money

- Flat clearance-check fee: $100–$250 per name search, covering a search across USPTO's trademark database plus common-law/marketplace checks (domain availability, social handle availability, existing marketplace listings using the same/similar name) and a plain-English risk summary.
- Multi-name comparison package: $250–$500 to check 3-5 candidate names side by side before the founder commits, positioned as a decision-support tool during the actual naming process rather than a post-decision check.
- Referral partnership with startup-focused attorneys: for names flagged as higher-risk or ambiguous, refer to a trademark attorney for formal clearance and registration — a natural, credibility-building complement rather than competing with legal services, potentially generating referral relationships in both directions.
- Rush fee for founders on a tight launch timeline: +$50–$100 for 24-hour turnaround.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Search the candidate name (and close variations/misspellings) in USPTO's free TESS (Trademark Electronic Search System) database, checking for existing registered or pending trademarks in the same or related goods/services categories.
   - Run a common-law search: Google the name plus relevant industry terms, check domain availability, check major social platform handle availability, and check whether the name is already in active commercial use anywhere relevant even without a formal registration (common-law trademark rights can exist without registration).
   - Deliver a plain-English risk summary: clear conflicts found (if any), ambiguous/moderate-risk findings worth attorney review, and a straightforward "looks clear based on available public records" if nothing concerning surfaces — explicitly framed as a risk-flagging screen, not a legal opinion.
2. **Software layer (build once 2–3 clients are live, funded by early fees):**
   - Script to query USPTO's TESS database (or its underlying data via available search interfaces) programmatically for a given name plus common variations, replacing repetitive manual search entry with a faster, more thorough automated pass — same automation-layer pattern used across the folder's other diagnostic services.
   - Simple domain/social-handle availability checker (many registrars/platforms expose free availability-check endpoints) bundled into a single automated first-pass report.
   - Reusable risk-summary template (same reporting pattern as `onepager.py`) populated from structured search findings, with an LLM assist translating raw database results into plain-English explanations for non-legal-background founders.

## Tools/Stack

- USPTO TESS (free, public) for federal trademark search.
- Domain registrar availability checks and social platform handle-search tools (free, publicly accessible).
- Claude/Gemini API for translating raw search findings into plain-English risk summaries.
- Google Docs for report delivery.
- Stripe/invoice for fee collection.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify prospects via founder communities where naming/branding decisions are actively being discussed ("what should I name my..." posts are extremely common and easy to find in startup/indie hacker communities) — a direct, self-identifying, perfectly-timed signal.
2. Free-sample hook: for a prospect openly discussing candidate names, run a quick free check on one of their options and share a genuinely useful finding: "Ran a quick trademark check on '[name]' — found [a close registered mark in a related category / it looks reasonably clear], want the full clearance report before you commit?" This is one of the most naturally-occurring free-sample opportunities in the folder, since founders are already publicly asking for input on names.
3. Position the pricing comparison clearly against attorney rates — "a fraction of what a full attorney search costs, and a check you should genuinely do before spending money on a logo/domain/materials" reframes this as a smart, cheap insurance step rather than a nice-to-have.
4. Startup accelerator/incubator communities and university entrepreneurship programs are a strong venue, since name-clearance is a standard piece of advice given to founders there but rarely actually acted upon due to cost/friction.
5. A single "caught a conflict before they spent $2k on branding" story is a highly credible, relatable case study within founder communities, since the counterfactual cost (a forced rebrand after launch) is well understood and feared by anyone who's heard of it happening to someone else.

## Time to First Dollar

- Day 1–3: identify 15-20 founders actively discussing naming decisions in public communities.
- Day 3–5: run free quick-checks on one candidate name each for the first 8-10, share findings as the outreach.
- Day 5–10: close 2–3 clients on the full clearance-check fee ($100–$250) or multi-name comparison package, collected upfront given the fast, pre-purchase-decision nature of the service.
- **First dollar within 1–2 weeks** — no build dependency, USPTO's database is free and immediately searchable, and turnaround per search can be same-day.

## Why This, Why Now

- Zero build required to start — the core diagnostic tool (USPTO TESS) is free, public, and immediately usable without any account or API access.
- Naturally occurring, high-frequency demand signal: founders publicly ask for naming help/opinions constantly in online communities, making prospecting unusually easy compared to services requiring you to identify a hidden problem.
- Extremely favorable price-vs-alternative comparison (attorney search cost vs. this service) makes the pitch land quickly without requiring buyer education.
- Genuine risk-aversion driver (similar to PoC 21's accessibility angle) tends to convert with real urgency once a founder understands the downside scenario (forced rebrand after real money is already spent).

## Risks / Open Questions

- **Not a substitute for legal clearance:** this must be marketed explicitly as a preliminary risk-flagging screen using public records, not a formal legal trademark clearance opinion — always recommend attorney review before actual trademark filing or for any higher-stakes launch (significant marketing spend, funded startup, litigious industry), and never represent findings as a legal guarantee of "no risk."
- **Search thoroughness has real limits:** a manual/semi-automated public-database search will miss some nuances a professional trademark attorney or full paid search service (which checks additional state-level and international registries) would catch — be transparent about scope boundaries in every deliverable.
- **Unauthorized practice of law risk, similar to PoC 11:** stick to factual risk-flagging (here's what exists in the databases) rather than legal interpretation or advice about likelihood of a successful legal challenge — this is a meaningful compliance boundary to respect consistently.
- **False sense of security risk:** a "looks clear" finding could be wrongly interpreted by a founder as a legal guarantee — be explicit in every report about what was and wasn't checked, and the inherent limits of a non-attorney-conducted search.

## Validation Signal to Watch

If 3+ of your first 10 free quick-checks generate a genuine "oh that's useful, tell me more" response, the naturally-occurring demand and hook are validated — scale outreach across more founder/startup communities. If most quick-checks come back entirely clear with nothing notable to report, the free sample may feel less compelling — consider leading instead with the multi-name comparison package framing (decision support during the naming process itself, not just a pass/fail check) where the value proposition doesn't depend on finding an actual conflict to feel useful.
