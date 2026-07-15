# PoC 21 — "Your Website Could Get You Sued" — ADA/WCAG Accessibility Audit & Fix Service for Small Business Websites

**Date:** 2026-07-11
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Website accessibility lawsuits (under the ADA in the US, and similar regulations elsewhere) targeting small and mid-size businesses have grown steadily — plaintiffs' firms actively scan sites for common accessibility failures (missing alt text, poor color contrast, unlabeled form fields, keyboard-navigation traps) and send demand letters, often for $5k-$25k+ in "damages" and legal fees, before a lawsuit is even filed. Most small business owners have never heard of WCAG guidelines and have zero visibility into whether their site is a target. This is distinct from every other service in this folder: the driving emotion isn't "make more money" or "save time," it's genuine legal-risk avoidance, which tends to convert faster and at a higher perceived-urgency level than an efficiency pitch — and unlike most legal-risk services, the diagnostic work itself is highly automatable with free, publicly available scanning tools.

## Who It's For

Small-to-mid businesses with a public-facing website that handles any transactions or has any real traffic (e-commerce stores, restaurants with online ordering, service businesses with booking forms, local retail) — accessibility lawsuit targeting correlates with visible business size/traffic more than with actual site quality, so a broad range of established local businesses are plausible targets regardless of industry.

## How It Makes Money

- Flat audit fee: $250–$500 for a full accessibility scan and prioritized findings report (critical legal-risk issues vs. lower-priority best-practice improvements), using free automated scanning tools plus manual verification of the highest-risk items.
- Fix implementation project fee: $500–$2,500 depending on scope, to actually remediate the flagged issues (adding alt text, fixing contrast ratios, labeling form fields, repairing keyboard navigation) — the highest-margin work and the natural next step once a business sees its risk exposure.
- Ongoing monitoring retainer: $100–$300/mo to re-scan monthly (sites drift out of compliance as content/features are added) and catch new issues before they accumulate — a genuinely justified recurring service given how easily new content breaks compliance.
- Documentation/accessibility statement add-on: a modest flat fee to draft a publicly posted accessibility statement, which some legal counsel view as a mitigating factor in demand-letter situations — a low-effort, high-perceived-value addition.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Run a prospect's public website through free automated scanning tools (WAVE, axe DevTools browser extension, Google Lighthouse's accessibility audit) — all free, no account required, and genuinely thorough for surfacing the most common, most litigated issue categories.
   - Manually verify and prioritize the top findings by legal-risk relevance (missing alt text on key images, insufficient color contrast on primary calls-to-action, unlabeled form inputs, and keyboard-navigation traps are the most commonly cited issues in actual demand letters — prioritize these over cosmetic-only issues).
   - Deliver a plain-English findings report: what's flagged, why it matters (referencing WCAG guideline numbers for credibility plus the plain-English legal-risk translation), and a clear list of fixes ranked by risk/effort.
2. **Software layer (build once 2–3 audits are sold, funded by early audit fees):**
   - Script wrapping the free scanning tools' output (several have CLI/API access, e.g., axe-core has a programmatic API) to auto-generate the first draft of the findings report, cutting audit turnaround from an hour of manual tool review to a fast automated pass plus manual verification — same automation-layer pattern used across PoC 05/10 in this folder.
   - Reusable fix-implementation snippets for the most common issue types (alt text patterns, contrast-safe color adjustments, ARIA label templates) so remediation work on a new client's site starts from proven, tested patterns rather than research from scratch each time.
   - Simple before/after scan-score tracker (Airtable/Google Sheets) to demonstrate concrete improvement to clients and build a case-study library ("reduced critical issues from 47 to 3").

## Tools/Stack

