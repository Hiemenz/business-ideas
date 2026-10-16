# PoC 58 — "Your Job Post Has Been Up for 6 Weeks and the Applicants Are Wrong" — Job Description Optimization & Rewrite Service

**Date:** 2026-07-18
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Most job descriptions are written by hiring managers who have never thought of a job post as a marketing document — and it shows. The opening paragraph describes the company ("we're a fast-growing startup disrupting X"), not the role or the candidate's opportunity. The requirements list has 12 items where 4 are real and 8 are aspirational filters that actively screen out qualified candidates (including, consistently, women and underrepresented groups who research shows apply only when they meet nearly all listed requirements). The responsibilities section lists activities rather than outcomes. The compensation is hidden or absent. And the whole thing reads like a legal document rather than a genuine pitch to a talented person who has options. The result is either a flood of poorly matched applicants who technically hit the keyword filters, or a dry pipeline of exactly the type of strong candidate the company claims to want. Every one of these problems is fixable with a rewrite that applies basic marketing-copy thinking — lead with the candidate's opportunity, be specific about what success looks like, trim the requirements to the genuine must-haves, include compensation, and end with a clear picture of what the first 90 days actually look like. This is a genuine services gap: companies spend $5K–$25K on recruiter fees to fill roles but zero on the document that determines who applies in the first place.

## Who It's For

Startups and small companies (10-150 employees) actively hiring for technical or professional roles — best entry points: companies with job posts that have been live for 4+ weeks without quality applicants (a visible, public signal of the problem), companies about to open a high-stakes hire (first engineer, first sales hire, first marketing lead) where getting the wrong person is costly, or HR leaders at growing startups who are managing 5+ open roles simultaneously and know their JDs are weak but don't have time to fix them.

## How It Makes Money

- Per-JD rewrite: $150–$300 per job description — intake (the existing JD + a 20-min conversation about the real requirements and what a great hire looks like), full rewrite, and delivery within 48 hours. Fast, bounded, immediately usable.
- Hiring sprint package: $500–$900 for a 5-JD batch rewrite — the most common real need for a growing startup opening multiple roles simultaneously; priced at a per-JD discount to reflect the efficiency of doing them together and the compounding value of consistent voice and framing across the company's entire open-role presence.
- Job post audit: $100–$200 for a written critique of an existing JD with specific, prioritized recommendations — for companies that want to DIY the rewrite but need a structured diagnosis of what's wrong first.
- Hiring page & employer brand add-on: $300–$500 to rewrite the company's careers page copy (the "why work here" section, benefits framing, team description) that every candidate reads before applying — the upstream conversion page that determines whether a strong candidate even bothers reading the individual JDs.
- Ongoing hiring retainer: $300–$500/mo for companies with continuous hiring needs — a new JD written within 48 hours of a role opening, with a consistent voice and framework across the entire open-role library.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Intake per role (20 min): gather what the existing JD says, what the hiring manager actually cares about (the 3-4 non-negotiable requirements vs. the full list), what a great hire looks like in their first 90 days, what the compensation range is (even if the client doesn't want to post it publicly — needed to calibrate expectations framing), and what makes this role genuinely interesting or different for a strong candidate who has options.
   - Rewrite using a structured framework: (1) Role headline that says what the job actually is in plain language; (2) 2-sentence "why this role matters" that frames the candidate's impact; (3) What you'll do — 4-6 outcome-oriented responsibilities rather than activity lists; (4) What we're looking for — 4-5 genuine must-haves only, with "nice to have" items explicitly labeled as such; (5) Compensation range (or honest explanation of why it's not listed); (6) What the first 90 days look like — one of the highest-conversion additions to any JD, because it signals the company has actually thought about onboarding; (7) How to apply — a specific, human next step.
   - Use an LLM to produce a first draft from the intake notes and the framework, then edit for the company's specific voice, the role's technical specifics, and genuine differentiation from the generic — the LLM handles structural drafting; the editing pass handles authenticity.
   - Deliver as a Google Doc ready to paste into Lever, Greenhouse, Workable, LinkedIn Jobs, or whatever ATS the company uses.
2. **Software layer (build once 2–3 clients are live):**
   - Reusable intake framework: 12 structured questions covering every variable needed for a strong rewrite (real requirements vs. wish list, success definition, compensation, team context, role-specific interesting problem) — built once and used as the standard intake for every engagement, ensuring the rewrite is informed by the information that actually matters rather than just the existing bad JD.
   - JD template library by role type (engineer, sales, marketing, product, operations, customer success) — the structure is consistent but the language conventions, typical requirements framing, and "what makes this interesting" hooks differ meaningfully by function; role-type templates make each new rewrite faster while staying relevant.
   - LLM prompt chain per section: one prompt for the "why this role matters" paragraph (given the company context and role impact, write a 2-sentence opening that speaks to a strong candidate who has options), one for the responsibilities section (given these activities, rewrite them as 5 outcome-oriented bullet points), one for the requirements trim (given this 12-item list, identify the 4-5 genuine must-haves) — each producing a first draft that requires editing but not writing from scratch.

## Tools/Stack

