# PoC 06 — "Post Daily, Close Deals" — LinkedIn Ghostwriting + Inbound Lead-Gen Service for B2B Consultants/Coaches

**Date:** 2026-07-08
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Independent B2B consultants, coaches, fractional executives, and boutique agency owners know LinkedIn is where their buyers are, and know that consistent posting drives inbound leads — but they don't have time to write, don't know what to post, and stop after two weeks. This is a well-proven service category (LinkedIn ghostwriters routinely charge $1,000–$3,000/mo) with a clear, provable ROI story: more profile views → more inbound DMs → more discovery calls → more closed deals. Unlike a generic content-writing gig, you can tie your fee directly to lead volume, which makes the retainer easy to justify and easy to renew.

## Who It's For

Solo/small B2B service providers who sell high-ticket offers (consultants, coaches, fractional CFO/CMO/COOs, boutique agency founders, B2B SaaS founders doing their own sales) — anyone whose next client is plausibly one LinkedIn post away, and whose deal size ($3k+) makes even one extra closed deal per quarter worth far more than your fee.

## How It Makes Money

- Flat monthly retainer: $750–$2,000/mo for 3–5 posts/week + weekly content strategy + engagement/DM monitoring.
- Lower-cost entry tier ($400–$600/mo) for 2 posts/week, used as the low-friction first yes before upselling to full cadence.
- Lead-gen upsell once posting is working: proactive outbound commenting/engagement on target accounts' posts (positions the client in front of buyers directly) for an added $300–$500/mo.
- One-time "voice + strategy" onboarding fee ($200–$300) to extract their expertise, tone, and target-client profile before writing begins.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Onboarding call: extract the client's expertise, best client-facing stories/wins, target buyer profile, and tone preferences.
   - Draft posts manually using an LLM prompted with their voice profile + a rotating content framework (lesson-from-a-client-story, contrarian take, how-to breakdown, behind-the-scenes) — review and edit each draft before sending for client approval.
   - Deliver a batch of 5–10 drafts weekly via a shared Google Doc or Notion page for client sign-off, then post directly to their LinkedIn (either you post using shared access, or they copy/paste — start with the lower-trust copy/paste option for new clients).
2. **Software layer (build once 2–3 clients are live, funded by early retainer cash):**
   - Per-client voice/strategy config (same YAML pattern as this repo's `config.yml`) capturing tone, pillars, target audience, and example posts — feeds a consistent LLM prompt template instead of rewriting context each time.
   - Simple content calendar tracker (Airtable/Google Sheets) logging what's been posted, engagement metrics (likes/comments/profile views, pulled manually at first from LinkedIn's native analytics), and draft approval status.
   - Weekly automated digest script (reuse this repo's `discord_notify.py`/notification pattern) that reminds you which clients' drafts are due and surfaces the prior week's top-performing post to inform the next batch.

## Tools/Stack

- Claude/Gemini API for first-draft generation from each client's voice profile — near-$0 per post.
- Google Docs/Notion (free tier) for client-facing draft review and approval.
- Airtable/Google Sheets (free tier) for content calendar and performance tracking.
- LinkedIn's native analytics (free, built into any profile) for engagement/profile-view tracking — no paid tool needed to prove ROI.
- Stripe for recurring retainer billing.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Start with your own LinkedIn: post about the offer itself ("I'm ghostwriting LinkedIn content for 3 consultants right now — here's what's working") — this is inherently on-platform, credible, and self-demonstrating (you're proving the exact skill you're selling).
2. Identify 20–30 consultants/coaches in your network or extended network (LinkedIn search filtered by title + "helping X do Y" bio patterns) who post rarely or inconsistently despite clearly having expertise worth sharing — that inconsistency is your opener.
3. Free-sample hook: offer to write and send 2 free sample posts in their voice, unsolicited, as a DM opener — same pattern proven in PoC 01/02/05, adapted to this medium. A well-written sample in their actual voice is the strongest possible proof of skill.
4. Close on a low-commitment first month (month-to-month, no contract) at the lower entry tier to reduce the decision cost, then upsell cadence/scope once they see engagement lift.
5. Ask for a testimonial post (about your service, on their own LinkedIn) after the first month — this becomes your best acquisition asset for the next 5 clients, since it's proof delivered in the exact channel your next prospects are already watching.

## Time to First Dollar

- Day 1–2: identify 20–30 target prospects, draft 2 free sample posts each for the first 10.
- Day 3–5: send DM outreach with free samples attached.
- Day 5–10: close 2–3 clients on the entry tier ($400–$600/mo), collected via Stripe upfront.
- **First dollar within 1–2 weeks** — no build dependency; the entire MVP is a voice-extraction call and LLM-assisted drafting you can start today.

## Why This, Why Now

- Zero software build required to start selling — pure sales/writing skill on day one, software automation compounds later without gating revenue.
- Deal-size leverage: because clients sell high-ticket offers, the ROI math is extremely favorable (one extra $5k client from an inbound DM easily justifies a year of your fee) — this makes the retainer far stickier than a typical content-writing gig.
- LinkedIn's organic reach for individual profiles (vs. company pages) remains strong, and the platform actively favors consistent posters — timing favors this service structurally, not just opportunistically.
- Testimonials generated by the service are posted on the exact platform where your next prospects are looking, creating a compounding acquisition loop unique to this business.

## Risks / Open Questions

- **Client bottleneck on approvals:** if a client is slow to review/approve drafts, cadence slips and so does the ROI story — mitigate by batching a full week of drafts at once and setting a default-approve window (e.g., "posting Monday's draft unless I hear otherwise by Sunday").
- **Voice-matching quality is the actual product:** a generic-sounding post undermines the whole pitch — invest real time in the onboarding voice-extraction call rather than treating it as a formality.
- **Crowded category:** LinkedIn ghostwriting is well-known and has real competition — differentiate on the free-sample-in-their-actual-voice opener and the lead-gen (not just content) framing, since most competitors sell "content" rather than "inbound deal flow."
- **Access/trust for posting:** some clients won't want to share login access — default to a copy/paste handoff workflow for new clients and only offer direct-posting access once trust is established.

## Validation Signal to Watch

If 2+ of your first 10 free-sample DMs get a reply expressing genuine surprise/approval at how well the sample matches their voice, the core skill-fit is proven and worth scaling outreach volume. If samples consistently miss the mark on voice, invest more onboarding-call time before continuing outreach — a bad sample burns the relationship faster than no sample at all.
