# Main Income Ideas - 2026-08-18 (Session 99)

## Who this is for

A 29-year-old software engineer with data analytics skills who wants to replace a full-time salary — targeting $8-15K+/mo — within 12-24 months, building solo in evenings and weekends with no outside funding. Every idea below needs to produce its first dollar in under 90 days and needs a named, reachable distribution channel, not a vague "market it online" plan.

## Ground rules for every idea in this series

- Solo-buildable start.
- Realistic path to $8-15K+/mo
- Time to first dollar < 90 days.
- Named distribution channel
- No repeats. This session covers five regulated industries never addressed in this repo's prior 98 main-income sessions or its 93 side-income sessions: **environmental site assessment (Phase I/II ESA) consulting firms**, **IDD residential group homes / HCBS waiver providers**, **independent medical examiner (IME) coordination companies**, **dietary supplement contract manufacturers**, and **debt buyers (charged-off portfolio purchasers)**. None of these are re-skins of prior sessions: ESA firms are governed by ASTM E1527-21 and the EPA AAI Rule (40 CFR Part 312) — a landowner-liability-defense framework with no overlap with the mold, radon, or water-testing-lab ideas from earlier sessions. IDD group homes answer to state Developmental Disabilities agencies and the HCBS Settings Rule (42 CFR 441 Subpart G) — a different regulator and a different resident population than the assisted living, CCRC, adult day care, sober living, or behavioral-health-HIPAA ideas already in the repo. IME coordination companies operate under state workers'-comp-board IME physician registration rules (e.g., 12 NYCRR 300.2) — distinct from the DOT medical examiner/occupational health clinic idea (NRCME registry, physical exams for commercial drivers) and from the general insurance-claims-adjuster ideas already covered. Dietary supplement contract manufacturers operate under 21 CFR Part 111, a cGMP framework entirely separate from the FSMA Preventive Controls rule (21 CFR 117) used by the earlier FDA food-facility idea, and separate from the cosmetics-MoCRA and hemp-processor ideas already in the repo. Debt buyers are legally distinct from the third-party debt collection agencies covered in prior sessions — debt buyers own the receivable and face state debt-buyer-specific licensing (e.g., California's Fair Debt Buying Practices Act) and chain-of-title documentation duties that a pure collection agency working accounts on behalf of a creditor never faces.

---

## Ideas

### 1. Environmental Site Assessment (ESA) Consulting Firm — Phase I/II Portfolio & AAI Compliance Tracker

**Problem:** Environmental consulting firms performing Phase I Environmental Site Assessments for property transactions must comply with EPA's All Appropriate Inquiries Rule (40 CFR Part 312) and the ASTM E1527-21 standard to preserve CERCLA landowner liability defenses (Innocent Landowner, Bona Fide Prospective Purchaser, Contiguous Property Owner). Each report has strict data-currency rules — environmental database records and the report itself have a defined "shelf life" (ASTM's 180-day/1-year update triggers, with a 135-day estimated-closing warning threshold) — and the signing "Environmental Professional" must meet 40 CFR 312.10 qualification criteria including active state licensure (e.g., Professional Geologist or PE) and CE hours. A 2-8 person ESA firm juggling 15-40 active projects tracks this across spreadsheets; a report that goes stale before closing, or an EP whose license lapses before signing, retroactively voids the client's liability defense.

**What to build:** Project portfolio dashboard by property address, assigned EP, and key AAI milestone dates (database order, site visit, interviews, draft/final report, client closing date) with automatic shelf-life countdown flags. EP credential tracker for state license and CE-hour status. A QA checklist mapped to ASTM E1527-21's required report sections so no element is missed before sign-off. A client-facing read-only status portal for real estate attorneys and lenders.

**Skill fit:** ASTM's required-elements structure and EPA's AAI rule text are public and highly structured — this is a deadline-engine and checklist-gate problem, not an environmental-science one.

