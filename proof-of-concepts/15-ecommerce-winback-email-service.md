# PoC 15 — "There's Revenue Sitting in Your Email List" — Win-Back Campaign Service for Dormant E-commerce Customers

**Date:** 2026-07-10
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Every e-commerce store with any operating history has a customer list full of people who bought once (or a few times) and went quiet — and acquiring a new customer costs far more than re-activating an existing one, yet almost no small/mid store owner runs a dedicated win-back program. They have the email platform (Klaviyo, Mailchimp, Shopify Email) already installed and the list already sitting there; what's missing is the segmentation logic, the offer strategy, and the actual campaign build. This is distinct from PoC 05 (which fixes acquisition-funnel leaks) and PoC 06/12 (which are about a founder's personal content) — this service monetizes a database the client already owns, with revenue results you can often point to within the same billing cycle.

## Who It's For

Shopify/WooCommerce stores with 12+ months of order history and an email platform already connected but an inactive or generic email program (infrequent sends, no segmentation, no win-back flow) — the same general prospect pool as PoC 05, making both services easy to cross-pitch to the same store owner.

## How It Makes Money

- Flat campaign-build fee: $400–$900 to segment the dormant list (e.g., "bought once 90-365 days ago, no repeat purchase"), write and set up a 3-4 email win-back sequence, and configure the automation in their existing platform.
- Performance-linked pricing option: reduced upfront fee ($200–$300) + 10-15% of attributed revenue from the campaign in its first 30 days — a strong closer since results are directly trackable through the email platform's own attribution.
- Ongoing lifecycle retainer: $300–$700/mo to maintain and expand beyond win-back into a full lifecycle program (post-purchase, VIP/repeat-customer, cart abandonment) — natural expansion once the first campaign proves ROI.
- Segment-specific micro-campaigns as repeat, lower-effort upsells (e.g., a holiday-specific win-back push) once the core flow is built and reusable.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Client grants access (or exports a customer/order CSV) from their email platform or Shopify admin.
   - Segment manually using the platform's built-in filters (most tools already support "last purchase date" and "total orders" filtering natively — no custom tooling needed) to define the dormant win-back audience.
   - Write the win-back sequence (3-4 emails: "we miss you," a value-reminder, a targeted incentive, a final urgency touch) using an LLM prompted with the brand's product catalog and tone, then set it up directly in the client's existing platform using its native automation builder.
   - Report results after 2-4 weeks using the platform's own attribution/reporting (opens, clicks, revenue attributed to the flow) — no separate analytics tooling required.
2. **Software layer (build once 2–3 clients are live, funded by early campaign fees):**
   - Reusable email-sequence prompt templates by store category (apparel, beauty, home goods, food/beverage) so each new client's copy starts from a proven scaffold rather than a blank page — same reusable-template pattern used throughout this folder.
   - A simple script pulling order data via the Shopify API to auto-generate the dormant-customer segment definition and flag the highest-value dormant segments (e.g., customers with high average order value who've gone quiet) rather than relying on the platform's basic filters alone.
   - Results-tracking sheet (Airtable/Google Sheets) aggregating campaign performance across clients — both for your own case-study library and to spot which offer types/sequences perform best, refining the template library over time.

## Tools/Stack

- Client's existing email platform (Klaviyo, Mailchimp, Shopify Email) — no new tooling cost, you're working inside what they already pay for.
- Shopify/WooCommerce APIs (free developer access) for order data segmentation once automating.
- Claude/Gemini API for email copywriting.
- Stripe/invoice for fee collection; performance-fee tracking via the platform's own attribution reporting.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify prospects the same way as PoC 05 (Facebook Ad Library for active-ad Shopify stores) plus a second, independent signal: stores with an inactive or generic-looking email presence — sign up for their list and observe send frequency/quality over a few days as a free, direct diagnostic.
2. Free-sample hook: calculate a rough dormant-list revenue estimate before outreach ("you likely have 400+ customers who bought once and went quiet — even a 5% reactivation rate at your average order value is real revenue sitting untouched") using only public storefront signals (average order value is often inferable from product pricing) — a compelling, specific number beats a generic pitch.
3. Position the performance-fee option prominently in outreach — "low upfront cost, I only make real money if this makes you money" mirrors the risk-reversal framing that's worked well across PoC 02/08 in this folder and is unusually easy to say yes to for a store owner who's skeptical of agency pitches.
4. Shopify/e-commerce founder communities (same venues as PoC 05) are a natural fit, and cross-selling into any existing PoC 05 client relationship is a same-call upsell rather than new outreach.
5. A single strong result ("this win-back flow generated $3,200 in the first 3 weeks") is a highly quotable, concrete case-study stat for both LinkedIn/community posts and future cold outreach.

## Time to First Dollar

- Day 1–3: identify 15-20 Shopify prospects with active ads and weak email presence, estimate rough dormant-list value for outreach.
- Day 3–5: send outreach leading with the specific revenue-opportunity estimate.
- Day 5–10: close 2–3 clients on the flat fee or performance-hybrid pricing, build and launch campaigns within days of closing since the platform/list already exists.
- **First dollar within 1–2 weeks** on the flat-fee portion; performance-fee revenue follows 2-4 weeks after launch once attribution data is available.

## Why This, Why Now

- Zero build required to start — segmentation, copywriting, and automation setup all happen inside tools the client already owns and pays for, with no new infrastructure needed.
- Strong, fast, and directly attributable ROI story: email platforms natively report revenue per flow, making results trackable and provable without any custom analytics work on your part.
- Performance-linked pricing option is one of the lowest-friction closes in this folder, since the client is monetizing a database they already own rather than being asked to fund new customer acquisition.
- Natural expansion path (win-back → full lifecycle program) creates a credible, low-effort route from a single project fee to an ongoing retainer.

## Risks / Open Questions

- **Deliverability/list quality risk:** emailing a genuinely dormant or old list can trigger spam complaints or hurt sender reputation if not handled carefully — recommend a smaller, most-recently-dormant segment first and monitor engagement/complaint rates before expanding to the full list.
- **Performance-fee attribution disputes:** be explicit upfront about what counts as "attributed revenue" (platform-native attribution window and rules) to avoid disagreements when it's time to invoice.
- **Results vary significantly by brand/offer strength:** a weak product or uncompetitive incentive will underperform regardless of email execution quality — set expectations accordingly during the sales conversation rather than promising a specific revenue outcome.
- **Overlap with PoC 05:** both target similar Shopify prospects — decide per-prospect which pain point is more visible/urgent to lead with (weak email presence → lead with this; slow site/high cart abandonment → lead with PoC 05) rather than pitching both simultaneously and diluting the message.

## Validation Signal to Watch

If 3+ of your first 10 outreach messages (each with a specific dormant-list revenue estimate) generate a reply, the hook is working — scale outreach volume. Once a campaign launches, if 30-day attributed revenue meaningfully exceeds your flat fee for 2+ of your first clients, the performance-fee pricing option is worth leading with more aggressively in future outreach, since it's both a stronger closer and reveals genuinely favorable unit economics for the client.
