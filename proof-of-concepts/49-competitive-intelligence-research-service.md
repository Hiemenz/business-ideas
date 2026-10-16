# PoC 49 — "Your Sales Team Doesn't Know Why You Lose to Competitor X" — Competitive Intelligence Research Service

**Date:** 2026-07-16
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Early-stage startups and small sales teams routinely face competitive objections they're unprepared for — "we're already using [Competitor]," "how are you different from [X]?" — and answer them with vague positioning ("we're more flexible," "we have better support") rather than specific, evidence-backed differentiation that actually moves a deal. The underlying problem is they've never done systematic competitive research: they don't have a clear, current picture of what each competitor charges, what customers actually complain about (vs. what the competitor's marketing says), what features each product does and doesn't have, and how competitors position themselves in sales conversations. All of this information is publicly available — competitor websites, pricing pages, G2/Capterra/Trustpilot reviews, job postings (which reveal strategic priorities), LinkedIn company data, and public community discussions — but pulling it together into a structured, actionable competitive battlecard or landscape report takes 8-15 hours of focused research most founding teams never carve out. The output is a direct sales-enablement asset: a competitive battlecard the sales team uses in every deal, and a landscape report that informs positioning and product roadmap simultaneously.

## Who It's For

Early-stage B2B startups and small sales teams (1-10 people) who are actively losing deals to specific competitors they can't counter effectively, or who are entering a new market and need to understand the competitive landscape before investing in go-to-market. Best entry points: founders who've lost multiple deals to the same competitor and don't have a strong counter-narrative, startups preparing to hire their first sales rep (who will immediately need competitive materials), or companies raising a round where the investor's first question is always "what about [big competitor]?"

## How It Makes Money