**MVP scope:** Weekend 1: project/EP/milestone data model and shelf-life logic. Weekend 2: ASTM-mapped QA checklist and document upload. Weekend 3: client status portal and alerts. First 5-8 clients from state Professional Geologist board rosters and the Environmental Assessment Association (EAA) member directory, pitched with a free shelf-life audit of their current active project list.

**Time to first $:** 30-45 days — direct outreach to EAA member firms and state-geologist-board-listed small firms, offering a 14-day pilot on their live project list.

**Income ceiling (realistic, with math):** $549/mo per firm (up to 20 active projects) + $20/mo per additional project. At 15 clients averaging 25 active projects (5 over base): 15 × ($549 + 5×$20) = 15 × $649 = $9,735/mo. At 20 clients: 20 × $649 = $12,980/mo.

**Why this can go beyond side money:** Every real estate transaction that touches commercial or industrial property generates a new Phase I with its own fresh countdown clock, so usage never plateaus — it scales with the firm's deal volume, not with a one-time setup.

**Biggest risk:** A firm might treat the shelf-life countdown as a nice-to-have rather than something worth paying for monthly. The product prevents this by making the countdown the thing that keeps a $3,000-8,000 report from becoming worthless overnight — a failure mode every EP has personally lived through.

**Growth path:** Side project → 8 firms paying → replaces-part-time-income → 15 firms with SKU-style project-overage pricing → replaces-full-time-salary.

---

### 2. IDD Residential Group Home / HCBS Waiver Provider Compliance Tracker

**Problem:** Small operators running 1-6 residential group homes for individuals with intellectual/developmental disabilities must maintain state Developmental Disabilities agency facility licensure, enroll as HCBS waiver providers under 42 CFR 441 Subpart G, and comply with the federal HCBS Settings Rule. Ongoing obligations include annual/biennial license renewal and unannounced-survey readiness, per-resident Person-Centered Service Plan review deadlines, incident and critical-event reporting to the state's incident management system within mandated windows (often 24-72 hours by incident category), and direct support professional (DSP) medication-administration certification renewal plus training-hour compliance (many states require NADSP-aligned or state-specific curricula). A 3-6 home operator with 15-40 staff has no dedicated compliance officer; a missed incident-report deadline or a lapsed medication cert can trigger a state corrective action plan or license suspension.

**What to build:** Per-home license/survey-readiness tracker with renewal countdowns. Per-resident PCSP review calendar. Incident-report deadline tracker that starts counting down the moment an incident is logged, with escalating alerts. DSP roster with a training-hour ledger and medication-cert expiration tracking gated against shift assignment — a DSP whose med-cert lapsed can't be scheduled for a medication-pass shift.

**Skill fit:** State DDS provider manuals and incident-reporting timeline tables are public documents; this is a structured data model plus a deadline/scheduling-gate engine, well within reach of a developer with no clinical background.

**MVP scope:** 2-3 weekends for the home/license tracker, PCSP calendar, and DSP credential ledger with shift-gating. First clients from state DDS public provider directories combined with outreach through ANCOR (American Network of Community Options and Resources) state chapters.

**Time to first $:** 30-45 days via ANCOR state-chapter outreach and direct calls to DDS-listed small providers, leading with the med-cert shift-gating feature.

**Income ceiling (realistic, with math):** $449/mo per operator (up to 3 homes) + $99/mo per additional home. At 15 clients averaging 4.5 homes (1.5 over base): 15 × ($449 + 1.5×$99) = 15 × $597.50 = $8,962.50/mo. At 20 clients: 20 × $597.50 = $11,950/mo.

**Why this can go beyond side money:** Incident reports, PCSP reviews, and DSP recertification happen continuously and per-resident, so the compliance calendar never empties — every new resident and every new hire adds recurring obligations to track.

**Biggest risk:** An operator scheduling a decertified DSP for a medication-pass shift is the exact failure the product exists to prevent — the shift-gating rule turns a paper-tracking gap into a hard stop before it becomes a state citation.

**Growth path:** Side project → 10 operators → replaces-part-time-income → 18 operators with per-home overage pricing → replaces-full-time-salary.

