# City Explorer: Gaps and Solutions

[Back to the City Explorer overview](../2026-11-14-city-explorer-badges-app.md) | [Focus and 4-week plan](01-focus-and-4-week-plan.md)

Second-pass fixes to unit economics, data sources, venue ROI, privacy, notifications, competition, safety and capacity. Numbers marked (assumption) are estimates.

---

## Remaining Gaps and Solutions

A second pass over the plan. Numbers marked **(assumption)** are planning estimates to replace with real data. Anything about third-party terms, prices or rules must be checked with the provider before you rely on it.

### 1. Unit economics were never calculated
**Fix:** Model both sides before building.

| Item | Assumption |
|---|---|
| Consumer price | $39/yr (about $3.25/mo) |
| Free-to-paid conversion | 5% of active free users |
| Cost per free subscriber (organic) | $1-3 |
| Cost per free subscriber (paid ads) | $4-8 |
| Messaging cost per user | $0.40/mo for SMS, near zero for email or push |
| Variable cost per paid user | about $0.60/mo including payments and messaging |
| Venue featured slot | $149/mo, 70% retention at 6 months |
| Fixed costs | Hosting, data, messaging, domain: about $200-350/mo |

**Reading it:** At a 5% conversion, a paying user costs $20-60 to acquire through paid ads, against about $39/yr revenue. Paid ads do not work for the consumer side, so grow it through email, partners and referrals. **Break-even is about 8 paying venues plus 100 paying users** to cover fixed costs. Venues are the income engine, as the main plan says, and must be proven first.

### 2. Where the place data comes from
Hand-curating 100-200 places works for a launch, but the plan never says how it scales or what is legal to use.
**Fix:**
- **Phase 1:** Hand-built list in one city, each place visited or checked by phone. This is also your quality edge.
- **Phase 2:** Venues add and update their own listings through the venue dashboard, with a monthly "still correct?" prompt.
- **Phase 3:** Add licensed data (for example a maps or places API or public city open-data feeds) for hours and addresses. Read each provider's terms on storage, caching and display, and price it, because per-request fees can exceed your revenue. Do not scrape sites that forbid it.
- **Events:** Pull from public city calendars and partner feeds, and let venues submit events.
- **Quality rule:** Every Thursday idea is re-verified (hours, open dates) within 7 days of sending.

