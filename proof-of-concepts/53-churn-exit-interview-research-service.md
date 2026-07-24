# PoC 53 — "You Know How Many Customers Churned. You Don't Know Why." — Customer Exit Interview & Churn Reason Research Service

**Date:** 2026-07-17
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Every SaaS company and subscription business tracks churn rate — the percentage of customers who cancel each month — but almost none of them systematically know the real reason customers leave. Cancellation surveys ("why are you cancelling?") produce low response rates and even lower candor: customers click "too expensive" or "missing features" because those are the options, not because they're accurate. The actual reasons — "our champion left the company," "we never got our team to adopt it," "the onboarding was confusing and we never got value," "we found something that does one thing better and that's all we needed" — only surface in a 20-minute conversation with a real person who knows how to ask. A structured exit interview program (reaching out to churned customers within 2-4 weeks of cancellation, conducting a 20-minute structured conversation, and synthesizing findings into a pattern report across 10-20 interviews) produces qualitative intelligence that is directly actionable for product roadmap, pricing, onboarding redesign, and sales objection handling — and that no dashboard or survey can replicate. This is explicitly distinct from PoC 18 (SaaS churn audit, which analyzes behavioral and cohort data to find the quantitative leading indicators of churn) — this is the qualitative research layer that explains the why behind the numbers PoC 18 surfaces.

## Who It's For

SaaS companies and subscription businesses with at least 10-20 churned customers per month — enough volume to produce statistically meaningful patterns across interviews — and a churn rate they're trying to understand and reduce but haven't successfully diagnosed through surveys or product analytics alone. Best entry points: companies that have run a churn cohort analysis (PoC 18 territory) and know they have a problem but not the cause, companies that have just experienced a sudden churn spike and need to understand it quickly, or companies preparing for a funding round where churn is a known investor concern and they want to be able to speak to root causes credibly.

## How It Makes Money

- Per-interview batch flat fee: $600–$1,200 for 10 completed exit interviews — outreach to churned customers, scheduling, conducting all 10 interviews (20 min each), transcript review, and a written synthesis report identifying the top 3-5 churn drivers with supporting quotes and frequency counts across the batch.
- Ongoing monthly interview program: $400–$700/mo to run 5-8 exit interviews per month as a continuous program, delivering a monthly findings update and flagging when a new churn driver pattern emerges — particularly valuable for companies where churn reasons shift as the product and customer mix evolve.
- Rapid diagnosis sprint: $800–$1,500 for 15 interviews conducted within 2 weeks specifically to diagnose a sudden churn spike — the urgency premium reflects compressed scheduling and delivery, for situations where a company needs answers before the next board meeting or investor call.
- Win/loss interview add-on (complementary): $300–$600 for 5 interviews with prospects who evaluated the product and chose a competitor instead — the sales-side mirror of exit interviews, revealing what the product-buying market perceives as weaknesses that churned customers didn't mention.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Intake with the client: get the list of churned customers from the past 60-90 days (name, email, cancellation date, plan they were on) — the client exports this from their billing system (Stripe, Chargebee, Recurly) in minutes.
   - Outreach to churned customers on the client's behalf (using a client-branded email address the client creates for this purpose, or a warm intro from the client's team): a brief, honest, non-salesy request — "We're doing a short research project to understand how we can improve [Product], and your perspective as a former customer would be genuinely helpful. No sales pitch — just 20 minutes of honest conversation. We'll send you a [gift card/coffee voucher worth $15-25] to thank you for your time." Response rates with a small incentive typically run 20-35% of contacted churned customers.
   - Conduct each 20-minute interview using a structured script covering: what they were trying to accomplish when they signed up, what happened during onboarding, at what point they started thinking about cancelling, what the final trigger was, what they're doing now instead, and what would have had to be different for them to stay.
   - Synthesize across all completed interviews using an LLM to identify pattern clusters across responses (group similar root causes, count frequency, extract representative quotes), then write the findings report — the LLM handles pattern clustering from raw notes; human judgment identifies which patterns are actionable vs. noise.