- Google Docs for delivery (paste-ready for any ATS).
- Claude/Gemini API for structured JD drafting from intake notes.
- Textio's free tier or Gender Decoder (free tool) to check for biased language patterns in the rewrite — a quick quality check that adds credibility and genuine value to the deliverable.
- Calendly free tier for intake call scheduling.
- LinkedIn Jobs (free to browse) for competitive benchmarking of how similar roles are positioned in the same market.
- Stripe/invoice for fee collection.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify prospects by browsing active job posts directly — LinkedIn Jobs, Indeed, and company careers pages are public and fully searchable; any job post that's been live for 4+ weeks without being taken down is a visible, real-time signal of a struggling hire, and the specific problems (boilerplate opening, inflated requirements, no compensation) are diagnosable in 3 minutes from the public post.
2. Free-sample hook: rewrite the opening paragraph of a prospect's current job post and send it unprompted: "Found your [Role] post on LinkedIn — rewrote the opening paragraph to lead with the candidate opportunity rather than the company description. Happy to rewrite the full JD if this direction looks right." A concrete, specific, immediately comparable before/after that requires 15 minutes and demonstrates the entire value proposition in a single artifact.
3. HR and people operations communities (People Ops Slack groups, r/humanresources, HR-focused LinkedIn communities) are strong venues — HR leaders who manage multiple open roles simultaneously are constant, high-volume consumers of this type of service and make faster purchasing decisions than founders who have to be educated on the problem first.
4. Recruiting agencies and fractional HR consultants are natural referral partners — they work with companies whose JDs are weak and have a direct financial incentive to refer a JD rewrite service that speeds up their client's time-to-fill.
5. A documented "JD was live for 8 weeks with 120 applicants, none advancing past screening — rewrote the JD, role filled in 11 days with 40 applicants, 8 advancing to interviews" result expressed in those specific metrics is immediately compelling to any hiring manager who's experiencing the same pattern.

## Time to First Dollar

- Day 1: build the intake framework and JD template library for the 5 most common role types (engineer, sales, marketing, product, ops); run the LLM prompt chain on 3-4 sample bad JDs to calibrate the rewrite quality and time per role.
- Day 2–3: identify 15-20 companies with job posts that have been live for 4+ weeks (a simple LinkedIn Jobs search filtered by date posted surfaces these immediately); rewrite the opening paragraph of each for the free-sample outreach.
- Day 3–6: send the free opening paragraph rewrite with the full JD offer.
- Day 6–12: close 3-5 companies (a higher volume of smaller transactions than most services in this folder — JD rewrites are easy to approve quickly at $150–$300); deliver each within 48 hours of the intake call.
- **First dollar within 1 week** — the prospecting trigger (a public job post that's been live too long) is visible and instantly actionable, the free sample takes 15 minutes per prospect, and per-JD prices are low enough to close without procurement cycles.

## Why This, Why Now

- Job posts are uniquely public and self-diagnosing: unlike most services in this folder where the problem is hidden inside the company, a bad job description is sitting on LinkedIn right now with a "posted 6 weeks ago" timestamp — the problem is visible, dated, and verifiable in 3 minutes without any conversation.
- The lowest friction purchase in the folder at the per-JD price: $150–$300 is below almost every approval threshold, closeable in a single email exchange, and clearly worth it to anyone experiencing a 6-week empty pipeline.
- Hiring urgency creates genuine time pressure: a role that's been open for months while the team is understaffed has a real, felt cost — every week the role is unfilled is a week of lost productivity, and the hiring manager knows it.
- Volume path is clear and fast: a startup with 5 open roles is a $750–$1,500 engagement, and a startup growing through a hiring sprint might open 10-15 roles in a quarter — making the path from first JD to meaningful monthly revenue unusually short compared to most services in this folder.

## Risks / Open Questions

- **JD quality alone doesn't fix sourcing or interviewing problems:** a better job description improves applicant quality and volume but can't compensate for a broken sourcing strategy (posting only on one job board) or a slow interview process that loses candidates to faster-moving competitors — be clear about what the rewrite addresses and what it doesn't.
- **Compensation transparency resistance:** many companies genuinely don't want to post salary ranges (for internal equity reasons, competitive reasons, or founder discomfort) — don't make compensation inclusion a non-negotiable gatekeeping condition, but be prepared to explain clearly why hiding it suppresses application volume from the candidates most likely to be worth hiring.
- **Role clarity is the client's responsibility:** a hiring manager who isn't clear on what they actually need (a common problem, especially for early hires into undefined roles) produces an intake conversation that can't generate a strong JD regardless of writing quality — when this happens, the right move is to push back gently on role clarity before drafting, not to write a polished JD for an undefined role.
- **ATS formatting constraints vary:** some applicant tracking systems strip formatting (bullet points, bold, headers) or have character limits that require adaptation — confirm the target platform before final delivery so the JD lands correctly in whatever system the company is using.

## Validation Signal to Watch

If the free opening-paragraph rewrites consistently generate "this is much better than ours" reactions followed by "can you do the whole thing?" — particularly from HR leaders managing multiple open roles simultaneously — the quality bar is landing and the volume path is real. The clearest product-market fit signal: a hiring manager who filled a previously stalled role within 2 weeks of the JD rewrite and attributes the quality improvement to the new post — that specific, attributable result is the foundation of every case study and referral conversation this service generates.
