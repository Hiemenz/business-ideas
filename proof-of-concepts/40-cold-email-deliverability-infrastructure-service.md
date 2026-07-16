# PoC 40 — "Your Cold Emails Are Going Straight to Spam" — Cold Email Deliverability Infrastructure Setup Service

**Date:** 2026-07-15
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Small B2B teams running outbound cold email campaigns routinely skip or misconfigure the technical infrastructure that determines whether their emails land in inboxes or spam folders — no SPF record, no DKIM signature, no DMARC policy, sending from their primary domain, using a single inbox for thousands of sends, no warm-up process. The result is deliverability rates that tank after the first few hundred sends (often destroying the reputation of their main business domain in the process) and sales teams blaming the messaging when the real problem is they're technically flagged as spam before anyone even reads the subject line. Every single one of these issues is fixable with proper DNS configuration, dedicated sending domains, inbox rotation, and a structured warm-up sequence — all of which requires technical knowledge that most sales/marketing teams at early-stage companies simply don't have, and that most agencies either don't offer as a standalone service or bundle into large monthly retainers the client doesn't need.

## Who It's For

Early-stage B2B startups and small sales teams (1-10 people doing outbound) who are running or about to run cold email campaigns — best entry point: teams actively setting up a cold outreach sequence for the first time, or teams who've noticed declining open rates and attribute it to "bad messaging" without realizing the problem is technical. Visible via sales-focused communities, SDR/BDR forums, startup Slack groups, or anyone posting "why are my cold emails going to spam?"

## How It Makes Money

