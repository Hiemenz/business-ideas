# City Explorer: A Badge-Collecting App That Gets You Out of the House (2026-11-14)

A local-discovery app. Users collect badges for doing different things in their own city, alone, with friends or with a partner. Every Thursday it sends one specific, seasonal idea for the weekend, tuned by what the user said they like at signup.

## Who this is for
A 29-year-old software engineer with data skills who wants $8-15K+/mo building solo, with no outside funding. This idea has a real mobile or web build, so the plan below keeps the first version very small.

## Lens: Alex Hormozi
- **Value equation:** The dream outcome is a fuller life in the city you already live in. Effort and time delay are the enemy, so the app removes the work of deciding what to do. It picks the thing, gives the address and hours, and says who it suits.
- **Grand Slam Offer (consumer):** "Get out of the house 4 times in 30 days, or your next month is free."
- **Grand Slam Offer (business side):** "We send you new customers who found you through a badge, and you pay only per verified visit."
- **Core Four fit:** Start with warm outreach to local organizers, then content (a free weekly Thursday email), then partnerships. Paid ads come last.

## The product

### 1. Intake (once, plus a refresh each season)
Ask 10 quick questions so the Thursday message feels chosen for them:
- Who do you usually go out with: alone, friends, partner, family, mix?
- Budget per outing: free, under $20, under $50, no limit
- Energy level: chill, active, adventurous
- Interests (pick up to 5): food, coffee, live music, outdoors, museums, sports, crafts, nightlife, markets, wellness, volunteering, kids' activities
- Neighborhood and how far they will travel
- Best days and times
- Dietary and accessibility needs
- Indoor-only in bad weather: yes or no
- Notification preference: Thursday text, email or push
- One thing they have always wanted to try in the city

### 2. The Thursday drop
- One main idea and two alternates, sent Thursday late morning, so there is time to plan the weekend.
- Each idea shows what it is, where, cost, travel time, best for (solo, friends or couples) and a "go with someone" button that shares the plan.
- **Seasonal library:** Fall (apple orchards, foliage walks, harvest markets), winter (holiday lights, ice skating, cozy cafes, indoor climbing), spring (farmers markets opening, flower walks, patio season), summer (outdoor movies, swim spots, night markets, festivals).
- Reply mechanic: "Going," "Maybe," "Not for me." The answer trains the next recommendation.

### 3. Badges
Badges make exploring feel like a game and give a reason to come back.
- **Categories:** Taste (try 5 ethnic cuisines), Outdoors (visit 3 parks), Culture (museum, gallery, theater), Local (visit 10 independent shops), Night (live music, late-night food), Seasonal (limited-time badges that vanish after the season).
- **Modes:** Solo badges ("Table for one"), Friends badges ("Group outing"), Couple badges ("Date night streak").
- **Levels:** Bronze, Silver and Gold for 1, 5 and 15 visits per category.
- **Proof of visit:** Location check-in within a short radius, or a photo, or a code at the venue. Pick the lightest method that is hard to fake.
- **Streaks and milestones:** "4 weekends in a row out of the house."
- **Passport:** A shareable page with the user's collected badges and a map.
- **Challenges:** Monthly "Neighborhood Explorer" with a prize from a partner venue.

### 4. Social layer (added after the core works)
- Invite a friend or partner to a shared badge hunt.
- Shared "bucket list" for a couple or friend group.
- Leaderboards limited to friends, not strangers, to keep it warm and safe.
- A feature link to the matchmaking idea: opt-in "find someone to go with" for solo badges. See `2026-11-14-matchmaking-business.md`.

## The "Friday Problem": From Idea to Locked-In Plan

