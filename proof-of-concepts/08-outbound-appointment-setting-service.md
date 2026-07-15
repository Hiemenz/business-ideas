# PoC 08 — "Book Meetings While You Build" — Outbound Appointment-Setting-as-a-Service for B2B Founders/Agencies

**Date:** 2026-07-08
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Early-stage B2B SaaS founders, agency owners, and consultants know they need consistent outbound to fill their sales pipeline, but they're either heads-down building/delivering and never get to it, or they try it themselves with generic mass-blasted emails that get ignored or land in spam. Meanwhile, dedicated outbound/SDR agencies exist but typically require $2k–$5k/mo retainers and 3-month contracts — priced for funded startups, not bootstrapped founders. This is a lean, personalized-at-scale version of that same service: you research prospects, write genuinely personalized outreach (not templated spam), and hand the founder a calendar full of qualified meetings — paid per meeting booked, which is an extremely easy yes for any founder who knows what a closed deal is worth.

## Who It's For

Bootstrapped/early-stage B2B SaaS founders, boutique agency owners, and consultants who have a validated offer and know their ideal customer profile but lack the time or team to run outbound themselves. Best entry point: founders actively posting about needing more pipeline/leads (a direct, visible signal of the exact pain you solve), or agencies you can see are understaffed on sales (small team, no dedicated BD person).

## How It Makes Money

- Pay-per-qualified-meeting: $75–$200 per booked call that meets the client's stated criteria (right title, right company size, genuine interest) — zero risk to the client, since they only pay for outcomes.
- Small monthly platform/tooling fee ($150–$300/mo) to cover email infrastructure and list-building time, credited against per-meeting fees — covers your fixed costs without relying entirely on variable outcomes.
- Retainer upgrade once volume is proven: $1,500–$3,000/mo flat for a guaranteed minimum meeting volume, once you have a repeatable process and want predictable income over pure pay-per-result.
- Natural upsell: once meetings are booked, offer to also draft the follow-up sequence/proposal templates that turn meetings into closed deals — extends your value past the top of the funnel.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Onboarding call: extract the client's ideal customer profile (industry, company size, title, pain point their product solves) and their unique value proposition/proof points.
   - Manually build a prospect list (50–100 names) using free tools: LinkedIn Sales Navigator free trial, company websites, Apollo.io free tier (limited but usable credits), or manually browsing LinkedIn search + company "About" pages for verifiable emails.
   - Write genuinely personalized first-line openers per prospect (referencing something specific — a recent post, a company milestone, a shared connection) using an LLM prompted with scraped context, then send via your own or the client's email (starting with low daily volume to protect deliverability, e.g., 20–30/day).
   - Manually track replies, qualify interest, and book meetings directly onto the client's calendar (Calendly link).
