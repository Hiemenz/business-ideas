# Main Income Ideas - 2026-07-29 (Session 3)

## Who this is for
Builder profile: 29, software engineering + data analytics skills. Same bar as Sessions 1-2: not "$500-3K/mo of side money" but a solo-buildable path with a credible route to **$8-15K+/mo** — full-time-salary-replacement income — within 12-24 months.

## Ground rules for every idea in this series
- **Solo-buildable start.** One person, evenings/weekends, no funding, no cofounder required to get the first version live.
- **Realistic path to $8-15K+/mo**, not a side-money ceiling — every idea states the math (case/deal/booking count x price point) plainly, no TAM hand-waving.
- **Time to first dollar < 90 days.** Long enterprise sales cycles are disqualifying by default.
- **Named distribution channel** for the first 10 customers *and* a credible path to the next 10x.
- **Boring is fine.** Low-glamour, real-pain problems beat trendy ones.
- **No repeats.** Nothing below overlaps a concept already covered across Sessions 1-2 of this series, `side-income-ideas/`, or `discovered-problems/`. This session adds three model variants not yet used in this series — **marketplace take-rate, deal-brokerage commission, and a regulated finder's fee** — alongside a second retainer idea in a fresh regulated vertical, continuing the pattern of pricing against transaction/asset size rather than a small-business subscription budget.

---

## Ideas

### 1. VA Disability Claims Appeal Assistance Service
**Problem:** Veterans routinely have valid VA disability claims denied or under-rated due to incomplete medical evidence, a missing nexus letter connecting a condition to service, or clerical errors — the average denied claim leaves thousands of dollars in monthly disability compensation and often tens of thousands in retroactive back pay unclaimed, and navigating the VA's claims process alone is famously difficult.
**What to build:** A claims-preparation and appeal-support service, backed by a document-organization/case-tracking tool that maps a veteran's service records and medical evidence against VA rating criteria and flags exactly what's missing for a stronger claim, operated as an accredited VA claims agent (or in partnership with one), charging the VA-regulated fee structure — up to 20% of past-due benefits awarded on a successful appeal, the same fee model long used by Social Security disability advocates.
**Skill fit:** Direct on the software half (structuring service records/medical evidence against rating criteria, case status tracking) — a rules-matching problem similar to other compliance-style ideas in this series; VA accreditation (a straightforward exam/application, not a bar-exam-level barrier) is the main non-technical requirement to legally charge a fee.
**MVP scope:** 2-3 weekends for a document-intake and evidence-gap-checking tool against a structured VA rating-criteria dataset; the filing/advocacy work is manual by design.
**Time to first $:** 60-90 days, including accreditation lead time — distribute through veteran-service-organization (VSO) referral relationships (American Legion, VFW posts) and veteran-focused Facebook/Reddit communities, where "your claim was underrated and here's why" is an immediately credible pitch.
**Income ceiling (realistic, with math):** Average successful appeal recovers $8,000-25,000 in retroactive back pay; a 20% fee is $1,600-5,000 per case, and 3-5 successful cases/mo = **$8-15K/mo** once a referral pipeline is running.
**Why this can go beyond side money:** The regulated fee is a percentage of a large lump-sum retroactive payment, not a subscription a small customer negotiates down — a single case can be worth what a niche SaaS tool earns from a customer over a year or more, and veteran disability claims are a large, ongoing population, not a one-time market.
**Biggest risk:** VA accreditation and fee rules are strictly regulated (fees can only be charged after a Notice of Disagreement is filed, and only on the specific increase won on appeal) — get properly accredited and structure fee agreements exactly to VA rules before taking a single case, since operating outside them risks disqualification from practicing before the VA at all.
**Growth path:** Side project → get accredited, take 3-5 cases through one VSO referral relationship, fully hands-on. Replaces-part-time-income → 8-10 cases/mo once the evidence-gap tool speeds up case prep and referral relationships expand to 2-3 VSO posts (~$6-9K/mo, lumpy with case timelines). Replaces-full-time-salary → a referral network across a state's VSO posts plus a veteran-community online presence, 15-20 cases/mo in the pipeline at any time, smoothing out individual case-resolution lumpiness.

---

