# PoC 47 — "Your Pricing Page Is Costing You 30% of Revenue" — SaaS Pricing Audit & Restructure Service

**Date:** 2026-07-16
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Early-stage SaaS founders almost universally underprice, mispackage, or confuse their pricing — not out of ignorance but because pricing is genuinely counterintuitive, most founders set prices early based on gut feel or copying a competitor, and revisiting pricing feels risky once revenue is flowing. Common, highly fixable problems: charging per seat when value scales by usage volume, three tiers that differ only by seat count rather than by value metric, a free plan that's too generous (cannibalizing paid conversions), no annual plan option (leaving 20-40% LTV on the table), pricing that doesn't align with how enterprise buyers actually evaluate the tool, or a pricing page so complex it creates decision paralysis. Every one of these issues is diagnosable from the public pricing page plus a 45-minute conversation about conversion and churn data — no internal data access required to produce a high-value initial finding. This is distinct from PoC 18 (SaaS churn audit, which focuses on retention and product engagement) and PoC 28 (agency profitability audit) — this is specifically about pricing architecture, packaging, and the revenue-per-customer optimization layer.

## Who It's For

Early-stage SaaS founders with $3K–$80K MRR who haven't revisited their pricing since launch, or who suspect their pricing is underperforming but don't have a framework for diagnosing why. Best entry points: founders who've raised prices and lost deals they didn't expect to lose, founders who've noticed their free-to-paid conversion rate is lower than benchmarks (~2-5% for freemium), or founders preparing to move upmarket (from SMB to mid-market) where the pricing architecture typically needs restructuring to support the new buyer profile.

## How It Makes Money

- Flat pricing audit: $400–$800 for a structured written analysis of the current pricing architecture — value metric assessment (are they charging for the right thing?), tier differentiation analysis, free plan cannibaliz­ation check, annual plan uplift opportunity, pricing page clarity evaluation, and competitive benchmarking — delivered with a prioritized list of specific, actionable changes ranked by estimated revenue impact.
- Pricing restructure: $800–$1,800 for the audit plus a full recommended pricing architecture — revised value metric recommendation, restructured tier definitions and feature gates, suggested price points based on willingness-to-pay signals, revised pricing page copy and layout brief, and a rollout plan for transitioning existing customers to the new structure without triggering churn.
- Pricing page conversion add-on: $300–$500 to audit and rewrite the pricing page copy specifically for conversion — clarity of value proposition per tier, objection handling, FAQ section, social proof placement, and CTA copy — distinct from the pricing architecture itself, which is about what to charge, not how the page presents it.
- Ongoing pricing advisory: $400–$700/mo for founders actively iterating on pricing (running price tests, preparing for a pricing change, moving upmarket) who want a structured sounding board and monthly check-in on pricing metrics.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Public audit pass: analyze the current pricing page entirely from public information — identify the value metric, count and differentiate the tiers, note the presence/absence of an annual plan, assess the free plan limits, check whether feature gates create meaningful separation between tiers, and benchmark against 3-5 direct competitors' pricing architectures.
   - Founder conversation (45 min): gather the internal data the public page can't reveal — free-to-paid conversion rate, most common tier purchased, most common plan that churns, whether enterprise deals require custom pricing conversations, average deal size, and whether customers have ever pushed back on price.
   - Synthesize findings using an LLM prompted with the audit framework and conversation notes to produce the initial written analysis, then sharpen with specific recommendations and revenue impact estimates based on industry benchmarks (e.g., "adding an annual plan at 20% discount typically increases LTV by 25-35% for SaaS at this stage").
   - Deliver the audit as a structured Google Doc with an executive summary, finding-by-finding analysis, and a prioritized action list.
2. **Software layer (build once 2–3 clients are live):**
   - Reusable pricing audit framework document: a structured set of questions covering every pricing architecture dimension (value metric, tier count and differentiation, free plan strategy, annual plan, enterprise pricing, pricing page clarity) — built once and used as the systematic input for every audit, ensuring nothing is missed regardless of the product category.
   - LLM prompt template that takes the audit framework responses and founder conversation notes as inputs and produces a first-pass written analysis in the correct format, dramatically reducing per-engagement drafting time.
   - Competitive pricing database: a growing internal library of pricing architectures across common SaaS categories (project management, analytics, HR tech, developer tools, marketing automation) — built across client engagements and reused for benchmarking, making competitive context faster to produce for each new client.

## Tools/Stack

