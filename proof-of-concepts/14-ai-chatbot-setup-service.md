# PoC 14 — "Answer Every Question, Even at 2AM" — AI Chatbot/FAQ Setup Service for Small Business Websites

**Date:** 2026-07-09
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Small businesses (local service providers, e-commerce shops, course creators, small SaaS companies) field the same repetitive questions over and over via email, phone, and DM — hours, pricing, availability, return policy, how something works — and either lose leads because no one answers fast enough outside business hours, or burn owner/staff time on questions that don't need a human. LLM-powered chatbots that answer from a business's own FAQ/docs are now cheap and fast to build, but most small business owners have no idea this is accessible to them at a reasonable price — they associate "AI chatbot" with enterprise tools or assume it requires a dev team. This is a build-and-deploy service, distinct from the research/audit/content services elsewhere in this folder: the deliverable is a working piece of software installed on the client's actual website, which is a highly tangible, demo-able product.

## Who It's For

Small businesses with a website that gets real traffic and repetitive inbound questions: local service businesses (spas, gyms, clinics), small e-commerce stores, course/coaching businesses, and small SaaS/software companies without a dedicated support team. Best entry point: businesses that already show signs of support overload — slow email response times (testable by simply emailing them a question and timing the reply), or a visible support/contact backlog.

## How It Makes Money

- Flat setup fee: $300–$800 to build and install a custom chatbot trained on the client's FAQ, product pages, and policies — priced by scope (a simple FAQ bot is cheaper than one integrated with booking/order-status lookups).
- Monthly hosting/maintenance retainer: $50–$150/mo covering LLM API costs, content updates as the business's offerings change, and monitoring for bad/incorrect answers — this is the natural recurring hook, framed honestly as "the AI needs upkeep as your business changes," not as an arbitrary fee.
- Advanced integration upsell: connecting the bot to live data (order status, appointment availability, inventory) rather than just static FAQ content — a meaningfully higher-ticket project fee ($500–$2,000) for clients who see clear value from the base version first.
- Lead-capture upsell: configure the bot to collect contact info from visitors it can't fully help, routing warm leads to the business — turns a cost-avoidance tool into a lead-generation tool, strengthening the retainer's renewal case.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, minimal code:**
   - Client shares their FAQ page, policies, and key product/service info (or you scrape it directly from their public website with permission).
   - Build a simple chatbot using an LLM API with the client's content as context (retrieval-augmented prompting: search the client's content for relevant sections, feed them into the prompt alongside the user's question) — this is a well-established, lightweight pattern that doesn't require a complex vector database at small scale; a simple keyword/section-matching approach over a modest FAQ document works fine to start.
   - Embed via a simple chat widget (a small HTML/JS snippet the client adds to their site, or a no-code embeddable chat tool free tier as a faster starting point before building custom).
   - Test thoroughly against real likely customer questions before going live, and set a clear fallback ("I'm not sure — here's how to reach a human") for anything outside its training content to avoid confidently wrong answers.
2. **Software layer (build once 2–3 clients are live, funded by early setup fees):**
   - Reusable chatbot scaffold (same LLM-call + context-retrieval pattern each time) so new client setups become a configuration exercise (swap in their FAQ content) rather than building from scratch — directly reuses this repo's existing pattern of structured prompt-building (`build_prompt` in `gemini_client.py`) applied to a new use case.
   - Simple admin view (even just an editable Google Doc/Airtable feeding the bot's content) so clients can flag wrong answers or request content updates without needing you for every small change.
   - Basic analytics logging (what questions are asked, which ones the bot couldn't answer) to identify content gaps and demonstrate value in monthly retainer check-ins.

## Tools/Stack

- Claude/Gemini API for the chatbot's response generation.
- Simple retrieval approach over the client's FAQ/docs (no complex infrastructure needed at small business scale).
- Lightweight embeddable chat widget (a small custom JS snippet, or a free-tier no-code chat widget tool as a faster MVP starting point).
- Basic hosting for the bot's backend (free-tier options like Render, Railway, or Vercel functions handle low-traffic small business volume comfortably).
- Stripe for setup fee and recurring retainer billing.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify prospects by testing their current responsiveness: email or DM a real question to 15-20 local businesses/small e-commerce sites and time how long it takes to get a reply — slow or no response is a direct, provable pain signal you can reference in outreach.
2. Free-sample hook: build a working demo chatbot using only their publicly available FAQ/website content (no client input needed to build a rough version) and send them a link to try it: "Built this off your public FAQ page — it can answer customer questions instantly, even at 2am. Want me to refine and install it on your site?" This is one of the strongest possible free-sample hooks in this folder, since the prospect can interact with a working product immediately rather than reading a written report.
3. Local business Facebook/Nextdoor groups and small business owner communities are good outreach venues, especially framed around the "never miss a lead outside business hours" angle rather than the more abstract "AI chatbot" framing.
4. E-commerce-specific communities (Shopify forums/groups) are a strong adjacent channel to PoC 05 — the same store owners who care about conversion rate optimization also care about reducing support burden and capturing after-hours leads.
5. Once installed, ask the client to share their bot on social media as a "look what we added" post — small businesses like showcasing modern touches to their customers, which doubles as a passive advertisement for your service.

## Time to First Dollar

- Day 1–3: identify 15-20 prospects via responsiveness testing, build free working demo bots for the 8-10 most promising using only public website content.
- Day 3–6: send outreach with the live demo link attached.
- Day 6–11: close 2–3 clients on the setup fee ($300–$800), collected upfront, plus recurring retainer starting the following month.
- **First dollar within 1–2 weeks** — build time per demo is short since it's reusing the same scaffold each time, and the demo itself requires no client cooperation to produce.

## Why This, Why Now

- Most concretely demo-able free sample of any idea in this folder — a working, interactive product beats a written report or screenshot for immediate persuasive impact.
- Directly and heavily plays to software/technical skill — this is the most build-intensive service in the folder, giving you a genuine specialization story ("I build and install AI chatbots for small businesses") that's easy to describe and remember.
- LLM API costs at small-business traffic volume are genuinely near-$0, meaning the ongoing retainer is close to pure margin once the scaffold is built.
- "AI chatbot" is a category small business owners have heard of but assume is out of reach — being the person who makes it concretely accessible and affordable is a clear market gap, not a saturated pitch.

## Risks / Open Questions

- **Wrong-answer risk:** a chatbot confidently giving incorrect information (wrong pricing, wrong policy) can create real problems for the client — build a conservative fallback behavior (defer to a human for anything uncertain) and test extensively before going live, and be transparent with clients about this limitation upfront.
- **Content maintenance is an ongoing dependency:** the bot's quality decays if the client's FAQ/offerings change and the bot's content isn't updated — the retainer needs to genuinely include this upkeep, not just be a fee for hosting.
- **Client technical comfort varies:** installing a JS snippet is trivial for some site platforms (Shopify, WordPress) and more involved for others (custom-built sites) — confirm platform compatibility during the sales conversation before quoting, and factor extra install complexity into the fee for non-standard platforms.
- **Competitive category:** numerous no-code chatbot tools exist for small businesses to self-serve — differentiation has to come from the done-for-you setup, the free working demo as proof, and genuinely responsive human maintenance, not from claiming to have invented a new category.

## Validation Signal to Watch

If 3+ of your first 10 demo-link outreach messages get a reply expressing genuine interest or surprise at how well the demo works, the hook is proven and worth scaling. If demo interactions reveal the free-demo bots frequently give poor/irrelevant answers even on public FAQ content, invest more time refining the retrieval/prompting approach before continuing outreach — a broken free demo actively damages the pitch rather than just failing to help it.