### 2. Specialty Heavy-Equipment Rental Marketplace
**Problem:** Small construction, excavation, and agricultural contractors need specialty equipment (a specific attachment, a mid-size crane, a trencher) for short jobs, but buying is uneconomical, and national rental chains (United Rentals, Sunbelt) price for volume/long-term rentals — there's no efficient local peer-to-peer market surfacing the idle equipment sitting unused on a neighboring contractor's lot.
**What to build:** A regional marketplace matching equipment owners with idle machines to contractors needing short-term rentals — listings with availability calendars, delivery-logistics coordination, and deposit/damage-protection handling — taking a transaction commission (10-15%) on each booked rental.
**Skill fit:** Direct — marketplace listing/matching/booking logic and payment/deposit handling is standard application engineering; no domain expertise beyond typical rental terms (day rates, delivery radius, damage deposit norms).
**MVP scope:** 3-4 weekends for listings, availability calendar, booking flow, and deposit handling for one regional market and a handful of equipment categories.
**Time to first $:** 45-60 days — seed both sides in one region: recruit equipment owners (small contractors/rental yards) directly and recruit renters through contractor Facebook groups and trade association member directories in the same region.
**Income ceiling (realistic, with math):** Average specialty rental runs $500-2,000 for a multi-day job; a 12% average commission on 60-100 bookings/mo in one growing region = **$4-24K/mo**, comfortably clearing $8-15K/mo once volume matures.
**Why this can go beyond side money:** Marketplace take-rate revenue scales with total transaction volume across many owners and renters, not a per-customer subscription price — the ceiling is set by regional rental-market size, not by how many individual software subscriptions a solo builder can sell and support.
**Biggest risk:** Two-sided marketplaces have a cold-start problem — solve it by concentrating exclusively on one region and manually recruiting the first 20-30 equipment owners directly (calls, rental-yard visits) rather than trying to build supply passively through the website alone.
**Growth path:** Side project → one region, 20-30 equipment listings recruited manually, first bookings brokered semi-manually to build trust in the deposit/damage process. Replaces-part-time-income → booking volume self-sustaining in that region with matching/payment handled automatically (~$5-8K/mo). Replaces-full-time-salary → expand to 2-3 adjacent regions reusing the same supply-recruitment playbook, commission revenue compounding without proportionally more manual work per region.

---

### 3. B2B Overstock/Closeout Liquidation Brokering
**Problem:** Manufacturers, distributors, and retailers routinely end up with overstock, closeout, or customer-returned inventory tying up warehouse space and capital, and while liquidators/discount retailers actively want to buy it cheap, there's no efficient, trustworthy channel connecting a mid-size seller with excess inventory directly to the right buyer — deals happen through a small, relationship-gated network of liquidation brokers.
**What to build:** A brokering operation, with a lightweight tool to catalog available overstock lots (photos, condition, quantity) and match them against a database of liquidation buyers by category and price tolerance, sourcing overstock listings directly from small-to-mid manufacturers/retailers and brokering each lot to the best-fit buyer for a commission (5-10%) on deal value.
**Skill fit:** Direct on the data/matching side (categorizing inventory, matching to buyer preferences is a structured-data problem); the deal-closing/negotiation side is a learned relationship-building skill, not a technical one.
**MVP scope:** 2-3 weekends for a lot-cataloging tool and buyer-matching database; sourcing and deal-closing is manual by design in v1.
**Time to first $:** 45-60 days — source the first sellers directly (small manufacturers and regional retail chains via industry trade shows and LinkedIn outreach) and the first buyer relationships from established liquidation marketplaces/auction houses willing to take referred lots.
**Income ceiling (realistic, with math):** A single liquidation lot is often worth $20,000-200,000 in inventory value; a 5-8% commission on just 4-6 closed deals/mo = **$8-24K/mo**, with deal size doing most of the work rather than deal volume.
**Why this can go beyond side money:** Brokerage commission is priced against wholesale inventory value, an order of magnitude larger than what any small business would pay for a software subscription — a handful of deals a month, not hundreds of customers, clears the main-income bar.
**Biggest risk:** Building genuine trust with sellers (who share sensitive inventory/financial information) and buyers (who need confidence in lot condition/quantity claims) takes real relationship-building time before the first deal closes — start by partnering with 1-2 already-established liquidation buyers who can vouch for the arrangement rather than cold-approaching unknown buyers with an unproven seller relationship.
**Growth path:** Side project → first 1-2 deals brokered manually through personal outreach and an established buyer relationship, proving the sourcing-to-close process. Replaces-part-time-income → 2-3 deals/mo once a repeatable sourcing channel (trade-show contacts, referrals from closed deals) and 3-4 buyer relationships exist (~$6-10K/mo, lumpy by deal timing). Replaces-full-time-salary → sourcing expanded to a second industry category and a wider buyer network, 5-6 deals/mo smoothing out individual deal-timing lumpiness.

