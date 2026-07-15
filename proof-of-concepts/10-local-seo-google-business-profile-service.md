# PoC 10 — "Show Up First on Google" — Local SEO & Google Business Profile Optimization Service

**Date:** 2026-07-09
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Local service businesses (dentists, contractors, salons, law firms, auto shops) live or die by whether they show up in Google's local "map pack" (the top 3 results shown for searches like "plumber near me"). Ranking there depends on a specific, well-documented set of factors — complete/accurate Google Business Profile data, consistent business citations across directories, category selection, photo volume, posting activity, and review velocity — that most owners have never properly configured. This is distinct from PoC 01 (which handles review *responses*): this service handles the underlying ranking mechanics that determine whether a business is found at all. It's a research-and-configuration service with a highly visible, easily demonstrated before/after (map pack position), making it one of the most concretely provable service categories to sell cold.

## Who It's For

Local service businesses in competitive categories (multiple providers competing for the same searches) with an incomplete or poorly optimized Google Business Profile — visible for free by simply searching their category + city and checking where they rank plus auditing their profile completeness. Best entry point: businesses ranking on page 2 or the bottom of the map pack despite having a real, established business (proves demand exists, just not visibility).

## How It Makes Money

- Flat one-time optimization fee: $300–$600 to fully audit and rebuild a Google Business Profile (categories, services, attributes, photos, Q&A seeding, initial post cadence) plus a citation consistency pass across major directories (Yelp, Apple Maps, Bing Places, industry-specific directories).
- Monthly maintenance retainer: $150–$350/mo for ongoing posting, photo refreshes, Q&A monitoring, and citation upkeep — rankings decay without maintenance, which is the natural recurring-revenue hook.
- Rank-tracking upsell: $50–$100/mo add-on to provide a monthly report showing map pack position changes for their top 5 target search terms — makes the value of the retainer visible and renewable.
- Bundle opportunity with PoC 01 (review-reply service) — same buyer, adjacent problem, natural cross-sell either direction.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Search a prospect's category + city on Google, screenshot their current map pack position (or lack thereof) as the outreach hook.
   - Audit their Google Business Profile manually (free, just requires being logged into a Google account or being granted manager access): check category accuracy, business description keyword usage, photo count/recency, Q&A section, posting frequency, and NAP (name/address/phone) consistency against a manual spot-check of 5-10 major directories.
   - Deliver a findings report plus, once engaged, do the actual configuration work directly in their Business Profile dashboard (add photos, correct categories, write keyword-aligned service descriptions, seed Q&A, set up a posting cadence).
2. **Software layer (build once 2–3 clients are live, funded by early project fees):**
   - Simple script to check current map pack ranking for a given search term + location (can be done via manual search initially, automated later via a rank-checking API or scheduled search-and-screenshot script) — turns a manual weekly check into an automated monthly report.
   - Citation-consistency checker: script that searches a business name across major directories and flags NAP mismatches, replacing the manual spot-check with a repeatable pass.
   - LLM-assisted content generation for Google Posts (weekly micro-updates) and keyword-optimized service descriptions, using a per-client profile of services/keywords — same reusable-template pattern as prior PoCs in this folder.

## Tools/Stack

- Google Business Profile Manager (free) — the core interface you're optimizing.
- Manual/free-tier directory checks (Yelp, Bing Places, Apple Maps Connect) for citation consistency.
- Claude/Gemini API for Google Posts drafting and service-description keyword optimization.
- Simple scheduled script (reusing this repo's cron-driven pattern) for rank tracking once volume justifies automation.
- Stripe/invoice for fee collection.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Pick 2-3 competitive local categories (HVAC, dentists, personal injury attorneys, auto repair) in your area and search each — screenshot results for businesses ranking poorly (page 2, or missing key profile elements like photos/reviews despite being an established business).
2. Free-sample hook: send the screenshot plus 2-3 specific, concrete fixes ("your category is set to 'General Contractor' but you should be 'Roofing Contractor' — this alone likely costs you visibility for your highest-intent searches") as a cold outreach opener — same specific-finding tactic proven across PoC 05 and 07.
3. Local chamber of commerce and small business networking events are strong in-person venues, since "why don't I show up on Google" is a near-universal frustration local business owners will volunteer unprompted once you ask.
4. Cross-sell into any existing PoC 01 (review-reply) relationships — same buyer profile, adjacent and complementary pain point, warm introduction already established.
5. A visible rank improvement (moving into the map pack, or moving up within it) within 2-4 weeks of optimization is a powerful, easily-shared testimonial — ask for a Google review from the client themselves once you see movement (fittingly on-brand for the service you sold them).

## Time to First Dollar

- Day 1–2: identify 15–20 poorly-ranked local businesses across 2-3 categories, screenshot findings.
- Day 2–4: send outreach with the specific-finding hook.
- Day 4–9: close 3–5 clients on the one-time optimization fee ($300–$600), collected upfront.
- **First dollar within 1–2 weeks** — the entire MVP is manual profile configuration work you can start same-day with zero build dependency.

## Why This, Why Now

- Zero build required to start — the initial service is pure manual configuration inside a free Google tool, directly playing to research/ops execution skill.
- Extremely visible proof of value: map pack position is a concrete, googleable, before/after fact that neither party can dispute — removes the "did this actually work" ambiguity that plagues vaguer services.
- Natural recurring revenue: rankings decay without maintenance (competitors keep posting/optimizing), which converts a one-time project into an obvious ongoing retainer rather than requiring you to invent a recurring hook.
- Directly complementary to PoC 01, creating a two-product local-business bundle (visibility + reputation) sold to the same buyer with a single outreach motion.

## Risks / Open Questions

- **Google's ranking algorithm changes over time** and isn't fully transparent — set expectations around "best practices, directional improvement" rather than guaranteed specific rankings.
- **Access/trust:** getting manager access to a client's Google Business Profile requires some trust — mitigate by offering a "you make the changes, I tell you exactly what to click" consulting-only option for the most trust-sensitive clients.
- **Competitive category saturation:** in categories where every competitor already has a well-optimized profile, the relative gain from optimization shrinks — prioritize categories/regions where you've verified multiple competitors have visibly weak profiles before investing outreach time.
- **Attribution ambiguity:** rank changes can be influenced by factors outside your control (competitor changes, algorithm updates) — track and report changes honestly rather than overclaiming credit for every fluctuation.

## Validation Signal to Watch

If 3+ of your first 10 outreach messages (each with a specific, concrete profile finding) generate a reply within a week, the hook and category selection are working — scale outreach in that category/region. If response rates are weak in one category, test another (dentists and attorneys tend to have higher marketing budgets and stronger ROI awareness than some trades) before concluding the offer itself needs rework.