2. **Software layer (build once 2–3 clients are live):**
   - Reusable interview script: 10-12 structured questions refined across every interview batch to consistently surface the decision timeline (when did they first think about leaving), the trigger (what made them actually cancel), and the alternative (what they're doing instead) — the three pieces of information most directly actionable for product and retention strategy.
   - LLM synthesis prompt: takes raw interview notes across a batch and produces a first-pass pattern analysis (here are the 4 most common themes, here are the representative quotes for each, here is the frequency count) that the researcher then edits and contextualizes for the specific client's product and situation.
   - Outreach sequence template: a 3-touch outreach sequence (initial ask, 5-day follow-up, final ask with incentive reminder) refined to maximize response rate from churned customers who have no remaining relationship incentive to respond — the incentive framing and honest "no sales pitch" positioning are the two highest-leverage variables in the outreach.

## Tools/Stack

- Google Meet or Zoom (free tier) for interviews; Otter.ai free tier or Whisper for transcription.
- A client-branded email address (client creates a simple alias like research@theircompany.com) for outreach — keeps the research credible as coming from the company, not a third party.
- Claude/Gemini API for interview note synthesis and pattern clustering across a batch.
- Google Docs for findings report delivery.
- Calendly free tier for interview scheduling.
- Small incentive ($15-25 Amazon/coffee gift card per completed interview) — typically billed as a pass-through cost to the client, not absorbed into the service fee.
- Stripe/invoice for fee collection.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify prospects in SaaS founder and product communities (Indie Hackers, r/SaaS, product management Slack groups, MicroConf community) where "we have high churn but don't know why" and "our cancellation survey data isn't useful" are expressed regularly — a direct, self-identifying pain signal from founders who've already tried the obvious fix (a survey) and found it insufficient.
2. Free-sample hook: for a prospect who mentions a churn problem, offer to conduct 3 exit interviews from their churned customer list for free — "Give me a list of 15 churned customers from the past 60 days and I'll conduct 3 interviews and share what I find, no charge. If the findings are useful, we can talk about running the full batch." The stakes for the client are zero, the value of even 3 interviews is often immediately surprising, and the pattern of findings across just 3 conversations is usually enough to make the case for the full batch.
3. Investors and board members who've flagged churn as a concern are an indirect but powerful pressure source: founders who've been asked "what do you know about why customers are leaving?" in a board meeting and couldn't answer well are highly motivated to fix that gap before the next meeting — a known event with a known date that creates real urgency.
4. Customer success and product management professional communities are a natural channel — practitioners who manage retention programs and want qualitative research support to complement their quantitative tools are a direct buyer for this service.
5. A "ran 12 exit interviews, discovered 80% of churn was from one onboarding failure point, fixed it, churn dropped 40% in 60 days" case study is among the most compelling possible evidence for this service — specific, causal, and expressed in the metric every SaaS founder tracks.

## Time to First Dollar

- Day 1: build the interview script and outreach email sequence; set up Otter.ai transcription; draft the LLM synthesis prompt using sample notes from a practice interview.
- Day 2–3: identify 15-20 SaaS founders expressing churn frustration in communities; prepare the 3-free-interview offer for each, personalized to their stated churn situation.
- Day 3–6: send the free-interview offers.
- Day 6–12: close 2–3 clients on the first interview batch ($600–$1,200 for 10 interviews), collected upfront; begin outreach to churned customers within 48 hours; deliver first findings report within 3 weeks.
- **First dollar within 1–2 weeks** — no build required beyond the interview script and outreach sequence, and the free-3-interview offer removes enough risk that conversion from offer to paid batch is high once the client sees initial findings.

## Why This, Why Now

- Churn is the highest-stakes metric in SaaS, and most companies know their rate but not their reason — creating a clear, felt need that no internal tool automatically fills.
- The service requires a human who can conduct a natural, empathetic conversation and read between the lines of what a churned customer says — a capability that doesn't have an obvious self-serve replacement, unlike many research tasks that are becoming automatable.
- Exit interviews are standard practice at well-run larger companies but consistently skipped at early-stage startups because they feel like overhead — creating a perpetually underserved market at exactly the stage where churn diagnosis matters most for survival.
- The free 3-interview offer is one of the lowest-friction free samples in the folder: the client expends minimal effort (sending a customer list), the output is tangible and surprising, and the transition from "free 3" to "paid 10" is the most natural upsell conversation possible once findings are in hand.

## Risks / Open Questions

- **Response rate is inherently uncertain:** churned customers have no remaining relationship incentive to respond — even with a small incentive, some batches will produce lower response rates than others depending on how the customer left (customers who churned after a negative support experience are less likely to engage; customers who churned due to budget changes are often willing to talk). Scope the service by "completed interviews" not "outreach attempts" so the client pays for what they receive, and build extra outreach volume into every batch to account for non-response.
- **Interviewer bias affects findings quality:** the way questions are asked determines what answers surface — train specifically on the non-leading interview technique (open questions, silence as a prompt, "tell me more" over "was it because of X?") since a biased interview produces confirmation of what the founder already suspects rather than genuine discovery.
- **Churned customers may not remember accurately:** customers who churned 90 days ago may have reconstructed their memory of why — the 2-4 week post-cancellation window produces the most accurate and emotionally fresh recall; scoping to recent churners whenever possible improves findings quality.
- **Confidentiality of findings cuts both ways:** the findings report will contain specific quotes from identifiable customers (even if anonymized by cohort) — handle with appropriate discretion and discuss with the client whether any findings should be kept internal vs. shared more broadly within their organization.

## Validation Signal to Watch

If the 3 free interviews consistently produce findings that genuinely surprise the founder ("I had no idea that was the reason — our survey always said 'too expensive'"), the interview methodology is surfacing real, novel information rather than confirming what the client already knew. That surprise reaction — specific, genuine, about something the client couldn't have gotten another way — is the signal that converts a free batch into a paid ongoing program, and is the core of every case study and outreach message the service should build around.