---

### 4. Certified Payroll / Prevailing-Wage Compliance Retainer for Government Contractors
**Problem:** Small construction and trade subcontractors bidding on public/government-funded projects must file certified payroll reports proving Davis-Bacon Act prevailing-wage compliance on every project, a notoriously tedious and error-prone requirement — a single mistake can trigger a contract audit, withheld payment, or even debarment from future public contracts, but most small subcontractors have no dedicated compliance staff for it.
**What to build:** A certified payroll compliance retainer: a tool ingesting a subcontractor's payroll/timesheet data, cross-checking it against the correct prevailing-wage determination for that project's location and trade classification, auto-generating the required certified payroll reports (WH-347 or state equivalent), and flagging discrepancies before submission to the contracting agency.
**Skill fit:** Direct — a rules-matching and document-generation problem (payroll data against a structured wage-determination dataset), the same compliance-monitoring pattern used elsewhere in this series, applied to a fresh, high-stakes government-contracting niche.
**MVP scope:** 3-4 weekends to build the wage-determination lookup/matching engine for one state plus the certified payroll report generator.
**Time to first $:** 45-60 days — reach small subcontractors directly through state contractor licensing boards' public-works bidder lists and trade association member directories, where "avoid a compliance audit finding" is a legible pitch to anyone who's bid on a public project before.
**Income ceiling (realistic, with math):** $400-700/mo retainer per subcontractor (a fraction of what a compliance consultant or dedicated staffer costs, trivial against debarment risk); 15-20 subcontractor clients = **$8-14K/mo**.
**Why this can go beyond side money:** The downside of getting this wrong (audit finding, withheld payment, or debarment from public work entirely) is severe enough relative to a small subcontractor's business that retainer price tolerance sits well above a typical small-business SaaS tool.
**Biggest risk:** Prevailing-wage determinations vary by project location, trade classification, and funding source, so a rules engine built for one jurisdiction doesn't transfer directly — launch fully correct for one state's rules, clearly positioned as a compliance aid the subcontractor's own accountant still reviews, before expanding jurisdiction by jurisdiction.
**Growth path:** Side project → one state's wage-determination rules built, 5-8 subcontractors onboarded via a state contractor licensing board's bidder list, manual report review. Replaces-part-time-income → 12-15 subcontractors with report generation running automatically, freeing time to build a second state's ruleset (~$6-9K/mo). Replaces-full-time-salary → 2-3 states/jurisdictions covered, 25-30 subcontractor clients total, contractor licensing boards and trade associations as an ongoing distribution channel per newly-covered jurisdiction.

---

