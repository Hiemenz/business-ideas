# Main Income Ideas - 2026-07-30 (Session 4)

## Who this is for
Builder profile: 29, software engineering + data analytics skills. Same bar as Sessions 1-3: not "$500-3K/mo of side money" but a solo-buildable path with a credible route to **$8-15K+/mo** — full-time-salary-replacement income — within 12-24 months.

## Ground rules for every idea in this series
- **Solo-buildable start.** One person, evenings/weekends, no funding, no cofounder required to get the first version live.
- **Realistic path to $8-15K+/mo**, not a side-money ceiling — every idea states the math (claim/report/flip/deal count x price point) plainly, no TAM hand-waving.
- **Time to first dollar < 90 days.** Long enterprise sales cycles are disqualifying by default.
- **Named distribution channel** for the first 10 customers *and* a credible path to the next 10x.
- **Boring is fine.** Low-glamour, real-pain problems beat trendy ones.
- **No repeats.** Nothing below overlaps a concept already covered across Sessions 1-3 of this series, `side-income-ideas/`, or `discovered-problems/`. Sessions 1-3 leaned heavily on contingency/finder's-fee models (insurance, freight, VA, unclaimed property); this session pulls back to just one and introduces two mechanics not yet used in this series — **flat fee-per-engagement (appraisal) and principal-trading arbitrage** — alongside a packaging-fee-plus-success-fee hybrid and a second brokerage-commission idea in a fresh vertical.

---

## Ideas

### 1. Class-Action Settlement Claims Filing Service for Small Businesses
**Problem:** Small and mid-size businesses are eligible class members in many commercial class-action settlements (payment-processor interchange-fee settlements, software antitrust settlements, price-fixing settlements for common business inputs) worth real money, but almost never file because the notice gets buried in email, proof-of-purchase requirements are confusing, and deadlines pass unnoticed — the large majority of eligible business claims go unfiled, and unclaimed funds simply revert.
**What to build:** A monitoring-and-filing service, backed by a tool tracking open commercial class-action settlements, their eligibility criteria, and filing deadlines, that matches a business's own purchase/transaction history against active settlements, prepares and files the claim before the deadline, and charges a contingency fee (20-30%) of whatever the business actually receives.
**Skill fit:** Direct — tracking settlement databases/eligibility rules and matching against transaction records is a structured-data problem; no legal argument is made, only accurate filing against published, non-negotiable settlement terms.
**MVP scope:** 2-3 weekends for a settlement-tracking database (many administrators publish eligibility/deadline data publicly) plus a claim-preparation workflow for the first few active settlements.
**Time to first $:** 45-75 days depending on the settlement's own payout timeline — distribute through small-business accountant/bookkeeper referral relationships (they see the transaction records that prove eligibility) and small-business owner Facebook/LinkedIn groups.
**Income ceiling (realistic, with math):** Average business claim payout runs $500-8,000 depending on the settlement and transaction volume; a 25% average fee on 15-25 filed claims/mo across several concurrent open settlements = **$3-15K/mo**, reaching the top once multiple settlements are tracked and filed simultaneously.
**Why this can go beyond side money:** Volume compounds because settlements are constantly opening and closing, not a one-time market — and accountant/bookkeeper referral partners see every client's transaction records, making them a uniquely efficient channel to identify eligible businesses at scale.
**Biggest risk:** Payout timing is entirely on the settlement administrator's schedule (often 6-18 months after filing), creating a real cash-flow lag between filing effort and fee collection — run several settlements' claim cycles concurrently and staggered from the start so payouts arrive on a rolling basis rather than betting on one settlement's timeline.
**Growth path:** Side project → track and file for 2-3 open settlements, 10-15 client businesses via one accountant referral relationship. Replaces-part-time-income → 5-6 concurrent settlements tracked, 40-60 client businesses in the pipeline, 2-3 accountant/bookkeeper referral partners (~$5-8K/mo as payouts arrive on a rolling basis). Replaces-full-time-salary → a broader accountant referral network across a metro plus automated eligibility-matching against a growing settlement database, payouts from many concurrent settlements smoothing into a steadier $10-15K/mo.

---

