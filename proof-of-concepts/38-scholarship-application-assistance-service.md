# PoC 38 — "There's Scholarship Money Nobody's Applying For" — Scholarship Search & Application Assistance Service

**Date:** 2026-07-14
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

High school students and their families face a genuinely overwhelming scholarship landscape — thousands of scholarships exist across national databases, local community foundations, employer-sponsored programs, and niche/identity-specific awards, but most families only ever hear about the handful of famous, hyper-competitive national scholarships and never discover the smaller, less-known, less-competitive local and niche awards where the odds of winning are dramatically better. Application essays are also a major bottleneck — students often qualify for awards they never apply to simply because writing a strong, tailored essay for each one is time-consuming and daunting. This mirrors PoC 07's grant/RFP research-and-writing structure, but for an entirely different, individual/family consumer market with its own urgency (application deadlines tied to a fixed academic calendar) and its own emotionally high-stakes framing (paying for college is one of the most significant financial decisions many families make).

## Who It's For

High school juniors/seniors and their families actively navigating college applications and financial planning — best entry point: families in the fall of senior year (peak scholarship application season) or those who've expressed sticker-shock/financial concern about college costs in parent communities or school-related forums.

## How It Makes Money

- Flat scholarship-search package: $150–$400 to research and deliver a curated, personalized list of 15-25 scholarships the student is genuinely eligible for (matched on major, background, location, interests, GPA range) — most families have no idea how many under-the-radar options exist until shown a real, tailored list.
- Per-essay assistance fee: $50–$150 per scholarship essay, providing structured feedback and editing support (never writing the essay for the student — see risk section) to strengthen a genuine submission.
- Full-service bundle: $500–$1,200 covering the search plus assistance on a defined number of applications, priced as the more common actual deal size for families ready to commit to a real scholarship-hunting push.
- Family/sibling discount for households with multiple students applying in different years — a natural, low-effort way to extend a single relationship into multiple engagements over subsequent years.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Intake conversation/form: student's intended major, GPA range, extracurriculars, background/identity factors relevant to niche scholarship eligibility, geographic location, and family financial context.
   - Search free, publicly available scholarship databases (Fastweb, Scholarships.com, College Board's BigFuture, local community foundation listings, state-specific education department scholarship pages) systematically against the student's profile, prioritizing lower-competition, well-matched opportunities over famous long-shot awards.
   - Deliver a curated, deadline-sorted list with eligibility rationale per scholarship, plus application requirement summaries (essay topics, letters of recommendation needed, deadlines) so the family can plan their application timeline.
2. **Software layer (build once 2–3 clients are live, funded by early package fees):**
   - Reusable eligibility-matching checklist/database (a growing internal list of scholarships tagged by eligibility criteria) that becomes more valuable and faster to search across every subsequent client — a genuine compounding asset similar in spirit to PoC 22's growing vendor-mapping library.
   - Simple scraping/monitoring script (consistent with this repo's existing tooling patterns) to track new scholarship postings and deadline changes across the most-used databases automatically, keeping the search process current without fully manual re-research each time.
   - LLM-assisted essay feedback framework providing structured, specific critique (clarity, specificity, matching the prompt's actual intent) rather than generic writing advice, applied consistently across every essay-assistance engagement.

## Tools/Stack

- Fastweb, Scholarships.com, College Board BigFuture, and local/state scholarship databases — all free, publicly searchable.
- Claude/Gemini API for essay feedback structuring and eligibility-matching assistance.
- Google Sheets/Airtable for the internal scholarship database and per-client tracking.
- Google Docs for delivering the curated scholarship list and essay feedback.
- Stripe/invoice for fee collection.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify prospects via parent communities (local Facebook groups for parents of high schoolers, school-specific parent groups) where college cost/financial aid anxiety is openly and frequently discussed — a direct, self-identifying, timely pain signal.
2. Free-sample hook: for a family who shares their student's basic profile (major interest, background, location), find and share 2-3 real, genuinely well-matched scholarships they likely haven't heard of: "Found these 3 scholarships your student looks like a strong match for — [brief eligibility rationale each] — happy to build out the full list if useful." A concrete, immediately actionable, low-effort-for-the-family demonstration of real value.
3. High school guidance counselors are a strong potential referral partner — counselors are often stretched thin and unable to give every student individualized scholarship research time, making this a genuine value-add they can point families toward without any downside to them.
4. Position the ROI framing simply and powerfully: "even a handful of smaller, less-competitive scholarships can meaningfully offset a year of college costs" — reframes the fee as a clearly favorable investment relative to the dollar amounts realistically at stake.
5. A single "found $8,000 in scholarships the family didn't know existed" result is a highly concrete, dollar-denominated, and emotionally resonant case study for parent community outreach.

## Time to First Dollar

- Day 1–3: identify 15-20 families via parent communities showing visible college-cost concern, prepare free-sample scholarship matches for the first 8-10 based on basic shared student profiles.
- Day 3–5: send outreach with the free-sample matches attached.
- Day 5–10: close 2–3 families on the flat search package fee ($150–$400), collected upfront.
- **First dollar within 1–2 weeks** — no build dependency, the entire MVP is systematic research against free public databases, doable same-day per student profile.

## Why This, Why Now

- Zero build required to start — every underlying scholarship database is free and publicly searchable, with the real, differentiated value being the systematic, tailored matching work most families never do themselves.
- Genuinely high-stakes, emotionally resonant pain point (college affordability) that requires little to no buyer education, similar in intensity to PoC 09's job-search urgency but on a fixed, predictable academic-calendar timeline that makes seasonal outreach timing straightforward.
- Fresh consumer vertical (education/family) diversifying the folder further while reusing the same core research/matching/writing skill set applied throughout.
- Guidance counselor referral channel offers a scalable, relationship-based acquisition path distinct from cold outreach, similar in structure to PoC 22's CPA channel.

## Risks / Open Questions

- **Academic integrity boundary is critical:** essay assistance must stay firmly in the territory of feedback, editing, and structural guidance — never writing the essay for the student. This is both an ethical requirement and often an explicit rule of the scholarships themselves (many require the essay to be the student's own original work) — be explicit about this boundary with every family from the first conversation.
- **Scholarship deadlines create hard, unmovable timing constraints:** unlike most services in this folder, a missed deadline isn't recoverable — build real buffer into your own delivery timelines and communicate deadline risk clearly and early rather than after the fact.
- **Outcome cannot be guaranteed:** scholarship awards are competitive and outside your control — the service's value is in expanding the pool of well-matched, applied-to opportunities and strengthening application quality, not promising a specific award outcome; be explicit about this distinction in marketing.
- **Database currency matters:** scholarship databases occasionally list expired or outdated opportunities — verify current deadlines/eligibility directly on the scholarship's own official page before including it in a client deliverable, not just trusting aggregator-site listings at face value.

## Validation Signal to Watch

If 2+ of your first 8-10 free-sample scholarship matches generate genuine excitement/follow-through from the family, the research method and hook are validated — scale outreach into parent communities and pursue guidance counselor referral relationships in parallel. If families are interested in the search but hesitant on the essay-assistance add-on, that's a useful signal to lead future outreach with the search package alone as the primary offer, keeping essay assistance as a natural, lower-friction upsell once trust from the search deliverable is established.
