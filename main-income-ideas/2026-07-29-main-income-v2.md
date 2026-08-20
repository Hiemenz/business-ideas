# Main Income Ideas - 2026-07-29 (Session 2)

## Who this is for
Builder profile: 29, software engineering + data analytics skills. Same bar as Session 1: not "$500-3K/mo of side money" but a solo-buildable path with a credible route to **$8-15K+/mo** — full-time-salary-replacement income — within 12-24 months.

## Ground rules for every idea in this series
- **Solo-buildable start.** One person, evenings/weekends, no funding, no cofounder required to get the first version live.
- **Realistic path to $8-15K+/mo**, not a side-money ceiling — every idea states the math (customer/claim/placement count x price point) plainly, no TAM hand-waving.
- **Time to first dollar < 90 days.** Long enterprise sales cycles are disqualifying by default.
- **Named distribution channel** for the first 10 customers *and* a credible path to the next 10x.
- **Boring is fine.** Low-glamour, real-pain problems beat trendy ones.
- **No repeats.** Nothing below overlaps a concept already covered across Session 1 of this series, `side-income-ideas/`, or `discovered-problems/`. This session leans further into pricing models that support high per-transaction value with small customer counts — **contingency fees, placement fees, and subscription+sponsorship media** — rather than another flat-rate retainer or SaaS subscription, since that's what lets a handful of transactions a month clear the $8-15K/mo bar solo.

---

## Ideas

### 1. Storm/Fire Insurance Claim Documentation & Maximization Service
**Problem:** Homeowners after storm, hail, or fire damage typically accept the insurer's first settlement offer because they don't know how to document damage properly or negotiate, and insurers are financially incentivized to lowball — the gap between the initial offer and a properly documented/negotiated claim is often 30-60% of the payout, money the homeowner never sees.
**What to build:** A service (backed by a lightweight photo/damage-documentation app and a repair-cost benchmarking lookup against regional pricing data) that helps homeowners document damage thoroughly and negotiate with the insurer — directly, or via a licensed public-adjuster partner where state law requires it — charging a contingency fee on the amount recovered above the insurer's initial offer.
**Skill fit:** Direct on the software half (documentation capture, cost-estimate benchmarking, claim timeline tracking); the negotiation/adjusting work may require a state public-adjuster license or a licensed partner, the main non-technical lift.
**MVP scope:** 2-3 weekends for a photo/document capture app plus a repair-cost benchmarking lookup; the negotiation itself is manual service work, not something to automate in v1.
**Time to first $:** 30-45 days after a storm event in one region — target homeowners directly after a hail/wind event via storm-tracking alerts and local Facebook/Nextdoor groups in the affected area; contingency pricing removes any upfront-cost objection.
**Income ceiling (realistic, with math):** $1,500-3,000 average contingency fee per claim (10-15% of a typical $15-25K recovered increase); 4-6 claims/mo once one storm-affected region is worked = **$8-15K/mo**, concentrated around storm-season spikes rather than a flat monthly rate.
**Why this can go beyond side money:** Contingency pricing ties income directly to claim size, not to a subscription price a small customer will tolerate — a single well-documented claim can be worth more than 6 months of any SaaS tool's revenue from one customer, and each storm event creates a fresh, geographically concentrated demand spike that's straightforward to target.
**Biggest risk:** Public-adjuster licensing rules vary sharply by state and some restrict who can negotiate a claim for a fee — confirm licensing requirements in the target state before taking a negotiation fee, and structure the offering as documentation-plus-referral to a licensed adjuster partner where solo operation isn't legally permitted.
**Growth path:** Side project → work one storm event in one metro, partnering with a licensed adjuster if required, proving the documentation-plus-negotiation workflow end to end. Replaces-part-time-income → follow 2-3 storm events per season across a wider region using storm-tracking data to target outreach (~$6-8K/mo averaged across the season). Replaces-full-time-salary → build a referral network of contractors/roofers who see damage first and refer homeowners for a fee split, turning storm response from "chase the news" into an inbound pipeline reaching $10-15K/mo across a full storm season.

---