- Per-competitor battlecard: $200–$400 per competitor for a structured one-page battlecard covering: company overview and funding, pricing and packaging, core feature comparison (what they have that the client doesn't, and vice versa), known weaknesses drawn from real customer reviews, how they position in sales conversations (drawn from their own website, case studies, and sales rep LinkedIn content), and a specific talk track for handling "we're already using [Competitor]" in a sales call.
- Full competitive landscape report: $600–$1,400 for a 3-5 competitor deep-dive packaged as a complete landscape document — individual battlecards plus a cross-competitor positioning map, a "where to win" section identifying which competitor's customers are most likely to switch and why, and a competitive differentiation brief the founder can use for investor, sales, and marketing positioning.
- Sales team competitive training session: $300–$500 for a 60-90 minute live session walking the sales team through the battlecards, practicing competitive objection responses, and leaving them with a repeatable framework for handling new competitive situations they encounter in the field.
- Quarterly competitive refresh: $300–$600/quarter to update the battlecards as competitors change pricing, launch new features, or shift positioning — a genuinely necessary refresh cycle since competitive landscapes in early-stage markets move fast and a stale battlecard can actively mislead a sales rep.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Gather the competitor list and the client's specific competitive pain point: which competitor(s) are they losing to most, in what type of deal (size, use case, industry), and what objection or comparison they can't currently counter well.
   - Research each competitor systematically using entirely public sources:
     - Pricing and packaging: competitor's public pricing page (and Wayback Machine for historical changes).
     - Feature set: their own feature/product pages, comparison pages (most competitors have explicit "vs. [client]" pages that reveal their positioning), and demo videos.
     - Customer sentiment: G2, Capterra, Trustpilot, and App Store reviews filtered to the most recent 6 months — the negative reviews are the most actionable, as they reveal specific, real weaknesses customers experience but competitor marketing never mentions.
     - Strategic priorities: recent job postings (a company hiring 5 ML engineers is prioritizing AI features; hiring 3 enterprise sales reps is moving upmarket) and LinkedIn company updates.
     - Sales positioning: their case studies, their own "why us" page, and any SDR/AE LinkedIn content showing how they pitch.
   - Synthesize findings using an LLM to structure raw research notes into the battlecard format, then sharpen with specific, quote-level evidence from reviews and a concrete talk-track section written for the client's specific sales context.
2. **Software layer (build once 2–3 clients are live):**
   - Reusable research framework: a structured checklist of every public source to check per competitor (website sections, review platforms, job boards, LinkedIn, Wayback Machine) — ensures systematic, repeatable coverage for every engagement and prevents gaps from ad-hoc research.
   - Battlecard template in Google Docs with fixed sections (overview, pricing, features, weaknesses, positioning, talk track) that produces a consistent, visually clean deliverable across every engagement — built once, used for every client.
   - LLM prompt chain: one prompt to extract the most actionable weaknesses from a batch of G2/Capterra reviews, one to synthesize feature comparison data into the battlecard format, one to write a specific talk-track section from the client's known differentiators — building a repeatable assembly line that compresses per-competitor research time from 4-6 hours to under 2 hours.

## Tools/Stack

- G2, Capterra, Trustpilot (all publicly searchable without login for review content) for customer sentiment research.
- Wayback Machine for historical pricing and positioning research.
- LinkedIn (basic, free) for job posting research and SDR/AE public content.
- BuiltWith or Similarweb free tier for tech stack and traffic context where relevant.
- Claude/Gemini API for research synthesis and battlecard drafting.
- Google Docs for battlecard and landscape report delivery.
- Stripe/invoice for fee collection.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify prospects in B2B sales and founder communities (r/sales, r/startups, sales-focused Slack groups, Indie Hackers) where "we keep losing to [Competitor X]" and "how do I counter [Competitor]?" are extremely common, specific, in-the-moment frustrations — a direct signal of the exact pain this service resolves.
2. Free-sample hook: for a prospect who names a specific competitor they struggle against, pull 5-6 real, recent negative G2/Capterra reviews of that competitor and share the most actionable weaknesses in a reply: "Pulled the last 6 months of G2 reviews for [Competitor] — the three most common complaints are [X, Y, Z], all with multiple corroborating reviews. If none of those match pain points your product solves, your positioning is leaving easy wins on the table. Want me to build the full battlecard?" A research-backed, specific, immediately useful response that demonstrates the methodology before any fee is discussed.
3. Sales enablement consultants and fractional sales leaders who work with early-stage startups are a natural referral channel — they regularly encounter founders whose teams need competitive materials and would refer a specialized research service rather than trying to produce battlecards themselves.
4. Fundraising context creates urgent demand: a founder preparing investor materials who needs to answer "what about [big competitor]?" credibly is highly motivated to pay for a structured competitive analysis — the investor Q&A framing makes the output useful in two contexts simultaneously (fundraising and sales).
5. A "built competitive battlecards for [client's space], sales team closed 3 deals in the next month that had previously stalled on [Competitor] objections" story is highly credible and directly attributable in a way that most sales-enablement work isn't.

## Time to First Dollar

- Day 1–2: build the research framework checklist and run one end-to-end competitive research pass on a competitor in a familiar market to calibrate time and validate the free-tool workflow; draft the battlecard template.
- Day 2–4: identify 15-20 founders/sales leads in communities actively naming specific competitive losses; pull free G2/Capterra review snippets for the named competitor in each case.
- Day 4–7: send outreach with the specific review-based weakness finding attached.
- Day 7–12: close 2–3 clients on the per-competitor battlecard fee ($200–$400 per competitor, typically 2-3 competitors per client = $400–$1,200 per engagement), collected upfront.
- **First dollar within 1–2 weeks** — research is entirely from free public sources, the LLM-assisted synthesis compresses per-competitor time significantly, and the free-sample (real review snippets) requires under 15 minutes per prospect.

## Why This, Why Now

- Competitive objections are one of the top 3 reasons deals stall or are lost, making this a revenue-critical, immediately felt problem for any sales team — not a "nice to have" but a "we're losing money right now without this" framing.
- The free-sample approach (real, sourced customer review quotes about the competitor) is unusually persuasive because it demonstrates both the research methodology and the output format in one artifact — the prospect can immediately imagine the full battlecard from a 5-bullet preview.
- Public review platforms (G2, Capterra) have made competitor customer sentiment more accessible than ever, but synthesizing it into an actionable sales tool still requires human judgment about what matters — creating a durable skills-arbitrage that doesn't disappear as the tools improve.
- Quarterly refresh retainer is genuinely, honestly justified in fast-moving early-stage markets where competitors change pricing, launch features, or shift positioning multiple times per year — one stale battlecard actively misrepresenting a competitor's current product is worse than no battlecard.

## Risks / Open Questions

- **Public information only — no pretexting or misrepresentation:** all research must use genuinely public sources; never pose as a potential customer to extract competitor pricing or product information in a sales conversation, as this crosses a clear ethical and in many contexts legal line — the entirely-public-source constraint is also a genuine feature since it means research can be done at any scale without access or relationship barriers.
- **Competitor information goes stale quickly:** a battlecard built today may be partially inaccurate in 90 days if the competitor changes pricing or launches a major feature — be explicit about the refresh cycle and build the quarterly update into the initial sale as a standard, expected follow-on rather than an afterthought.
- **Review platform bias:** G2 and Capterra reviews skew toward dissatisfied customers (people with a strong opinion are more likely to leave a review than satisfied users) — present review-sourced weaknesses as "known customer pain points" rather than "what most users experience," and note the limitation clearly in the deliverable.
- **Battlecard adoption requires sales team buy-in:** the research deliverable only produces revenue impact if the sales team actually uses it in deals — for clients with an existing sales team, include a brief rollout recommendation (training session, integration into CRM deal notes) alongside the battlecard delivery, not just a Google Doc dropped in a folder.

## Validation Signal to Watch

If the free G2/Capterra review snippets consistently generate "I had no idea customers complained about that" responses from founders, the research methodology is surfacing genuinely novel, actionable information — that surprise reaction is the strongest possible signal that the paid deliverable will deliver clear value. Once 3+ full landscape reports are delivered, track which competitor categories recur across clients (certain well-funded incumbents appear in competitive research across many client engagements) — building deep, reusable research dossiers on the highest-frequency competitors dramatically compresses future engagement time and becomes a genuine competitive moat for the service itself.
