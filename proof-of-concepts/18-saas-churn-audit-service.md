# PoC 18 — "Why Are They Leaving?" — Churn & Onboarding Audit Service for Small SaaS Companies

**Date:** 2026-07-10
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Small SaaS companies (bootstrapped or early-funded, $5k-$100k MRR) lose subscribers every month and usually know their churn rate but not *why* people leave — cancellation surveys go unread, support tickets from frustrated users pile up unanalyzed, and onboarding drop-off points are rarely mapped. Founders are heads-down on product and growth, and churn analysis is exactly the kind of unglamorous, time-consuming diagnostic work that gets perpetually deprioritized despite directly determining whether growth actually compounds. This is distinct from PoC 05 (which fixes e-commerce conversion/speed) — the audience is subscription software businesses, the diagnostic method is analyzing existing qualitative data (cancellation reasons, support tickets, onboarding funnel drop-off) rather than page-speed tooling, and the fix recommendations are product/onboarding-focused rather than technical-performance-focused.

## Who It's For

Small SaaS founders/teams with a real subscriber base (100+ paying customers is a reasonable floor for having enough churn data to analyze) who collect some cancellation feedback (even a basic "why are you leaving" survey field) or have support ticket history, but haven't systematically reviewed it. Best entry point: founders posting about churn/retention frustration on Twitter/LinkedIn or in SaaS founder communities — a direct, self-identifying pain signal.

## How It Makes Money

- Flat audit fee: $500–$1,500 for a full churn/onboarding audit — categorizing and quantifying cancellation reasons, mapping the onboarding funnel for drop-off points, and delivering a ranked list of highest-impact fixes.
- Implementation upsell: $1,000–$3,000 project fee to actually build the top 1-2 recommended fixes (e.g., a revised onboarding email sequence, an in-app checklist, a win-back offer for cancelling users) — converts the software skill directly into higher-ticket revenue beyond the audit.
- Ongoing retainer: $300–$800/mo to re-run the analysis monthly and track whether churn rate/cancellation reason mix is improving — recurring revenue hook, since churn analysis decays in relevance the same way SEO/CRM data does without regular attention.
- Research-only lightweight tier: $200–$300 for just the cancellation-reason categorization (using their existing survey/ticket data), as a lower-commitment entry point before the full audit.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Client exports cancellation survey responses (if collected) and/or shares support ticket history and basic funnel data (signup → activation → paid conversion rates, usually available in their existing analytics tool).
   - Manually/LLM-assisted categorize cancellation reasons into themes (price, missing feature, poor onboarding, found alternative, no longer needed) and quantify frequency — surfacing which theme is actually the biggest lever, which is often not what the founder assumed.
   - Walk through the product's own signup/onboarding flow yourself as a new user would, noting friction points, confusing steps, or missing "aha moment" guidance — a fresh-eyes audit the founder is too close to the product to run objectively.
   - Deliver a ranked findings report: top 3 churn drivers by frequency/impact, plus specific, concrete fix recommendations for each.
2. **Software layer (build once 2–3 clients are live, funded by early audit fees):**
   - LLM-assisted text classification script to categorize open-ended cancellation survey responses or support ticket text into consistent themes automatically, rather than manual reading for every case — this is the single highest-leverage automation, since the categorization task is repetitive and well-suited to LLM classification at scale.
   - Reusable onboarding-audit checklist (common friction patterns: too many steps before value, unclear next action, no progress indicator, missing empty-state guidance) refined and reused across clients — same reusable-scaffold pattern used throughout this folder.
   - Simple reporting template (same Markdown/PDF generation pattern as `onepager.py`) populated from structured findings rather than written from scratch each time.

## Tools/Stack