- WAVE, axe DevTools, and Google Lighthouse (all free) for automated accessibility scanning.
- axe-core's programmatic API (free, open source) for building the semi-automated scan-to-report pipeline.
- Claude/Gemini API for translating raw technical findings into plain-English risk explanations for non-technical business owners.
- Direct website code access (via the client's CMS or a developer handoff) for implementation work.
- Stripe/invoice for fee collection.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Run free automated scans against a list of 20-30 local business websites (restaurants, retail, service businesses with booking/ordering) before outreach — this costs nothing and takes minutes per site using the free browser-extension tools.
2. Free-sample hook: lead outreach with a specific, real finding: "Ran an accessibility check on your website and found 3 issues that are exactly the kind plaintiffs' law firms scan for and send demand letters over — happy to send you the details, free." This is a uniquely urgency-driven version of the specific-finding tactic used throughout this folder, since the framing taps genuine risk-aversion rather than opportunity-cost reasoning.
3. Position credibly and honestly — this should never be framed as scare-tactic fearmongering divorced from reality; accessibility lawsuits targeting small businesses are a well-documented, real phenomenon, and the pitch is strongest when grounded in that reality rather than exaggerated.
4. Local chamber of commerce and small business associations are a strong venue, and web developers/agencies who don't offer accessibility auditing themselves can be a valuable referral partner (their clients' sites are exactly the target profile, and it's a value-add they can offer without doing the work themselves).
5. A single "avoided what looked like it was heading toward a demand letter" story (even without dramatizing it) is a credible, quietly powerful case study within local business communities where this fear is real but rarely discussed openly.

## Time to First Dollar

- Day 1–2: run free automated scans against 20-30 local business websites, identify the ones with genuinely serious findings (not just minor issues).
- Day 2–4: send outreach with the specific finding as the opener.
- Day 4–9: close 3–5 clients on the audit fee ($250–$500), collected upfront, with fix-implementation upsell pitched immediately upon delivery.
- **First dollar within 1–2 weeks** — the free automated tools make the entire diagnostic MVP buildable and demonstrable same-day, with no client cooperation required to produce the initial finding.

## Why This, Why Now

- Zero-cost, genuinely thorough diagnostic tooling already exists (WAVE, axe, Lighthouse) — this is one of the most automatable diagnostics in the entire folder, and free tools do most of the technical heavy lifting from day one.
- Risk-avoidance framing tends to convert faster than efficiency/opportunity framing for buyers who've never thought about a problem before, since the downside (a legal demand letter) is concrete and frightening in a way a missed optimization isn't.
- Directly plays to technical skill for the fix-implementation upsell, which is genuinely valuable, billable work (real code/content changes) rather than just advisory output.
- Accessibility lawsuit activity against small businesses is a well-documented, ongoing trend, not a speculative or manufactured risk — the pitch doesn't require inventing urgency, only surfacing an already-real one.

## Risks / Open Questions

- **Ethical/reputational line around fear-based marketing:** this must stay grounded in real, verifiable risk (actual flagged issues, real WCAG guideline references) rather than exaggerated scare tactics — misrepresenting risk to close a sale would be both unethical and likely to backfire on reputation.
- **Not a legal service:** be explicit that this is a technical accessibility audit, not legal advice, and recommend clients consult an attorney for any active demand letter or legal situation — avoid any language that could be construed as practicing law.
- **Automated scanners have real limitations:** they catch a meaningful share of common issues but miss some contextual/manual-testing-only problems (e.g., logical reading order for screen readers) — be transparent that the audit covers common, high-frequency issues rather than claiming full WCAG compliance certification, which requires more rigorous manual testing than this service's scope covers.
- **Implementation complexity varies by platform:** fixing issues on a Shopify/WordPress site is more standardized than on a custom-built site — confirm platform during the sales conversation and price implementation work accordingly.

## Validation Signal to Watch

If 3+ of your first 10 outreach messages (each with a real, specific flagged issue) generate a reply, the risk-avoidance hook is landing — scale outreach across more local business categories. If response rates are strong but conversion to paid audits is weak, the issue may be trust/credibility rather than interest — consider adding a link to a real, well-known past demand-letter case (publicly reported, not fabricated) to ground the risk in verifiable reality rather than an abstract warning.
