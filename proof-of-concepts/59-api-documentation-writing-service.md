# PoC 59 — "Developers Try Your API Once and Never Come Back" — API Documentation Writing Service

**Date:** 2026-07-18
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

Developer tools, SaaS products with APIs, and infrastructure companies live and die by their documentation quality — but most early-stage companies have documentation written by engineers who understand the API perfectly and therefore write for themselves rather than for a developer encountering it for the first time. The result is docs that skip the authentication setup (because the author found it obvious), describe what an endpoint does without explaining when to use it, have no working code examples, bury the quickstart in a sidebar nobody finds, and leave critical error responses undocumented. A developer who hits a 401 with no explanation in the docs, or who can't get a working example running in under 10 minutes, doesn't file a support ticket — they close the tab and use a competitor whose docs work. The documentation quality gap is directly measurable in API trial-to-integration conversion rates, support ticket volume (most support tickets are documentation failures), and developer community sentiment. Every one of these problems is fixable by someone who can read an API spec, understand it technically, and write for a developer who's seeing it cold — a combination that's genuinely rare and genuinely valuable. This is distinct from every other writing or technical service in this folder — it requires actual technical fluency with APIs (auth flows, request/response structure, error codes, SDK patterns) combined with the specific writing discipline of technical documentation.

## Who It's For

Early-stage developer tool companies, SaaS businesses with a public or partner API, and internal platform teams whose developer-facing documentation is underdeveloped, outdated, or simply absent. Best entry points: companies that are about to launch a public API for the first time, companies that have received consistent "the docs are confusing" feedback in developer community discussions, or companies where the engineering team is small and writing documentation is consistently the task that gets cut when a sprint gets tight.

## How It Makes Money

- Documentation audit: $300–$600 for a written assessment of the current docs against a structured quality framework — is there a working quickstart? Are all endpoints documented? Do code examples actually run? Are error responses explained? Are there conceptual guides explaining when and why, not just how? Delivered as a prioritized gap report with specific fix recommendations.
- Quickstart guide write: $300–$500 for a single, complete, tested quickstart guide — the most critical piece of any developer-facing documentation, the first thing every new developer reads, and the one that most directly determines whether they proceed to integration or abandon. Covers: account setup, API key acquisition, authentication, first successful API call with working code, and the 3-5 most common next steps.
- Full API reference documentation: $800–$2,000 for complete endpoint-by-endpoint documentation of a defined API surface — every endpoint, every parameter, every response schema, every error code, working code examples in 1-2 languages (Python and JavaScript cover most developer audiences), and a reference index. Priced by API surface size (up to 20 endpoints at the base tier).
- Developer guide set: $500–$1,200 for 4-6 conceptual "how-to" guides covering the most common developer use cases — not reference docs (which describe what exists) but task-oriented guides (how do I authenticate as a user, how do I handle pagination, how do I set up webhooks) that are frequently more valuable than the reference for developers actually building integrations.
- Documentation maintenance retainer: $300–$600/mo to keep docs current as the API evolves — new endpoints documented within 72 hours of release, deprecation notices added, code examples tested against current API behavior quarterly.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Audit the existing documentation from the perspective of a developer encountering it cold: attempt to complete the quickstart with zero prior knowledge, try to make a real API call using only the docs, attempt to handle an error using only the documented error responses. Document every point where progress stalls.
   - Gather the API spec (OpenAPI/Swagger spec if available, or a list of endpoints from the engineering team) plus any internal notes or Notion pages the team uses as informal documentation.
   - Write a sample endpoint documentation page — pick the most commonly used endpoint, write it to the full standard (description, when to use it, request parameters with types and validation rules, response schema with field-level descriptions, error codes and their meaning, working code examples in Python and JavaScript tested against the live API sandbox) — and deliver it as the free sample.
   - Use an LLM to produce first drafts of endpoint documentation sections from the OpenAPI spec plus brief engineering notes, then edit and test each example for accuracy — the LLM accelerates structured documentation drafting significantly; the accuracy testing and clarity editing are the human contribution.
2. **Software layer (build once 2–3 clients are live):**
   - Documentation audit checklist: every dimension of developer documentation quality assessed systematically (quickstart completeness, endpoint coverage, code example currency, error documentation, search/navigation quality, conceptual guide coverage) — built once and used for every audit engagement, producing consistent, comparable findings.
   - LLM prompt chain for endpoint documentation: one prompt for the description section (given this endpoint's function and parameters, write a clear description for a developer who hasn't used it before), one for the code example section (given this endpoint spec, write working Python and JavaScript examples with realistic parameter values), one for the error table (given these error codes, write developer-useful explanations of what causes each and how to handle it) — each producing a technically accurate first draft that requires testing and editing but not writing from scratch.
   - Reusable documentation structure templates for the most common doc types (quickstart, endpoint reference, conceptual how-to guide, authentication guide, webhook guide) — consistent structure across all docs reduces the cognitive load on the developer reading them and makes each new doc section faster to draft.

## Tools/Stack

