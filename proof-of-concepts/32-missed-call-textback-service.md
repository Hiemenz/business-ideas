# PoC 32 — "Every Missed Call Is a Lost Customer" — Missed-Call Text-Back & Lead Capture Service for Local Businesses

**Date:** 2026-07-13
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Local service businesses (plumbers, HVAC, salons, auto shops, contractors) lose real revenue every time a call goes unanswered — busy with a customer, out on a job, after hours — because most callers who hit voicemail simply hang up and call the next business on the list instead of leaving a message. The fix is well-proven and simple: the instant a call is missed, an automated text immediately goes out ("Sorry we missed your call! What can we help with?"), which captures a huge share of callers who would otherwise have been lost, since replying to a text is far lower-friction than leaving and waiting on a voicemail. This exact category exists at the enterprise level (Podium, similar tools bundle this into larger, expensive packages), but a lean, standalone version of just this one feature is easy to build and sell on its own, distinct from PoC 14's website chatbot (this captures phone-based leads, not web visitors) and PoC 01 (this happens at the moment of missed contact, not after a review is left).

## Who It's For

Local service businesses that take a meaningful volume of inbound calls and are often unable to answer immediately (tradespeople who are frequently on job sites, salons/clinics where staff are often with a client, single-location shops with limited staff) — an easily identifiable, broad local-business pool, especially those without an existing answering service or receptionist.

## How It Makes Money

- Monthly service fee: $75–$200/mo per business phone line — genuinely low-cost to deliver at scale (SMS/telephony API costs are cents per interaction) and structured, like PoC 29, as recurring revenue from the first sale rather than needing a separate upsell motion.
- Setup fee: $50–$150 one-time to configure call forwarding/tracking and the auto-text sequence — a natural first invoice alongside the recurring signup.
- Lead-routing upsell: a higher tier that also logs captured leads into a simple shared spreadsheet/CRM view and sends a daily summary, turning raw text replies into an organized, actionable lead list rather than just a phone inbox.
- Multi-location package for small local chains: bundled per-line pricing for businesses managing several locations from one lead-capture setup.

## MVP — Buildable in Days, ~$0-Low Cost

1. **Week 1, minimal setup:**
   - Set up a business SMS/voice number using a telephony API (Twilio's free trial credit covers substantial initial testing and early low-volume client usage before ongoing costs, which remain cents per text/call even at real scale) and configure call forwarding or a simple missed-call webhook from the client's existing number.
   - Configure an automated text sent immediately on any missed/unanswered call, with a friendly, on-brand opening message and a simple prompt for what the caller needs.
   - Route replies to a shared inbox/notification (even just forwarding to the business owner's own phone/email) so they can respond directly and continue the conversation.
2. **Software layer (build once 1-2 clients are live, funded by early setup fees):**
   - Simple script/webhook handler (using Twilio's API, consistent with a lightweight Python backend pattern) that detects a missed call event and triggers the auto-text — this is genuinely core, necessary software work from day one, not a later automation layer, since the entire service depends on this working reliably.
   - Lead-logging integration (a simple database/spreadsheet write on each captured lead) for the lead-routing upsell tier, giving clients a running list rather than just individual text threads.
   - Reusable auto-text template library by business type (a plumber's message differs slightly from a salon's) so each new client setup is a quick configuration exercise rather than custom-built each time.

## Tools/Stack

- Twilio (or similar telephony API) for SMS/call forwarding and missed-call detection — free trial credit covers initial build/testing, ongoing costs remain low (cents per interaction) even at scale.
- A simple Python backend (consistent with this repo's existing tooling patterns) to handle the missed-call-to-text-trigger logic, hosted on a free-tier platform (Render, Railway) for low traffic volume.
- Claude/Gemini API optionally for drafting business-specific auto-text copy variations.
- Google Sheets or Airtable for the lead-routing upsell tier's captured-lead log.
- Stripe for recurring monthly billing.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify prospects among local service businesses (trades, salons, single-location shops) via the same local-business channels used in PoC 01/10 (Google Maps search by category, local Facebook/Nextdoor groups) — a broad, easily-found pool, especially field-service businesses where staff are frequently away from the phone.
2. Free-sample hook: call the prospect's business number yourself during a plausible busy period (or simply note if a call to them goes unanswered/to voicemail) and use that as a direct, honest opener: "Called your business earlier and it went to voicemail — how many calls like that do you think go to a competitor instead? I can fix that for about $100/mo." A concrete, personally-verified finding rather than a hypothetical pitch.
3. Trade associations and local contractor/service-business networking groups are strong venues, since missed-call loss is a widely (if quietly) acknowledged pain in exactly these industries.
4. Position the ROI math simply and concretely: "if this captures even one extra job a month, it pays for itself many times over" — an easy, intuitive calculation for a trades/service business owner to do in their head.
5. A single "captured a $2,000 job from a call we would've otherwise lost" story is a highly persuasive, concrete case study for these communities, where word travels fast among business owners who know each other.

## Time to First Dollar

- Day 1–3: identify 15-20 local service business prospects, personally test-call a subset during business hours to identify genuine missed-call cases.
- Day 3–5: send outreach with the personally-verified missed-call finding as the opener.
- Day 5–10: close 2–3 clients on the setup fee plus monthly retainer, collected via Stripe with the recurring fee starting immediately.
- **First dollar within 1–2 weeks**, with recurring revenue starting the same cycle — similar to PoC 29, this is structured as a subscription offer from the first sale, not a one-time-project-then-upsell motion.

## Why This, Why Now

- Low, manageable build cost (a Twilio trial plus a simple webhook script) delivers the actual core service from day one — this is one of the few ideas in the folder requiring genuine, necessary software infrastructure upfront rather than pure manual/research work, giving a clear technical specialization story.
- Structured as recurring revenue from the very first sale, like PoC 29, directly building durable MRR rather than requiring a separate retainer-conversion step.
- Extremely concrete, intuitive ROI story ("one recovered job pays for months of the service") that requires zero buyer education, especially for trades/service businesses used to thinking in terms of job value.
- The free-sample hook (personally testing whether a call goes unanswered) is honest, cheap to produce, and creates a genuinely persuasive, first-person-verified opener rather than a generic pitch.

## Risks / Open Questions

- **Reliability is critical:** since the entire value proposition depends on the auto-text firing reliably every time a call is missed, thorough testing before going live with each client is essential — a missed trigger undermines the whole pitch immediately.
- **Telephony/compliance considerations:** SMS marketing/messaging carries some regulatory considerations (opt-in/consent norms, carrier registration requirements for business messaging at scale) — start with low-volume, direct-response use cases (replying to an inbound missed call, not proactive marketing blasts) which sit on much safer regulatory ground, and be aware of carrier registration requirements as volume grows.
- **Setup complexity varies by client's existing phone system:** call forwarding configuration is straightforward for some setups and more involved for others (multi-line systems, existing VoIP providers) — confirm the client's phone setup during the sales conversation before quoting a simple flat setup fee.
- **Ongoing telephony costs scale with usage:** at high call volume, per-message/per-minute costs could erode margin on the flat monthly fee — monitor unit economics as client call volume grows and adjust pricing tiers if a particularly high-volume client's usage costs approach the flat fee.

## Validation Signal to Watch

If 3+ of your first 10 outreach messages (each with a personally-verified missed-call finding) generate a reply, the hook is landing — scale outreach across more local trade/service categories. If early clients report captured leads/jobs directly attributable to the auto-text within the first month, that becomes a strong, concrete proof point for both retention and future outreach; if capture rates are lower than expected, review and refine the auto-text copy and response-routing setup before assuming the underlying concept needs rework.
