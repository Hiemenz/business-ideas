# PoC 52 — "You Published 80 Blog Posts and Google Sends You 200 Visitors a Month" — Technical SEO Audit Service

**Date:** 2026-07-17
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

SaaS companies, content businesses, and e-commerce stores regularly invest heavily in content — blog posts, landing pages, comparison pages — and then wonder why organic traffic never materializes despite months of publishing. The answer is almost always a layer below the content itself: technical SEO problems that prevent Google from properly crawling, indexing, and ranking the pages that already exist. Common, highly diagnosable issues include: pages marked noindex by accident, duplicate content from URL parameter variations, slow Core Web Vitals that suppress rankings, broken internal linking that leaves pages as orphans, missing or malformed structured data, canonical tag errors sending link equity to the wrong URL, and a sitemap that lists pages Google has already decided aren't worth indexing. None of these problems require sophisticated content strategy to fix — they require a methodical technical audit using free tools, a clear findings report, and specific implementation instructions. This is explicitly distinct from PoC 10 (Local SEO / Google Business Profile, which is about local search map pack visibility for brick-and-mortar businesses) and PoC 30 (AI Answer Engine Optimization, which is about LLM citation and featured snippet optimization) — this is the foundational technical health layer that determines whether any SEO investment pays off at all.

## Who It's For