- The client's API directly (use the sandbox/test environment for all code example development and testing — free to access once the client grants API credentials).
- Swagger/OpenAPI spec (if available — most mature APIs have one) as the structured input for endpoint documentation drafting.
- Claude/Gemini API for first-draft documentation generation from structured spec inputs.
- Postman or curl for testing every code example before it goes into the docs — a non-negotiable quality step, since untested code examples are worse than no examples.
- ReadMe, Mintlify, or GitBook (all have free tiers) as doc hosting platforms if the client doesn't already have a docs site — these are the industry-standard developer documentation platforms and produce polished, searchable docs from Markdown without any engineering work.
- Google Docs for draft review and client collaboration before publishing.
- Stripe/invoice for fee collection.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify prospects in developer tool communities (Hacker News, r/devops, r/webdev, DevRel Slack groups, APIs.guru public API directory) where "the docs are terrible" is a recurring specific complaint about a specific product — public developer frustration about documentation quality is unusually visible and specific, naming exact products and exact gaps.
2. Free-sample hook: attempt the quickstart of a target company's API as a new developer, identify the first point where the docs fail, and write a fixed version of that specific section: "Tried your quickstart this morning — hit a 401 with no explanation on step 3. Wrote what that section should look like: [attach the fixed version]. Happy to audit and rewrite the full docs if useful." A specific, tested, credible finding that took 30-45 minutes and demonstrates both the ability to read the API and the ability to fix the docs.
3. Developer-facing companies that are newly public with their API (visible from Product Hunt launches, developer blog announcements, API directory listings) are at the highest-leverage moment for documentation investment — the first 60 days of a public API launch is when documentation quality has the most impact on adoption trajectory.
4. DevRel (developer relations) teams at larger companies that manage documentation as part of a broader developer program are natural buyers and referral sources — they understand the problem intimately, often have budget, and frequently need external writing support for documentation backlogs their internal team can't keep current.
5. A "API trial-to-integration conversion rate improved from 12% to 34% in 60 days after documentation overhaul" result — expressed in the developer adoption metric companies actually track — is the most compelling possible evidence for this service.

## Time to First Dollar

- Day 1: attempt the quickstart of 5-6 public APIs in the dev tool space to calibrate what good vs. bad documentation looks like and build intuition for the most common failure patterns; draft the documentation audit checklist.
- Day 2–3: identify 10-15 developer tool companies with publicly visible documentation quality complaints (GitHub issues labeled "docs," developer community threads naming specific gaps, or App Store reviews for mobile SDKs); attempt each quickstart and identify the first failure point.
- Day 3–6: write and send the free fixed-section sample to each, with the full audit or quickstart rewrite offer.
- Day 6–12: close 2–3 clients on the quickstart rewrite ($300–$500) or full audit ($300–$600), with sandbox API credentials provided on payment; deliver within 5-7 days.
- **First dollar within 1–2 weeks** — sandbox API access is typically granted instantly, the free sample takes 45 minutes from a public API, and the per-section price point is low enough to close without procurement involvement.

## Why This, Why Now

- Documentation quality is a developer adoption lever that most early-stage companies have never deliberately invested in — the opportunity is large, the competition among specialist documentation writers is thin, and the gap between "engineer-written docs" and "developer-experience-optimized docs" is consistently wide.
- The free sample (attempting the quickstart as a new developer and writing a fixed version of the first failure point) is uniquely credible because it proves both technical competence (you successfully used the API) and writing quality (you fixed the specific problem) in a single 45-minute artifact.
- Developer complaints about specific API documentation failures are more publicly visible than almost any other product complaint — GitHub issues, Stack Overflow questions, and Hacker News comments routinely name specific companies and specific documentation gaps, creating a searchable, self-updating prospect list.
- Maintenance retainer is genuinely justified: APIs change with every release, and documentation that isn't actively maintained becomes a liability within 3-6 months — the retainer value compounds as the client relationship deepens and the documentation maintainer understands the API architecture well enough to document new features accurately and quickly.

## Risks / Open Questions

- **Technical accuracy is non-negotiable:** a code example that doesn't run, an endpoint description that's wrong, or an error code explanation that's misleading is worse than no documentation — every code example must be tested against the live API before delivery, and every parameter description must be verified against the actual API behavior, not just the spec (which is often out of date).
- **API access and sandbox availability vary:** some APIs don't have a sandbox environment, requiring either production credentials (which adds risk to testing) or working from the spec alone (which produces less accurate documentation) — clarify API access availability in the scoping conversation before committing to a timeline.
- **Scope creep is high in documentation projects:** "write the docs" can expand from a defined API surface to "also document the SDK, and can you write the conceptual guides, and can you update the changelog" — scope each engagement explicitly by deliverable type and API surface size, and price additional scope separately rather than absorbing it.
- **Client engineering availability is a dependency:** accurate documentation requires access to an engineer who can answer questions when the spec is ambiguous or when behavior doesn't match the spec — factor in a response time expectation (24-hour turnaround on clarifying questions) as part of the engagement terms, since blocked questions directly affect delivery speed.

## Validation Signal to Watch

If the free quickstart-attempt findings ("here's the specific point your docs fail a new developer, and here's what the fixed section looks like") consistently generate reactions of genuine surprise from engineering or DevRel teams ("we didn't realize that was the failure point"), the outside-developer perspective is producing real, novel insight — that reaction pattern is the strongest signal the service is accessing information the client can't generate internally. First hard validation: a client who publishes the rewritten docs and sees a measurable drop in "docs confusion" support tickets within 30 days — support ticket reduction is the most directly attributable and easily measured outcome for documentation quality improvement.