- Public pricing pages and Wayback Machine (for historical pricing snapshots) for the initial audit.
- Similarweb free tier, G2/Capterra competitor pages for competitive benchmarking context.
- Claude/Gemini API for structured analysis drafting from the audit framework inputs.
- Google Docs for audit and restructure deliverable.
- Calendly (free tier) for founder conversation scheduling.
- Stripe/invoice for fee collection.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify prospects in SaaS founder communities (Indie Hackers, r/SaaS, MicroConf community, Twitter/X SaaS builder circles) where "is my pricing right?" and "how do I know if I'm undercharging?" are perennial, never-fully-resolved questions — every SaaS founder has pricing anxiety at some point, and it surfaces visibly in these communities.
2. Free-sample hook: for a prospect founder, analyze their public pricing page and identify one specific, concrete problem with a one-sentence explanation: "Your three tiers differ only by seat count — there's no feature gate creating genuine separation, so most buyers default to the cheapest tier because there's no visible reason to upgrade. Adding one meaningful feature gate to your top tier would likely shift 15-20% of users to a higher plan." A precise, specific, data-backed finding that requires no internal information and takes under 10 minutes from their public pricing page alone.
3. SaaS pricing is a topic with active, ongoing community discourse — being a consistently insightful, specific contributor to pricing conversations in Indie Hackers and similar forums builds genuine reputation and inbound, since pricing advice that's vague is common and pricing advice that's specific and backed by a framework stands out immediately.
4. Warm outreach to founders whose products you use or know well — "I've been using [product] for six months and noticed your pricing has [specific observation]. Would you be open to a quick conversation about whether that's intentional?" — a credible, specific, non-cold opener.
5. A documented "changed value metric from per-seat to per-usage, MRR increased 40% in 90 days with zero new customer acquisition" case study is uniquely powerful in SaaS communities because it demonstrates the high-leverage, revenue-without-new-customers outcome that every founder wants.

## Time to First Dollar

- Day 1–2: build the pricing audit framework and run a test audit on 3-4 publicly visible SaaS pricing pages in different categories to calibrate findings quality and audit time.
- Day 2–4: identify 15-20 founders in SaaS communities with public pricing pages that have visible structural issues; prepare a one-finding free assessment for the 8-10 most specific.
- Day 4–7: send outreach with the specific pricing finding attached.
- Day 7–12: close 2–3 founders on the flat audit fee ($400–$800), with the founder conversation scheduled within 48 hours of payment and the full audit delivered within 5 days.
- **First dollar within 1–2 weeks** — no build required, the initial audit is entirely based on publicly available information plus one conversation, and the free-sample finding is generatable in under 10 minutes per prospect.

## Why This, Why Now

- Pricing has among the highest leverage of any business variable — a 10% price increase on $20K MRR is $2K/mo in incremental revenue with zero new customers, zero churn reduction, and zero product improvement. Every founder intellectually knows this; few have ever been given a structured, specific framework to act on it.
- The free-sample finding (one specific pricing page problem, publicly derivable) is unusually persuasive because it demonstrates both that you found something real and that you did it without any access — immediately establishing credibility and removing the "I'd have to share sensitive data with you" barrier.
- Pricing anxiety is perennial and high in SaaS founder communities — there is no shortage of prospects, and the topic has enough ongoing public discourse that building visibility through insightful contributions is a realistic organic channel.
- The restructure tier ($800–$1,800) is a high-conviction purchase for any founder who's seen the audit findings and agrees the problem is real — the audit itself functions as the case for the restructure, creating a natural two-step sales motion where the first purchase funds the second.

## Risks / Open Questions

- **Pricing recommendations without A/B test data are inherently probabilistic:** the audit identifies likely problems and recommends changes based on benchmarks and frameworks; actual impact depends on the specific market, buyer behavior, and implementation — present findings as high-confidence hypotheses with supporting rationale, not guaranteed outcomes.
- **Existing customer pricing transitions are politically sensitive:** recommending a price increase or package restructure for an early-stage founder with existing customers requires a careful rollout plan (grandfathering, notice period, migration path) to avoid triggering churn — always include a transition plan alongside any structural pricing change recommendation, not just the "what" but the "how do you implement without losing existing customers."
- **Value metric changes are high-risk, high-reward:** recommending a switch from per-seat to per-usage (or vice versa) is the highest-impact single pricing change possible and also the most technically complex to implement and the most disruptive to existing customers — be clear about implementation complexity and transition risk when this recommendation is warranted, rather than treating it as a quick fix.
- **Competitor pricing benchmarks go stale quickly:** SaaS pricing in competitive categories changes frequently; always verify competitor pricing as current at time of audit rather than relying on data collected weeks earlier.

## Validation Signal to Watch

If the free one-finding assessments consistently generate "that's exactly the concern I've had but couldn't articulate" reactions from founders, the audit framework is identifying real, felt problems — that specific response pattern is the strongest possible signal that the paid audit will deliver value. Once 3+ paid audits are delivered, track which finding categories are most common (free plan too generous, no annual plan, wrong value metric, weak tier differentiation) — those recurring patterns are the highest-leverage inputs for a productized "SaaS Pricing Health Check" offering that could be delivered faster and priced lower as a lead-generation mechanism for the full restructure engagement.