---

### 3. Independent Medical Examiner (IME) Network Scheduling & Compliance Company

**Problem:** IME coordination companies dispatch independent medical examinations to a panel of contracted physicians on behalf of workers'-comp insurers, disability carriers, and auto no-fault claims administrators. Several states require the coordinating company or individual physicians to hold specific IME registration (e.g., New York Workers' Compensation Board IME registration under 12 NYCRR 300.2, renewed annually), and most workers'-comp systems impose statutory report-turnaround deadlines (commonly 30 days from exam date) plus scheduling-window requirements for offering the injured worker an exam date. A small IME company running 200-800 exams/month across 20-60 panel physicians has no systematic way to track which physicians' state registrations are current or which exams are approaching their statutory report deadline — a compliance risk and a client-retention risk at once, since insurers drop IME vendors who blow deadlines.

**What to build:** Physician panel roster with per-state IME registration/certification expiration tracking, gated against case assignment so a physician can't be assigned in a state where their registration has lapsed. Case-level scheduling and report-deadline tracker counting down from exam date to the statutory report-due date, with escalation alerts as the deadline nears. A client-facing on-time-report-percentage dashboard by physician, useful both for internal QA and as a sales differentiator with carriers.

**Skill fit:** State workers'-comp board IME regulations and deadline tables are public regulatory text — a scheduling-and-deadline engine plus a lightweight credential registry, both standard data-engineering work.

**MVP scope:** 2-3 weekends: physician roster with state-registration gating, case tracker with deadline countdown, on-time-percentage dashboard. First 5-8 clients via the SEAK IME conference exhibitor/attendee network and regional IME companies listed in state workers'-comp approved-vendor lists.

**Time to first $:** 30-45 days — SEAK network and state vendor-list outreach, offering a free audit of the physician panel's registration status.

**Income ceiling (realistic, with math):** $599/mo per IME company (up to 15 panel physicians, 300 exams/mo) + $25/mo per additional physician. At 10 clients averaging 25 physicians (10 over base): 10 × ($599 + 10×$25) = 10 × $849 = $8,490/mo. At 15 clients: 15 × $849 = $12,735/mo.

**Why this can go beyond side money:** Physician registrations expire on a rolling schedule and every new case adds a fresh statutory deadline, so the tracker's job never finishes — it scales directly with the company's exam volume.

**Biggest risk:** A physician assigned to a case in a state where their registration lapsed can invalidate the exam's legal standing entirely. The assignment gate makes that scenario structurally impossible rather than relying on office staff to remember 60 physicians' renewal dates across a dozen states.

**Growth path:** Side project → 8 IME companies → replaces-part-time-income → 14 companies with per-physician overage pricing → replaces-full-time-salary.

---

### 4. Dietary Supplement Contract Manufacturer cGMP & Facility Compliance Tracker

**Problem:** Small contract manufacturers producing vitamins, protein powders, and other dietary supplements for private-label brands must comply with FDA's dietary supplement cGMP regulation (21 CFR Part 111) — a framework distinct from conventional food cGMP (21 CFR 117) — requiring master manufacturing records and batch production records per SKU, component identity testing before use (a frequent FDA 483 citation point), finished-product specification testing, and equipment cleaning/calibration logs. Facilities must also separately maintain FDA Food Facility Registration, renewed biennially under FSMA, and operate a documented complaint-handling and serious-adverse-event-reporting system with a 15-business-day FDA reporting window once a reportable event occurs. A 10-30 employee contract manufacturer running 40-150 SKUs for rotating brand clients tracks master formulas and identity-test results across shared drives; a missing identity test or an expired scale calibration on a released batch can trigger an FDA warning letter or a forced recall.

**What to build:** SKU-level master manufacturing record and batch production record tracker with a pre-release checklist gate — component identity testing complete, in-process specs met, equipment calibration current — that blocks batch-release sign-off until every Part 111-required element is checked. Equipment calibration/cleaning log with due-date alerts. Facility-registration renewal countdown. Adverse-event intake log with the 15-business-day FDA reporting countdown.