### 2. Used Heavy/Industrial Equipment Appraisal-as-a-Service
**Problem:** Lenders, insurers, estate/divorce attorneys, and buyers/sellers of used industrial and construction equipment regularly need a defensible valuation report (loan collateral assessment, insurance claim, estate settlement, purchase negotiation), but certified equipment appraisers are few, slow, and expensive — especially for small-ticket equipment that doesn't justify a $2,000+ traditional appraisal engagement.
**What to build:** A data-driven appraisal service backed by a comparables database (aggregating auction results, dealer listings, and completed-sale data across major equipment categories) and a report-generation tool producing a structured valuation report with methodology and supporting comps, delivered faster and cheaper than a traditional appraiser for small-to-mid-ticket equipment.
**Skill fit:** Direct — the comps database and valuation-methodology engine is a data-analytics problem (aggregating/normalizing pricing data across sources, applying depreciation/condition adjustments); no credential required for most categories, though some lending contexts may require a credentialed appraiser designation added later.
**MVP scope:** 3-4 weekends to build the comps-aggregation pipeline for 3-5 common equipment categories (forklifts, construction equipment, restaurant equipment) plus a report template/generator.
**Time to first $:** 30-45 days — distribute directly to equipment-finance lenders, insurance adjusters, and estate/divorce attorneys who regularly need these reports and actively want a faster, cheaper alternative to traditional appraisers; speed is a real differentiator.
**Income ceiling (realistic, with math):** $300-1,200 per report depending on equipment complexity; 15-25 reports/mo once referral relationships are running = **$5-25K/mo**, comfortably clearing $8-15K/mo at moderate volume.
**Why this can go beyond side money:** Each report is priced per-engagement against what a professional appraisal service already charges, not a small-business subscription budget, and volume scales directly with lender/attorney/insurer referral relationships, not the size of any single customer.
**Biggest risk:** Some lending/legal contexts require a credentialed appraiser (e.g., ASA-certified) for evidentiary purposes — scope the initial service to contexts that don't require formal credentialing (internal lender risk assessments, negotiation support, insurance pre-claim estimates) while pursuing a credential in parallel to unlock higher-stakes engagements later.
**Growth path:** Side project → 5-10 reports/mo for one or two equipment categories, sourced through direct outreach to local equipment-finance lenders. Replaces-part-time-income → 15-20 reports/mo across 3-4 categories, referral relationships with 2-3 attorneys and an insurance adjuster established (~$6-10K/mo). Replaces-full-time-salary → credentialing pursued to unlock higher-stakes lending engagements, referral network expanded regionally, report volume and average report value both rising toward $12-15K/mo.

---

### 3. Government/Municipal Surplus Auction Arbitrage
**Problem:** Government agencies, municipalities, and utilities regularly auction off surplus vehicles, machinery, and equipment (GovDeals, PublicSurplus, and hundreds of individual municipal auction sites) at prices frequently well below private-market resale value, because bidder awareness is thin and listings are scattered across dozens of disconnected auction platforms with no unified way to spot the systematically underpriced lots.
**What to build:** A monitoring tool aggregating active listings across major government/municipal surplus auction platforms, cross-referencing each lot against private-market resale comps (dealer listings, completed sales data) to flag listings priced meaningfully below resale value and rank opportunities by expected margin — used personally to identify, bid on, win, and resell equipment, rather than sold as a tool to others.
**Skill fit:** Direct — a data-aggregation and comps-matching problem, the same core skillset used elsewhere in this series, but here the builder is the principal trading on the signal rather than selling the signal or brokering someone else's deal.
**MVP scope:** 2-3 weekends to build the listing-aggregation and comps-matching pipeline for 2-3 equipment categories with liquid resale markets (vehicles, forklifts, generators); buying/reselling itself is manual operating work, not something to automate in v1.
**Time to first $:** 30-45 days — the monitoring tool identifies the first underpriced lot, capital is put up to win the auction, and resale happens through existing channels (dealer networks, Facebook Marketplace, equipment resale sites) for that category.
**Income ceiling (realistic, with math):** A typical underpriced-lot flip nets $500-3,000 in margin after resale, transport, and minor refurbishment costs; 6-10 flips/mo once the monitoring tool reliably surfaces opportunities and resale channels are established = **$5-20K/mo**, with margin per flip and flip volume both improving as category expertise deepens.
**Why this can go beyond side money:** As the principal buying and reselling directly, all margin is captured rather than a brokerage percentage of someone else's deal — capital availability, not customer acquisition, becomes the main scaling constraint, and capital compounds as early flips fund larger/more numerous later ones.
**Biggest risk:** Requires real working capital tied up in inventory between purchase and resale, and a flip can lose money if the resale market moves or equipment has undisclosed mechanical issues — start with categories that have deep, liquid, fast-moving resale markets (common vehicles, generators) rather than anything requiring specialized buyers or slow-moving niche equipment, to keep capital cycling quickly.
**Growth path:** Side project → 2-3 flips/mo in one equipment category, using personal savings as working capital, learning the category's true resale comps and refurbishment needs firsthand. Replaces-part-time-income → 5-6 flips/mo across 2 categories, working capital recycling faster as resale channels and category expertise mature (~$5-8K/mo). Replaces-full-time-salary → 8-10 flips/mo across 3 categories, working capital scaled from reinvested profits (avoiding outside financing), monitoring tool automated enough to surface daily opportunities without full-time manual searching.

