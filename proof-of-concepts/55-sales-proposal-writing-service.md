# PoC 55 — "You Had a Great Sales Call and Then Lost the Deal to Your Own Proposal" — Sales Proposal & RFP Response Writing Service

**Date:** 2026-07-18
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Small agencies, consultancies, and B2B service businesses routinely win the sales conversation and then lose the deal to a poorly constructed written proposal. The problems are consistent across almost every small firm: the proposal opens with a company overview nobody asked for, buries the recommended solution under pages of methodology, lists deliverables without connecting them to the buyer's stated outcomes, uses a scope-of-work format when the buyer needed a business case, and closes with a pricing table and no explicit ask. The buyer, who had a genuine conversation with a human who understood their problem, receives a document that reads like a generic service menu and forwards it to a decision-maker who wasn't on the call — and it fails to close. Every element of a winning proposal is learnable and formulaic: mirror the buyer's stated problem back to them in their own language, lead with the outcome not the service, scope clearly without overwhelming, price with context, and make the next step impossible to be vague about. This is explicitly distinct from PoC 07 (grant and government RFP writing for nonprofits and public-sector funding) — this is commercial B2B proposals where the buyer is a business making a budget decision, a completely different format, framing, and decision dynamic.

## Who It's For

Small agencies (design, marketing, development, PR, consulting) with deal sizes of $5K–$150K that are winning discovery calls but losing at the proposal stage more than they should be — visible in their close rate on proposals sent vs. verbal interest received. Best entry points: agencies that have just lost a deal they were confident about after sending a proposal, firms preparing to respond to a formal RFP from a mid-size or enterprise buyer for the first time, or consultants who know their work is excellent but whose proposals consistently undersell it.

## How It Makes Money