### 2. Independent Pharmacy Reimbursement Intelligence Newsletter + Benchmarking Subscription
**Problem:** Independent pharmacies are being squeezed out of business by Pharmacy Benefit Manager (PBM) reimbursement rates often below the pharmacy's own drug acquisition cost, but individual owners have no visibility into whether their specific rates are in line with peers or a clear signal of which PBM contracts to renegotiate or drop.
**What to build:** A paid intelligence product combining (a) a newsletter tracking PBM policy changes, reimbursement trends, and state pharmacy-advocacy wins, and (b) an anonymized benchmarking subscription where pharmacies submit their own reimbursement data (by drug/PBM) and see how their rates compare to an aggregated peer baseline, flagging specific underwater contracts.
**Skill fit:** Direct — data aggregation and the benchmarking/comparison engine is core data-analytics work; the newsletter is a research/writing lift, not an engineering one.
**MVP scope:** 2-3 weekends for the data-submission form and benchmarking logic for a starter set of common drugs/PBMs; the newsletter starts manually written.
**Time to first $:** 45-60 days — distribute the free newsletter through independent pharmacy owner Facebook groups and the National Community Pharmacists Association (NCPA) network to build a list, then convert a portion to the paid benchmarking tier once submitted data makes the comparison meaningful.
**Income ceiling (realistic, with math):** $49-99/mo subscription x 100-150 pharmacies = $5-15K/mo, plus $1,500-3,000/mo per sponsor (pharmacy software vendors, wholesalers, GPOs wanting this exact underserved, high-intent audience) for 2-3 sponsorship slots — comfortably into **$8-15K/mo** once both are filled.
**Why this can go beyond side money:** Combines a subscription product with a media/sponsorship stream serving the same underserved, highly motivated audience — independent pharmacy owners currently fighting for survival make both "am I being underpaid" and "reach this exact audience" easy sells, unlike a broad SaaS tool competing on features alone.
**Biggest risk:** Getting enough pharmacies to submit real reimbursement data early enough for the benchmark to be meaningful is a cold-start problem — seed it with published PBM reimbursement studies and a small design-partner cohort before opening the subscription broadly.
**Growth path:** Side project → free newsletter plus a design-partner cohort of 10-15 pharmacies submitting data manually. Replaces-part-time-income → paid benchmarking live, 40-60 subscribing pharmacies plus the first sponsor slot filled (~$4-6K/mo). Replaces-full-time-salary → 100-150 subscribing pharmacies nationally plus 2-3 recurring sponsor slots, with NCPA or state pharmacy associations as an ongoing low-cost distribution partner.

---