---

### 4. SBA Loan / Grant Application Packaging Service for Small Manufacturers
**Problem:** Small manufacturers seeking SBA 504/7(a) financing or state manufacturing grants for equipment purchases or facility expansion routinely get denied or delayed not because they're ineligible, but because the loan/grant packaging (financial statement organization, business plan narrative, cash-flow projections, use-of-funds documentation) is done poorly — a well-known failure point lenders and grant reviewers see constantly, but small manufacturers rarely have in-house finance staff who know how to package an application properly.
**What to build:** A loan/grant packaging service, backed by a tool that ingests a manufacturer's financial statements and generates the structured projections, ratios, and narrative sections lenders/reviewers expect, formatted to the specific SBA program or grant's requirements, preparing complete, lender-ready application packages, charging a flat packaging fee plus a smaller success fee contingent on approval.
**Skill fit:** Direct on the data/document-generation side (financial statement analysis and structured projection/narrative generation is squarely the data-analytics skillset); lender/program-requirements knowledge is a learnable domain skill, and SBA packaging is a recognized role that doesn't require a professional credential to practice.
**MVP scope:** 3-4 weekends to build the financial-statement ingestion and projection/narrative generation tool for the most common SBA program (7(a) or 504) plus a document-assembly template matching that program's exact requirements.
**Time to first $:** 45-60 days — distribute through relationships with SBA-preferred lenders (loan officers routinely refer applicants who need packaging help, since a well-packaged application is less work for them too) and state manufacturing association member directories.
**Income ceiling (realistic, with math):** $2,000-5,000 flat packaging fee plus a 1-2% success fee on approved loan amounts (often $250K-1M+ for equipment/facility financing, adding $2,500-20,000 per approved deal); 4-6 packaged applications/mo = **$8-20K/mo** between flat fees and success fees on approved deals.
**Why this can go beyond side money:** The success fee is priced against loan/grant amounts an order of magnitude larger than a small manufacturer's software budget, and SBA lenders are a self-reinforcing referral channel — a loan officer who sees one well-packaged application refers the next borrower who needs the same help.
**Biggest risk:** Success-fee income depends on actual loan/grant approval, which isn't fully in the packager's control — price the flat packaging fee high enough on its own to cover the real time investment regardless of outcome, treating the success fee as upside rather than the core of the pricing model.
**Growth path:** Side project → 2-3 packaged applications/mo sourced through one SBA-preferred lender relationship, fully manual financial analysis and document generation. Replaces-part-time-income → 4-5 applications/mo across 2-3 lender relationships, the generation tool speeding up turnaround so more applications fit in the same hours (~$6-10K/mo). Replaces-full-time-salary → lender referral network expanded regionally plus a second SBA program/grant type added, 6-8 applications/mo with a growing base of approved-deal success fees compounding on top of flat packaging fees.

---