**Skill fit:** 21 CFR Part 111's required-records structure is public and maps cleanly to a checklist/gate data model — no chemistry background needed, only the ability to encode a regulation's record-keeping requirements.

**MVP scope:** 2-3 weekends: MMR/BPR data model with pre-release gate, calibration log, facility-registration countdown, adverse-event tracker. First clients via the Natural Products Association (NPA) contract-manufacturer member list and supplement trade-show exhibitor directories, pitched with a free Part 111 gap-check against their current batch-record template.

**Time to first $:** 45-60 days — trade-show exhibitor list outreach plus NPA member directory cold email, leading with the batch-release gate as the pitch.

**Income ceiling (realistic, with math):** $699/mo per facility (up to 60 active SKUs) + $8/mo per additional SKU. At 10 clients averaging 90 SKUs (30 over base): 10 × ($699 + 30×$8) = 10 × $939 = $9,390/mo. At 15 clients: 15 × $939 = $14,085/mo.

**Why this can go beyond side money:** Every new SKU a facility contract-manufactures adds its own master formula and ongoing batch-release gate, so revenue grows with the client's own business growth, not just their headcount.

**Biggest risk:** Releasing a batch without complete component identity testing is the single most common Part 111 audit failure. The pre-release gate makes that release physically un-signable in the system until the record is complete.

**Growth path:** Side project → 6 facilities → replaces-part-time-income → 12 facilities with per-SKU overage pricing → replaces-full-time-salary.

---

### 5. Debt Buyer Portfolio & FDCPA/Reg F Compliance Tracker

**Problem:** Debt buyers — companies that purchase charged-off consumer debt portfolios — face a licensing and documentation regime distinct from third-party collection agencies. States including California (Fair Debt Buying Practices Act, Civil Code §1788.50 et seq.), New York, and Maryland impose debt-buyer-specific licensing or a duty to retain and produce chain-of-title documentation (original account agreement, bill of sale, full assignment history) before initiating collection or filing suit — a requirement that has sunk thousands of collection lawsuits when buyers couldn't produce it. Debt buyers must also comply with CFPB Regulation F's validation-notice and time-barred-debt disclosure requirements. A small debt-buying operation managing 15-60 purchased portfolios, each with thousands of accounts, tracks chain-of-title documents across a mix of seller data files and manual folders; missing documentation on a portfolio is a business-ending liability the moment a state AG or plaintiff's firm challenges it.

**What to build:** Portfolio-level intake tracker recording seller, purchase date, account count, and a chain-of-title document checklist that must be complete before any account in that portfolio is flagged as collection-eligible. State debt-buyer license tracker gated against which states' accounts can be actively worked. A Reg F validation-notice and time-barred-debt-disclosure compliance log per collection letter batch.

**Skill fit:** State debt-buyer statutes and Regulation F requirements are public regulatory text with a clear document-checklist structure — a document-completeness gate plus a license-jurisdiction matching problem, both standard data-engineering patterns.

**MVP scope:** 2-3 weekends: portfolio intake with chain-of-title gate, state license tracker gated against account state, Reg F disclosure log. First clients via the Receivables Management Association International (RMAI) member directory — the debt-buying industry's own trade association, which runs a Certified Receivables Compliance Professional credential, making its members unusually compliance-conscious.

**Time to first $:** 30-45 days — RMAI member directory outreach, leading with a free chain-of-title completeness audit on one sample portfolio.

**Income ceiling (realistic, with math):** $549/mo per debt buyer (up to 20 active portfolios) + $18/mo per additional portfolio. At 12 clients averaging 30 portfolios (10 over base): 12 × ($549 + 10×$18) = 12 × $729 = $8,748/mo. At 18 clients: 18 × $729 = $13,122/mo.

**Why this can go beyond side money:** Every new portfolio purchase resets the chain-of-title gate and adds a new set of state-licensing dependencies, so the tool's usage tracks the buyer's acquisition volume directly.

