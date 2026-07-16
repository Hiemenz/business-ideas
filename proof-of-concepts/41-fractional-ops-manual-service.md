# PoC 41 — "If You Got Hit by a Bus, Would Your Business Survive?" — Fractional Operations Manual Service for Solo Founders

**Date:** 2026-07-15
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Solo founders and tiny teams (1-5 people) running revenue-generating businesses are deeply operationally fragile: every critical process — how they fulfill orders, how they onboard clients, how they handle refunds, how they run payroll, how they renew key subscriptions, what their login credentials are and where they're stored — lives entirely in the founder's head. This is functionally fine until it isn't: a health emergency, a vacation, a desire to hire a VA or part-time helper, or simply wanting to sell the business someday all suddenly require that implicit knowledge to exist somewhere external. Building a complete operations manual from scratch is a multi-week project most founders perpetually defer because there's always something more urgent. This is distinct from PoC 31 (which documents operational SOPs for existing processes in established small businesses) — this is specifically targeted at the solo founder who needs a ground-up "if I disappeared, could someone else run this?" survival document, a more personal and urgency-laden framing with a different trigger and emotional hook.

## Who It's For

Solo founders and micro-business owners running businesses that have real revenue but zero documentation — best entry points: founders actively hiring a VA or assistant for the first time (the moment the knowledge-transfer problem becomes immediately, practically urgent), founders who've tried to take a vacation and couldn't actually disconnect, or founders who've said publicly they want to sell or step back from day-to-day operations within the next 12-24 months (a business with no operations manual has a meaningfully lower acquisition valuation than one with solid documentation).

## How It Makes Money

