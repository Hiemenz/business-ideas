# PoC 56 — "We've Been Meaning to Run a Webinar for Six Months" — Webinar Production & Ops Service

**Date:** 2026-07-18
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

B2B companies — SaaS businesses, agencies, consultancies, professional services firms — consistently identify webinars as a high-intent lead generation channel and consistently fail to execute them. Not because they don't have the expertise to present or the audience to invite, but because the operational complexity of actually running a webinar is distributed across a dozen small tasks nobody owns: setting up the registration page, configuring the streaming platform, writing the promotional email sequence, managing the live event tech (slides handoff, Q&A moderation, recording), sending the replay and follow-up sequence, and repurposing the recording into clips and a transcript. Each individual task is straightforward; the combined project management of all of them is what perpetually gets deprioritized. A webinar production specialist who owns the entire operational layer — so the presenter just shows up and presents — removes the only real barrier between a company that wants to run webinars and one that actually does. This is explicitly distinct from PoC 12 (podcast repurposing, which takes existing recorded audio content and repurposes it into derivative assets) — this is the live event production and operational management layer, from registration page to post-event follow-up, for events that haven't happened yet.

## Who It's For

B2B SaaS companies, agencies, and professional services firms with a genuine topic expertise and an existing email list or social audience to promote to — companies that have said "we should do a webinar" multiple times but haven't shipped one, or companies that ran one webinar poorly (bad tech setup, no follow-up, no replay) and need someone else to own the ops to run them consistently. Best entry points: companies actively doing content marketing who've discussed webinars as the next channel, companies preparing for a product launch where a live demo webinar would accelerate the pipeline, or marketing teams that have budget for lead generation but limited internal bandwidth to execute.

## How It Makes Money

- Per-webinar production fee: $500–$1,000 to produce a single webinar end-to-end — registration page setup (Zoom Webinar, StreamYard, or Demio free/trial tier), promotional email sequence (3 emails: save the date, reminder, day-of), live event tech management (host the session, manage slides and screenshare, run Q&A, record), and post-event sequence (replay email, follow-up nurture email, registration-to-attendee conversion report).
- Webinar series package: $1,200–$2,500 for a 3-webinar series produced on a monthly cadence — the most common real need, since a single webinar rarely produces enough data or pipeline to justify the investment, but a consistent quarterly series builds audience and compound value.
- Webinar-to-content repurposing add-on: $200–$400 per webinar to produce 5-7 short video clips (60-90 seconds, captioned, sized for LinkedIn/Twitter), a written transcript summary formatted as a blog post, and a key-takeaways email to send to registrants who didn't attend — drawing on the same repurposing skill from PoC 12 but applied to webinar recording rather than podcast audio.
- Webinar program setup: $400–$700 one-time to build the reusable webinar infrastructure for a company that wants to run webinars on their own going forward — registration page template, email sequence templates, speaker briefing document, run-of-show template, and a checklist the team uses for every future event without needing additional ops support.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Scoping call (30 min): establish the topic, presenter(s), target audience, date/time, expected registrant volume, and which platform the client already has access to (Zoom, Google Meet, StreamYard — all have free tiers sufficient for an initial webinar).
   - Build the registration page using Zoom Webinar's built-in registration (included in Zoom Pro, which most companies already have) or a free Luma/Eventbrite registration page if they're on Zoom Basic — no new tool purchase required in the vast majority of cases.
   - Write the 3-email promotional sequence (save the date with topic hook and registration link, 7-day reminder with social proof or agenda preview, day-of reminder with join link) using an LLM prompted with the webinar topic, target audience, and the single most compelling reason to attend.
   - On event day: join 30 minutes early as tech host, manage the recording start, admit attendees, monitor chat, run Q&A in the final 10 minutes, and confirm the recording is captured before ending.
   - Post-event: send the replay email (within 24 hours), pull the attendee vs. registrant report from the platform, and deliver a brief performance summary (registrants, attendees, attendance rate, Q&A questions asked — the 5 metrics that tell the client whether the webinar worked).
2. **Software layer (build once 2–3 clients are live):**
   - Reusable run-of-show template: a minute-by-minute event timeline covering pre-event tech check, attendee admission, welcome and housekeeping, main content, Q&A, close and CTA, and recording wrap — built once and customized per event in under 20 minutes.
   - Email sequence template library by webinar type (product demo, thought leadership, customer panel, how-to tutorial) — the promotional framing and follow-up CTA differ meaningfully by webinar type; having pre-built templates per type makes each new engagement's email sequence fast to adapt.
   - Post-event report template: a clean Google Doc pulling the 5 key metrics (registrants, attendees, attendance rate, peak concurrent viewers, Q&A engagement) plus 3-5 notable attendee questions — built once and replicated per event as the standard deliverable.

## Tools/Stack

