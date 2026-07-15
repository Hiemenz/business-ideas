# PoC 16 — "We Found Your Next Hire" — Candidate Sourcing-as-a-Service for Early-Stage Startups

**Date:** 2026-07-10
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Early-stage startup founders and hiring managers need to fill roles (engineers, first salesperson, ops hire) but don't have a recruiter, and traditional agency recruiters charge 20-25% of first-year salary — often $20k-$40k+ per hire — which is out of reach for a seed-stage company hiring their 5th-15th employee. What they actually need is just the sourcing step: a curated shortlist of genuinely qualified, reachable candidates so the founder's own time goes into interviewing, not searching. This is distinct from PoC 08 (which books sales meetings with buyers) — the outbound skill is the same, but the target, message, and buyer economics are entirely different, aimed at the hiring/people-ops budget rather than sales pipeline.

## Who It's For

Seed/Series A startup founders and early hiring managers actively hiring for a specific, defined role (visible via job postings on their site, LinkedIn "we're hiring" posts, or AngelList/Wellfound listings) without an in-house recruiter or People/Talent function yet.

## How It Makes Money

- Flat fee per shortlist: $300–$600 for a curated list of 10-15 qualified, contact-verified candidates for a single role, delivered within a week.
- Pay-per-hire fee: $1,500–$4,000 due only if a sourced candidate is actually hired — dramatically cheaper than traditional agency fees while still being a meaningful, easily-justified win for the founder relative to the cost of an empty seat.
- Hybrid model (recommended default): smaller upfront sourcing fee ($300–$500) that funds your time regardless of outcome, plus a reduced success fee ($1,000–$2,500) only if hired — balances near-term cash need against the stronger, easier-to-close success-fee pitch.
- Retainer for startups hiring multiple roles in a short window: $1,000–$2,500/mo covering ongoing sourcing across 2-3 open roles simultaneously.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Intake call: extract the exact role requirements, must-have vs. nice-to-have skills, comp range, and what's made the role hard to fill so far.
   - Manually source candidates via LinkedIn search (filtered by title, skills, current company patterns relevant to the role), GitHub (for technical roles, searching by relevant language/project activity), and niche community job boards where the target candidate profile is likely active.
   - Reach out to prospective candidates with a personalized message (using an LLM to help draft, referencing something specific about their background) gauging interest and basic fit before adding them to the shortlist — only forward candidates who've expressed genuine openness, not cold names.
   - Deliver the shortlist with a one-line fit summary per candidate plus contact info/LinkedIn profile, so the founder can go straight to outreach or a first conversation.
2. **Software layer (build once 1–2 clients are live, funded by early sourcing fees):**
   - Reusable sourcing-query templates per role archetype (backend engineer, first AE, ops generalist) — same reusable-scaffold pattern used throughout this folder, cutting search setup time on repeat engagements.
   - Simple tracking sheet (Airtable/Google Sheets) logging candidates contacted, response status, and shortlist status per client/role — both for your own pipeline management and as a transparency artifact you can share with the client mid-engagement.
   - LLM-assisted resume/profile screening pass (summarizing a candidate's background against the role's must-haves) to speed up qualification once your outreach volume grows beyond what you can manually review candidate-by-candidate.

## Tools/Stack

- LinkedIn (manual search, free account sufficient for early volume; Sales Navigator/Recruiter Lite free trials extend reach if needed) for general sourcing.
- GitHub search and relevant community-specific boards for technical role sourcing.
- Claude/Gemini API for personalized outreach message drafting and resume/profile screening summaries.
- Airtable/Google Sheets (free tier) for pipeline tracking.
- Stripe/invoice for sourcing fees; a simple written agreement for success-fee terms (definition of "hired," payment timing) to avoid disputes.

## Go-to-Market — First 3-5 Customers, Zero Ad Spend

1. Identify prospects via live job postings on startup job boards (Wellfound/AngelList, Y Combinator's Work at a Startup, company career pages) and "we're hiring" LinkedIn posts from founders — a direct, self-identifying, time-bound signal of need.
2. Free-sample hook: source 2-3 genuinely qualified, reachable candidates for their exact open role and send as a DM: "Saw you're hiring for [role] — found these 3 people who look like strong fits and are open to hearing more, happy to share who they are." This is a uniquely high-value free sample, since a founder's time-to-hire pain is acute and immediate, unlike services where the pain is more abstract.
3. Founder communities (Y Combinator alumni networks, local startup Slack/Discord groups, indie founder communities) are dense with exactly this buyer and this pain point, openly discussed.
4. Position the pricing explicitly against traditional agency recruiter fees in outreach — "a fraction of what a 20% agency fee would cost you" is an immediately understandable, favorable comparison for any founder who's priced out agency recruiting before.
5. A single successful hire is an extremely strong referral trigger — ask for an intro to another founder in their network immediately upon a hire being made, while the relief/gratitude of solving the hiring problem is freshest.

## Time to First Dollar

- Day 1–3: identify 10-15 actively-hiring startups via job board/LinkedIn signals, source 2-3 real candidates per prospect for the first 6-8 as free samples.
- Day 3–6: send outreach with the free-sample candidates attached.
- Day 6–12: close 2–3 clients on the hybrid pricing model (upfront sourcing fee + reduced success fee), collected upfront for the sourcing portion.
- **First dollar within 1–2 weeks** via the upfront sourcing fee; success-fee revenue follows on whatever timeline the client's hiring process takes (often 3-8 weeks), so the upfront fee is what carries near-term cash needs.

## Why This, Why Now

- Zero build required to start — sourcing is fundamentally a research and outreach skill, directly playing to sales/ops strength, with software automation as a pure efficiency layer added later.
- Extremely favorable and easy-to-understand price comparison against the incumbent alternative (traditional agency recruiters), making the pitch nearly self-evident once a founder has been quoted an agency fee before.
- Acute, time-bound pain (an open role is costing the company real productivity every week it's unfilled) creates urgency that shortens the sales cycle relative to less time-pressured service categories.
- Founder networks are tightly connected and referral-dense — a single successful hire tends to travel fast within the same communities where prospects are found in the first place.

## Risks / Open Questions

- **Sourcing quality is the entire product:** a shortlist of poorly-matched or unreachable candidates destroys credibility immediately — never pad a shortlist to hit a number; a shorter list of genuinely strong, pre-qualified candidates beats a longer weak one.
- **Success-fee timing risk:** hiring processes can stall or fall through for reasons outside your control (budget freeze, role gets deprioritized) — the hybrid pricing model's upfront portion is what protects your near-term cash flow against this variability.
- **Role-market difficulty varies widely:** some roles (senior specialized engineers, in particular) are genuinely hard to source regardless of effort — set expectations honestly during the intake call about how competitive a given role/market is rather than overpromising shortlist quality or timeline.
- **Definition disputes on "hired":** be explicit in writing about what triggers the success fee (offer accepted vs. start date vs. passed probation) before starting the engagement.

## Validation Signal to Watch

If 2+ of your first 6-8 free-sample candidate lists generate a genuinely enthusiastic reply (not just polite acknowledgment) from the founder, the sourcing quality and targeting are working — scale outreach into founder communities next. If free samples are consistently met with lukewarm responses, revisit whether the role/company selection is too competitive for your current sourcing reach, and consider targeting roles or company profiles where you can more reliably surface strong, reachable candidates.