2. **Software layer (build once 1–2 clients are live, funded by early per-meeting fees):**
   - Simple scraper/enrichment script (reuse this repo's existing scraping patterns from `trends.py`) to pull prospect company info and recent public activity (LinkedIn posts, press mentions) that feeds the LLM personalization prompt — turns manual research into a repeatable pipeline.
   - Sequence tracker (Airtable/Google Sheets) logging send status, replies, qualification outcome, and meeting-booked status per prospect — same lightweight tracking pattern as PoC 02's case tracker.
   - Reply-classification pass using an LLM to flag "interested," "not now," and "not interested" responses automatically, so you spend your time only on genuinely warm replies instead of manually triaging every inbox response.

## Tools/Stack

- LinkedIn (manual research + free Sales Navigator trial), Apollo.io free tier, or company websites for prospect data — no paid data tool required to start.
- Claude/Gemini API for personalized opener generation and reply classification.
- Gmail/Google Workspace alias (or the client's own domain, once trust is established) for sending — low volume per day protects deliverability without needing paid cold-email infrastructure at first.
- Calendly (free tier) for meeting booking.
- Airtable/Google Sheets (free tier) for pipeline tracking.

## Go-to-Market — First 3-5 Customers, Zero Ad Spend

1. Identify founders/agency owners in your network or on LinkedIn/Twitter who are visibly posting about needing more leads, slow sales, or "doing outbound myself and it's rough" — this is a direct, low-effort-to-find pain signal.
2. Free-sample hook: research and personally write 3 real, ready-to-send outreach messages for their actual ideal customer profile, and send them as a DM: "Here's 3 messages I'd send on your behalf this week, free — if any land a reply, let's talk about doing this ongoing." This mirrors the free-sample pattern from PoC 01/02/05/06, adapted to this offer.
3. Position the pay-per-meeting pricing explicitly as the differentiator versus traditional SDR agencies — "no retainer, no contract, you only pay when a real meeting lands on your calendar" removes essentially all of the buyer's risk and objection surface.
4. Founder communities (Indie Hackers, small SaaS Slack/Discord groups, local startup meetups) are a strong low-cost venue since the exact buyer persona congregates there and openly discusses pipeline struggles.
5. Once you've booked meetings for a first client, ask them to share the result (even anonymized: "booked 8 qualified meetings in 3 weeks for a client") in relevant founder communities — social proof in this niche travels fast because founders talk to each other about what's working.

## Time to First Dollar

- Day 1–3: identify 10–15 target founders/agencies showing visible pipeline pain, build ICP-matched prospect lists (30–50 names) for the top 5.
- Day 3–5: draft and send 3 free sample outreach messages per prospect as the opener DM.
- Day 5–10: close 2–3 clients on the pay-per-meeting model, begin sending personalized outreach on their behalf.
- Day 10–18: first qualified meetings booked and invoiced — **first dollar within 2-3 weeks**, slightly slower than the audit/research-based ideas in this folder since outbound requires replies to convert to meetings, but each meeting is a clean, easily justified invoice.

## Why This, Why Now

- Zero paid tooling required to start — free-tier tools plus manual research cover the entire MVP, with software automation purely a speed/scale upgrade layered in once revenue is flowing.
- Pay-per-meeting pricing is close to the lowest-friction sales pitch of any idea in this folder, since it structurally cannot fail to deliver value the client didn't ask to pay for.
- Deep alignment with sales/marketing/ops skill set specifically (prospecting, personalization, qualification) while software skill compounds it into a scalable pipeline rather than a manual grind.
- Every B2B founder/agency owner has the exact same underlying problem (not enough pipeline) and the exact same budget objection (can't afford a $3k/mo agency) — this offer is purpose-built for that gap.

## Risks / Open Questions

- **Deliverability risk:** sending cold email at volume without proper domain warm-up/authentication (SPF/DKIM/DMARC) can damage a client's email reputation — start at low daily volume and, once trust is established, recommend the client set up a secondary sending domain rather than risking their primary domain's reputation.
- **Qualification disputes:** "qualified meeting" needs a crystal-clear, agreed-upon definition upfront (title, company size, expressed interest) to avoid disputes over what's payable — put this in writing before starting.
- **Time-intensive at first:** manual research and personalization don't scale past 2–3 clients simultaneously without the software layer — cap client count early and reinvest first revenue into the scraping/enrichment automation before taking on more.
- **Reply-rate variance by ICP:** some industries/titles respond far better to cold outreach than others — if a client's ICP has structurally low response rates (e.g., very senior enterprise buyers), pay-per-meeting economics may not work for you; qualify this in the onboarding call before agreeing to pricing.

## Validation Signal to Watch

If your first 3 free-sample outreach messages per prospect generate at least one genuine reply (positive or negative — a reply proves the personalization is landing, not going to spam), the approach is working and worth pitching as an ongoing service. If replies are near-zero across multiple free samples, the issue is likely email deliverability or list quality rather than message quality — diagnose before assuming the offer itself is weak.