**The real problem (from the founder's own experience):** It is Friday, nothing is planned and there is no clear place to start. An idea alone does not fix this. What fails is the work after the idea: choosing, checking hours, inviting someone, deciding on a time and committing. Each step is a chance to give up and stay home. The app should remove those steps, not just suggest.

**Design principle:** The unit of value is a *plan that is already made*, not an idea. The weekend plan should exist before Friday evening, and if it does not, the app rescues the night.

### The weekly rhythm (replaces the single Thursday message)

| When | Message | Goal |
|---|---|---|
| **Wednesday evening** | "Planning ahead: pick one for this weekend" with 3 ideas as big tappable cards | Get a choice before the week fills up |
| **Thursday late morning** | If no choice yet: one pre-made default plan ("Saturday 11am, farmers market, then coffee next door, 12 min away") with **Lock it in** | Turn a maybe into a yes |
| **On "Lock it in"** | Add to the calendar, pick or invite a person in one tap with a pre-written message, and confirm hours | Lower effort to near zero |
| **Friday 3pm** | Check-in: "Still on for tomorrow?" with a weather-aware swap if needed | Prevent the Friday slide |
| **Friday 5-6pm, no plan locked** | **Rescue mode:** "Nothing planned? Here are 3 things open tonight within 20 min, all easy to say yes to" | Catch the exact moment of the problem |
| **Saturday morning** | Reminder with address, hours, travel time and one tip | Make going frictionless |
| **Sunday evening** | "How was it?" with a one-tap check-in for the badge | Close the loop and feed the next pick |

### Features that fix it
- **One-tap default plan:** Always show a complete plan (activity, time, route, a nearby second stop), never just a place name.
- **Plan templates by situation:** "Solo, 2 hours, under $15," "Date night, indoor," "Friends, rainy," "Last-minute tonight." Pick a template and it fills in the details.
- **Rescue mode:** An always-available "I have nothing planned" button that returns open-now options sorted by distance and effort.
- **Pre-written invites:** One tap sends a text such as "Want to check out the night market Saturday at 7? I'll grab tickets," so asking someone takes seconds.
- **Commitment device:** Optional "pledge" with a friend: both lock in, and a missed plan costs a small badge streak, not money.
- **Calendar hold:** Add the plan to the user's calendar with a travel-time buffer.
- **Weather and energy swap:** One tap to switch to an indoor or lower-effort option if conditions change.
- **Pre-checked details:** Hours, price and reservation needs are verified, since "closed when we arrived" kills the habit.
- **Backlog ("Someday list"):** Save ideas as they appear so there is always a bank to draw from on Friday.

### Updated intake additions
- "When do you usually decide your weekend plans?" (during the week, Friday, day-of)
- "What stops you from going out?" (no ideas, no one to go with, cost, effort, weather, tiredness)
- "Who would you want to ask?" (so invites can be pre-filled)

### Updated success metrics
- **Plan lock rate:** Share of users who tap "Lock it in" by Thursday night (target 40%+).
- **Friday rescue use:** Share of users with no plan who open rescue mode and go out (target 30%+).
- **Follow-through rate:** Locked plans that end in a check-in (target 60%+).
- **Weekends out per month** per active user (the main outcome, target 3+).

### Updated validation test
For the free Thursday list, test the two versions side by side with 50 subscribers each:
- **A:** Idea only.
- **B:** Wednesday pick, Thursday default plan, Friday rescue and one-tap invite.
Measure which group actually goes out more. If B does not beat A by a clear margin, the extra steps are not worth building.

---

## Business model

| Revenue line | How it works | Price |
|---|---|---|
| **Consumer subscription** | Free tier: one Thursday idea. Paid: personalized ideas, all badges, planning tools, group features | $4.99/mo or $39/yr |
| **Venue partnerships** | Local businesses pay to be featured as a Thursday idea or a badge location, per verified visit | $2-5 per visit, or $99-299/mo for a featured slot |
| **Sponsored seasonal challenges** | A brewery district, a tourism board or a business improvement district sponsors a badge series | $500-3,000 per campaign |
| **Employers and relocation programs** | A "settle in" version for new hires: badges for finding your neighborhood | $3-6 per employee per month |
| **City and tourism offices** | License for a branded city version | $5-25K per year |

**Realistic income math (a one-city launch):**
- 1,500 paying users x $39/yr (about $3.25/mo) = about $4,900/mo
- 40 venue partners x $150/mo = $6,000/mo
- 1 sponsored challenge a month x $1,000 = $1,000/mo
- **About $11,900/mo** from one mid-size city at maturity, which is ambitious. Expect months to reach 25% of this.

## Why this could work
- Venues and districts already pay for foot traffic, and a verified-visit fee is easy for them to measure.
- The Thursday message gives the app a habit anchor that does not depend on someone opening it.
- Badges are cheap to create and extend per season.
- The data (which ideas people accept, visit and repeat) is useful to venues and city offices.

## Honest risks
- **Consumer apps are hard to monetize:** Many people will not pay $5/mo to be told where to go. Treat the venue side as the main revenue source and keep the consumer side cheap, or free with ads and sponsors.
- **Content upkeep:** Hours and events change. Start with 150-200 hand-checked places in one city and refresh them each month. Do not try to cover everything.
- **Cold start:** An empty city feels useless. Seed the app with your own curated list before launch and prove value with a free weekly email first.
- **Retention:** Novelty fades. Seasonal badges, streaks, friends and the weekly drop fight this, and you need to measure week-4 and week-12 retention.
- **Proof-of-visit fraud:** Location check-ins are easy to spoof. Venue payments should only count visits verified by code or purchase.
- **Competition:** Review and map apps, event-listing platforms, and city guides already exist. The difference is the weekly personalized push, the game layer and the paid-by-visit venue model.
- **Safety:** Suggestions for solo outings should favor public, well-lit places and avoid late-night isolated spots by default.

## Validation plan (before building an app)
1. **Weeks 1-2:** Choose one city and neighborhood cluster. Curate 100 places and 20 seasonal ideas in a spreadsheet.
2. **Weeks 2-4:** Run a free **Thursday email or SMS list** with an intake form. Goal: 300 subscribers. Measure open rate, reply rate ("Going") and a follow-up survey on whether they went.
3. **Weeks 4-6:** Offer a paper-simple version of badges: a printable or web checklist with 10 badges. Measure how many complete one.
4. **Weeks 5-8:** Pitch 15 local venues on a $99 featured-slot trial or a per-visit deal with a code. Goal: 5 paying venues.
5. **Gate to build the app:** 300+ list members, 30%+ say they went to at least one suggestion and 5 venues pay. If not, change the city, the segment or the message first.

## MVP scope
- **Phase 0 (no code):** Spreadsheet, form tool and an email or SMS sender. Two weekends.
- **Phase 1 (web app, 4-6 weekends):** Intake, Thursday sender with simple matching, a badge page with manual or code-based check-in, and a venue dashboard with visit counts.
- **Phase 2:** Mobile app, friends features, shareable passports and sponsor challenges.

## Go-to-market
- **Warm start:** Local newcomer groups, run clubs, coworking spaces, neighborhood associations and independent-business alliances.
- **Content:** The Thursday list itself is the marketing. Make it good enough to forward.
- **Venue-first partnerships:** Business improvement districts and main-street programs already fund foot traffic. One partnership gives you 20-50 venues.
- **Local press and creators:** City-blog writers and local social creators can run a "collect all 10 badges" challenge.
- **Employers:** Offer a pilot to one HR or relocation team.

## Key numbers to track
Subscribers, intake completion, Thursday open rate, reply "Going" rate, visits per user per month, badge completion, week-4 and week-12 retention, venue-paid visits, cost per verified visit, paying venues and monthly revenue.

## Open decisions
- Which city to start in (pick the one you know best and can visit).
- Consumer-paid versus venue-paid as the primary model. This file recommends venue-paid first.
- Whether to build the social layer or stay solo-first.
- Name and branding (examples: "Out & About," "Local Passport," "Thursday List").

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
