# PoC 31 — "What Happens If You Get Hit By a Bus" — SOP & Process Documentation Service for Small Businesses

**Date:** 2026-07-13
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Small businesses run almost entirely on undocumented tribal knowledge — the owner or one key employee knows exactly how to onboard a new client, process a return, close the books each month, or handle a specific recurring issue, and none of it is written down anywhere. This becomes acutely painful at predictable moments: hiring a new employee (who has to be trained entirely by shadowing, slowly), an owner wanting to take real time off without the business falling apart, preparing to sell the business (buyers discount heavily for undocumented, founder-dependent operations), or simply a key employee leaving and taking undocumented knowledge with them. This is a structured knowledge-extraction and writing service — you interview the person who knows the process and produce a clear, usable SOP (standard operating procedure) document, a task well-suited to a combination of structured interviewing skill and LLM-assisted writing.

## Who It's For

Small business owners with 3+ employees (past the point where the owner personally does everything, but before they have dedicated ops/training staff) who are hiring, planning time away from the business, or considering a future sale/exit — each a distinct, identifiable trigger moment. Also a strong fit for franchise-adjacent or multi-location businesses where consistency across locations depends entirely on documented process.

## How It Makes Money

- Flat fee per documented process: $150–$400 per SOP, covering an interview/observation session plus a polished, usable written (and optionally video-supplemented) procedure document.
- Bundle package: $800–$2,500 for a set of 5-10 core processes documented together (onboarding, most common customer issue resolution, monthly financial close, key vendor management) — the more common actual deal size, since most businesses need several documented at once.
- Ongoing documentation retainer: $200–$500/mo for growing businesses that continuously develop new processes as they scale, keeping documentation current rather than letting it go stale again.
- Training-material upsell: once core SOPs exist, package them into a structured new-hire onboarding curriculum — a natural extension that converts static documentation into an active training asset with clear additional value.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Structured interview with the person who currently performs a given process, asking them to walk through it step by step as if training a new hire, while you take detailed notes (or record with permission) — the extraction method itself, not any tooling, is the core skill here.
   - Use an LLM to help structure raw interview notes into a clear, step-by-step SOP format (numbered steps, decision points, common edge cases, who to contact for exceptions) — turning a rambling verbal walkthrough into a clean, scannable reference document.
   - Review the draft with the interviewed person for accuracy and completeness before final delivery, since the person who actually does the work is the only real check on whether the documentation is genuinely usable.
2. **Software layer (build once 2–3 clients are live, funded by early project fees):**
   - Reusable SOP document template (consistent formatting: purpose, step-by-step process, common exceptions, escalation contact) applied across every engagement — same reusable-scaffold pattern used throughout this folder, giving every client a clean, professional, consistent deliverable.
   - Interview-question-bank library by process type (customer onboarding, financial processes, vendor management, common troubleshooting) refined over repeated engagements to extract more complete information faster in each new interview.
   - Simple documentation-library organization system (a shared Notion/Google Drive structure) delivered to the client so their growing SOP collection stays organized and findable rather than becoming its own new mess of scattered documents.

## Tools/Stack

- No special tooling required for the interview/extraction process itself — just structured questions and note-taking/recording.
- Claude/Gemini API for structuring raw interview notes into clean, formatted SOP documents.
- Notion or Google Drive (free tier) for organizing the delivered documentation library.
- Free screen/video recording tools if supplementing written SOPs with short walkthrough videos for visual/software-based processes.
- Stripe/invoice for fee collection.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify prospects at a visible trigger moment: businesses actively hiring (job postings signal an imminent training need), business owners posting about struggling to take time off or feeling indispensable, or businesses in a visible growth phase (adding locations/employees) where consistency starts to matter more.
2. Free-sample hook: offer to document one specific, high-value process for free based on a short conversation — "Tell me how you currently onboard a new client, I'll turn it into a clean SOP doc you can hand to anyone, free — if it's useful, let's do the rest of your key processes." A concrete, low-effort-for-the-prospect ask (one conversation) that produces a genuinely useful artifact.
3. Small business owner communities and local chamber of commerce networking are strong venues, since "I'm the only one who knows how to do X" is a nearly universal, openly acknowledged frustration among growing small business owners.
4. Position around the concrete trigger moments directly in outreach — "hiring soon? here's what happens if your new hire has no documented process to learn from" reframes documentation from an abstract nice-to-have into a specific, immediate practical need.
5. A single "cut new-hire ramp-up time in half" or "took a real two-week vacation for the first time in years without the business falling apart" result is a highly relatable, emotionally resonant case study for small business owner communities.

## Time to First Dollar

- Day 1–3: identify 15-20 prospects at a visible trigger moment (hiring, growth, owner burnout signals).
- Day 3–5: offer the free single-process documentation sample to the first 8-10 responsive prospects, conduct the interview and deliver quickly.
- Day 5–10: close 2–3 clients on the bundle package ($800–$2,500) or per-process fee, collected upfront or in a deposit-plus-delivery structure.
- **First dollar within 1–2 weeks** — no build dependency, the entire MVP is a structured interview plus LLM-assisted writing, doable same-day per process.

## Why This, Why Now

- Zero build required to start — the core skill (structured interviewing plus clear writing) requires no special tooling and is immediately deployable.
- Extremely relatable, near-universal small business pain point that requires little to no buyer education — most owners already know, uncomfortably, that too much lives only in their own head or one key employee's.
- Directly tied to concrete, high-stakes trigger moments (hiring, time off, eventual sale) that create natural urgency and easy-to-time outreach.
- The free-sample deliverable (one documented process) is both genuinely useful on its own and a clear, tangible preview of the fuller bundle engagement, making the upsell path unusually intuitive.

## Risks / Open Questions

- **Interview quality depends heavily on the interviewee's ability to articulate their own process:** some people who are excellent at a task struggle to explain it step-by-step — build in follow-up questions and, where possible, direct observation of the process being performed rather than relying solely on verbal recall.
- **Documentation goes stale if processes change:** without the ongoing retainer, a one-time SOP set can become outdated within months for a fast-changing business — set expectations about this upfront and use it as the natural case for the retainer tier rather than letting it undermine trust when documentation later feels out of date.
- **Some processes are genuinely hard to fully capture in writing** (highly judgment-based, relationship-dependent work) — be honest about what can and can't be effectively documented rather than forcing every process into a rigid step-by-step format that doesn't fit.
- **Sensitive territory around job security:** some employees may (reasonably or not) feel threatened by their knowledge being documented and made replaceable — this is worth being aware of and handling with care during interviews, framing the work around business resilience and easier delegation rather than replaceability.

## Validation Signal to Watch

If 2+ of your first 8-10 free single-process documentation samples generate a genuinely enthusiastic "this is exactly what we needed" response, the service and interview method are validated — scale outreach around trigger-moment targeting. If interviewees consistently struggle to articulate their process clearly even with structured questions, consider incorporating direct observation/shadowing into the standard method rather than relying on interview-only extraction, since that may meaningfully improve documentation quality and client satisfaction.
