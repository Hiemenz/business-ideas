# PoC 37 — "Get Your Address Off the Internet" — Personal Data Broker Opt-Out & Privacy Cleanup Service

**Date:** 2026-07-14
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Dozens of data broker/people-search sites (Spokeo, Whitepages, BeenVerified, and many more) publicly list individuals' home addresses, phone numbers, relatives, and background information, scraped and aggregated from public records — and most people have no idea how exposed they are until they search their own name, or until a specific trigger event makes it suddenly urgent (a stalking/harassment concern, a divorce, starting a public-facing job, a doxxing incident, or simply a privacy-conscious person discovering the problem). Each site has its own opt-out process — usually free but genuinely tedious, requiring a separate manual request per site, sometimes with identity verification steps, and data frequently reappears months later as sites re-scrape source records. This is a well-validated market (paid consumer services like DeleteMe already prove people pay $100+/yr for exactly this), but a lean, near-$0 version of the same service is entirely buildable using nothing but the same free opt-out processes those paid services rely on.

## Who It's For

Individuals with an elevated privacy concern: people going through a divorce or leaving an abusive relationship (highest urgency, most reachable through relevant support organizations), public-facing professionals (real estate agents, healthcare providers, teachers, executives) whose home address exposure creates real personal risk, and generally privacy-conscious consumers who've simply never gotten around to doing the tedious opt-out work themselves.

## How It Makes Money

- Flat one-time cleanup fee: $80–$200 to search and submit opt-out requests across the 15-20 most prominent data broker sites for a given individual.
- Ongoing monitoring/re-removal subscription: $8–$15/mo (mirroring the pricing structure of established paid competitors like DeleteMe) to periodically re-check and re-submit opt-outs as data reappears — the natural, well-precedented recurring revenue model for this category, since removal is not permanent without ongoing maintenance.
- Family/household package: a bundled rate to cover a full household (spouse, and where relevant, information about children that appears in family-member listings) — a common and higher-ticket real-world need.
- Rush/priority tier for people in an active safety-concern situation who need requests submitted immediately rather than as part of standard batch processing.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Search the client's name (with permission and only the information needed) across the most prominent data broker/people-search sites to identify where they're listed.
   - Manually submit each site's specific, established opt-out process (most are free and don't require any paid tooling — just following each site's documented removal procedure, which varies site to site but is consistently accomplishable).
   - Track submission status per site (some confirm immediately, others take days to weeks to actually remove the listing) and follow up on any that don't process within the site's stated timeframe.
   - Deliver a completion report: which sites were found, which were successfully removed, and which require ongoing monitoring since they're known to be more persistent/re-scrape more frequently.
2. **Software layer (build once 2–3 clients are live, funded by early cleanup fees):**
   - Reusable checklist/playbook of the top 15-20 data broker sites with their specific opt-out process documented (URL, required steps, typical processing time) — this is the core reusable asset of the entire service, built once and reused across every client, directly reducing per-client time investment as your playbook matures.
   - Simple tracking system (Airtable/Google Sheets) logging per-client, per-site submission and completion status, essential for managing the ongoing monitoring/re-submission subscription tier at any real client volume.
   - Scheduled re-check reminders (consistent with this repo's cron-driven pattern) prompting periodic re-verification for subscription clients, so re-appeared listings get caught and re-submitted without relying on manual memory.

## Tools/Stack

- No paid tooling required — every data broker site's opt-out process is free to use directly; the service is entirely about doing the tedious, time-consuming work on the client's behalf.
- Airtable/Google Sheets (free tier) for per-client, per-site tracking.
- Simple scheduled reminder script for the ongoing monitoring tier.
- Stripe for one-time and recurring subscription billing.

## Go-to-Person Outreach — First 5 Customers, Zero Ad Spend

1. Identify prospects via a genuinely helpful, low-pressure free-sample approach: offer to search someone's name across a few major data broker sites and simply report back what's publicly listed about them — most people are surprised (often uncomfortably so) by what turns up, making this an unusually persuasive, personally-relevant demonstration.
2. Domestic violence/safety advocacy organizations, and communities supporting people going through separation/divorce, are a high-urgency, high-relevance venue — reach out to offer this as pro-bono or discounted support for people in an active safety situation, which is both genuinely valuable to a vulnerable population and a strong source of word-of-mouth referral within those support networks.
3. Public-facing professional communities (real estate agent associations, healthcare worker groups) are a strong fit given the direct, tangible personal-safety stakes of home address exposure in those professions.
4. Privacy-conscious online communities (there are active communities specifically focused on digital privacy/opsec) are a natural, highly receptive venue where this exact pain point is a constant topic of discussion.
5. A simple, honest "here's what's publicly listed about you right now" free check, sent directly to a specific individual, is one of the most personally compelling free-sample hooks possible, since the finding is about them specifically, not an abstract example.

## Time to First Dollar

- Day 1–3: build the initial 15-20 site opt-out playbook (a one-time research investment that pays off across every future client), identify 10-15 individuals in relevant communities/networks for free sample checks.
- Day 3–5: run free sample searches and share findings directly with prospects.
- Day 5–10: close 2–3 clients on the flat cleanup fee, collected upfront, with the ongoing monitoring subscription offered immediately upon completion.
- **First dollar within 1–2 weeks** — no build dependency beyond the initial playbook research, and manual opt-out submission work can begin the same day a client is closed.

## Why This, Why Now

- Zero cost required to start — every underlying opt-out process is free; the entire service value is your time and organized persistence doing tedious work most people won't do themselves.
- Well-validated market with clear, established paid competitors (DeleteMe and similar) proving real willingness to pay for exactly this, meaning no need to convince anyone the business model works — only to compete on price, personal touch, or a specific underserved niche (safety-situation urgency, for example).
- Genuinely high-stakes, personally resonant value proposition for the right audience (safety-concern individuals, public-facing professionals) creates strong urgency and word-of-mouth potential within tight-knit relevant communities.
- Natural recurring-revenue structure that's honestly justified (data does reappear over time as sites re-scrape), not a manufactured retainer hook.

## Risks / Open Questions

- **Identity verification and access boundaries:** performing this work on someone else's behalf may occasionally require information or verification steps that are more naturally done by the individual themselves — be clear about what you can do on a client's behalf versus what requires their direct action, and never request more personal information than is genuinely necessary to complete the opt-out process.
- **No removal is fully permanent:** data broker sites re-scrape source records periodically, meaning even a completed cleanup isn't a one-time fix — set this expectation clearly upfront so clients understand why the monitoring subscription has real, ongoing value rather than feeling like an unnecessary add-on.
- **Emotionally sensitive client situations:** working with people in active safety concerns (domestic violence, stalking situations) requires real care and discretion — treat this population's engagements with particular seriousness and confidentiality, and be honest about the limits of what this service can guarantee in a genuinely dangerous situation (this is a data-privacy service, not a substitute for law enforcement or a safety plan in an acute crisis).
- **Opt-out process changes over time:** individual sites periodically change their removal procedures — the playbook requires periodic verification/maintenance to stay accurate, which is itself part of what justifies charging for a service built on ostensibly "free" underlying processes.

## Validation Signal to Watch

If your free sample searches consistently surface genuinely surprising, uncomfortable findings for the people you check (a strong signal the underlying problem is real and personally resonant), and 2+ of your first 8-10 free-sample recipients convert to a paid cleanup, the service and outreach approach are validated — scale outreach into the highest-urgency channels (safety-concern-adjacent communities, public-facing professional groups) first, since those carry both the strongest willingness to pay and the most meaningful real-world impact.
