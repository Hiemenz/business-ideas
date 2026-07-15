# PoC 09 — "Get Past the ATS, Get the Interview" — Resume/LinkedIn/Application Acceleration Service for Job Seekers

**Date:** 2026-07-08
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Laid-off and actively-searching professionals (especially in tech, where layoffs have been frequent and public) are applying to dozens or hundreds of jobs and getting almost no responses — not because they're unqualified, but because most resumes fail to pass Applicant Tracking System (ATS) keyword filters, and LinkedIn profiles/cover letters are generic rather than tailored per role. This is a well-established service category (resume writers, career coaches) but most existing options are either expensive career coaches ($150–$300/hr) or cheap-but-generic resume mills. The gap is a fast, technically rigorous, per-application-tailored service at a mid-market price — and it's a market that's currently large and actively searching, with urgency baked in (people need a job now, not eventually).

## Who It's For

Actively job-searching professionals, especially those laid off in the last 1–6 months (highest urgency, most receptive to paid help), concentrated in tech, product, marketing, and finance roles where ATS filtering is heaviest and LinkedIn-based recruiting is most common. Best entry point: people visibly posting "open to work" on LinkedIn or in layoff-support communities — a direct, self-identified signal of both need and urgency.

## How It Makes Money

- Flat package fees, tiered by scope:
  - **ATS Resume Rebuild** — $150–$250 for a single rewritten, keyword-optimized resume.
  - **Full Package** — $350–$600 for resume + LinkedIn profile rewrite + a reusable cover letter template + one round of revisions.
  - **Ongoing tailoring retainer** — $99–$199/mo for continued per-application resume/cover-letter tailoring during an active search (highest-margin, most recurring option).
- Upsell: mock interview coaching session ($75–$150/session) once resume/profile work is delivered and the client starts landing interviews.
- Referral incentive: offer a discount to clients who refer another job seeker — job seekers talk to each other constantly (support groups, laid-off cohorts), so referral velocity in this niche is unusually high.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Intake call/form: current resume, target roles, 2-3 real job postings they're applying to.
   - Run their existing resume through a free ATS-compatibility checker (Jobscan free tier, or a manual keyword-gap comparison against the job posting) to identify specific missing keywords and formatting issues (tables, graphics, non-standard headers that ATS parsers choke on).
   - Rewrite the resume manually with LLM assistance: feed the job posting + their real experience into an LLM to draft achievement-oriented, keyword-aligned bullet points, then edit for accuracy and voice — never fabricate experience, only reframe and surface what's real.
   - Deliver via Google Doc with tracked changes/comments so the client sees exactly what changed and why.
2. **Software layer (build once 2–3 clients are live, funded by early package fees):**
   - Reusable prompt template per role-family (e.g., "PM resume bullet rewrite," "software engineer resume bullet rewrite") so tailoring a new resume to a new job posting takes minutes, not a from-scratch rewrite each time — same reusable-template philosophy as `onepager.py`.
   - Simple keyword-extraction script that pulls the top recurring skills/requirements from a job posting (basic text frequency analysis, no ML needed) to feed directly into the LLM prompt and flag gaps against the client's current resume automatically.
   - Client profile store (skills, achievements, quantified results bank) so the ongoing tailoring retainer clients get fast turnaround — you're remixing a maintained fact bank per application, not rewriting from scratch each time.

## Tools/Stack

- Jobscan free tier or manual keyword-gap analysis for ATS compatibility checking.
- Claude/Gemini API for bullet-point drafting, cover letter generation, and LinkedIn "About" section rewrites.
- Google Docs (free) for collaborative editing/delivery.
- LinkedIn itself for finding prospects and for reviewing/rewriting client profiles directly.
- Stripe/PayPal for package fee collection.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Search LinkedIn for recent "open to work" banner posts, layoff-announcement posts, and posts in your network expressing job-search frustration — these are self-identifying, high-intent prospects you can find for free in under an hour.
2. Free-sample hook: offer to rewrite one resume bullet point or the LinkedIn headline for free, unsolicited, showing the before/after — a small, concrete demonstration of skill that's low-effort for you and highly persuasive for someone actively frustrated with no responses. Same free-sample pattern used across every prior PoC in this folder.
3. Layoff-specific communities (company-specific laid-off alumni Slack/Discord groups, "laid off from [Company]" LinkedIn groups, r/layoffs-adjacent communities) are dense, high-intent audiences where a helpful free tip post can generate multiple inbound leads at once.
4. Local career fairs, university alumni job-search groups, and outplacement-adjacent communities (some laid-off employees get outplacement stipends they haven't spent) are additional zero-cost channels.
5. Once a client lands an interview or offer, ask for a testimonial and referral immediately — the emotional high of landing an interview after a long dry spell makes this the easiest moment to ask, and job seekers are unusually willing to share what worked with their peers.

## Time to First Dollar

- Day 1–2: identify 15–20 "open to work" / layoff-signal prospects, prepare one free-sample rewrite for the first 10.
- Day 2–4: send outreach with the free sample attached.
- Day 4–8: close 3–5 clients on the Full Package tier ($350–$600), collected upfront via Stripe/PayPal.
- **First dollar within 1–2 weeks** — no build dependency, entirely research/writing skill plus free ATS tooling.

## Why This, Why Now

- Large, currently active, highly motivated buyer pool — unlike B2B service pitches that require convincing someone a problem exists, job seekers already feel the pain acutely and are actively looking for help.
- Zero cost to start, fastest-possible sales cycle of any idea in this folder in terms of urgency (a job seeker with bills due doesn't take weeks to decide), even though average deal size is smaller than the B2B-focused ideas.
- Direct, visible before/after proof (rewritten resume, ATS score improvement) makes the free-sample hook unusually persuasive compared to services with less tangible immediate output.
- Strong organic referral dynamics — job seekers are embedded in support communities that actively share "what worked," creating word-of-mouth growth without ad spend.

## Risks / Open Questions

- **Lower average deal size** than most other ideas in this folder — needs higher client volume to hit the same revenue target, meaning outreach volume/conversion efficiency matters more here than in higher-ticket B2B services.
- **Emotionally sensitive buyer state:** job seekers are often stressed/vulnerable — outreach and service delivery need a genuinely helpful, non-salesy tone; a pushy pitch in this niche risks real reputational damage given how tight-knit these communities are.
- **Outcome expectations must be managed carefully:** you can improve interview odds through better ATS pass-through and positioning, but you cannot guarantee interviews or offers — be explicit about this in all marketing to avoid overpromising.
- **Crowded low end of the market:** cheap/automated resume-builder tools and templates are widely available for free or near-free — differentiation must come from the human judgment in tailoring and the ATS-specific technical rigor, not from "a resume" as a generic deliverable.

## Validation Signal to Watch

If 3+ of your first 10 free-sample rewrites generate a reply expressing genuine surprise at the improvement, the skill-fit and hook are proven — scale outreach into the layoff-community channels next. If interview-callback rates for early clients don't visibly improve within 2-3 weeks of using the new materials, revisit whether the ATS keyword-matching approach is actually the binding constraint for that client's specific role/industry, or whether the issue lies elsewhere in their search (network, targeting, application volume).