- Flat setup fee: $300–$700 to configure the complete cold email sending infrastructure — dedicated sending domain(s) purchased and configured, SPF/DKIM/DMARC DNS records set, sending mailboxes created, warm-up tool connected and started, recommended sending limits documented, and a brief written SOP for the team covering what to never do to protect their deliverability going forward.
- Audit-only tier: $100–$200 for teams who already have infrastructure set up but aren't sure if it's correct — a full technical review of their current DNS records, domain reputation, blacklist status, and warm-up state, with a written findings report and prioritized fix checklist.
- Ongoing deliverability monitoring add-on: $75–$150/mo to watch domain reputation scores, blacklist status, and inbox placement rates monthly, flagging any emerging issue before it tanks an active campaign.
- Emergency rescue: $400–$800 for teams whose sending domain has already been blacklisted or flagged — full triage, new domain setup, migration of sequences, reputation recovery strategy.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Intake: gather the client's current sending setup (domain, email provider, sending volume, sequences running), then run a full technical audit using free tools (MXToolbox for DNS record validation and blacklist check, Google's MX Lookup, Mail-tester.com for a live inbox-placement test, dmarcian or similar for DMARC analysis — all free).
   - Identify every gap: missing or misconfigured SPF/DKIM/DMARC, sending from the primary domain, no warm-up, inbox overloaded, missing from/reply-to separation.
   - Configure fixes: register a dedicated sending domain (~$12/yr, billable to client or included in setup fee), configure DNS records step by step (all documented in standard syntax; provider-specific help docs exist for every major registrar/host), create sending mailboxes, connect a free-tier warm-up tool (Warmup Inbox, MailReach free tier, or Instantly's built-in warm-up on their lowest plan), set recommended daily sending limits, document the configuration in a handoff SOP.
2. **Software layer (build once 2–3 clients are live):**
   - Reusable DNS configuration checklist and exact record templates by sending provider (Google Workspace, Outlook/Microsoft 365, Zoho, FastMail) — built once, reused with minor per-client customization across every engagement, same scaffold-reuse pattern throughout this folder.
   - Automated audit script: a lightweight Python script using dns.resolver + requests against MXToolbox's API (free tier) to programmatically check all required DNS records and blacklist status for a given domain in under 30 seconds, producing a structured findings report — the kind of technical-differentiator tooling that makes the audit tier genuinely fast to deliver at volume.
   - Client tracking spreadsheet logging domain, setup date, warm-up start date, warm-up end date, and monthly deliverability check status for the monitoring tier.

## Tools/Stack

- MXToolbox, Google MX Lookup, Mail-tester.com, dmarcian (all free) for auditing and validation.
- Standard DNS registrar control panel (Namecheap, GoDaddy, Google Domains, Cloudflare DNS) — client typically already has one.
- Free-tier warm-up tools (Warmup Inbox, MailReach, or built-in via Instantly/Smartlead trial) for warm-up setup.
- Python + dns.resolver for the automated audit script (optional, build after first 2-3 paid engagements).
- Google Docs for the deliverability handoff SOP.
- Stripe/invoice for fee collection.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify prospects in sales/SDR communities (r/sales, r/coldemail, Slack groups for early-stage startups and sales teams) where "cold emails going to spam" and "open rates dropped to zero" are extremely common, frequent complaints — these are essentially self-identified, in-the-moment leads expressing exactly the pain this service solves.
2. Free-sample hook: for a prospect describing a deliverability problem, run a quick free check of their sending domain's DNS records and blacklist status (MXToolbox is instant and free), then reply with one or two specific, real findings: "Checked your domain — you're missing a DMARC record entirely and your SPF is using the wrong include syntax, both of which are likely contributing to the spam placement. Happy to walk through the full fix." A concrete, specific, immediately credible technical demonstration that takes under 5 minutes and is far more persuasive than any description of the service.
3. Warm intro via startup/founder networks: any founder or early sales hire you know personally who's running outbound is a natural first client — the service is invisible until it's working but immediately obvious when it isn't, making it easy to explain to a friendly contact in one sentence.
4. Sales tool/CRM communities (Apollo, Clay, Instantly, Smartlead user groups) are a natural venue — tools built for cold outreach attract exactly the buyer profile, and deliverability is a constant community topic in all of them.
5. A single documented "went from 8% open rate to 42% open rate after fixing infrastructure" before/after story (anonymous is fine) is a highly concrete, compelling case study for this exact community.

## Time to First Dollar

- Day 1–2: build the master DNS configuration checklist and free audit workflow using MXToolbox and Mail-tester; do a test audit on your own domain to verify the process end to end.
- Day 2–4: identify 15-20 prospects in sales/outbound communities actively complaining about deliverability, run free quick-checks on their public sending domains.
- Day 4–7: send outreach with the specific finding attached as the opener.
- Day 7–12: close 2–3 clients on the flat setup fee ($300–$700), collected upfront; deliver each setup within 1-2 hours of payment since the DNS configuration work is fast once the process is documented.
- **First dollar within 1–2 weeks** — the entire audit and setup process uses free tools, takes 1-3 hours per engagement once practiced, and the prospect pool actively and publicly identifies themselves.

## Why This, Why Now

- Pure technical knowledge gap in a non-technical buyer population — the people running cold email campaigns (SDRs, sales ops, growth marketers) are rarely the people who know how DNS records work, creating a genuine, clean arbitrage between what it costs you to do this and what it's worth to them.
- Dramatically faster value delivery than most services in this folder: a complete setup is 1-3 hours of focused work, deliverable same day, with a visible, measurable result (inbox placement test goes from "spam" to "inbox") the client can verify themselves immediately after handoff.
- The free-sample hook (instant DNS audit using free tools) is unusually low-friction and high-signal — it takes 5 minutes to generate a genuine, specific finding for any prospect with a public sending domain, making it the most concrete and personal possible demonstration of competence.
- No recurring tool cost to you — every audit tool used is free, and the only out-of-pocket expense per engagement is the dedicated sending domain (~$12, billable to client).

## Risks / Open Questions

- **Warm-up takes time regardless of configuration correctness:** even a perfectly configured new domain needs 3-6 weeks of warm-up before it can send at meaningful volume — set this expectation clearly and early so clients don't blame the setup when they can't immediately send 500/day from a brand-new domain.
- **DNS propagation delays:** DNS record changes take time to propagate (minutes to 48 hours depending on TTL settings and provider), meaning the setup isn't instantly verifiable — walk clients through what to check and when to expect full propagation rather than leaving them uncertain about whether it worked.
- **Not a solution for fundamentally broken content or targeting:** deliverability infrastructure is necessary but not sufficient — if the emails are going to spam because the content is flagged (spam trigger words, misleading subject lines, purchased lists with spam traps), no amount of DNS configuration fixes that. Be explicit that this service solves the technical infrastructure layer, not copy quality or list hygiene — which are distinct, separately addressable problems.
- **Domain reputation is fragile and client behavior matters post-setup:** a perfectly configured infrastructure can be ruined quickly if the client ignores the sending-limit SOP and blasts 1,000 emails/day from a brand-new domain in week one. The handoff SOP and explicit "don't do this" guidance are as important as the technical configuration itself.

## Validation Signal to Watch

If your free quick-audits consistently surface real, specific findings for the prospects you check (a strong signal the problem is genuinely common and undiscovered), and 2+ of your first 8-10 outreach messages with a real finding generate a reply, the hook is working — scale into the sales/outbound tool communities where this buyer concentrates, and begin building the automated audit script to speed up the free-check step so you can run more per hour. If clients frequently want help beyond infrastructure (copy review, list sourcing), note that as a natural expansion path rather than scope-creeping the current engagement.