### 3. Freight Detention & Accessorial Charge Recovery Audit
**Problem:** Small-to-mid trucking fleets and owner-operators are frequently owed detention pay and accessorial charges (long load/unload waits, layover, extra stops) that shippers and brokers routinely don't pay unless specifically invoiced and disputed — most small carriers lack the back-office time to track and fight for these charges, leaving real money on the table on nearly every load.
**What to build:** An audit service (with a tool ingesting a carrier's rate confirmations, BOLs, and ELD/detention-timestamp data) that identifies underbilled detention/accessorial charges per load, generates dispute documentation, and files the recovery claim with the broker/shipper on the carrier's behalf, charging a contingency percentage of what's actually recovered.
**Skill fit:** Direct — a data-matching/reconciliation problem (rate confirmation terms vs. ELD timestamps vs. what was actually invoiced), squarely in the data-analytics skillset; the accessorial-charge conventions are standard and well-documented industry knowledge to pick up.
**MVP scope:** 3-4 weekends to build the ingestion/reconciliation pipeline for common ELD export formats and rate-confirmation templates, plus a dispute-letter generator.
**Time to first $:** 45-60 days — pitch small fleet owners (5-30 trucks) and owner-operators via trucking Facebook groups and owner-operator associations; "no recovery, no fee" removes the adoption barrier entirely.
**Income ceiling (realistic, with math):** 20-30% contingency fee on recovered amounts; a fleet with 10-15 trucks typically has $2,000-5,000/mo in unrecovered detention/accessorial charges, so 8-12 fleet clients at a 25% average contingency = **$8-14K/mo** once running consistently.
**Why this can go beyond side money:** Contingency pricing scales with the fleet's own load volume and rates, not a flat subscription fee — a single active mid-size fleet client can be worth 10-20 small-vertical SaaS customers combined, and "no recovery, no fee" makes the first sale nearly frictionless.
**Biggest risk:** Recovery rates depend heavily on how disputes actually resolve with brokers/shippers, which varies by relationship and leverage — start with carriers who have clean, well-documented rate confirmations and ELD data rather than the messiest back offices, to keep early recovery rates high enough to prove the model.
**Growth path:** Side project → 2-3 fleet clients, fully manual audit-and-dispute process, proving real dollars recovered. Replaces-part-time-income → 5-6 fleet clients, ingestion pipeline handling common data formats automatically so turnaround drops from days to hours (~$5-8K/mo). Replaces-full-time-salary → 10-12 fleet clients plus a referral relationship with a trucking association or ELD/fuel-card vendor treating this as a value-add for their existing base, pushing recovered-fee revenue past $10-14K/mo.

---

### 4. Blue-Collar Trade Shortage Placement Agency (e.g., diesel mechanics or crane operators)
**Problem:** Trades facing acute labor shortages (diesel/heavy-equipment mechanics, crane operators, industrial electricians) have openings sitting unfilled for months because generic job boards and even trade-specific recruiters aren't actually sourcing candidates who hold the right certifications and are open to relocating for the pay premium these roles command.
**What to build:** A tech-enabled staffing/placement operation for one specific shortage trade — a sourcing pipeline aggregating certification databases, union hall postings, and trade-school graduate networks into a real candidate pool, plus a lightweight matching/outreach tool — monetized the way staffing agencies always have: a placement fee (15-20% of first-year salary) paid by the hiring employer, not a subscription.
**Skill fit:** Direct on the sourcing/data side (the same data-aggregation skillset used elsewhere in this series, applied to candidate data instead of business/property data); the employer relationship and candidate vetting is a learned service skill, not a technical one.
**MVP scope:** 3-4 weekends for the candidate-sourcing pipeline and a simple matching/tracking tool for one trade; placement itself (screening calls, employer relationships) is manual by design.
**Time to first $:** 60-90 days — real hiring cycles make this slower than a software sale, but a single placement fee is large enough that 1-2 placements in the first 90 days validates the model; distribution is direct outreach to employers with known open shortage-role postings via industry job boards and trade association employer directories.
**Income ceiling (realistic, with math):** A shortage-trade placement (diesel mechanic, crane operator) typically commands $60-90K first-year salary; a 15-20% placement fee is $9,000-18,000 per hire — just 1-2 placements/mo reaches **$9-18K/mo**, the highest per-transaction value in this series.
**Why this can go beyond side money:** Placement fees price against what an employer is desperate to pay for a hard-to-fill role, not what a small business tolerates for a software subscription — the one model here where a single transaction alone can exceed a full month's target income.
**Biggest risk:** A shortage trade's candidate pool can dry up fast once the same small pool of qualified people gets placed — build ongoing top-of-funnel relationships with the trade schools/certification programs producing new candidates every semester, rather than treating sourcing as a one-time build.
**Growth path:** Side project → first 1-2 placements in one trade/one region, entirely manual sourcing and screening, proving the fee economics. Replaces-part-time-income → 3-4 placements/mo once a repeatable pipeline and a few repeat-employer relationships exist (~$9-12K/mo, lumpy month to month). Replaces-full-time-salary → expand to a second shortage trade or region reusing the same sourcing pattern, smoothing the lumpiness across two verticals.

---

### 5. Cannabis/Hemp Retail Compliance-as-a-Service Retainer
**Problem:** Licensed cannabis and hemp retailers operate under state seed-to-sale tracking mandates, packaging/labeling rules, and audit requirements that change frequently and vary sharply by state — a single compliance failure can mean a suspended or revoked license, an existential risk for a small dispensary, but most small operators can't afford (or don't know they need) a dedicated compliance specialist.
**What to build:** A compliance monitoring and audit-prep retainer: a tool tracking a retailer's seed-to-sale system data (via existing Metrc/BioTrack APIs) against current state regulatory requirements, flagging discrepancies before a state audit does, maintaining a regulatory-change alert feed for the retailer's specific state, and reviewing documentation ahead of scheduled inspections.
**Skill fit:** Direct — a rules-engine-plus-data-monitoring problem (matching operational data against a structured ruleset and flagging discrepancies), the same monitoring pattern used elsewhere in this series, applied to a new regulatory domain most small operators badly need but can't easily hire for.
**MVP scope:** 3-4 weekends to build the discrepancy-checking rules engine for one state's requirements plus a regulatory-change alert feed, integrating with the seed-to-sale platforms retailers already use.
**Time to first $:** 45-60 days — reach licensed retailers directly through state cannabis retailer associations and cannabis-industry Facebook/LinkedIn groups, where "avoid losing your license" is an immediately legible, high-stakes pitch.
**Income ceiling (realistic, with math):** $600-1,000/mo retainer per retailer (a fraction of a dedicated compliance hire, trivial against the cost of a suspended license); 12-18 retailers in one or two states = **$8-15K/mo**.
**Why this can go beyond side money:** The stakes per customer (license suspension/revocation) support a retainer price far above a typical small-business SaaS tool, because the cost of getting it wrong isn't inconvenience, it's the business itself — that underwrites a much higher price tolerance than most solo-buildable niches.
**Biggest risk:** Cannabis regulation varies enormously by state and changes often, so a rules engine built for one state doesn't transfer directly — launch fully correct in one state, clearly scoped as a compliance aid the retailer's own counsel still reviews, before expanding state by state rather than attempting shallow multi-state coverage early.
**Growth path:** Side project → one state's rules fully built, 5-8 retailers onboarded via a state cannabis retailer association, manual discrepancy review. Replaces-part-time-income → 12-15 retailers in that state plus the regulatory-alert feed running automatically, freeing time to build a second state's ruleset (~$7-9K/mo). Replaces-full-time-salary → 2-3 states covered, 25-30 retailers total, state associations serving as an ongoing distribution channel for each newly-covered state.