### 5. Unclaimed Property & Estate Asset Recovery Service
**Problem:** Heirs going through probate routinely miss real money the deceased was owed — forgotten bank accounts, uncashed checks, old insurance payouts, and unclaimed property sitting in state unclaimed-property databases (collectively holding tens of billions of dollars nationally) — because searching these fragmented state-by-state databases and old financial records isn't something a grieving family or even most estate attorneys have time to do thoroughly.
**What to build:** An asset-recovery service, backed by a tool that systematically searches all 50 state unclaimed-property databases plus common overlooked-asset categories (old life insurance policies, uncashed dividend checks, forgotten security deposits) for a deceased person's name and known past addresses, identifying recoverable assets and handling the claims paperwork to recover them, charging a finder's fee (10-15%) of what's recovered.
**Skill fit:** Direct — a structured multi-source search-and-matching problem (name/address matching across 50 disparate state database formats), core data-analytics work; no legal expertise beyond following each state's standard, well-documented claims-filing process.
**MVP scope:** 3-4 weekends to build the multi-state database search tool (most are searchable, several via NAUPA's national database) plus a per-state claims-tracking system.
**Time to first $:** 45-60 days — distribute through probate/estate attorneys and estate-sale companies (via local bar association probate sections and estate-sale industry directories) who routinely see grieving families overwhelmed by exactly this kind of loose-end asset hunting and are happy to refer a specialist for a fee.
**Income ceiling (realistic, with math):** Recovered assets per estate average $2,000-15,000; a 12% average finder's fee is $240-1,800 per estate, so 15-25 estates/mo (feasible once referral relationships are running, since new estates open constantly) = **$5-15K/mo**, reachable with volume from a handful of steady referral sources.
**Why this can go beyond side money:** The finder's fee is priced against recovered dollar amounts that are, in aggregate across many small line items, meaningfully larger than any subscription a grieving family would pay for a tool — and probate attorneys are a renewable referral source since new estates open every day regardless of economic conditions.
**Biggest risk:** Volume, not deal size, drives this one, so it depends on building real referral relationships with probate attorneys and estate-sale companies rather than a one-off marketing push — invest early in a handful of attorney relationships with real service quality (fast turnaround, clean paperwork) rather than spreading thin across many low-trust cold outreach attempts.
**Growth path:** Side project → first 5-10 estates through one probate attorney relationship, fully manual search and claims filing, proving average recovery per estate. Replaces-part-time-income → 15-20 estates/mo once 3-4 attorney/estate-sale referral relationships exist and the search tool runs largely automatically (~$5-8K/mo). Replaces-full-time-salary → referral relationships expanded to a metro's full probate-attorney community plus a state bar association CLE presentation as a credibility/distribution move, pushing volume to 30-40 estates/mo.

---

## Scoring Summary (this session)

| # | Idea | Model | MVP effort | Time to first $ | Income ceiling (main-income path) |
|---|------|-------|------------|------------------|-------------------------------------|
| 1 | VA disability claims appeal assistance | Regulated contingency fee | 2-3 weekends | 60-90 days | $8-15K/mo (lumpy) |
| 2 | Specialty heavy-equipment rental marketplace | Marketplace take-rate | 3-4 weekends | 45-60 days | $4-24K/mo |
| 3 | B2B overstock/closeout liquidation brokering | Deal brokerage commission | 2-3 weekends | 45-60 days | $8-24K/mo |
| 4 | Certified payroll/prevailing-wage compliance | Retainer | 3-4 weekends | 45-60 days | $8-14K/mo |
| 5 | Unclaimed property & estate asset recovery | Finder's fee | 3-4 weekends | 45-60 days | $5-15K/mo |

---

## This Session's Pick: Start With #4, Track #3 as the Highest-Ceiling Bet

**Steadiest, clearest recurring path:** Idea #4 (certified payroll compliance retainer) again offers the most predictable revenue in this batch — a flat retainer, a clean licensing-board-based channel, and stakes (debarment from public work) high enough to support a well-above-market price without a long sales cycle, mirroring why #5 was Session 2's steady pick.

**Highest per-transaction ceiling:** Idea #3 (liquidation brokering) has the largest per-deal economics in this series ($20K-200K lot values), but deal-sourcing and trust-building make it slower to ramp — best run as a parallel bet once #4's retainer base provides a revenue floor, rather than as the sole first bet, the same pairing logic used in Sessions 1-2.

Running #4 as the primary build (predictable, licensing-board-channel-driven, high per-customer stakes) while sourcing the first 1-2 liquidation deals for #3 in parallel continues this series' established pattern: a steady build paired with a higher-variance, higher-ceiling bet running alongside it.

---

## Files Created (3 sessions - 15 ideas)
1. `2026-07-29-main-income-v1.md` (5 ideas: managed retainer, data API, acquisition, education+retainer models)
2. `2026-07-29-main-income-v2.md` (5 ideas: contingency fee, subscription+sponsorship, and placement fee models)
3. `2026-07-29-main-income-v3.md` (5 ideas: regulated contingency fee, marketplace take-rate, brokerage commission, retainer, finder's fee models)

**Total: 15 ideas across 3 sessions**

**Cron Loop:** `0 */5 * * *` continues — each session adds new solo-startable ideas with a credible, math-backed path to full-time-salary-replacement income, spanning new sectors and business models, never repeating a concept already covered in this series, `side-income-ideas/`, or `discovered-problems/`.
