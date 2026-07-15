# PoC 30 — "Does ChatGPT Even Know You Exist?" — AI Answer Engine Optimization (AEO) Service for Small Businesses

**Date:** 2026-07-13
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

A meaningful and growing share of buying research now happens inside AI assistants (ChatGPT, Perplexity, Claude, Google's AI Overviews) instead of traditional search — someone asks "what's the best [product/service] in [city]" or "recommend a [category] tool for [use case]" and gets a direct, synthesized answer with a handful of named businesses, not a page of blue links to click through and compare themselves. Most small businesses have never checked whether they're mentioned in these answers at all, and almost none have done anything intentional to influence whether they are. This is a genuinely new discipline (often called AEO/GEO — answer/generative engine optimization) distinct from PoC 10's local SEO (which optimizes for Google's map pack, a different ranking mechanism entirely) — it's specifically about how AI systems select, cite, and describe businesses when synthesizing an answer, and it plays directly to a technical understanding of how LLMs retrieve and weight source content that most marketers don't yet have.

## Who It's For

Small-to-mid businesses selling a product/service category where people plausibly ask an AI assistant for a recommendation — SaaS tools, professional services, local businesses with a strong online presence, e-commerce brands in a specific niche. Best entry point: businesses that already invest in traditional SEO/content marketing (proving they value visibility and have budget for it) but have never specifically checked or optimized for AI-assistant visibility — an entirely unaddressed adjacent gap for an already-receptive buyer.

## How It Makes Money

- Flat AEO audit fee: $300–$700 — systematically query multiple AI assistants (ChatGPT, Perplexity, Claude, Google AI Overviews) with realistic buyer questions in the client's category, document whether/how they're mentioned versus competitors, and identify why competitors are being cited instead (structured content, clear comparison pages, Wikipedia/review-site presence, consistent third-party mentions).
- Implementation project fee: $500–$2,000 to actually make the content changes that improve AI-citation likelihood — restructuring key pages with clear, extractable factual statements (AI systems favor content that directly answers questions in scannable, unambiguous language), adding comparison/FAQ content, and pursuing the third-party mentions/citations that AI systems draw from.
- Ongoing monitoring retainer: $150–$400/mo to re-query AI assistants periodically and track whether visibility is improving as models update and content changes take effect — a justified recurring service given how quickly this landscape shifts and how invisible changes are without deliberate tracking.
- Category-monitoring/competitive intelligence add-on: tracking not just the client but their top 3-5 competitors' AI visibility over time, valuable competitive context that most businesses have zero insight into today.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Compile a realistic set of 10-15 buyer-intent questions in the client's category (e.g., "best project management tool for a 10-person marketing agency," "who does [service] in [city]") based on how real customers would plausibly phrase a research question to an AI assistant.
   - Manually run these queries across ChatGPT, Perplexity, Claude, and Google's AI Overview feature, documenting whether the client is mentioned, how they're described, and which competitors appear instead and why (what content/structure/citations those competitors seem to have that the client doesn't).
   - Deliver a findings report: current AI-visibility baseline, competitor comparison, and specific, concrete content/structure recommendations (clearer comparison pages, more direct factual statements, pursuing citations on sites AI systems draw from) to improve citation likelihood.
2. **Software layer (build once 2–3 clients are live, funded by early audit fees):**
   - Scripted query-and-log system that runs a defined question set against multiple AI assistants' APIs (where available) on a schedule, replacing manual re-querying with automated, trackable results over time — turns a one-time audit into an efficiently repeatable monitoring product.
   - Reusable question-set templates by business category (SaaS, local service, e-commerce) so each new client engagement starts from a relevant, refined baseline rather than building the query set from scratch.
   - Content-scoring checklist (structured against known patterns that correlate with AI-citation likelihood: direct factual statements, clear comparison structures, FAQ formatting, third-party citation presence) applied consistently across client content reviews.

## Tools/Stack

- Direct access to ChatGPT, Perplexity, Claude, and Google AI Overviews (free tiers sufficient for manual querying at audit scale) — no paid tooling required to start.
- API access to relevant AI assistants (where available) for the automated monitoring layer once volume justifies building it.
- Claude/Gemini API for content restructuring and drafting AEO-optimized page copy.
- Google Docs for report delivery.
- Stripe/invoice for fee collection.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify prospects among businesses already actively investing in content/SEO marketing (visible via an active blog, clear existing SEO effort) — proven budget and belief in visibility as a growth lever, just missing this specific new angle.
2. Free-sample hook: run 2-3 realistic buyer questions for a prospect's category through an AI assistant and share the actual result: "Asked ChatGPT '[realistic buyer question in their category]' — you weren't mentioned, but [Competitor] was, three times. Want to know why and what to do about it?" A uniquely concrete, easy-to-verify finding (the prospect can literally run the same query themselves and see it), making this one of the most credible free-sample hooks in the folder.
3. Marketing/SEO professional communities are a strong, highly on-topic venue right now, since AEO/GEO is an actively emerging, widely-discussed topic among exactly the people who'd either buy this service themselves or refer clients who need it.
4. Position clearly as a genuinely new, largely unaddressed gap — most competitors in the traditional SEO space haven't yet built a systematic AEO offering, giving early positioning value as someone who understands this specific new mechanism.
5. A single "went from zero AI-assistant mentions to being cited in 6 of 10 test queries" result is a highly concrete, timely, and shareable case study, especially valuable right now given how new and interesting this topic is to marketing-adjacent audiences.

## Time to First Dollar

- Day 1–3: identify 15-20 prospects with existing SEO/content investment, run free-sample queries for the first 8-10's categories.
- Day 3–5: send outreach with the specific, verifiable AI-query finding as the opener.
- Day 5–10: close 2–3 clients on the flat audit fee ($300–$700), collected upfront.
- **First dollar within 1–2 weeks** — no build dependency, the entire audit MVP is manual querying across free-tier AI assistant interfaces, doable same-day.

## Why This, Why Now

- Zero build required to start — the diagnostic tool is literally asking questions to free-tier AI assistants and documenting results, immediately actionable without any special access.
- Genuinely novel, emerging category with limited existing competition compared to well-established services like traditional SEO — meaningful early-mover positioning value for whoever builds credibility here first.
- Directly and uniquely plays to a technical understanding of how LLMs retrieve, weight, and cite source content — a distinctive edge over traditional marketers who understand search engine ranking factors but not the different mechanics of AI-answer synthesis.
- Timely and inherently interesting topic that generates its own word-of-mouth and content-marketing opportunities (this is a genuinely engaging thing to talk about in marketing communities right now, distinct from more established, less novel service categories).

## Risks / Open Questions

- **Rapidly evolving, less-established methodology:** unlike traditional SEO with decades of documented ranking-factor research, AEO/GEO best practices are still emerging and less certain — be honest with clients that recommendations are based on observed patterns and reasonable inference from how LLMs process content, not a fully mature, proven playbook.
- **Results are harder to guarantee or fully control:** AI assistant outputs can vary between queries and shift as underlying models update — set expectations around directional improvement and ongoing monitoring rather than promising specific guaranteed citation outcomes.
- **Query/result variability:** the same question can get different answers across different sessions or model versions — run multiple queries per question and report patterns/frequency rather than treating any single query result as definitive.
- **Category applicability varies:** some business categories (highly local, low-online-research-intent purchases) may see limited real-world benefit from AI-assistant visibility compared to categories where research-heavy buying behavior is common (software, professional services, considered purchases) — screen for genuine category fit during the sales conversation rather than pitching universally.

## Validation Signal to Watch

If 3+ of your first 10 outreach messages (each with a real, verifiable AI-query finding) generate a reply, the hook and category positioning are working — scale outreach into marketing/SEO professional communities, where the novelty of the topic should drive strong organic interest. If early implementation engagements show measurable improvement in AI-assistant mention frequency on re-query after a few weeks, that becomes a powerful, concrete case study — and if they don't, revisit whether the specific content changes made actually target what's influencing citation behavior, since this is still an evolving, imperfectly understood mechanism.