### 5. Structured Settlement Secondary-Market Brokering
**Problem:** Recipients of structured settlements (from personal injury lawsuits) or lottery winnings paid out over time sometimes need a lump sum today and can legally sell future payments on an established secondary market — but they typically get one quote from whichever factoring company found them first (often through aggressive TV/direct-mail advertising) and have no easy way to shop competing offers, routinely leaving significant money on the table in a market with wide pricing variance between factoring companies.
**What to build:** A brokering platform that takes a seller's payment-stream details, submits the opportunity to multiple licensed factoring companies simultaneously, and presents competing offers side by side — functioning as a rate-shopping broker for the seller, taking a referral/broker commission from the winning factoring company (the standard arrangement in this market) rather than charging the seller directly.
**Skill fit:** Direct — building the multi-quote submission/comparison workflow and the factoring-company relationship database is standard application engineering; no specialized financial licensing is typically required to operate as a broker/referral source in this market, and court approval of the underlying sale (required by law in most states) is handled by the factoring company, not the broker.
**MVP scope:** 2-3 weekends for a payment-stream intake form and a multi-factoring-company quote-request/comparison workflow; establishing factoring-company relationships (5-8 companies willing to receive and quote referred deals) is the main non-technical setup work.
**Time to first $:** 45-60 days — reach sellers directly through search-intent content and ads around "sell my structured settlement" (a well-established high-intent search category) and through referral relationships with financial advisors/CPAs who occasionally have clients considering this.
**Income ceiling (realistic, with math):** Broker commissions typically run 2-4% of the payment stream's purchase price; a typical deal size of $30,000-150,000 in purchased value generates $600-6,000 in commission, and 3-6 closed deals/mo = **$5-20K/mo**, with deal size doing most of the work.
**Why this can go beyond side money:** Commission is priced against the purchase value of a multi-year payment stream, not a subscription — a handful of closed deals a month, sourced from a well-established high-intent search category, clears the main-income bar without a large customer base.
**Biggest risk:** A heavily regulated, consumer-protection-sensitive market (courts must approve each sale, and some sellers are financially vulnerable) — operate strictly as a neutral rate-shopping intermediary, disclose commission arrangements transparently, and never pressure a seller toward a sale, both because it's the right thing to do and because regulatory/reputational risk here is real.
**Growth path:** Side project → first factoring-company relationships established (5-8 companies), first 2-3 deals closed through direct search-intent content, proving the multi-quote model beats a single-quote pitch. Replaces-part-time-income → 4-5 deals/mo once search-intent content ranks consistently and 1-2 financial-advisor referral relationships are active (~$5-9K/mo). Replaces-full-time-salary → broader factoring-company panel (10-15 companies for better competitive quotes) plus an expanded referral network, 6-8 deals/mo with a stronger reputation as the trusted neutral broker in the category.

---

## Scoring Summary (this session)

| # | Idea | Model | MVP effort | Time to first $ | Income ceiling (main-income path) |
|---|------|-------|------------|------------------|-------------------------------------|
| 1 | Class-action settlement claims filing (SMBs) | Contingency fee | 2-3 weekends | 45-75 days | $3-15K/mo |
| 2 | Used industrial equipment appraisal | Flat fee per report | 3-4 weekends | 30-45 days | $5-25K/mo |
| 3 | Government surplus auction arbitrage | Principal trading margin | 2-3 weekends | 30-45 days | $5-20K/mo |
| 4 | SBA loan/grant application packaging | Packaging fee + success fee | 3-4 weekends | 45-60 days | $8-20K/mo |
| 5 | Structured settlement secondary-market brokering | Broker commission | 2-3 weekends | 45-60 days | $5-20K/mo |

---

## This Session's Pick: Start With #2, Track #3 as the Capital-Leverage Parallel Bet

**Fastest, steadiest ramp:** Idea #2 (equipment appraisal-as-a-service) has the shortest time to first dollar in this batch (30-45 days), a flat per-report fee with no dependency on court approval, loan-committee timelines, or settlement payout schedules, and a channel (equipment-finance lenders, attorneys, insurers) that's easy to reach directly — the cleanest, most predictable build this session.

**Highest-leverage parallel bet:** Idea #3 (surplus auction arbitrage) doesn't compete for the same weekly hours once the monitoring tool is built — sourcing, bidding, and reselling happens on its own cadence — and captures full margin as principal rather than a commission slice, making it a strong complement once #2's report income covers working capital for the first few flips.

Running #2 as the primary build (fast ramp, clean per-engagement pricing, low dependency on third-party timelines) while using early appraisal income to fund the first auction flips for #3 continues this series' established pattern of pairing a steady build with a higher-variance, higher-ceiling bet running alongside it.

---

## Files Created (4 sessions - 20 ideas)
1. `2026-07-29-main-income-v1.md` (5 ideas: managed retainer, data API, acquisition, education+retainer models)
2. `2026-07-29-main-income-v2.md` (5 ideas: contingency fee, subscription+sponsorship, and placement fee models)
3. `2026-07-29-main-income-v3.md` (5 ideas: regulated contingency fee, marketplace take-rate, brokerage commission, retainer, finder's fee models)
4. `2026-07-30-main-income-v4.md` (5 ideas: contingency fee, flat fee-per-report, principal-trading arbitrage, packaging+success fee, brokerage commission models)

**Total: 20 ideas across 4 sessions**

**Cron Loop:** `0 */5 * * *` continues — each session adds new solo-startable ideas with a credible, math-backed path to full-time-salary-replacement income, spanning new sectors and business models, never repeating a concept already covered in this series, `side-income-ideas/`, or `discovered-problems/`.