---

## Scoring Summary (this session)

| # | Idea | Model | MVP effort | Time to first $ | Income ceiling (main-income path) |
|---|------|-------|------------|------------------|-------------------------------------|
| 1 | Storm/fire insurance claim maximization | Contingency fee | 2-3 weekends | 30-45 days | $8-15K/mo (seasonal) |
| 2 | Independent pharmacy reimbursement intel | Subscription + sponsorship | 2-3 weekends | 45-60 days | $8-15K/mo |
| 3 | Freight detention/accessorial recovery audit | Contingency fee | 3-4 weekends | 45-60 days | $8-14K/mo |
| 4 | Blue-collar trade shortage placement agency | Placement fee | 3-4 weekends | 60-90 days | $9-18K/mo (lumpy) |
| 5 | Cannabis/hemp retail compliance retainer | Retainer | 3-4 weekends | 45-60 days | $8-15K/mo |

---

## This Session's Pick: Start With #5, Track #4 as the Highest-Ceiling Bet

**Steadiest, clearest recurring path:** Idea #5 (cannabis/hemp compliance retainer) has the most predictable month-to-month revenue of this batch — a flat retainer rather than a contingency fee or lumpy placement fee — a clean association-based channel, and stakes (license survival) high enough to support a well-above-market retainer price without a long sales cycle.

**Highest per-transaction ceiling:** Idea #4 (trade shortage placement agency) has the highest single-transaction value in this series ($9K-18K per placement), but real hiring cycles make it slower and lumpier than a retainer — best run as a parallel bet once idea #5's retainer base gives a revenue floor to smooth out placement-to-placement gaps, rather than as the sole first bet.

Running #5 as the primary build (predictable, association-channel-driven, high per-customer stakes) while sourcing the first 1-2 placements for #4 in parallel mirrors last session's pairing of a steady build with a higher-variance, higher-ceiling bet running alongside it.

---

## Files Created (2 sessions - 10 ideas)
1. `2026-07-29-main-income-v1.md` (5 ideas: managed retainer, data API, acquisition, education+retainer models)
2. `2026-07-29-main-income-v2.md` (5 ideas: contingency fee, subscription+sponsorship, and placement fee models)

**Total: 10 ideas across 2 sessions**

**Cron Loop:** `0 */5 * * *` continues — each session adds new solo-startable ideas with a credible, math-backed path to full-time-salary-replacement income, spanning new sectors and business models, never repeating a concept already covered in this series, `side-income-ideas/`, or `discovered-problems/`.