- Zoom Webinar or Google Meet (clients almost always already have access — no new purchase required for the first several engagements).
- Luma or Eventbrite free tier as a registration page alternative if the client doesn't have Zoom Webinar.
- StreamYard free tier (up to 2 participants, branded stream) for clients who want a more polished broadcast-style production.
- Claude/Gemini API for promotional email sequence writing and post-event summary drafting.
- Descript or CapCut free tier for the repurposing clip add-on.
- Google Docs for run-of-show, speaker briefing, and post-event report delivery.
- Stripe/invoice for fee collection.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify prospects in B2B marketing and SaaS communities (r/marketing, r/SaaS, B2B marketing Slack groups, Indie Hackers) where "we want to run webinars but haven't started" and "we tried one webinar and the ops were a disaster" are recurring expressions — both are direct signals of the exact problem this service solves.
2. Free-sample hook: for a prospect who mentions wanting to run a webinar, produce a complete webinar run-of-show template and 3-email promotional sequence for their stated topic at no charge: "If you're planning a webinar on [topic], here's the run-of-show and email sequence I'd use — take it and run it yourself, or let me produce it for you." A concrete, complete, immediately usable deliverable that takes 45 minutes to produce and demonstrates operational depth rather than just claiming it.
3. Product launch timing is an exceptionally strong prospecting trigger: any company that announces a new product, feature, or major update is a natural candidate for a launch webinar — proactive outreach immediately after a product announcement ("a live demo webinar would be a strong way to convert the interest from this announcement into pipeline — happy to produce it end-to-end") has unusually precise timing and a clear, immediate application.
4. Marketing agencies that produce content strategies for clients but don't have webinar production capacity are strong referral partners — they regularly recommend webinars as part of a content strategy and immediately need someone to produce them when the client says yes.
5. A "ran first webinar, 340 registrants, 52% attendance rate, 18 qualified pipeline conversations booked in the 2 weeks after" result (specific numbers from a real engagement) is immediately compelling to any B2B marketing leader who's been measuring webinar ROI in those terms.

## Time to First Dollar

- Day 1: set up test Zoom Webinar registration, write a sample 3-email promotional sequence for a fictional webinar topic to validate the LLM prompt chain and template structure; build the run-of-show template.
- Day 2–3: identify 15-20 B2B companies in communities expressing webinar intent or facing product launches; prepare the free run-of-show + email sequence for the 8-10 most specific topics mentioned.
- Day 3–6: send the free deliverable with the production offer.
- Day 6–12: close 2–3 clients on the per-webinar fee ($500–$1,000), collected upfront; begin registration page and email sequence setup within 48 hours of payment.
- **First dollar within 1–2 weeks** — no tool costs since clients typically have Zoom already, the free deliverable takes under an hour to produce per prospect, and the product-launch trigger creates recurring, predictable prospecting opportunities from public announcements every week.

## Why This, Why Now

- Webinar ops is a project management and technical coordination problem masquerading as a content problem — companies think they need to "figure out webinars" when what they actually need is someone to own the operational layer so they can focus on what they're already good at (the expertise and the audience relationship).
- Product launch triggers make prospecting self-populating: every week there are dozens of B2B companies publicly announcing new products or features who are natural, immediately relevant webinar production prospects — no effort required to find them, just attentiveness to product announcement channels.
- The free deliverable (run-of-show + email sequence) is fully reusable for the prospect even if they don't hire for production — making it a genuinely useful gift rather than a thinly veiled pitch, which creates goodwill and makes the "let me just produce it for you" conversation feel like a natural offer rather than a sales pressure.
- Webinar series packages ($1,200–$2,500 for 3 events) create meaningful per-client revenue quickly, and the repeat engagement structure (same client, same setup, 3 events) makes each subsequent event faster to produce as familiarity with the client's tools, audience, and style builds.

## Risks / Open Questions

- **Date and time commitments require reliable availability:** webinar production involves being live on a specific date and time — unlike most services in this folder where delivery is asynchronous, a missed tech-host commitment the day of a live event is a serious client relationship failure; be conservative about how many concurrent webinar production commitments to hold at once.
- **Platform access and tech variability:** different clients use different webinar platforms with different features, quirks, and admin access flows — build in a mandatory 30-minute platform tech check 48 hours before every event to catch access or feature issues before the day of, not during it.
- **Registrant volume is the client's responsibility:** production ops doesn't generate the audience — the client's email list, social presence, and promotional effort determine how many people show up. Set clear expectations that production manages the technical and operational layer; promotion volume is the client's variable, not yours.
- **Recording and replay rights:** some webinar topics involve guest speakers or third-party content — confirm recording and replay distribution rights before the event, particularly for customer panel webinars where multiple parties' consent matters.

## Validation Signal to Watch

If the free run-of-show and email sequence deliverables consistently generate "this is exactly what we needed — we just needed someone to put this together" reactions, the ops-gap diagnosis is correct and the free sample is hitting the right need. The strongest production-specific validation: a client who runs their first webinar with your production support, achieves an attendance rate above 40% (the industry benchmark), and immediately books the next event — that repeat booking without additional sales effort is the clearest possible signal the service is delivering real, felt value.
