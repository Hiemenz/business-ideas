# PoC 36 — "Your Business Has Zero HR Policies in Writing" — Employee Handbook & HR Compliance Document Service

**Date:** 2026-07-14
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Small businesses that grow past a handful of employees rarely have a proper written employee handbook — no documented PTO policy, no anti-harassment policy, no clear at-will employment language, no remote-work or overtime policy — leaving them both operationally inconsistent (different managers handling the same situation differently) and legally exposed (many jurisdictions have specific required postings/policies once headcount crosses certain thresholds, and an undocumented policy is much harder to defend in a dispute than a clearly written one that was consistently applied). This is distinct from PoC 31 (which documents operational how-to processes) — a handbook covers employment policy and legal-compliance territory, a different domain with the same genuine legal-risk-avoidance framing used successfully in PoC 21 (accessibility) and PoC 27 (trademark clearance), and it becomes acutely relevant at a predictable trigger moment: crossing a headcount threshold, hiring the first remote employee, or after a workplace incident that revealed the absence of a clear policy.

## Who It's For

Small businesses with 5-50 employees who've never had a formal, written employee handbook, or whose handbook (if one exists) is years out of date — best entry point: businesses actively hiring (a new-hire onboarding moment naturally raises "what do we even give them to read"), or businesses expanding to remote/multi-state employees, which meaningfully increases compliance complexity since employment law varies significantly by state.

## How It Makes Money

- Flat handbook-build fee: $500–$1,500 depending on business size/complexity, to draft a complete, jurisdiction-appropriate employee handbook covering standard core policies (PTO, at-will employment, anti-harassment/discrimination, code of conduct, remote work if applicable, standard leave policies).
- Multi-state compliance add-on: additional fee per state for businesses with employees across multiple states, since specific policy language (sick leave accrual, meal/rest break rules) genuinely varies by jurisdiction and requires deliberate handling, not a one-size-fits-all template.
- Annual update retainer: $200–$500/yr to review and refresh the handbook as employment law changes or the business's policies evolve — a naturally justified recurring service, since employment law is genuinely not static and a stale handbook can itself become a liability.
- New-hire onboarding packet bundle: pairing the handbook with a structured first-week onboarding document (drawing on the same documentation skill as PoC 31) as a combined higher-ticket package.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Intake conversation: gather the business's actual current practices (informal PTO approach, any existing ad-hoc policies, state(s) of operation, remote/in-person mix) so the handbook reflects real practice rather than generic boilerplate.
   - Draft the handbook using an LLM prompted with standard handbook structure and the client's specific details, cross-checking core legally-relevant sections (at-will language, required policy disclosures, anti-discrimination language) against publicly available, reputable reference sources (state labor department websites, SHRM's publicly available guidance) for the client's specific jurisdiction(s).
   - Deliver a clean, organized document, explicitly flagged as a strong starting draft that should get a final review from an employment attorney before formal adoption — especially critical for any client with employees in multiple states or in a higher-litigation-risk industry.
2. **Software layer (build once 2–3 clients are live, funded by early project fees):**
   - Reusable, modular handbook template with state-specific policy variants as swappable sections (since many core policies are standard but certain sections — sick leave, break requirements — genuinely differ by state) — same reusable-scaffold pattern used throughout this folder, with the added structure of jurisdiction-specific modules.
   - Simple client-intake form capturing the structured inputs (headcount, states of operation, remote/in-person mix, existing informal policies) that feed directly into the drafting prompt, speeding up each new engagement.
   - Update-tracking system flagging when a state's relevant employment law changes, informing which existing clients' handbooks may need a refresh — directly supports the annual retainer's actual delivered value.

## Tools/Stack