- Flat operations manual build fee: $600–$1,500 for a complete, founder-specific operations manual covering: all recurring processes (daily/weekly/monthly), all key tool logins and where credentials are managed, all vendor/supplier/contractor relationships with contact info, all critical renewal dates and subscriptions, client onboarding and offboarding steps, and the "break glass in emergency" section (who to call if something breaks and the founder can't be reached).
- VA onboarding add-on: $200–$400 to adapt the completed manual into a structured onboarding document specifically formatted for handing off to a new virtual assistant or part-time employee — a common immediate next step for founders who've just finished the manual.
- Quarterly refresh retainer: $150–$300/quarter for a 2-hour review session to update the manual as the business evolves — justified for any founder who's actively scaling, since a stale manual becomes worse than no manual if a VA acts on outdated instructions.
- Pre-sale documentation package: $800–$2,000 for founders actively preparing a business for acquisition, producing the full operations manual plus a structured business overview document (revenue model, customer breakdown, key dependencies) that meaningfully de-risks the buyer's due diligence process and often directly improves acquisition offers.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Intake interview (60-90 min): walk through the founder's typical Monday, all recurring tasks over a rolling month, all tools/accounts used, all vendors/contractors relied on, and the "if I was unreachable for 2 weeks, what would break first?" question — the last one reliably surfaces the highest-urgency undocumented processes.
   - Draft the manual in Google Docs using an LLM to structure and write clean documentation from your interview notes and any raw notes the founder shares — the same LLM-assisted structuring pattern used throughout this folder, applied to the structured output from a conversational intake rather than a form.
   - Deliver a reviewed, organized manual in a shared Google Doc, formatted into clearly navigable sections with a table of contents, explicit "owner if founder is unavailable" fields, and flagged gaps (processes the founder mentioned but couldn't fully articulate during the interview, earmarked for a follow-up session).
2. **Software layer (build once 2–3 clients are live):**
   - Reusable intake interview framework: a structured set of questions covering every category of business operations (tools, processes, relationships, subscriptions, financial accounts, emergency contacts) — built once and reused across every engagement, refined with each new client type (e-commerce solo founder vs. service business vs. digital product creator are meaningfully different but share 70% of the same checklist).
   - Template manual structure by business type (product, service, SaaS) that pre-populates the section headers and common process categories specific to that model, reducing per-engagement drafting time significantly.
   - Simple recurring-process discovery prompts for the LLM that reliably surface implicit, habitual tasks founders don't think to mention until asked directly ("do you do anything differently at the end of each month?" "what do you check every morning before opening your email?").

## Tools/Stack

- Google Docs for manual delivery and ongoing collaborative updates.
- Claude/Gemini API for structuring interview notes and drafting clean documentation sections.
- Loom (free tier) as an optional but high-value supplement — a short founder screen-recording walkthrough of a tool or process is often faster than a text description and can be embedded or linked in the manual.
- Google Meet/Zoom for the intake interview.
- Stripe/invoice for fee collection.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify prospects in solo founder and micro-business communities (Indie Hackers, r/Entrepreneur, Twitter/X founder circles, solo operator newsletters) where operational fragility is a recurring, openly discussed anxiety — "I can't take a real vacation" and "I want to hire help but don't know where to start" are extremely common themes.
2. Free-sample hook: offer a free 20-minute "ops fragility check" — a quick structured conversation using 5-6 intake questions to identify the single biggest documentation gap in their current business, then share the specific finding: "Based on what you told me, your biggest fragility is [specific process] — if you couldn't work for 2 weeks, that's the first thing that would break." A personally relevant, specific finding that no generic content can replicate.
3. Warm referrals from the VA/virtual assistant hiring ecosystem: VA agencies and freelance VA communities regularly encounter founders struggling with exactly this problem (they can't onboard the VA because nothing is documented), making them natural referral partners who immediately understand the value proposition.
4. Business brokers who help solo founders sell their businesses are an unusually high-intent referral channel — they routinely encounter founders whose acquisition process stalls because buyers find zero documentation, and they have a clear, direct financial incentive to refer the founder to a documentation service that can unblock the deal.
5. A single "founder built the manual in a week, handed off to a VA, and took a 10-day vacation for the first time in 4 years" story (anonymous) lands extremely well in founder communities because it addresses a very real, very felt aspiration.

## Time to First Dollar

- Day 1–2: build the intake interview framework (50-60 structured questions across 8-10 process categories) and draft the template manual structure for the most common solo founder business type (service business is the largest and most reachable population).
- Day 2–4: identify 15-20 prospects in founder communities displaying visible operational-fragility signals (vacation anxiety, VA hiring intent, acquisition interest), prepare a personalized free ops-fragility check opening for each.
- Day 4–7: send outreach with the free check offer.
- Day 7–12: close 2–3 founders on the flat operations manual fee ($600–$1,500), collected as a deposit-on-signing structure (50% upfront, 50% on delivery); schedule the intake interview and complete the first manual within 3-5 days of the interview.
- **First dollar within 1–2 weeks** — no build dependency beyond the interview framework, which is a half-day of structured writing work.

## Why This, Why Now

- Emotionally resonant, personally specific trigger framing ("if you disappeared tomorrow, would your business survive?") that cuts through founder noise more effectively than generic productivity or efficiency pitches — it addresses a real anxiety most solo founders quietly carry.
- Natural, high-value referral channels (VA agencies, business brokers) that are motivated to refer because the documentation problem directly blocks their own work, not just the founder's comfort.
- Pre-sale documentation tier is particularly high-leverage: founders preparing to sell are extremely motivated, typically have the most cash, and the manual directly affects the acquisition outcome — making the ROI case unusually concrete and easy to make.
- Reusable intake framework compounds across business types: each new solo founder engagement refines the question set and surfaces new common patterns, making each subsequent engagement faster to execute.

## Risks / Open Questions

- **Founders are often protective of the operational details they share:** the intake interview requires genuine trust-building, since founders may be reluctant to share login structures, financial account details, or vendor relationships with someone they've just met — go slowly, be explicit about how you handle sensitive information (you're structuring it, not storing or accessing it), and never request credentials yourself; the document is for the founder's secure storage, not yours.
- **Scope can balloon without clear boundaries:** a thorough operations manual for a complex business could easily become a 6-month engagement — define scope explicitly upfront by business type (e.g., "this covers your top 10 recurring processes and all critical tool/vendor relationships, not every edge case"), and price additional depth separately.
- **Manual quality depends heavily on founder participation:** the intake interview only surfaces what the founder remembers to mention, and gaps are common — the follow-up session for flagged gaps is important to include in the delivery structure rather than treating the first draft as complete.
- **Maintenance is the real ongoing challenge:** a manual that isn't updated as the business evolves quickly becomes a liability rather than an asset; the quarterly refresh retainer is genuinely important to pitch as part of the initial sale, not as an afterthought.

## Validation Signal to Watch

If the free ops-fragility check consistently generates strong reactions from founders ("I've been meaning to do this for two years" is the most common response pattern this service should produce), and 2+ of your first 8-10 free check conversations convert to a paid manual build, the framing and hook are validated. Track time-per-engagement carefully across the first 5 clients — if the intake interview plus LLM-assisted drafting plus review cycle takes more than 8-10 hours total, identify which step is taking longest and build a more structured template or prompt to compress it, since per-hour economics need to stay favorable relative to the flat fee.