- Client's existing survey tool (Typeform, in-app cancellation flow) and support tool (Intercom, Zendesk, or even just email) for raw data — no new tooling cost to access.
- Client's existing analytics tool (Mixpanel, Amplitude, or even basic Stripe/signup data) for funnel drop-off numbers.
- Claude/Gemini API for cancellation-reason text classification and onboarding-flow analysis synthesis.
- Google Docs for report delivery.
- Stripe/invoice for fee collection.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify prospects via SaaS founder communities (Indie Hackers, MicroConf-adjacent communities, SaaS-specific Slack/Discord groups) where churn/retention is a constantly recurring topic of open discussion — a dense, self-identifying, on-topic audience.
2. Free-sample hook: for a prospect posting about churn frustration, offer a quick, free take based only on publicly observable signals — sign up for their free trial/demo yourself, note 2-3 concrete onboarding friction points you hit firsthand, and share them unsolicited: "Tried signing up for [product] — hit some friction at [specific step] that's probably costing you activations. Happy to do a full churn audit if useful." This is a strong, cheap-to-produce demonstration of real product insight, not generic advice.
3. Position the audit as complementary to (not competing with) whatever growth/marketing efforts they're already running — churn reduction and acquisition are both levers, and founders often over-invest in acquisition while under-investing in retention, a framing that resonates once named explicitly.
4. Cross-sell potential with PoC 14 (AI chatbot setup) for the same SaaS buyer profile — a chatbot that catches confused users mid-onboarding is a natural extension of a churn/onboarding audit's findings.
5. A single "found the #1 reason 40% of your cancellations were happening" result is a highly specific, credible case-study stat for SaaS founder community posts.

## Time to First Dollar

- Day 1–3: identify 15-20 SaaS founders showing visible churn/retention frustration signals, sign up for the first 8-10 products' free trials to produce free-sample onboarding observations.
- Day 3–5: send outreach with the specific friction-point finding as the opener.
- Day 5–10: close 2–3 clients on the flat audit fee ($500–$1,500), collected upfront.
- **First dollar within 1–2 weeks** — no build dependency, the entire MVP is manual analysis plus a real trial signup, both doable same-day.

## Why This, Why Now

- Zero build required to start — signing up for a free trial and reading cancellation data requires no special tooling or access beyond what the founder already has.
- Recurring, structural pain: churn is a permanent, ongoing metric every subscription business tracks and worries about, unlike one-time problems — creating a naturally renewable audit/retainer cycle.
- Deal-size leverage similar to PoC 08/16: a SaaS business's customer lifetime value math makes even a modest churn-rate improvement worth many multiples of the audit fee, an easy ROI story once quantified concretely in the findings report.
- Directly plays to both technical skill (data categorization, product-flow analysis) and sales/ops skill (finding and closing founders in dense online communities) — a well-balanced fit for the stated skill set.

## Risks / Open Questions

- **Founders may already suspect the cause and be defensive about it:** frame findings constructively and back them with quantified data (frequency counts, not just impressions) to keep the conversation collaborative rather than critical.
- **Data quality varies:** some SaaS companies have sparse or low-response-rate cancellation surveys, limiting how much signal is actually available to analyze — the free-trial-based onboarding audit (which requires no client data at all) is a valuable fallback/starting point when survey data is thin.
- **Implementation upsell requires product/technical judgment specific to each company's stack** — be honest about the boundary between "I can tell you what to fix" and "I can build it in your specific codebase," and don't overcommit on implementation scope during the sales conversation.
- **Crowded adjacent category:** product consultants and growth agencies already offer churn-reduction services at a higher price point — differentiate on speed, specificity (real trial-signup findings, not generic frameworks), and accessible pricing for bootstrapped-stage companies rather than competing head-on with funded-stage growth consultancies.

## Validation Signal to Watch

If 3+ of your first 10 outreach messages (each containing a real, specific friction point you personally hit signing up for their product) generate a reply, the hook and research method are working — scale outreach into SaaS founder communities more broadly. If cancellation-reason categorization on early client data doesn't surface any single dominant, actionable theme, the churn driver may be more structural (pricing, product-market fit) than fixable via onboarding/communication changes — be transparent with the client about that finding rather than manufacturing a false "easy fix" narrative.