- Per-proposal writing fee: $300–$700 for a complete, client-specific sales proposal written from a 30-minute intake call covering the deal context (what the buyer said, what they care about, what competing options they're evaluating), delivered within 48 hours of the intake call — the speed is part of the value, since proposals sent within 24 hours of a sales call close at significantly higher rates than those sent a week later.
- RFP response package: $500–$1,200 for a formal RFP response (structured to the RFP's required sections while injecting genuine differentiation into each required response) — the higher price reflects the longer format, the requirement to address mandatory sections, and the competitive stakes of a formal procurement process.
- Proposal template build: $400–$800 one-time to build a firm's master proposal template — a reusable structure with variable sections the firm fills in per deal, a fixed opening framework that always works, and a pricing presentation format that reduces sticker shock — built once and used for every future proposal without additional per-proposal fees.
- Win/loss proposal review: $200–$350 to review a proposal the firm recently lost and deliver a specific, written assessment of what structurally went wrong and what to do differently — a lower-commitment entry that produces immediate, specific value and naturally surfaces template work or ongoing per-proposal needs.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - 30-minute intake call per proposal: gather the deal context — who is the buyer (title, company, size), what did they say their problem is in their own words, what outcome are they measuring success by, what options are they evaluating, what's the timeline and budget signal, what did the sales conversation go particularly well on, and what objections came up.
   - Write the proposal using a proven B2B proposal structure: (1) Situation — mirror the buyer's stated problem back in their language so they feel understood; (2) Recommendation — one clear recommended approach, not a menu of options; (3) Outcomes — 3-5 specific, measurable results they'll achieve, tied to their stated success metrics; (4) Scope — clear, bounded deliverables written as outputs rather than activities; (5) Investment — pricing contextualized against the outcome value, not presented as a standalone number; (6) Next step — a single, specific, frictionless action (a 30-min call to review, a signature, a date to start).
   - Use an LLM to produce a first draft from the intake call notes and the structure above, then edit heavily for the buyer's specific language, the firm's voice, and the deal-specific context — the LLM produces the structure and first pass; human editing produces the specificity that makes it feel written for this buyer, not templated.
   - Deliver as a Google Doc (or PDF export) within 48 hours of the intake call.
2. **Software layer (build once 2–3 clients are live):**
   - Intake call framework: a structured 12-question brief that reliably surfaces every variable needed to write a strong proposal — buyer's stated problem (in their words), success metric, timeline, competing options, objections, and what the salesperson feels most confident about — refined after each proposal to fix questions that produce vague answers.
   - Proposal section templates by deal type (project-based, retainer, hybrid; technical implementation vs. strategic advisory vs. creative services) — the recommended structure is consistent but the language and emphasis shift meaningfully by deal type, and having pre-built section templates per type accelerates first-draft production.
   - LLM prompt chain: one prompt for situation summary (given these intake notes, write a 2-paragraph situation section that mirrors the buyer's stated problem), one for recommendation (given this service and these outcomes, write a single clear recommendation paragraph), one for scope (given these deliverables, write them as outcomes rather than activities) — each prompt producing a first draft that requires editing but not writing from scratch.

## Tools/Stack

- Google Docs or Notion for proposal delivery (whichever the client prefers to share with their buyer).
- Claude/Gemini API for first-draft proposal writing from structured intake notes.
- Calendly free tier for intake call scheduling.
- Loom free tier as an optional but high-converting add-on: a 90-second video walkthrough of the proposal recorded by the selling firm before sending — proposals accompanied by a personal video walk-through close at meaningfully higher rates, and offering to script the Loom as part of the deliverable adds value without significant additional time.
- Stripe/invoice for fee collection.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify prospects in agency and consultant communities (r/agency, r/consulting, agency owner Slack groups, freelancer communities on Indie Hackers) where "sent a proposal, never heard back" and "I don't know why we keep losing at the proposal stage" are regular, specific frustrations — direct expressions of the pain this service resolves.
2. Free-sample hook: for a prospect who shares a lost deal or a proposal they're uncertain about, offer a free structural review of their current proposal template: "Happy to take a look at your proposal structure and tell you the 2-3 things most likely to lose you deals. No charge — takes me 20 minutes." A low-commitment offer that produces a specific, immediately useful finding and naturally opens the conversation about per-proposal writing or a template rebuild.
3. Agencies that have recently scaled their sales motion — just hired a first business development person, or started attending conferences to pitch for work — are newly generating more proposals than before and suddenly aware of their proposal quality as a variable; a predictable, recurring outreach trigger visible in job postings and LinkedIn announcements.
4. Freelance platforms (Toptal, Contra, Expert360) where independent consultants compete for project work are a natural venue — proposal quality is often the only differentiator between two technically equivalent candidates, making it a felt, immediate need.
5. A documented "same firm, same services, same pricing — rewrote the proposal structure, close rate went from 28% to 51% in 90 days" result is among the most commercially credible case studies possible, because close rate is a metric every agency tracks and the improvement is directly attributable to the proposal, not other variables.

## Time to First Dollar

- Day 1: build the intake call framework and the 6-section proposal structure; write a sample proposal from a fictional deal scenario to validate the LLM prompt chain and measure time from intake notes to final draft.
- Day 2–3: identify 15-20 agencies and consultants in communities expressing proposal-stage losses; review any proposal templates they've shared publicly or request a look.
- Day 3–6: send the free structural review offer to each, or engage in the conversation with specific, knowledgeable observations.
- Day 6–12: close 2–3 clients on the per-proposal fee ($300–$700) or the template build ($400–$800); first proposal delivered within 48 hours of intake call.
- **First dollar within 1–2 weeks** — no build required beyond the intake framework and proposal structure, LLM-assisted drafting makes each proposal fast to produce, and the deal-urgency of an active proposal the client needs to send by Friday creates natural, immediate closing pressure.

## Why This, Why Now

- The proposal stage is a known, measurable choke point in almost every agency's sales funnel, but it's rarely treated as something a specialist can improve — most agency owners have just accepted their close rate as fixed. Reframing it as a skill with a knowable best-practice structure that can be brought in externally is the core positioning insight.
- Deal-urgency creates same-week sales cycles: a client with an active RFP due on Friday and a weak draft will pay $500 on Monday to have a strong one by Wednesday — the time pressure is built into the engagement rather than something that needs to be manufactured.
- Per-proposal pricing makes the ROI calculation trivial: if the average deal is $20K and the close rate improvement from a $500 proposal is even 15 percentage points, one additional closed deal pays for 40 proposals. Any agency owner can do that math in seconds.
- The template build tier ($400–$800) produces a one-time deliverable that the agency uses indefinitely — making it a high-value, easy-to-approve purchase for any firm that generates more than 5 proposals per month.

## Risks / Open Questions

- **Proposal quality is necessary but not sufficient for closing:** a great proposal doesn't fix a bad fit, a misaligned price expectation, or a buyer who was never seriously evaluating the firm — be clear that the service improves the document's ability to convert genuine interest, not that it creates interest that wasn't there.
- **Speed of delivery is a core part of the value:** a proposal writing service that takes a week to deliver is almost worthless — the 48-hour turnaround commitment must be held consistently, since proposals sent more than 72 hours after the sales call lose a meaningful percentage of their closing power; this means managing intake call scheduling and queue carefully from the start.
- **Confidentiality of deal details:** intake calls surface sensitive competitive information (who the client is competing against, what the buyer's budget is, internal sales strategy) — be explicit about how you handle this information and build appropriate confidentiality language into your service agreement.
- **Firm voice matching requires editing:** the LLM's first draft will be structurally correct but tonally generic — the editing pass that makes the proposal sound like it came from the selling firm's voice rather than a template is the most important and least automatable step; don't deliver LLM first drafts without this pass.

## Validation Signal to Watch

If the free structural review offers consistently produce "this is exactly what's wrong with ours" reactions followed by "can you help us fix it?", the diagnosis is landing and the need is real. The strongest possible validation signal: a client who sends a proposal you wrote, wins the deal, and attributes the win specifically to the proposal document — that single attributable win, with the client's permission to reference it, is worth more than any other marketing asset this service can generate.