### 3. Venues need proof of return on investment
The model depends on venues paying, but there is no sales process or attribution.
**Fix:**
- **Attribution:** A unique code or QR on the badge page ("show this at the counter") or a link-tracked reservation. Count only redeemed codes.
- **Pilot offer:** First 60 days at no fee, then $2-5 per redeemed visit. Hormozi style: "If we send you 20 visits you can count in 60 days, you keep us at $149/mo. If not, you pay nothing."
- **Venue report:** Monthly one-page email: visits, estimated spend (use the venue's average ticket), repeat visitors and the cost per visit.
- **Sales script:** Go in person to 30 independent venues, show last month's visits from the free list and ask for one featured slot.
- **Target venues first:** Places with empty weekday or off-peak hours, since they gain most from a new visitor.

### 4. Location and personal data
The app handles location history, who goes out with whom and relationship status.
**Fix (practical flags, confirm locally with a lawyer):**
- Collect the minimum: check-in at a badge location, not continuous tracking.
- Ask for location permission only at check-in time ("while using").
- Write a plain-language privacy policy covering what is stored, for how long and who sees it. Offer one-tap delete and export.
- Keep badge and passport pages private by default, and make sharing opt-in.
- **Messaging consent:** Get explicit opt-in for SMS, honor "STOP" immediately, and check carrier registration rules and costs for business texting in your country before sending at volume. Start with email and push if registration is a barrier.
- Do not sell user-level location data to venues. Share only aggregate counts and redeemed-code visits.

### 5. Notification fatigue
A Wednesday, Thursday, Friday and Saturday cadence can feel like nagging and cause unsubscribes.
**Fix:**
- Default to **2 messages a week** (Wednesday pick, Friday rescue only if nothing is locked). The others fire only when the user has taken an action.
- Let users choose their cadence and quiet days at intake.
- Auto-reduce frequency after 3 ignored messages and ask "want a lighter touch?"
- Track unsubscribe rate per message type and cut any message above 2% per send.

### 6. Why users would stay and pay
Badges and ideas may fade after novelty wears off, and the free tier may be enough.
**Fix:**
- **Free tier:** One idea a week and the basic passport. Keeps the funnel wide.
- **Paid tier benefits that matter:** Lock-in tools (invites, calendar hold, rescue mode), personalized picks, all badge categories, shared bucket lists, partner perks (a free coffee at badge venues), and an annual "year in review" passport.
- **Perks make it pay for itself:** Partner discounts worth more than $39/yr (for example 10 venue perks averaging $5) give a plain reason to subscribe.
- **Retention loops:** Seasonal limited badges, friends-only leaderboards, streak protection (one free skip a month for paying users) and a quarterly "refresh your interests" prompt.

### 7. Competition and moat
The first file lists risks but not a defensible edge.
**Fix:**
- **Competitors to study (verify current features):** Event-listing and local-discovery apps, map and review apps, loyalty and passport programs, city "bucket list" guides and dinner-with-strangers services.
- **Differentiation:** (a) The action layer: plan lock-in, rescue mode and pre-written invites. Most competitors stop at the idea. (b) Verified visits sold to venues. (c) A game layer tied to a real city.
- **Moat over time:** Local curation quality, venue relationships and exclusive perks, and the data on what plans actually get done. Copying the features is easy and copying a trusted, curated local brand is hard.
- **Local first:** Win one city completely before any second one.

### 8. Cold start and choosing the city
**Fix:**
- Choose a city by these criteria: you live there or can visit weekly, it has 200k+ people with a walkable or transit-friendly core, it has an independent-business alliance or main-street group, and it has a seasonal climate that gives you natural content variety.
- Launch inside one **neighborhood cluster** (for example 3-4 adjacent neighborhoods), not the whole metro.
- Seed with 100 places and 20 seasonal ideas before the first message goes out.
- Use the free list as the audience builder, and only invite venues to pay after the list proves reach.

### 9. Invites depend on the other person
The social features fail if friends and partners must install the app.
**Fix:**
- Invites arrive as a plain text with a web link that works without an account, showing the plan and a one-tap "I'm in."
- The invitee sees a soft prompt to claim a badge afterward, which becomes the referral path.
- Two-person and group plans share the badge when both check in.

### 10. Safety, accessibility and inclusion
**Fix:**
- Default solo suggestions to busy, well-lit public places and daylight or early-evening hours. Add a "share my plan with a friend" button.
- Intake and filters for accessibility (step-free entry, seating, quiet hours), sensory needs, dietary needs and kid or pet friendliness.
- Budget filters that keep free and low-cost ideas prominent, and badges that do not require spending.
- Language and cultural variety in curation, with a "suggest a place" form so locals fix blind spots.

### 11. Proof-of-visit fraud
Location check-ins can be spoofed and venue payments depend on counting real visits.
**Fix:**
- Badges can use a light check (location within 150 m plus a code or photo) because the stakes are low.
- **Venue-billed visits** require a redeemed code, QR scan or a reservation or purchase link. These are the only visits venues pay for.
- Flag accounts with impossible patterns (many badges in one hour across the city) and cap daily badge claims.

### 12. Platform and build risk
**Fix:**
- Launch as a **web app and email list**, not a native app, to avoid app-store review, fees and delays. Add a native app only when retention justifies it.
- Keep the stack simple (a hosted database, a scheduled job for the weekly sends, a mapping or places provider and a payments tool) and cap monthly costs under about $350 until revenue covers them.
- Keep data exportable so you are not locked into one vendor.

### 13. Seasonality and revenue timing
**Fix:**
- Sell annual venue and consumer plans so winter or summer lulls do not cause cancellations.
- Build year-round content (indoor and outdoor, free and paid) and a distinct seasonal badge series each quarter.
- Time sponsor campaigns to peak local events (holiday markets, festivals, restaurant weeks).

### 14. Solo-founder capacity
The plan needs sales, curation, support and building.
**Fix (weekly, about 12-15 hours):**
- 3 hours: curation and verification
- 3 hours: venue outreach and reporting
- 4 hours: build and fixes
- 2 hours: content and community
- 1 hour: numbers review
- **Delegation triggers:** At 100 listings, pay a part-time local curator by the listing. At 25 paying venues, hire a part-time sales rep on commission.

### 15. Defining success and when to stop
**Fix:**

| Checkpoint | Success signal | If missed |
|---|---|---|
| Week 4 | 300 list members, 30%+ say they went out | Change city or message |
| Week 8 | 5 venues paying or committed | Revisit venue offer and targets |
| Month 4 | 1,000 list members, 8 paying venues, 25+ paying users | Narrow the segment or stop |
| Month 8 | 20 paying venues, $2,500+/mo revenue | If under $1,000/mo, pivot to the employer or city-office model or stop |

### Revised first-90-days plan

| Window | Actions |
|---|---|
| Days 1-14 | Pick the city and neighborhood cluster, curate 100 places and 20 seasonal ideas, set up intake and a free email list, and run the Friday-rescue test on yourself |
| Days 15-45 | Grow the list to 300, run the A/B (idea-only vs. lock-in plan), build the web version of intake, Wednesday pick and Friday rescue, and sell the first 3 venues a free pilot with redeemed codes |
| Days 46-90 | Convert pilot venues to paid slots, add badges and passport, launch the free-vs-paid tiers, send the first venue report and decide at the month-4 gate |

### Open assumptions to replace with real data
- Conversion (5%), churn, venue retention, cost per subscriber and messaging costs are estimates.
- Third-party data, messaging and app-store terms and prices must be checked before commitment.
- Local privacy and messaging rules need review by a qualified attorney.