SaaS companies and content-heavy websites that have been publishing content for 6+ months without meaningful organic traffic growth, or e-commerce stores whose product/category pages aren't ranking despite having real inventory. Best entry points: founders who've invested in content but are puzzled by the lack of traffic, companies that recently relaunched or migrated their website (migrations routinely introduce technical SEO regressions that aren't caught until traffic drops), or companies preparing to invest in a content program who want to confirm the technical foundation is solid before spending.

## How It Makes Money

- Flat technical SEO audit: $400–$900 for a complete technical audit covering crawlability, indexation, Core Web Vitals, duplicate content, internal linking, structured data, sitemap quality, and redirect integrity — delivered as a prioritized findings report with specific fix instructions for each issue ranked by estimated traffic impact.
- Site migration audit: $600–$1,200 specifically for companies planning or having just completed a website migration (domain change, platform change, URL restructure) — the highest-risk SEO event a site goes through, where a pre-migration audit prevents catastrophic traffic loss and a post-migration audit catches regressions before they compound.
- Implementation support: $200–$400/mo to oversee or directly implement the technical fixes from the audit, confirm each fix is correctly deployed, and monitor Google Search Console for indexation improvements — for clients who don't have technical resources to execute the fixes themselves.
- Quarterly technical health check: $250–$500/quarter for an ongoing lightweight audit of the same site, catching new technical issues introduced by content updates, platform changes, or CMS upgrades before they accumulate into a major traffic problem.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Run a full crawl of the target site using Screaming Frog SEO Spider (free up to 500 URLs — sufficient for most SaaS and small content sites; for larger sites, Sitebulb has a free trial or the crawl can be scoped to the highest-priority site sections).
   - Check Google Search Console (client grants read access) for: pages with manual actions, index coverage errors, Core Web Vitals failures by page group, and the crawl stats report to see which pages Google is and isn't visiting.
   - Run PageSpeed Insights (free, no login) on the 5-10 highest-priority pages for Core Web Vitals scores and specific performance bottleneck identification.
   - Validate structured data using Google's Rich Results Test (free) on key page types.
   - Synthesize findings: categorize every issue found by type (crawlability, indexation, performance, structured data, duplicate content, internal linking), assign a severity tier (critical/high/medium/low based on estimated traffic impact), and write specific implementation instructions per issue using an LLM to translate technical findings into clear, developer-ready fix briefs.
   - Deliver as a structured Google Doc: executive summary (the 3 issues causing the most traffic suppression), detailed findings by category with fix instructions, and a prioritized implementation roadmap.
2. **Software layer (build once 2–3 clients are live):**
   - Reusable audit checklist: every category of technical SEO issue systematically checked in the same order across every engagement — ensures nothing is missed and makes the audit faster with each repetition.
   - LLM prompt template that takes structured crawl data and Search Console findings as input and produces a first-pass findings narrative in the correct report format, dramatically reducing per-engagement writing time.
   - Fix-instruction library: a growing internal collection of specific, copy-pasteable fix instructions for the most common technical SEO issues (how to fix a noindex tag in WordPress, how to implement canonical tags correctly in Shopify, how to fix duplicate content from pagination) — built once per issue type and reused verbatim across every client where the same issue appears.

## Tools/Stack

- Screaming Frog SEO Spider free tier (500 URL crawl limit — sufficient for most initial audits).
- Google Search Console (free, client grants read access — this is the single highest-signal data source for any technical SEO audit).
- PageSpeed Insights / Lighthouse (free, no login required) for Core Web Vitals.
- Google's Rich Results Test (free) for structured data validation.
- Ahrefs Webmaster Tools free tier or Google Search Console for backlink and indexation data.
- Claude/Gemini API for findings narrative drafting and fix-instruction writing.
- Google Docs for audit report delivery.
- Stripe/invoice for fee collection.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify prospects in SaaS and content marketing communities (Indie Hackers, r/SEO, r/SaaS, content marketing Slack groups) where "I've been publishing for a year and my traffic is flat" and "our blog isn't driving any organic traffic" are extremely common expressions of exactly this problem — direct, high-intent signals from founders who've already invested in content and are confused about the return.
2. Free-sample hook: run a quick free check of a prospect's site using publicly available tools (PageSpeed Insights for their homepage, a manual spot-check of 3-5 of their blog posts in Google's site: search operator to see what's indexed) and report a specific finding: "Checked your site — your Core Web Vitals score is failing on mobile for your blog section, and Google site: search shows only 12 of your 80 posts are indexed. Those two issues alone would explain most of the traffic underperformance. Want the full audit?" A specific, data-backed finding that requires 10 minutes and no access, immediately distinguishing this from generic SEO advice.
3. Website migration announcement is a perfect prospecting trigger: any company that publicly announces a website redesign or platform migration (visible on Twitter/X, LinkedIn, product update emails) is about to introduce — or has just introduced — technical SEO regressions. Proactive outreach immediately after a public migration announcement has unusually high relevance and timing.
4. Agencies that do web design or content marketing but don't have technical SEO depth are natural referral partners — they frequently deliver sites or content programs to clients who then experience the traffic gap, and referring the technical audit to a specialist is both a client service and a revenue-share opportunity.
5. A "fixed 3 technical issues, organic traffic increased 340% in 90 days" result expressed in those specific numbers and a before/after Google Search Console screenshot is among the most compelling possible evidence for this service — traffic is measurable, the timeline is visible, and the causal link from specific fixes to outcome is credible.

## Time to First Dollar

- Day 1: install Screaming Frog, run a test crawl on your own site or a public site to calibrate the workflow; build the audit checklist and fix-instruction library skeleton for the 8-10 most common issues.
- Day 2–3: identify 15-20 SaaS founders or content site operators publicly expressing frustration about organic traffic underperformance; run a quick free check (PageSpeed + site: search) for each.
- Day 3–6: send outreach with the specific free-check finding.
- Day 6–12: close 2–3 clients on the flat audit fee ($400–$900), with Google Search Console read access granted on payment; deliver the full audit within 5-7 days.
- **First dollar within 1–2 weeks** — the free tools are immediately usable, the free-sample finding takes 10 minutes per prospect, and founders with visible organic traffic problems are abundant in SaaS communities.

## Why This, Why Now

- Technical SEO problems are invisible to non-technical founders — they can see the traffic isn't coming but have no way to diagnose why without someone who knows where to look, making this one of the cleanest expertise-arbitrage opportunities in the folder.
- Free diagnostic tools (Search Console, PageSpeed Insights) make the free-sample hook unusually low-effort to produce with genuine data behind it — not a vague "your SEO could be better" but a specific "12 of your 80 posts aren't indexed" finding that only someone who knows to check can surface.
- Migration timing creates a predictable, recurring demand spike: every website redesign, CMS change, or domain migration is a guaranteed technical SEO event — and companies announce these publicly, making them a reliable prospecting trigger.
- The technical SEO audit is a gateway to ongoing work (implementation support, quarterly health checks) that is genuinely justified by the ongoing nature of site changes — a site that's technically healthy today can develop new issues from any CMS update, plugin change, or content migration, creating a natural recurring relationship.

## Risks / Open Questions

- **Google Search Console access is essential and requires client trust:** the highest-signal data for any technical audit comes from Search Console, which requires the client to grant you read access — position this early in the conversation as a requirement for a useful audit (not just nice to have), and be explicit about what you're accessing and why.
- **Technical fixes require developer implementation:** the audit produces specific, actionable instructions, but most fixes require a developer to implement — for clients without a developer, either scope implementation into the engagement (implementation support tier) or be explicit upfront that the audit deliverable is the findings and fix brief, not deployed changes; otherwise clients feel the audit didn't "do" anything.
- **Traffic improvement timelines are slow:** fixing technical SEO issues doesn't produce overnight traffic gains — Google re-crawls and re-indexes at its own pace, and meaningful traffic impact typically takes 4-12 weeks to appear after fixes are deployed. Set this expectation firmly upfront so clients don't judge success in the first 2 weeks.
- **Screaming Frog's 500-URL free limit:** sites with more than 500 pages (common for established content sites and e-commerce stores) require either a paid Screaming Frog license ($260/yr) or scoped crawling of the most critical site sections — account for this in scoping and price the audit accordingly for larger sites, or use the site migration audit pricing for complex, large-site engagements.

## Validation Signal to Watch

If the free-check findings (indexation gap + Core Web Vitals failure) consistently generate "I had no idea that was happening" responses, the diagnostic hook is surfacing genuinely novel, actionable information — the surprise is the signal. First concrete validation: a client who implements the prioritized fixes from the audit and sees a measurable indexation improvement in Search Console within 60 days — specifically the "Coverage" report showing previously excluded pages moving to "Indexed" status — that's the before/after screenshot that becomes the core case study for all future outreach.