**Biggest risk:** A collection lawsuit filed on an account with an incomplete chain of title can be dismissed and expose the buyer to an FDCPA counterclaim. The collection-eligible flag makes that scenario impossible to reach without the documentation checklist being complete first.

**Growth path:** Side project → 8 debt buyers → replaces-part-time-income → 15 buyers with per-portfolio overage pricing → replaces-full-time-salary.

---

## Scoring Summary (this session)

| # | Idea | Model | MVP effort | Time to first $ | Income ceiling |
|---|------|-------|------------|------------------|-----------------|
| 1 | Environmental Site Assessment (ESA) consulting firm Phase I/II & AAI shelf-life compliance | Monthly retainer per firm (per-project add-on) | 2-3 weekends | 30-45 days | $9.74-12.98K/mo |
| 2 | IDD residential group home / HCBS waiver provider licensing & incident-report compliance | Monthly retainer per operator (per-home add-on) | 2-3 weekends | 30-45 days | $8.96-11.95K/mo |
| 3 | Independent medical examiner (IME) network physician registration & report-deadline compliance | Monthly retainer per IME company (per-physician add-on) | 2-3 weekends | 30-45 days | $8.49-12.74K/mo |
| 4 | Dietary supplement contract manufacturer 21 CFR Part 111 cGMP & batch-release compliance | Monthly retainer per facility (per-SKU add-on) | 2-3 weekends | 45-60 days | $9.39-14.09K/mo |
| 5 | Debt buyer chain-of-title & state debt-buyer licensing compliance | Monthly retainer per buyer (per-portfolio add-on) | 2-3 weekends | 30-45 days | $8.75-13.12K/mo |

---

## This Session's Pick: #4 for Highest Ceiling and Stickiness; #5 for Sharpest Single-Document Failure Mode

**Highest ceiling and stickiness:** Idea #4 (dietary supplement contract manufacturer) has the steepest per-SKU pricing lever in this session — a facility running 90+ SKUs for a rotating roster of brand clients pays for every new formula it takes on, so revenue compounds with the client's own growth rather than staying flat. The NPA member directory and supplement trade-show exhibitor lists give a concentrated, well-documented first 5-8 prospects, and the batch-release gate targets the single most-cited Part 111 audit failure (incomplete component identity testing), making the pitch immediately concrete to a plant manager who has lived through an FDA 483.

**Sharpest single-document failure mode:** Idea #5 (debt buyer) has the most binary, catastrophic failure condition of the five — a single missing bill-of-sale or assignment link in a chain-of-title can get a collection lawsuit dismissed and expose the buyer to an FDCPA counterclaim on that entire portfolio. RMAI's concentrated, compliance-literate membership (many holding the CRCP credential) makes for an unusually receptive first outreach list, since these operators already think in compliance-audit terms.

Idea #1 (environmental site assessment firms) rounds out the session as the highest-frequency compliance event: every Phase I report a firm issues starts its own shelf-life countdown clock, so a firm with a steady deal pipeline generates fresh, ongoing usage without any additional sales effort — a dynamic similar to Session 98's asbestos-abatement idea, but anchored in a completely different regulatory framework (ASTM/CERCLA liability defenses rather than emissions notification).

---

## Files Created (99 sessions - 495 ideas)
1-98. Sessions 1-98 — 490 ideas
99. `2026-08-18-main-income-v99.md` — 5 ideas: environmental site assessment (ESA) consulting firm Phase I/II & AAI compliance (monthly retainer), IDD residential group home / HCBS waiver provider licensing & incident-report compliance (monthly retainer), independent medical examiner (IME) network physician registration & report-deadline compliance (monthly retainer), dietary supplement contract manufacturer 21 CFR Part 111 cGMP & batch-release compliance (monthly retainer), debt buyer chain-of-title & state debt-buyer licensing compliance (monthly retainer)

**Total: 495 ideas across 99 sessions**
