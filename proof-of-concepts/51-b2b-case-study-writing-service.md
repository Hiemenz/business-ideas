# PoC 51 — "Your Best Customer Result Is Sitting in a Slack Message Nobody Can Find" — B2B Case Study Writing Service

**Date:** 2026-07-17
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Almost every B2B SaaS company and service business has customers who've achieved real, specific, quantifiable results — "reduced onboarding time by 60%," "closed 3x more deals after switching tools," "cut reporting time from 4 hours to 20 minutes" — and almost none of them have turned those results into polished, structured case studies that sales reps can send in deals, that marketing can publish, and that prospects can find through search. The bottleneck isn't the lack of results — it's that writing a good case study requires: identifying which customer to feature, getting their permission and participation, conducting a structured interview that surfaces the right before/after details, writing a narrative that's both honest and compelling, and producing a document that actually gets used. This is a multi-step project that falls through the cracks at every stage. The result: sales reps copy-paste metrics from Slack messages, founders tell the same anecdotal win story in every sales call, and the company's best proof points never become durable, shareable sales assets. A skilled writer who understands B2B products and can conduct a focused 30-minute customer interview can produce a polished, sales-ready case study in a single day — something most companies have been "planning to do" for a year.

## Who It's For

B2B SaaS companies and service businesses with 5-100 customers who have at least 1-2 customers with a clear, quantifiable result and a good relationship with the vendor — best entry points: companies who've just hit a meaningful customer milestone (first 10, 25, or 100 customers), companies that have been asked by prospects "do you have any case studies?" and had to say no, or companies preparing for a funding round where customer proof points are a critical due-diligence element.

## How It Makes Money

- Per case study flat fee: $400–$800 for a complete, publication-ready case study — customer interview (30 min), written case study (600-900 words in standard format: customer background, challenge, solution, results, quote), and two derivative assets: a 150-word sales summary version for email use and a pull-quote graphic brief for the design team.
- Case study bundle: $1,000–$2,000 for 3 case studies produced in a single engagement, typically featuring 3 different customer segments or use cases — the most common real need, since a single case study rarely covers enough buyer diversity to be useful across all deals.
- Case study-to-content repurposing: $200–$400 additional per case study to produce LinkedIn post copy, a short email sequence variant, and a website testimonial page excerpt from the same interview — drawing on the same skill as PoC 12 (podcast repurposing) but applied to a written source asset rather than audio.
- Win/loss interview add-on: $150–$300 to conduct a structured lost-deal interview with a prospect who chose a competitor, producing a confidential written summary of the real reasons for the loss — a complement to the competitive intelligence from PoC 49, sourced directly from the buyer's mouth rather than public reviews.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Intake with the client (20 min): identify the 1-2 best candidate customers (strongest result, best relationship, most representative of the ideal buyer), confirm the client will make the intro, and gather any existing internal notes on the customer's results (support tickets, success team notes, the Slack message where the customer said something great).
   - Customer interview (30 min, conducted by you): structured around 5 core questions — what was the situation before, what specific problem were you trying to solve, what made you choose this product, what specifically changed after using it, and what would you tell someone considering it. The before/after structure and the specific numbers question ("you mentioned time savings — can you put a rough number on that?") are the two highest-leverage moves in the interview.
   - Write the case study using an LLM prompted with the interview transcript and the standard case study structure, then edit for accuracy, voice, and the specific detail that makes it feel real rather than generic — the LLM handles the first draft; human editing handles the 20% that makes it actually good.
   - Deliver: the full case study, the 150-word sales summary, and the pull-quote brief — all in a Google Doc the client can publish or share immediately.
2. **Software layer (build once 2–3 clients are live):**
   - Reusable customer interview script: 8-10 structured questions that reliably surface before/after specifics, quantifiable results, and quotable moments regardless of product category — refined after each interview to fix questions that produce vague answers and double down on questions that reliably produce specific, usable material.
   - LLM prompt template that takes the interview transcript as input and produces a first-draft case study in the correct format (challenge → solution → results → quote structure), with specific instructions to preserve numerical claims exactly as stated and flag any claims that need verification.
   - Case study template library by product category (SaaS productivity tool, analytics platform, service business) with slightly different emphasis per type — a productivity tool case study leads with time saved, an analytics case study leads with decisions improved, a service business case study leads with outcomes delivered — making each first draft faster to write and more naturally compelling for that buyer type.

## Tools/Stack