- Claude/Gemini API for handbook drafting from structured intake inputs.
- Publicly available, free reference sources (state labor department websites, SHRM public resources) for cross-checking jurisdiction-specific requirements.
- Google Docs for collaborative drafting/delivery.
- Stripe/invoice for fee collection.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify prospects among small businesses actively hiring (job postings signal growing headcount, often crossing the threshold where a formal handbook becomes genuinely necessary) or expanding to remote/multi-state hires (visible via "remote OK" job postings from a business you can otherwise tell is small/local).
2. Free-sample hook: offer a free, quick review of whatever informal policies a prospect currently has (even just "here's what I tell new hires") and flag one specific, concrete gap: "Noticed you don't have anything in writing about [specific policy, e.g., overtime eligibility] — that's actually one of the more commonly disputed areas without clear documentation. Want a full handbook built out?" A grounded, specific, credible opener rather than generic fear-based marketing.
3. Local HR/small business associations, and referral partnerships with the same local CPAs/bookkeepers used in PoC 22's referral channel, are strong venues — professionals who already serve small business owners on adjacent compliance matters (taxes, books) are natural, credible referral sources for handbook/HR compliance work too.
4. Position the pitch around the genuine two-sided value: consistency in how the business is actually run day-to-day, plus real legal-risk reduction — avoid over-indexing on fear alone, since the operational-consistency benefit is real and resonates even with owners not worried about legal exposure.
5. A single "used the handbook to handle a disciplinary situation cleanly and consistently, avoided what could've been a messy dispute" story (even anonymized) is a credible, relatable case study for small business owner communities.

## Time to First Dollar

- Day 1–3: identify 15-20 prospects showing visible hiring/growth signals, review whatever public/informal policy information is available for the first 8-10.
- Day 3–5: send outreach with the specific policy-gap finding as the opener.
- Day 5–10: close 2–3 clients on the flat handbook-build fee ($500–$1,500), collected upfront or in a deposit-plus-delivery structure.
- **First dollar within 1-2 weeks** — no build dependency, LLM-assisted drafting from structured intake plus reference-source cross-checking is genuinely fast per engagement.

## Why This, Why Now

- Zero build required to start — reusable template structure plus LLM-assisted drafting makes each new engagement fast once the reference-checking process is established for a given jurisdiction.
- Genuine, dual-sided value proposition (operational consistency plus real legal-risk reduction) gives this pitch broader appeal than a purely fear-based angle, similar in spirit to PoC 21/27 but with an even more universally applicable trigger (any business with employees eventually needs this, not just businesses with a public-facing website or a new product name).
- CPA/bookkeeper referral channel (mirroring PoC 22's approach) offers a scalable, relationship-based acquisition path distinct from cold outreach alone.
- Recurring annual-update retainer is genuinely, honestly justified — employment law changes regularly enough that a stale handbook really can become newly non-compliant without anyone realizing it, unlike some services where the recurring hook is more manufactured.

## Risks / Open Questions

- **Not a substitute for attorney review, and this boundary matters more here than almost anywhere else in this folder:** employment law carries real legal stakes (discrimination claims, wage-and-hour disputes) — every handbook delivered must be explicitly and clearly flagged as a strong starting draft requiring final review by a licensed employment attorney before formal adoption, especially for multi-state employers or higher-risk industries; this is the single most important disclaimer across every idea generated in this folder given the stakes involved.
- **Jurisdiction accuracy is critical and non-trivial:** employment law varies meaningfully by state (and sometimes city/county) — cross-checking against reputable public sources is necessary but not sufficient for full legal accuracy, reinforcing why attorney review is a required step, not an optional upsell.
- **Client's actual practices may not match written policy:** a handbook is only protective if the business actually follows it consistently — flag this directly to clients, since a handbook that says one thing while the business does another can create its own liability.
- **Multi-state complexity scales quickly:** a business with employees in 5+ states requires meaningfully more careful, differentiated work than a single-state small business — price and scope accordingly rather than treating all engagements as equivalent effort.

## Validation Signal to Watch

If 2+ of your first 8-10 outreach messages (each with a specific, real policy-gap observation) generate a reply, the hook is working — scale outreach around hiring/growth-signal targeting and pursue CPA/bookkeeper referral relationships in parallel. Given the elevated legal stakes here relative to most other ideas in this folder, prioritize validating that the attorney-review disclaimer and referral relationship (having a real employment attorney to point clients toward) are solidly in place before scaling volume, rather than treating this purely as a sales-velocity question.
