# PoC 19 — "200 Applicants, 10 Worth Your Time" — Applicant Screening Triage Service for High-Volume Hiring

**Date:** 2026-07-10
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

A single job posting from a small or early-stage company can pull in 100-500+ applications within days, and the founder or hiring manager has no time to read them all carefully — so screening becomes a rushed skim, genuinely strong candidates get missed, and hiring drags on for weeks past when the role should've been filled. This is the inverse problem to PoC 16 (which sources candidates for hard-to-fill roles with too few good applicants); here the company has the opposite problem — too many applicants and no time to sort signal from noise. It's a highly structured, LLM-well-suited task: rank a large stack of resumes/applications against explicit role criteria and return a short, genuinely defensible shortlist, fast.

## Who It's For

Startups and small companies who just posted (or are about to post) an open role and are already visibly drowning in applicant volume — visible directly on job posting platforms (many show live applicant counts) or inferable from posting age plus company size/desirability (well-known or well-funded small companies attract disproportionate volume). Best entry point: roles that have been open 2+ weeks despite high applicant volume — a direct signal that screening bandwidth, not candidate supply, is the bottleneck.

## How It Makes Money

- Flat fee per role screened: $250–$600 to screen a full applicant pool (regardless of size, up to a reasonable cap) and deliver a ranked shortlist of the top 10-15 candidates with a one-line rationale per candidate.
- Rush fee upsell: +$100–$150 for 24-hour turnaround on an already-open, urgent role.
- Ongoing screening retainer for companies hiring multiple roles in a growth period: $500–$1,500/mo covering screening across 2-4 simultaneously open roles.
- Natural upsell into PoC 16 (candidate sourcing) for any role where the screening process reveals the applicant pool is genuinely thin on qualified candidates, not just poorly triaged — same buyer, complementary and opposite-direction problem, single outreach motion covers both.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Intake call: extract exact must-have vs. nice-to-have criteria for the role (specific skills, years of experience, deal-breakers) — precision here is what makes the shortlist defensible rather than generic.
   - Client exports applicant data (most ATS tools and job boards support a CSV/resume export) or grants read access to the applicant pipeline.
   - Manually/LLM-assisted review each resume/application against the criteria, scoring and ranking, with particular attention to catching strong candidates whose resumes are poorly formatted or under-marketed (a common miss in rushed human skims) — this "catches what a rushed skim would miss" framing is a key differentiator, not just faster skimming.
   - Deliver a ranked shortlist with a one-line rationale per candidate explaining why they made the cut, so the founder can move straight to outreach/interviews with confidence.
2. **Software layer (build once 2–3 clients are live, funded by early screening fees):**
   - LLM-assisted resume parsing and scoring script that extracts structured data (years of experience, key skills, relevant keywords) from each resume and scores against the role's explicit criteria — the single highest-leverage automation, since this task is repetitive, well-structured, and directly reduces per-role turnaround time as volume grows.
   - Reusable scoring-rubric templates by role archetype (engineer, salesperson, ops/admin) so each new engagement starts from a refined framework rather than building criteria weighting from scratch — same reusable-scaffold pattern used throughout this folder.
   - Simple tracking sheet (Airtable/Google Sheets) logging applicant counts, shortlist size, and time-to-deliver per engagement — both for your own throughput management and as a "screened 340 applicants down to 12 in 48 hours" case-study stat.

## Tools/Stack

- Client's existing ATS or job board export (most platforms support CSV/resume export, no new tooling cost to access).
- Claude/Gemini API for resume parsing, scoring against role criteria, and rationale drafting.
- Airtable/Google Sheets (free tier) for tracking.
- Google Docs for shortlist delivery.
- Stripe/invoice for fee collection.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify prospects via job board applicant-count signals (many platforms display "100+ applicants" publicly) combined with posting age — a role open 2+ weeks with high visible applicant volume is a strong, directly observable target.
2. Free-sample hook: for a prospect's specific open role, pull a handful of publicly available applicant profiles (where visible, e.g., via LinkedIn's "people who've applied" signals or the job posting's own comment/interest activity) and flag one or two who look like strong, possibly-overlooked fits: "Noticed your [role] posting has 150+ applicants — spotted a couple of candidates in the public activity around it who look like strong fits and might be getting lost in the volume. Want a full screened shortlist?" This is a lower-effort, less complete version of the paid deliverable, similar in spirit to the free-sample tactics used throughout this folder.
3. Founder and hiring-manager communities (same venues as PoC 16 — Y Combinator networks, startup Slack/Discord groups) are a natural fit and allow you to pitch both PoC 16 and PoC 19 to the same audience depending on which pain point (too few vs. too many candidates) a given prospect is experiencing.
4. Position pricing explicitly against the alternative cost: "a week of a founder's time spent skimming resumes instead of building/selling" reframes the fee as a time-recovery purchase, not just a hiring expense.
5. A single "found the candidate they ended up hiring, buried on page 4 of their applicant list" story is a highly persuasive, concrete case study for this specific service.

## Time to First Dollar

- Day 1–3: identify 15-20 prospects with visibly high-applicant-volume open roles, prepare free-sample observations for the first 8-10.
- Day 3–5: send outreach with the free-sample finding as the opener.
- Day 5–10: close 2–3 clients on the flat screening fee ($250–$600), collected upfront, with rush-fee upsell offered at close for genuinely urgent roles.
- **First dollar within 1–2 weeks** — no build dependency, and turnaround per engagement can be as fast as 24-48 hours once you have applicant data in hand, meaning cash can land quickly after close.

## Why This, Why Now

- Zero build required to start — this is fundamentally a structured research/evaluation task well-suited to manual-plus-LLM review from day one, with automation as a pure speed multiplier layered in once volume justifies it.
- Directly complementary to PoC 16, covering both directions of the hiring-bottleneck problem (too few qualified candidates vs. too many to sort) for the same buyer persona, effectively doubling the addressable pitch from a single outreach motion.
- LLM-assisted resume screening is a genuinely strong fit for the underlying task (structured extraction and ranking against explicit criteria), making the eventual automation layer unusually high-leverage compared to more open-ended services in this folder.
- Fast turnaround (a role can be screened within days) creates a short, satisfying sales-to-delivery cycle that builds momentum and referenceable case studies quickly.

## Risks / Open Questions

- **Screening bias and legal sensitivity:** hiring-related work touches employment law territory (discrimination concerns) more directly than most other services in this folder — score strictly against job-relevant criteria (skills, experience, explicitly stated requirements) and avoid any criteria or commentary that could be construed as filtering on protected characteristics; this is a real compliance boundary, not just a best practice.
- **Quality dependency on criteria precision:** a vague or poorly-defined set of role criteria from the client produces a correspondingly weak shortlist — invest real time in the intake call to nail down specific, objective criteria rather than accepting a generic job description at face value.
- **Data access/privacy:** applicant resumes contain personal information — be explicit about data handling and deletion practices given the sensitivity of the data involved.
- **One-off nature per role limits deal size** relative to retainer-based services elsewhere in this folder — the retainer tier for companies hiring multiple roles is what converts this from one-off project income into more durable recurring revenue.

## Validation Signal to Watch

If 3+ of your first 10 outreach messages (each containing a real, specific candidate-visibility finding) generate a reply, the hook is working — scale outreach via job-board applicant-volume targeting. If early shortlists consistently include candidates the founder says they'd already identified themselves, refine the scoring approach to weight more heavily toward catching under-marketed or poorly-formatted-resume candidates specifically, since that's the differentiated value proposition versus a founder's own rushed skim.
