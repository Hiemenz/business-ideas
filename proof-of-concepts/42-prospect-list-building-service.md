# PoC 42 — "Your Sales Team Spends 40% of Their Time Finding Contacts" — B2B Prospect List Building & Enrichment Service

**Date:** 2026-07-15
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Most small B2B sales teams and solo founders doing outbound spend a disproportionate amount of their selling time on manual prospecting — searching LinkedIn, manually pulling company data, trying to find verified email addresses, and organizing everything into a usable spreadsheet. This is genuinely low-leverage work: a skilled salesperson's time is worth far more spent on calls and closing than on list building. Every part of the prospecting and enrichment workflow is automatable or systematizable using a combination of free and low-cost tools (Apollo.io's free tier, Hunter.io's free lookup quota, LinkedIn basic search, and a structured enrichment process), and the output — a targeted, verified, prioritized prospect list — is a concrete, immediately usable deliverable that saves the buyer 10-20 hours of work they can directly attribute to the purchase. This is distinct from PoC 08 (outbound appointment setting, which actually runs the outreach on the client's behalf) — this is the upstream step: building the list the client then works themselves.

## Who It's For

Early-stage B2B startups with 1-3 salespeople, solo founders doing their own outbound, or marketing agencies running campaigns for clients who need targeted prospect lists as inputs. Best entry points: teams who've just hired their first SDR, teams launching a new product or entering a new market vertical, or founders who've expressed frustration about how much time prospecting takes relative to actual selling.

## How It Makes Money

- Per-list flat fee: $150–$400 for a targeted prospect list of 200-500 verified contacts matching a specified ICP (industry, company size, geography, job title/function, tech stack used), delivered as a clean CSV with company name, contact name, title, LinkedIn URL, verified email, and any enrichment fields specified (e.g., funding stage, headcount, tech stack).
- Ongoing list refresh: $100–$200/mo to update a defined ICP list monthly — removing churned contacts, adding new hires/companies matching the criteria, and re-verifying email addresses that bounce — for clients running continuous outbound programs.
- ICP definition workshop add-on: $150–$250 for clients who aren't sure exactly who their best prospect looks like — a structured 60-min session using their existing customer data to identify the highest-fit ICP attributes, producing the targeting criteria that inform all future list builds.
- Segmented multi-list packages for clients entering multiple new verticals simultaneously, bundling 3-5 lists at a per-list discount.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Take a detailed ICP brief from the client: target industry(ies), company size range (employees or revenue), geography, job titles/functions to target, and any disqualifying criteria (e.g., exclude companies using a specific competitor tool).
   - Use Apollo.io's free tier (provides contact search with limited export credits — enough to validate the workflow and fulfill the first 1-2 paid lists), LinkedIn basic search for company identification, and Hunter.io's free monthly domain lookup quota for email verification to build the initial list manually.
   - Verify emails for deliverability using NeverBounce or ZeroBounce free trial credits before delivery.
   - Deliver a structured CSV with a brief methodology note (search criteria used, sources checked, verification approach) so the client understands what they received.
2. **Software layer (build once 2–3 clients are live, funded by early list fees):**
   - Reusable ICP brief template and intake form that captures every attribute needed to run a precise search, reducing back-and-forth and enabling faster turnaround per list.
   - Lightweight Python enrichment script combining Apollo.io API (paid tier justified by client volume once revenue supports it), Hunter.io API, and LinkedIn data to automate the bulk of the contact-finding and enrichment work, reducing per-list time from 4-6 manual hours to under 1 hour.
   - Email verification pipeline (integrated NeverBounce or ZeroBounce API call as a final step) run automatically on every list before delivery, ensuring deliverability rate is consistently high enough that clients trust the list quality.

## Tools/Stack

