# PoC 17 — "Get Paid What You're Owed" — Late Invoice Collections for Freelancers & Small Agencies

**Date:** 2026-07-10
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Freelancers, consultants, and small agencies routinely have unpaid or overdue invoices sitting for 30, 60, 90+ days — not because the client won't ever pay, but because the freelancer hates the awkwardness of chasing money and lets it slide, or sends one polite reminder and gives up. This is money that already belongs to them, sitting uncollected purely due to an avoided-conversation problem, not a legal or product dispute. Traditional collections agencies exist but are built for larger B2B debt and often damage the client relationship; what's missing is a firm-but-professional, done-for-you follow-up service sized for freelancer/small-agency invoice amounts ($500-$15k range). This is the mirror image of PoC 02 (overcharge auditing recovers money wrongly paid out) — here you recover money rightly owed but never collected, using the same contingency-pricing, zero-buyer-risk structure that's proven to close easily throughout this folder.

## Who It's For

Freelancers, consultants, small creative/marketing/dev agencies, and solo contractors with at least one invoice 30+ days overdue — an extremely common and almost universally embarrassing-to-discuss situation, making this an easy problem to surface once you ask directly rather than something prospects volunteer unprompted.

## How It Makes Money

- Contingency fee only (primary model, maximizes conversion): 15-25% of any amount successfully collected — the freelancer pays nothing if nothing is recovered, removing all buyer risk, mirroring PoC 02's structure exactly.
- Flat "collections sequence setup" fee alternative: $150–$300 to write and hand off a proven escalating follow-up sequence the freelancer sends themselves, for those who want to keep it in-house but need the words/structure.
- Ongoing AR (accounts receivable) management retainer: $150–$400/mo for freelancers/agencies with recurring client relationships and a steady trickle of new invoices, where you proactively follow up on anything crossing the 15-day-overdue threshold before it becomes a bigger problem.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Client shares the overdue invoice details (amount, due date, client contact, any prior communication) and grants permission to follow up on their behalf, either from their own email (cc'd/bcc'd to you) or from you directly identifying yourself as handling their AR.
   - Run an escalating sequence: a professional first reminder, a firmer second touch after 5-7 days referencing the original agreement/invoice terms, and a final notice outlining next steps (late fees if applicable, pause of future work, or formal next steps) if unpaid after a defined window — using an LLM to draft each stage's tone precisely (firm but professional, never hostile) then reviewing before sending.
   - Track responses and payment status manually; once paid, invoice the freelancer for your contingency percentage.
2. **Software layer (build once 2–3 clients are live, funded by early recovered-fee income):**
   - Reusable escalation-sequence templates by scenario (unresponsive client vs. client disputing scope vs. client citing cash flow issues) so each new case starts from a refined playbook rather than being drafted from scratch — same reusable-template pattern used throughout this folder.
   - Simple case tracker (Airtable/Google Sheets) logging invoice amount, days overdue, sequence stage, and outcome per case — both for managing multiple simultaneous cases and as a track-record stat ("recovered $X across Y cases") for marketing.
   - Automated reminder scheduling (a simple scheduled script, consistent with this repo's cron-driven pattern) to trigger the next escalation stage automatically if no response is received by the deadline, rather than manually tracking every case's timing.

## Tools/Stack

- Email (client's own account, cc'd, or a dedicated collections email identity) — no paid tooling required.
- Claude/Gemini API for drafting each escalation stage's message, tuned for a firm-but-professional tone.
- Airtable/Google Sheets (free tier) for case tracking.
- Simple scheduled script for automated reminder timing once volume justifies it.
- Stripe/invoice for your own contingency fee collection once the client's invoice is paid.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Freelancer and consultant communities (Indie Hackers, freelance-specific Slack/Discord/Facebook groups, subreddit communities for freelancers) are dense with people who openly complain about clients who won't pay — a direct, self-identifying pain signal you can respond to immediately.
2. Free-sample hook: offer to review one overdue invoice's history and draft the next follow-up message for free, unsolicited, in response to someone publicly venting about a non-paying client — a small, immediately useful gesture that naturally leads into the full offer.
3. Position the contingency-only pricing prominently: "I only get paid if you get paid" is one of the easiest possible pitches in this entire folder, since there's no rational reason for a freelancer with a genuinely overdue invoice to decline free-to-try help.
4. Local freelancer/small-agency networking events and coworking spaces are a strong in-person venue, since this is a near-universal shared frustration that comes up naturally in conversation.
5. A single successful recovery story ("got a freelancer $4,200 that had been sitting unpaid for 4 months") is a highly relatable, shareable case study within freelancer communities — this niche talks to itself constantly about exactly this problem.

## Time to First Dollar

- Day 1–3: identify 15-20 freelancers/small agencies via community posts or direct network outreach who have a visibly overdue invoice situation.
- Day 3–5: offer free draft-message help to the first 8-10, converting genuine engagement into full contingency-based cases.
- Day 5–14: run escalation sequences on 3–5 active cases; contingency fee is earned only once the client's invoice is actually paid, so timing depends on how quickly the debtor responds to a professional follow-up (often faster than the freelancer expects, since a structured, non-emotional sequence frequently succeeds where an avoided, awkward personal follow-up failed).
- **First dollar within 1-3 weeks** — faster cases (a debtor who simply forgot or was waiting to be asked firmly) can resolve within days of the first professional follow-up; harder cases take longer, so prioritize cases with a clear paper trail (signed agreement, clear invoice, no scope dispute) for your first close-fast wins.

## Why This, Why Now

- Zero build required to start — this is pure communication/negotiation skill, directly playing to sales/ops strength, with software automation as a pure scaling layer added later.
- Contingency-only pricing is about as close to a risk-free yes as any offer in this folder — there's essentially no downside for a freelancer to say yes once you've demonstrated real skill with a free sample message.
- The underlying problem (avoided, awkward money conversations) is near-universal among freelancers and independent contractors, and it's evergreen rather than tied to any particular market condition or season.
- Recovered amounts can be substantial relative to your time investment — a single $5k invoice recovery at a 20% contingency fee is a meaningful single-case payout for what's often just a few well-crafted emails and some patient follow-through.

## Risks / Open Questions

- **Not all non-payment is a communication problem:** some cases involve genuine scope disputes, dissatisfaction with delivered work, or the debtor's real inability to pay — screen cases during intake to prioritize those with clear agreements and no legitimate dispute, since those are both faster to resolve and less likely to damage your reputation if they don't succeed.
- **Reputation risk to the freelancer's client relationship:** since many freelancers want to preserve the relationship (especially if it's an ongoing client), tone calibration matters enormously — always confirm with the freelancer upfront how aggressive they're comfortable with the sequence becoming.
- **No collection means no fee:** contingency-only pricing means dry spells are possible if you take on several hard cases in a row — the flat "sequence setup" fee alternative exists partly to smooth cash flow during ramp-up rather than relying entirely on contingency outcomes.
- **Legal boundary awareness:** this should stay within the bounds of assertive-but-professional business communication, not formal collections/debt-collection-agency activity, which carries separate regulatory requirements (e.g., FDCPA-type rules in some contexts) — keep the positioning as "AR follow-up assistance," not a licensed collections agency, and avoid threats or language a real collections agency would need specific licensing to use.

## Validation Signal to Watch

If 2+ of your first 8-10 free-sample draft messages lead to a genuine "yes, please help with the full thing" response, the pitch and skill-fit are validated — scale outreach into freelancer communities more broadly. If early contingency cases are taking far longer to resolve than expected, tighten your intake screening to prioritize only the clearest, most straightforward non-payment situations until you've built a track record and refined the escalation sequence templates.