- Google Meet or Zoom (free tier) for customer interviews.
- Otter.ai free tier or MacOS Whisper transcription for interview transcription.
- Claude/Gemini API for first-draft case study writing from the interview transcript.
- Google Docs for delivery and collaborative review with the client.
- Canva free tier for the pull-quote graphic if the client doesn't have a design resource.
- Stripe/invoice for fee collection.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify prospects in B2B SaaS and service business communities (Indie Hackers, r/SaaS, sales-focused Slack groups, founder Twitter/X) where "we don't have any case studies yet" and "prospects keep asking for social proof" are common, openly stated problems — particularly from companies approaching their first 10-25 customers where case study need becomes acute.
2. Free-sample hook: for a prospect who mentions a specific customer win (even mentioned casually — "a customer just told us we saved their team 10 hours a week"), offer to turn it into a case study outline for free: "That's a great result — happy to sketch out what the full case study structure would look like if you can share a bit more about that customer's before/after. Takes 15 minutes on your end." A low-commitment entry that produces a useful artifact and naturally transitions into a paid engagement.
3. Fundraising prep timing: founders preparing for a seed or Series A need customer proof points in their data room and often need case studies for the first time at exactly this moment — a highly motivated, time-compressed buyer who has both need and budget.
4. Warm outreach to B2B companies whose product you use or whose customer results you've seen mentioned in communities: "I saw you mentioned [Customer X] achieved [specific result] — that's a compelling result that a lot of your prospects probably never see. Have you turned that into a case study?" — a credible, specific opener that shows you've been paying attention.
5. A meta case study ("here's the case study I wrote for [client], and here's the 2 deals they closed in the 30 days after publishing it") is particularly compelling because it documents the commercial impact of the deliverable itself, not just its quality.

## Time to First Dollar

- Day 1: build the customer interview script (10 questions) and case study template; draft the LLM prompt chain for transcript-to-case-study.
- Day 1–3: identify 15-20 founders in SaaS communities who've mentioned specific customer results but have no case study; prepare the free case study outline offer for each.
- Day 3–6: send outreach with the free outline offer.
- Day 6–12: close 2–3 clients on the per-case-study fee or bundle ($400–$2,000 per engagement), collected upfront or 50% deposit; schedule customer interview within 48 hours of payment and deliver the finished case study within 3-5 days of the interview.
- **First dollar within 1–2 weeks** — no build required beyond the interview script and template, the LLM handles 80% of first-draft writing, and the per-case-study price point is easy to approve without a long procurement process.

## Why This, Why Now

- Case studies are one of the three most-requested sales assets in B2B deals (alongside pricing and demo), meaning every company without them is leaving a known gap in their sales motion — no buyer education required about whether case studies matter.
- The skills required (structured interview technique, B2B product comprehension, narrative writing) are genuinely hard to find in combination, even though the individual components seem simple — most marketers can write, but can't ask the right interview questions; most technical people can understand the product, but can't write a compelling narrative. The combination is the edge.
- LLM assistance makes the core deliverable (a 700-word case study) producible in under 3 hours total from interview to final draft, creating strong economics at the $400–$800 per-unit price point.
- Every published case study generates a durable, compounding sales asset for the client — unlike most deliverables in this folder which solve a problem once, a well-written case study continues to close deals for years after it's written, making the ROI case unusually easy to make concrete.

## Risks / Open Questions

- **Customer participation is required and not guaranteed:** the client needs to make the intro and the customer needs to agree to participate — some clients have the results but don't have a relationship quality that makes asking comfortable, or their customer is in a competitive industry and declines to be named publicly. Scope the service to include anonymous versions (describing the customer by industry/size without naming them) as a fallback that still produces a usable asset.
- **Accuracy is the service's credibility foundation:** case studies make specific claims about results — every number in the final case study must be directly confirmed by the customer in the interview, not inferred or extrapolated. Build explicit verification ("you mentioned 60% time reduction — is that a figure you'd be comfortable with us publishing?") into the interview script as a standard step.
- **Client review cycles can delay delivery:** clients often want to review the case study with their customer before publishing, which can add 1-2 weeks to the timeline. Set this expectation upfront and build it into the project timeline rather than treating delivery of your draft as project completion.
- **Thin customer base limits immediate scale:** a company with only 5 customers may only have 1-2 who are willing and appropriate to feature — work with what's available and identify the expansion path (additional case studies as the customer base grows) as part of the initial engagement conversation.

## Validation Signal to Watch

If the free case study outline offers (built from a specific customer result the founder mentioned) convert at 2+ per 10 outreach messages, the hook and timing are right. The clearest product-market fit signal: a client who publishes the case study and then re-engages within 60 days asking for 2-3 more — that repeat purchase pattern, without any additional sales effort, is the strongest possible confirmation that the deliverable is producing real business value for them.