- Apollo.io free tier (contact search and limited export) — upgrade to $49/mo paid tier once client volume justifies it, billable as a cost pass-through.
- Hunter.io free tier (domain email lookup and verification) for initial engagements.
- LinkedIn basic search for company identification and contact validation.
- NeverBounce or ZeroBounce free trial for initial email verification.
- Google Sheets / CSV for list delivery.
- Python + requests for the enrichment automation script (build after first 2-3 paid lists).
- Stripe/invoice for fee collection.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify prospects in sales and founder communities (r/sales, r/startups, Indie Hackers, B2B SaaS Slack groups) where "how do I build a prospect list" and "we spend too much time prospecting" are constant, highly specific complaints — direct, in-the-moment demand signals.
2. Free-sample hook: for a prospect who describes their ICP, pull a small sample list (25-50 contacts) for free using the free-tier tools, deliver it unprompted as the opener: "You mentioned you're targeting [ICP]. Built a quick 30-contact sample list — here's what it looks like [attach CSV snippet]. Happy to build out the full 300 if the targeting looks right." A concrete, tangible deliverable that requires no explanation and demonstrates quality before the client has committed to anything.
3. Outreach to early-stage founders who've recently raised a seed round (public information from Crunchbase/TechCrunch announcements) — these founders are almost universally starting to build outbound for the first time and have both the need and the budget, with a highly predictable post-funding urgency window.
4. Apollo.io, Clay, and similar sales tool user communities are a strong venue — these are exactly the buyers who understand what a prospect list is worth and are already investing in the outbound infrastructure to use one.
5. A documented "replaced 15 hours/week of manual prospecting with a $250 list" ROI story lands immediately and concretely with any sales leader.

## Time to First Dollar

- Day 1–2: build the ICP intake brief template and run one end-to-end test list build on your own mock ICP to validate the free-tier workflow and measure time per contact.
- Day 2–4: identify 15-20 prospects actively building outbound programs, prepare a sample list snippet (10-15 contacts) for the 8-10 most specific ICP descriptions you find.
- Day 4–7: send outreach with the sample list attached.
- Day 7–12: close 2–3 clients on the per-list fee ($150–$400), collected upfront; deliver within 2-3 days per list.
- **First dollar within 1–2 weeks** — the free-tier tools are immediately usable, the first list is fully buildable manually, and the sample-list hook is one of the highest-converting free-sample approaches in the folder because the deliverable speaks for itself.

## Why This, Why Now

- Concrete, measurable ROI that is trivially easy for the buyer to calculate: if an SDR costs $50/hr and spends 10 hours/week prospecting, a $300 list pays for itself in hours — a math problem any sales leader can do in their head.
- Free-sample hook (a real, targeted sample list) is uniquely persuasive because it demonstrates both the targeting methodology and the data quality in a single artifact, removing all ambiguity about what the buyer is purchasing.
- Apollo.io and similar tools have democratized the underlying data but not the judgment layer (knowing which criteria produce high-fit prospects vs. noise) — the service charges for that judgment plus the time, not the data access itself.
- Natural progression into ongoing monthly refresh retainer once a client has built their outbound program around a specific ICP list, creating genuinely recurring revenue without needing a new sale each month.

## Risks / Open Questions

- **Email deliverability is a shared-responsibility problem:** even a verified list will have some bounce rate; set clear expectations upfront (target <3% hard bounce rate, not 0%) and don't guarantee deliverability for contacts whose roles may have changed between list build and send date.
- **Apollo.io free tier limitations will cap early throughput:** the free tier's export limits mean the first few lists may require some manual supplementation — be transparent about this with clients and upgrade to paid tier as soon as the revenue math supports it (at $300/list, a 2-list week more than covers the $49/mo Apollo paid tier).
- **Data privacy compliance varies by geography:** prospect lists for contacts in the EU/UK may have GDPR implications depending on how the client uses them — note this clearly in your service terms and recommend the client consult their legal counsel on compliant outbound use, since you're building the list, not running the campaign.
- **ICP precision matters more than list size:** a 200-contact list of perfectly-matched prospects outperforms a 2,000-contact list of loosely-matched ones — push back on clients who want maximum volume over targeting precision, since their results (and therefore your reputation) depend on quality.

## Validation Signal to Watch

If your free sample lists consistently prompt immediate, specific feedback from prospects ("these look exactly right" or "can you filter out companies under 50 employees?"), the targeting methodology and ICP capture process are working — volume of that specific, engaged feedback is a better early signal than conversion rate alone. Once 3+ clients are on monthly refresh retainers, that's the signal to invest in the automation layer (Python enrichment script + API integrations) to bring per-list time under 1 hour and make the economics meaningfully more favorable at scale.
