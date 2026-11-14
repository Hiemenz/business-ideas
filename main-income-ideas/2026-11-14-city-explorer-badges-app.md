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

---

## Life-Stage Cohorts: Different People, Different Weekends

One feed for everyone fails. A parent with a toddler and a retiree with a free Tuesday have different constraints, so the app sorts users into **cohorts** at intake and tunes ideas, timing, badges and venues for each. Cohorts are about what someone needs on a given weekend, not a label, so a person can belong to more than one and can switch.

### The cohorts

| Cohort | Who | Main obstacle | What the app solves |
|---|---|---|---|
| **Young families (babies and toddlers, 0-4)** | New parents, often tired and short on time | Nap schedules, gear, cost, "will it be a disaster?" | Nap-friendly, short, low-stress outings with changing tables and stroller access verified |
| **Young families (school age, 5-12)** | Parents of kids in school and activities | Packed weekends, kids bored of the same places | Weekly family-friendly ideas, rainy-day backups and kid-led badges |
| **Teens and young adults (16-24)** | Students and first-job adults | Budget, transport, wanting something to do with friends | Free and cheap ideas, transit-reachable, group badges |
| **Young professionals (25-40, solo or friends)** | Often relocated, social circles still forming | Not knowing the city, deciding alone | The core app described above, plus the "find someone to go with" opt-in |
| **Couples** | Dating, newlywed or long-term | Date-night rut, planning fatigue | Date ideas by mood and budget, couple badges and anniversary or "firsts" lists |
| **Empty nesters (50-65)** | Kids grown, more free time and money | Rebuilding a social life and routines | Culture, travel-light day trips, small-group activities and weekday ideas |
| **Retirees (65+)** | Flexible schedules, mobility varies | Isolation, transport, accessibility | Daytime and weekday ideas, seated and step-free filters and companion invites |
| **Newcomers (any age, new to the city)** | Moved in the last 12 months | Everything is unknown | A "first 90 days" badge path across neighborhoods and a local welcome list |

Start with **two cohorts** (see launch order below) and add the rest as each proves itself.

### How cohort works in the product
- **Intake:** Add "Who are you planning for?" (me, me and a partner, my family, my friends, my parents) and ask for kids' ages by range only (under 2, 2-4, 5-8, 9-12, teens). Do not collect kids' names or photos.
- **Thursday and Friday messages:** Tuned per cohort. A toddler-family message arrives Wednesday evening and suggests morning outings that finish before naps. A retiree message may arrive Monday for a weekday idea. A young professional message arrives Wednesday with a social option.
- **Rescue mode by cohort:** Parents get "open now, kid-friendly, under 20 minutes away, changing table, indoor." Couples get "dinner and a walk tonight."
- **Badges by cohort:** Families earn "Park Explorer" (visit 10 playgrounds), "Rainy Day Hero" (3 indoor outings) and "Library Card" badges, with a shared family passport kids can help fill. Couples earn "Date Night Streak." Retirees earn "Weekday Wanderer" and "Local History Buff."
- **Filters that matter per cohort:** Stroller and changing-table access, kid age fit, nap-time windows, noise level, parking, accessibility, cost per person versus per family, and group-size limits.
- **Multi-cohort users:** A parent of a toddler can switch on "date night" for a night out and "solo" for a rare free evening.
- **Cross-cohort moments:** Seasonal city events (festival, lights, markets) show up for everyone with a version per cohort.

### Cohort-specific content examples (one city, fall)
- **Young families (0-4):** Pumpkin patch with a short loop, a library story time, a splash-free indoor play cafe.
- **Young families (5-12):** Apple-orchard day with a maze, a science museum free-admission day, a kids' cooking class.
- **Young professionals:** A trivia night, a neighborhood food crawl, a pickup sports league.
- **Couples:** A cider-mill date, a gallery walk and a wine-and-paint evening.
- **Empty nesters:** A weekday foliage drive with a lunch stop and a walking history tour.
- **Retirees:** A morning farmers market with seating, a matinee at a local theater and a community concert.

### Business model by cohort
- **Pricing:**
  - Individual: $39/yr.
  - **Family plan:** $59/yr for up to 4 profiles, including kid-friendly planning and a shared passport. Parents are the highest-intent payers because they are short on time.
  - Couples plan: $59/yr for two.
  - Free tier for all, with the Friday rescue as the hook for parents.
- **Venue side:** Sell family-friendly venues (play cafes, farms, museums, kids' classes) the same per-visit model. Families visit in groups, so one redeemed code means more visits and higher spend per visit, which makes family cohorts the strongest ROI story for venues.
- **Sponsors:** Local pediatric and family-service businesses, children's retailers and libraries sponsor family challenges. Senior centers and community colleges sponsor retiree and empty-nester challenges.
- **Employers:** Family-friendly weekend packs as an employee perk, and new-hire "settle in" packs for relocated staff.
- **Community institutions:** Libraries, parks departments and parent groups can distribute the free list to reach cohorts at low cost.

### Why start with young families
- **Highest pain and willingness to act:** Planning a weekend with kids is hard, and the Friday problem is worse with children.
- **Clear venue demand:** Family venues want weekday and weekend foot traffic and already advertise to parents.
- **Easy to find:** Parent groups, preschool and library networks and neighborhood social groups are findable through warm outreach.
- **Strong viral loop:** Parents share good outings with other parents.

**Recommended launch order:** (1) Young families in one neighborhood cluster, (2) young professionals or newcomers (the core app), (3) couples as an add-on mode, (4) empty nesters and retirees once content and venue relationships exist, (5) teens last, since they need extra safety and consent design.

### Data, safety and rules for families
These are practical flags. Confirm local rules with a lawyer, especially anything involving children.
- **Do not collect children's personal data.** Store only age ranges and the parent's account. Do not let kids create accounts or post.
- Kid-friendly photo check-ins should not require a child's image. Offer a parent-controlled badge unlock instead.
- Rules on children's data differ by country and state. If any feature is directed at children, review the requirements first, or keep the product parent-operated.
- Make family passports private by default, with no public location history of a family's routine. Delay posting of outings until after the visit if sharing is on.
- Show safety details for family venues (fenced areas, supervision expectations and age limits) and verify them.
- Cohort data is sensitive (kids' ages, health or accessibility needs). Collect only what you use and offer delete and export.

### Metrics by cohort
Track each cohort separately: intake completion, Thursday and Friday open rate, plan-lock rate, follow-through, weekends out per month, 12-week retention, paid conversion, venue visits and revenue. Compare cohorts to decide where to put effort.

**Targets to test (assumptions):**
- Young families: 45%+ plan-lock rate, 55%+ follow-through and 8%+ paid conversion on the family plan.
- Young professionals: 35%+ plan-lock and 5% paid conversion.
- Retirees: lower digital engagement, so test email and print or phone options.

### Validation for the cohort model
1. **Weeks 1-3:** Run two free lists in the same neighborhood cluster, one for young families and one for young professionals, each with its own intake and Thursday message. Goal: 150 members each.
2. **Weeks 3-6:** Compare plan-lock and follow-through between cohorts and interview 10 members in each.
3. **Weeks 4-8:** Offer 5 family venues and 5 general venues a pilot with redeemed codes. Compare visits per code and venue interest.
4. **Gate:** Pick the lead cohort by the strongest combination of follow-through, venue interest and willingness to pay, and put the second cohort on hold until the first hits the month-4 checkpoint.

### Open decisions
- Which two cohorts to launch first (this file recommends young families plus the core young-professional or newcomer group).
- Whether the family plan is one price or tiered by number of kids.
- Whether to support teens at all in version one (this file recommends not yet).
- How to reach retirees (email, print or phone) if digital engagement is low.

---

## Scavenger Hunts and Photo Proof: Visits That Build the Data

Replace the plain check-in with a **photo scavenger hunt**. To earn a badge, you photograph a specific thing at the place ("the mural on the north wall," "the menu board," "the trailhead sign"). The same prompt repeats across visits, so over time the app collects many photos of the same spot. That solves two problems at once: it proves you were there, and it keeps the place data fresh at almost no cost.

### How the hunt works
- **Prompts, not "take any photo":** Each badge location has 1-3 photo targets. Examples: "the front entrance," "the daily specials board," "the best view from the top," "the kids' play area."
- **Hunt types:**
  - **Single-stop:** One place, one photo target.
  - **Trail hunts:** 5-8 stops in a neighborhood, each with its own target and a finish badge.
  - **Seasonal hunts:** "Find 5 places decorated for the season."
  - **Family hunts:** Kid-friendly clues ("find the animal carved in stone") that a child can help spot, with the parent taking the photo.
  - **Couple and friend hunts:** Shared photo targets that unlock when everyone checks in.
  - **Solo hunts:** A quiet-spot or "table for one" photo target.
- **Clues:** Short riddles or hints rather than addresses on harder hunts, so it feels like a game.
- **Streak photo:** Repeat visits to the same spot ask for the same shot, building a personal "then and now" collage on the passport.

### Verifying that you were really there
No method is perfect, so combine light checks and match the strictness to the stakes.
- **Location and time:** Check the photo's location metadata or the phone's location at capture, within a radius, and accept only photos taken in the app (not uploads from the gallery) for venue-billed visits.
- **Image match:** Compare the photo against reference images of the target, using image similarity. If it is a near-match to the reference or to prior users' photos, accept it. If it is a mismatch, send it to review.
- **Freshness:** Require a live capture in the app, plus a time window around check-in. Reject screenshots and photos of screens where detectable.
- **Fake and AI-generated images:** Detection tools are imperfect. Keep the stakes low for casual badges, and require a redeemed code, QR scan or purchase link for visits that venues pay for.
- **Review queue:** Borderline photos go to a quick human or community review, and repeat offenders lose badge eligibility.
- **Honest limit:** Expect some cheating. For badges that is acceptable. For venue billing it is not, so billing relies on codes.

### The data this builds over time
Many photos of the same target, taken by different people on different days, produce useful signals:
- **Place freshness:** Is it open, closed, renovated or under construction? A drop in matching photos can flag a closure.
- **Condition and seasonality:** The trail in fall versus winter, the patio in summer, the decorations at the holidays.
- **Crowd and wait signals:** Timestamped photos show how busy a place looks at different times (use only counts and general impressions).
- **Menu and price boards:** Photos of menus and boards can update prices and specials if the venue allows it.
- **Accessibility details:** Photos of entrances, ramps, seating and restrooms help build accessibility information that is rare and valuable.
- **Activity imagery:** A growing bank of real photos that can replace stock images in the Thursday message.
- **Venue insight:** Aggregate views of how visitors experience a place can feed the venue report (no individual user data).

### Photo challenges: fill the gaps on demand
When the app needs better or newer images, it posts a **challenge** instead of hiring photographers.
- **Gap detection:** Flag places with no photo, old photos or low-quality photos, and flag missing facts (no accessibility photos, no menu photo).
- **Challenge types:** "Get a clear photo of the playground entrance this week," "Photograph 3 spots that look good in the snow," "Capture the accessible entrance at these 10 venues."
- **Rewards:** Bonus badge points, a limited-edition badge, entry in a monthly prize draw from a partner venue, or a small credit toward the paid plan.
- **Venue-sponsored challenges:** A venue pays for a challenge to refresh its own images ("photograph our new patio"), which doubles as marketing.
- **Quality selection:** The app keeps the best-rated photos per target and lets users vote or flag, so quality improves over time.
- **Public-benefit challenges:** City offices or districts sponsor challenges to document accessible routes, public art or seasonal events.

### What this adds to the business
- **Cheaper data:** Photos refresh listings that you would otherwise pay to maintain by hand or by license.
- **Better product:** Real, recent photos make the Thursday idea more convincing and raise plan-lock rates, so test this.
- **Venue value:** Fresh images and visit evidence strengthen the pitch and the monthly report.
- **New revenue lines:** Sponsored challenges ($100-500 each), city-funded documentation projects and, later, an image and place-freshness data product for other local apps (price and terms to be tested, and subject to the rights issues below).
- **Retention:** Hunts give users a reason to return and to revisit the same place across seasons.

### Rights, privacy and safety (practical flags, confirm with a lawyer)
- **Content license:** Your terms must say users keep ownership but grant the app a license to store and display their photos. Do this before collecting anything, and say whether venues can reuse photos.
- **Faces and bystanders:** Prompt "photograph the thing, not people." Auto-blur detected faces in stored images and let anyone request removal.
- **Children:** Do not request or store photos of children. Family hunts should target objects, and the app should detect and blur or reject images with children in them. Keep the app parent-operated, as in the cohorts section.
- **Private property and conduct:** Keep prompts to public or customer-accessible areas, and never ask for photos that require trespassing or unsafe positions (cliff edges, roads). Add a short safety note to every hunt.
- **Location privacy:** Strip precise metadata from public images and do not publish a person's visit history. Share aggregate counts only.
- **Venue consent:** Tell venues photos are being taken. Let them request removal of images of sensitive areas such as staff areas or security details.
- **Copyrighted works:** Murals and public art can have copyright limits on commercial reuse. Display in the app only and check before using any in marketing or sale.
- **Moderation:** Flag and remove inappropriate or unsafe images quickly, and keep a way to report.

### Costs and build notes
- **Storage and processing:** Photos cost money to store and run through checks. Compress and resize on upload, keep one best photo per target plus a short history, and cap monthly spend (assumption: $50-150/mo at the first 1,000 users, to be measured).
- **Start simple:** Phase 1 is manual review of photos from a small set of prompts. Add automated image matching only after you have enough photos to tune it.
- **Reference images:** Collect them yourself for the first 100 places, which also gives you the curated quality edge.
- **Web or app:** In-browser camera capture can work for the first version, avoiding an app-store build.

### Metrics
Photos submitted per week, share accepted, repeat photos of the same target, time to refresh a stale listing, challenge completion rate, plan-lock lift for ideas with fresh photos versus stock images, cost per accepted photo and venue interest in photo-backed reports.

### Validation (inside the existing free-list tests)
1. **Weeks 1-3:** On the free list, add one hunt per week with a single photo target. Measure how many members send a photo, compared with plain check-ins.
2. **Weeks 3-5:** Run one challenge ("photograph the entrance of these 10 places") and measure completion, photo quality and listing freshness.
3. **Weeks 4-6:** A/B test Thursday messages with stock photos against fresh member photos to see whether real images raise plan-lock rate.
4. **Weeks 5-8:** Offer 3 venues a sponsored photo challenge and see if they will pay.
5. **Gate:** Keep the photo feature if 25%+ of active members submit a photo, at least 70% of photos pass review and fresh photos improve plan-lock. If not, fall back to code-based check-ins.

### Risks to watch
- **Friction:** Taking and sending a photo takes effort, and some people will skip badges. Keep photo proof optional for casual badges and required only for hunts and billed visits.
- **Fakes:** AI-made or reused images will appear. Keep stakes low and tie money to codes.
- **Privacy incidents:** One photo of a child or an identifiable person can damage trust. Auto-blur, strict prompts and fast removal are essential.
- **Rights disputes:** Venues, artists or users may object. Clear terms, quick takedown and display-only use for art reduce this risk.
- **Costs:** Storage and review can grow faster than revenue. Cap volumes and sample reviews.
- **Quality:** Many photos are poor. Use clear prompts with an example image and let the community vote for the best.

### Open decisions
- Whether photo proof is required or optional for each badge type.
- Whether to build image matching early or rely on manual review at first.
- Whether to sell photo-backed data to others later, which depends on the license terms you set now.
- Which gap-filling challenge to run first (this file recommends "entrances and accessibility photos" because it is both useful and rare).

---

## Date Spots: A Date-Night Mode for Couples

A dedicated mode for couples, including parents who rarely get an evening out. It solves the same Friday problem for two: nobody has planned the night, and booking, finding a sitter and choosing a place all feel like work.

### What a "date spot" is
A place or short itinerary tagged for couples, with the details that decide whether a date goes well: noise level, seating, lighting, reservation needs, price per person, how long a typical visit lasts and what to do before or after.

### How it works
- **Date-night plans, not single places:** Each plan is a 2-3 stop evening, such as "coffee, a gallery walk and dessert" or "early dinner, a short walk and live music." Total cost, travel time and start and end times are shown up front.
- **Intake additions:** Ask what kind of dates they like (quiet, active, food-focused, cultural, outdoors), budget per date, how often they go out, preferred times (daytime date, early evening, late night), whether they need to be home by a set time and any dietary or accessibility needs.
- **Date-night modes:**
  - **Spontaneous tonight:** Open-now options within 20 minutes, no reservation needed.
  - **Planned weekend:** Plans that need booking, with reservation links and a reminder to book.
  - **Parents' night out:** Short plans that end early, sit near home and pair with a sitter reminder ("book your sitter by Wednesday").
  - **Anniversary and milestone:** Special-occasion plans and a reminder a few weeks ahead.
  - **Budget date:** Free or under $25.
  - **Try-something-new date:** An activity neither has done before (pottery class, climbing, a tasting).
- **Thursday and rescue messages for couples:** A Wednesday pick of three date plans, a Thursday default plan with one-tap lock-in that texts the partner ("Saturday 6pm, I'm booking"), and a Friday rescue with tonight-only options.
- **Shared plan:** Both partners see the plan, can vote between two options and get the same reminder. The partner does not need the app, since the plan arrives as a link.
- **Calendar hold and travel buffer:** The plan goes on both calendars, with the time to leave built in.

### Date-spot badges
- **Date Night Streak:** Dates in consecutive weeks or months. Forgiving rules so one missed week does not reset it.
- **Firsts:** First coffee spot, first live-music night, first new cuisine together.
- **Neighborhood Date Map:** One date in each of 6 neighborhoods.
- **Seasonal Dates:** Limited-time badges (fall cider-mill date, winter lights walk).
- **Return Visit:** Go back to a favorite spot and add a "then and now" photo of the same table or view.
- **Shared bucket list:** The couple's own list of places to try, with a progress map.
- **Photo hunt for two:** A scavenger hunt where each partner finds a different clue, unlocked when both check in. The photo target is an object or view, not people.

### Data and curation for date spots
- **Fields to collect per place:** Noise level, lighting, seating type (booth, bar, patio), reservation needed, wait time at peak hours, price per person, parking, accessibility, kid-free or kid-friendly, how long couples usually stay and nearby add-on stops.
- **Photo prompts:** "The table you'd ask for," "the view from the patio," "the menu and prices." Repeat visits build up this data, as in the photo-hunt section.
- **Couples' ratings:** After a date, one tap each: "Would you go again?" and "Good for a first date / anniversary / casual night?" Aggregate only.
- **Tags that matter:** First-date safe (public, easy exit, not too intimate), quiet enough to talk, good for a special occasion, good for a rainy night, good when you only have two hours.

### Business model additions
- **Venue side:** Restaurants, wine bars, cafes, galleries, activity studios and theaters pay per redeemed visit or for a featured date-night slot. Couples spend more per visit than solo visitors, which helps the venue's return on investment.
- **Packages:** Venues can offer a "Date Night Bundle" (set menu, class or show plus a drink) with a code redeemable through the app. The app takes a share of redeemed bundles.
- **Off-peak push:** Venues pay to fill weekday and early-evening tables, so the app sends couples to quiet times.
- **Sitter partners:** Referral partnerships with local babysitting services, with a fee per booked sitter from a "parents' night out" plan.
- **Sponsored seasonal dates:** A district or hotel sponsors "Date Night in [District]" challenges.
- **Consumer plan:** The couples plan ($59/yr for two) includes shared plans, date bundles and the anniversary reminders. Parents are the strongest buyers, so test a bundle with the family plan ("family weekends plus one date night a month").

### Link to the other ideas
- **Cohorts:** The couples cohort and the parents-of-young-kids cohort share this mode, with a "parents' night out" variant.
- **Matchmaking idea:** Date spots can also serve first dates in the matchmaking business (see `2026-11-14-matchmaking-business.md`), such as public, easy-to-leave places, which makes this a possible shared venue network.
- **Marketing plan:** Add the date-night plan as a lead magnet for parents ("5 date nights within 20 minutes of home that you can pull off with a sitter"), described in `2026-11-14-city-explorer-parent-marketing-plan.md`.

### Safety and trust
- **First-date and solo-safe options:** Tag public, well-lit places with easy transit or parking, and avoid isolated spots.
- **Share-my-plan button:** Send the plan and place to a friend.
- **No private or sensitive data in public:** Couples' passports are private by default. Do not publish a couple's routine or anniversary dates.
- **Partner inclusion:** Use inclusive language for all couples and avoid assumptions about who is going out together.
- **Alcohol:** Offer non-alcohol options and filter them on request.
- **Messaging and consent:** Plans sent to a partner should come from the user ("Sam invited you") with a clear opt-out, and not as unsolicited marketing.

### Metrics
Date-plan lock rate, share of plans sent to a partner, follow-through, repeat dates per couple per month, date-night streak length, redeemed bundles, revenue per redeemed visit versus solo visits, sitter referrals and conversion to the couples plan.

### Validation
1. **Weeks 1-3:** Add one date-night plan a week to the free list for the couples and parent cohorts. Measure replies and "Going" taps compared with other ideas.
2. **Weeks 3-5:** Offer 5 venues a trial "Date Night Bundle" with a code, and count redemptions.
3. **Weeks 4-6:** Test the "parents' night out" plan with a sitter-booking reminder on 50 parents and measure follow-through.
4. **Gate:** Keep the mode if date plans match or beat other plan types on lock rate and at least 3 venues redeem bundles. If not, fold date spots into the general ideas.

### Risks
- **Narrow audience for a paid plan:** Dating couples may use it rarely. Parents are the better market, so lead with them.
- **Reservation friction:** Booking links break the flow. Prefer no-reservation spots for rescue mode and pre-fill booking links for planned dates.
- **Venue overload:** Popular date spots can get swamped, which hurts the experience. Spread recommendations across several places and times.
- **Sitter dependence:** Many parents lack a sitter. Offer daytime dates and at-home or short dates as alternatives.
- **Sensitivity:** Relationship status is personal data. Collect only what you use.

### Open decisions
- Whether date spots are a separate mode or part of the general feed with a couples filter.
- Whether to build the bundle and sitter-referral features in version one or add them after venue pilots.
- Whether to offer a combined family-plus-date-night plan.

---

## The Connection Cohort (Dates): Going Deeper, Not Just Going Out

This replaces the earlier "date spots" idea with something more useful. A **date cohort** is not a list of places. It is for people who want to build a deeper connection with the person they are with, or to meet someone through a shared activity. The activity is the setting, and a guided conversation is the product.

**Goal:** Help two people actually get to know each other as they are. A good outing becomes a good conversation, and over time that becomes intimacy.

### Framework: seven levels of intimacy
The question flow follows the progression in Matthew Kelly's *The Seven Levels of Intimacy*. Each level asks for a little more openness than the last:

| Level | Name | What it explores |
|---|---|---|
| 1 | Clichés | Moving past small talk to how life really is |
| 2 | Facts | Background, family and the experiences that shaped someone |
| 3 | Opinions | Beliefs, values and non-negotiables |
| 4 | Hopes and dreams | What each person wants from the future |
| 5 | Feelings | Emotional world: feeling loved, appreciated and connected |
| 6 | Faults, fears and failures | Imperfections, insecurities and lessons learned |
| 7 | Legitimate needs | What someone truly needs to feel loved and fulfilled |

**The guiding question for the whole cohort:** "Are we getting to know each other as we really are, or only the versions of ourselves that we want the other person to see?"

**Source and rights:** The question lists you shared are drawn from this book's framework. Before building a product around the book's questions, wording or name, check the author's and publisher's permissions. Safest approach: write original questions for each level (examples below), name the levels in your own words, and credit the book as inspiration only with permission. The full list you shared stays in your notes as source material.

### Who is in the date cohort (relationship stages)
Different stages need different depth. The app should never push a first date to Level 6.

| Stage | Who | Levels offered | Tone |
|---|---|---|---|
| **First dates and meeting through an activity** | Strangers or new acquaintances | 1-2 | Light, curious, low pressure |
| **Early dating** | A few dates in | 1-4 | Getting to know values and hopes |
| **Committed or engaged** | Serious relationship | 1-7 | Deeper, with the option to pause |
| **Married and long-term** | Years together, including busy parents | 1-7, with "reconnect" prompts | Renewing connection after routine and kids |
| **Friends** (optional side track) | Close friends | 1-5 | Depth without romance |

**Rule:** A level unlocks only when **both** people choose it. No one can push a partner deeper, and "pass" is always one tap away.

### How it works in the app
- **Pick the stage and goal at intake:** "Planning a date with: someone new, someone I'm dating, my partner or spouse." Goal: "Meet someone new, get to know my date better or reconnect."
- **The Thursday or Wednesday plan includes a conversation card:** The date idea (a walk, a cooking class, a market) comes with one question chosen for that stage and level, plus a "follow-up if it goes well" question.
- **Pace over performance:** Show one or two questions per outing, not a list. The prompt is to let one question lead to another and to share your own answer too.
- **Match the activity to the level:**
  - **Walks and drives:** Levels 1-4 (side by side is easier for talking).
  - **Cooking, pottery and other hands-on classes:** Levels 1-3, with shared attention that eases awkwardness.
  - **Quiet cafes and dinners:** Levels 4-7 where there is privacy and time.
  - **Active dates (climbing, kayaking):** Levels 1-2 and fun, with a 5-minute reflection afterwards.
  - **Group activities and meetups:** Levels 1-2 only, with icebreakers.
- **After-date reflection:** A private two-minute check-in for each person: "What did you learn about them?" and "Did you feel heard?" Not shared unless both opt in.
- **Reconnect mode for busy parents:** "Parents' night out" plans with a short question card for the car ride and one for dessert.
- **Pause and skip:** Any question can be skipped without telling the other person which. A "not tonight" button changes the card.

### Original example prompts by level (written for the product)
Use these as the model for your own bank, rather than copying the book.

1. **Clichés → real answers:** "What's been taking up most of your headspace this week?" "What's one thing you're looking forward to?"
2. **Facts:** "What was a place you grew up like?" "Who shaped how you see the world?"
3. **Opinions:** "What's something you'd never compromise on?" "What does a good partner do?"
4. **Hopes and dreams:** "What does a good ordinary day look like for you in ten years?" "What do you hope we'd build together?"
5. **Feelings:** "When do you feel most appreciated?" "How do you like to be supported on a hard day?"
6. **Faults, fears and failures:** "What's something you're still working on in yourself?" "What did a mistake teach you?"
7. **Legitimate needs:** "What helps you feel safe with someone?" "What's hard for you to ask for?"

**Two question tracks:** A values-neutral track and an optional faith-aware track, since faith and marriage questions matter deeply to some users and not at all to others. Let users choose.

### Badges for connection (no scoreboards of intimacy)
- **Not competitive:** Do not rank couples or score closeness. Badges mark effort and shared experiences.
- **"Level Opened":** A private badge shown only to the two people, earned when both choose to open a level.
- **"Ask Me Something":** For trying a question card on three outings.
- **"Back to Back":** Dates in consecutive weeks or months, with a forgiving streak.
- **"New Ground":** A first-time activity together.
- **"Good Listening":** An optional badge a partner can give after a date ("I felt heard").
- **Couple passport:** A private page with places and the dates, with no question answers saved unless both want them kept.

### Meeting people through the activity
This cohort also supports the matchmaking idea (see `2026-11-14-matchmaking-business.md`).
- **Activity meetups for singles or new couples:** Small, hosted, interest-based outings (a pottery class, a trivia night, a hike) with Level 1-2 icebreaker cards.
- **Introduce-and-plan:** After a matched introduction, send a suggested public first activity and a Level 1-2 card for each person.
- **Followed by an opt-in check-in:** "Would you like to see them again?" with the answer revealed only if both say yes.
- **No pressure to go deeper:** Strangers never see Levels 3-7 prompts.

### Business model additions
- **Couples plan ($59/yr) includes** connection cards, shared plans and the private couple passport.
- **Premium add-on:** Seasonal "Deeper" packs (for example a "First Year Together" pack or a "Reconnect After Baby" pack for parents, $9 each) or a monthly card drop in the subscription.
- **Venue side:** Quiet, conversation-friendly places (cafes, tea rooms, scenic walks, wine bars) get a "good for talking" tag and pay for featured slots. Hands-on class studios (pottery, cooking) get a "good for first dates" tag.
- **Partnerships:** Marriage-preparation programs, couples' retreats, counselors' practices offering optional "date homework," faith communities, and relationship-education nonprofits can distribute the cards. Offer a referral fee or free access.
- **Gifts:** A "date night kit" gift (a plan, a card pack and a voucher from a partner venue).
- **Employer and wellness plans:** A relationship-wellness perk for employees (test with an HR contact).

### Safety and emotional care (important)
- **Not therapy:** State clearly that the app is not counseling and cannot treat or diagnose. Link to professional and crisis resources for abuse or distress, and keep the link visible on Levels 5-7.
- **Consent for depth:** Mutual unlock, easy skip and no record of who skipped. No guilt messages.
- **Unsafe relationships:** Do not push anyone to share more with a partner who makes them uncomfortable. Add a quiet "I'm not comfortable" option that leads to support resources and does not notify the partner.
- **Privacy:** Answers are not stored by default. Anything saved is visible only to the two people who both opted in. Delete on request.
- **First-date safety:** Public places, share-my-plan and no deeper levels for strangers.
- **Inclusivity:** Language works for all couples and relationship styles, and does not assume marriage as the goal, though a marriage-focused track can exist.
- **Cultural and faith sensitivity:** Let users choose tracks and tone, and avoid assuming values.

### Metrics
Connection-card use per outing, levels opened by stage, share of dates with a follow-up outing, after-date "felt heard" rate, repeat dates per couple, couples-plan conversion, card-pack purchases, partner-venue visits, skip rate (high skip rates mean questions are too deep or too clinical) and support-resource clicks.

### Validation
1. **Weeks 1-3:** Add one connection card to each date idea on the free list. Measure replies and compare "Going" and follow-through against plans without a card.
2. **Weeks 3-5:** Interview 10 couples (dating and married) after using three cards. Ask what felt natural and what felt forced.
3. **Weeks 4-6:** Test a "Reconnect After Baby" card pack with 30 parents and measure use and willingness to pay $9.
4. **Weeks 5-8:** Run one hosted singles' activity meetup with Level 1-2 cards and measure show-up rate and second-meeting interest.
5. **Gate:** Keep the cohort if cards are used on 50%+ of date plans, "felt heard" is positive for most users and skip rates stay moderate. If cards feel forced, cut the number of questions and make them optional.

### Risks
- **Feels scripted:** Cards can make dates feel like homework. Keep them short, optional and tied to the activity.
- **Emotional harm:** Pushing disclosure can backfire. Mutual unlock and easy skip protect against this.
- **Rights issue:** Using the book's framework, questions or name without permission is a legal and reputational risk. Write original content and get permission before using any of the author's wording.
- **Narrow audience:** Not everyone wants guided conversation. Position it as an optional "go deeper" layer, with the outing still useful without it.
- **Fit with the core promise:** The app's core is getting out of the house. Keep the connection layer light enough not to slow the Friday plan.

### Open decisions
- Whether to license or ask permission to use the book's questions, or write an original bank.
- Whether to offer a faith-aware track in version one.
- Whether to sell card packs separately or include them in the couples plan.
- Whether to start with committed couples and parents (easier) or with first dates and singles (more matchmaking value).

---

## Date Ideas Bank for the Connection Cohort

Starter library for the date cohort. Each idea lists the best stage, the conversation levels it suits (from the seven-level framework above), rough cost and a note on why it works for connection. Replace generic entries with real, verified local places once a city is chosen. Costs are rough planning figures **(assumption)**.

### First dates and meeting through an activity (Levels 1-2)
Goal: easy to leave, easy to talk, no pressure.

| Idea | Cost | Why it works |
|---|---|---|
| Coffee and a short walk | $ | Public, short, easy exit, side-by-side talking |
| Farmers or night market stroll | $ | Things to look at give natural topics |
| Bookstore or record-shop browse, then a drink | $ | Shows taste without a quiz |
| Free museum or gallery hour | Free-$ | Opinions come up naturally |
| Food-truck or street-food crawl | $$ | Shared tasting breaks the ice |
| Mini-golf, bowling or arcade | $$ | Playfulness lowers nerves |
| Drop-in pottery or paint class | $$ | Shared focus, low pressure to fill silence |
| Group trivia night as a pair | $ | Team feeling, others around |

### Early dating (Levels 1-4)
Goal: learn values, background and hopes.

| Idea | Cost | Why it works |
|---|---|---|
| Hike or park trail with a picnic | $ | Walking talk, room for longer answers |
| Cooking class or cook together at home | $$ | Cooperation shows how you work together |
| Farmers-market shop, then cook what you bought | $$ | Planning together, a meal at the end |
| Bike ride to a cafe or viewpoint | $ | Shared adventure, conversation at stops |
| Neighborhood walking tour or history walk | $ | Many topics, a "what would you change" prompt |
| Live music at a small venue | $$ | Shared experience, then a talk afterward |
| Volunteer shift together | Free | Shows values in action |
| Visit each other's favorite place | Free-$ | A natural Facts and Opinions conversation |

### Committed couples (Levels 1-7)
Goal: depth, trust and shared plans.

| Idea | Cost | Why it works |
|---|---|---|
| Quiet dinner with no phones | $$-$$$ | Room for Levels 5-7 |
| Sunset or sunrise spot with a thermos | $ | Calm setting for dreams and feelings |
| Day trip to a small town | $$ | Time away from routine |
| "Future map" date: coffee and a list of 1, 5 and 10-year hopes | $ | Level 4 on paper |
| Revisit where you met, a first date or a meaningful place | Free-$ | Shared history, gratitude |
| Couples' class (dance, pottery, language) | $$ | New skill together, mild vulnerability |
| Stargazing or a night walk | Free | Quiet, intimate and distraction-free |
| Write letters to each other over dessert | $ | Level 5-7 in a low-pressure format |

### Married, long-term and busy parents: reconnect dates (Levels 1-7)
Goal: reconnect after routine, kids and tiredness.

| Idea | Cost | Why it works |
|---|---|---|
| Two-hour coffee date while kids are in school or with a sitter | $ | Short, realistic and protected |
| Early dinner, home by 8:30 | $$ | Fits a sitter's hours and early bedtimes |
| Walk the neighborhood after bedtime with a baby monitor | Free | No sitter needed |
| At-home "restaurant night" with a card from the app | $ | Zero logistics, still special |
| Lunch date on a weekday | $$ | Easier childcare, cheaper menus |
| Date swap with another couple | Free | Trade sitting, both get a night |
| Revisit an early-dating idea, then a "remember when" talk | $-$$ | Level 2 and 4 refresh |
| Quarterly overnight, even a one-night local hotel | $$$ | Longer uninterrupted talk for Levels 6-7 |

### Friends (optional track, Levels 1-5)
| Idea | Cost | Why it works |
|---|---|---|
| Hike or long walk | Free | Talk without eye contact pressure |
| Cook-together night | $$ | Teamwork and a meal |
| Game night or board-game cafe | $ | Play first, talk follows |
| Volunteer day | Free | Meaning and shared values |
| Seasonal festival or market | $ | Shared novelty |

### Seasonal date ideas (rotate by quarter)
- **Fall:** Apple or cider-mill visit, leaf-peeping drive, pumpkin carving at home, harvest market, cozy cafe with a board game.
- **Winter:** Holiday-lights walk with hot chocolate, ice skating, an indoor climbing or bouldering session, a museum on a cold day, soup-making night.
- **Spring:** Flower or botanical-garden walk, first patio drink of the year, farmers-market opening day, bike ride, plant-a-garden date.
- **Summer:** Outdoor movie, sunset picnic, swim spot or lake, night market, outdoor concert, ice-cream walk.

### By budget
- **Free:** Sunrise or sunset walk, stargazing, volunteer shift, visit a favorite place, library browse, neighborhood photo walk.
- **Under $25:** Coffee and a walk, farmers-market picnic, record or book shop browse, food-truck date, mini-golf.
- **$25-75:** Cooking or pottery class, live music, a nice casual dinner, day trip fuel and lunch.
- **$75+:** Tasting menu, special-occasion dinner, overnight stay, a couples' workshop or retreat.

### By energy level
- **Chill:** Cafe, bookshop, gallery, picnic, sunset spot.
- **Moderate:** Walking tour, market crawl, pottery, trivia, bike ride.
- **Active:** Hike, climbing gym, kayaking, dance class, pickleball or tennis with a drink after.

### Date idea formats the app can send
- **Single idea:** "Saturday, 10am: farmers-market stroll and a shared breakfast. Suggested topic: Facts (what was home like growing up?). About $20. 15 minutes away."
- **Three-stop evening:** "Early dinner, then a short walk, then dessert. $60 total, home by 9:30. Good for parents with a sitter."
- **Rescue mode:** "Nothing planned tonight? Three open-now spots within 20 minutes that need no reservation."
- **Theme pack:** "First Year Together: 12 dates, one per month, each with a conversation card."
- **Challenge:** "Try three new cuisines this month. Earn the Taste badge for two."

### How the app should choose
Score each idea by relationship stage, conversation level, cost, travel time, available hours, season and weather, past likes and dislikes, accessibility and whether a sitter is needed. Show a primary pick and two alternates. After the date, ask "Would you do this again?" and feed the answer back into the next pick.

### Quality rules for date ideas
- Every date has a **backup** if it rains or the place is full.
- Every stranger or first-date idea is **public, easy to leave and well-lit**.
- Parent dates state the **time window** ("fits a 3-hour sitter slot").
- **No pressure to spend:** Free and low-cost options appear in every set.
- **Verify before sending:** Hours, prices and reservations are checked within 7 days.
- **Vary the mix:** Avoid sending the same type of date two weeks in a row.

### Open decisions
- Which stage to build the first 20 ideas for (this file suggests committed couples and parents, since they are the strongest paying audience).
- Whether to include a friends track in version one.
- Whether to sell theme packs such as "First Year Together" or include them in the plan.

---

## Two Date Tracks: Married Date Nights and Dating

The connection cohort splits into two tracks. They share the activity library and the seven-level conversation cards, but the problem each one solves is different.

| | **Dating** | **Married date nights** |
|---|---|---|
| **Core problem** | "Where do we go, and how do I get to know them?" | "We never go out, and when we do we talk about logistics." |
| **Main obstacle** | Awkwardness, choosing a place, fear of getting it wrong | Time, childcare, routine, tiredness |
| **Goal** | Learn who the other person really is, then decide if there is a future | Stay close, renew connection, keep choosing each other |
| **Conversation levels** | 1-4 early, up to 7 as it becomes serious | 1-7, with a focus on 4-7 (hopes, feelings, needs) |
| **Rhythm** | Weekly or every other week | A protected date every 1-2 weeks, plus a longer one each quarter |
| **Who plans** | Taking turns, with the app suggesting | One tap lock-in, partner notified, the plan is already made |
| **Paying audience** | Moderate | Strong, especially parents |

---

### Track A: Dating

**Purpose:** Help two people find out whether they are compatible, without an interview feel.

**Progression the app guides (about 6-8 dates):**

| Date | Setting | Levels | Aim |
|---|---|---|---|
| 1 | Coffee and short walk, public and easy to leave | 1-2 | Comfort and curiosity |
| 2 | A shared activity (market, class, mini-golf) | 1-3 | See how you play and cooperate |
| 3 | A meal where you can talk | 2-4 | Background, values, hopes |
| 4 | Something active or outdoors | 1-3 | Energy, adventure, humor |
| 5 | Visit each other's favorite place | 2-5 | Meet each other's world |
| 6 | Quiet evening, no phones | 4-6 | Feelings, dreams, honest talk |
| 7 | Meet something in each other's life (a friend, a family event, a volunteer shift) | 3-5 | Values in action |
| 8 | The "where is this going" date | 4-7 | Needs, expectations and next steps |

**Features specific to dating:**
- **Date-number awareness:** The app knows how many dates in and keeps the depth sensible.
- **Both-say-yes continuation:** After each date, each person privately answers "see them again?" and the answer reveals only if both say yes.
- **First-date safety:** Public places, share-my-plan and an easy exit option.
- **Taking-turns planning:** "Your pick" and "their pick" cards so effort is shared.
- **Red-flag and green-flag notes (private):** A personal notes page for what you noticed. Never shared and not a scoring system.
- **Dating-goal intake:** Casual, serious, marriage-minded. The app matches the pace and the questions to that.
- **No pressure on depth:** The deeper levels unlock only when both choose.

**Dating date ideas by vibe:**
- **Low pressure:** Coffee walk, market, bookstore, gallery hour, trivia as a pair.
- **Playful:** Mini-golf, bowling, arcade, a drop-in class, a food crawl.
- **Getting to know you:** Cook a meal, picnic and hike, favorite-place tour, volunteer shift.
- **Going deeper:** Quiet dinner, sunset spot, a day trip, a "future map" coffee.

---

### Track B: Married Date Nights

**Purpose:** Make a regular, protected, connecting date easy to plan and easy to keep, even with kids and a full schedule.

**The married-date-night rhythm the app builds:**

| Cadence | What | Example |
|---|---|---|
| **Weekly (10-20 minutes)** | A "connection check-in" at home | Two questions over tea after the kids sleep |
| **Every 1-2 weeks** | A protected date night out | Early dinner, home by 9 |
| **Monthly** | A "try something new" date | A class, a new neighborhood, a new cuisine |
| **Quarterly** | A longer reconnect | A day trip or one night away |
| **Yearly** | An anniversary plan | Revisit where you met, plus letters |

**Features specific to married couples:**
- **Standing date night:** Pick a recurring slot (for example every other Friday). The app proposes a plan each time and holds it on both calendars.
- **Logistics handled:** Sitter reminder two days ahead, reservation reminder, travel buffer and a "home by" time that matches your sitter.
- **Partner-planned and surprise modes:** One partner can plan a date and the other receives only the time and what to wear.
- **At-home date mode:** For nights without a sitter, with a meal idea, a game or a conversation card, and a "phones in a basket" prompt.
- **Conversation cards with a married focus:** Levels 4-7 emphasize hopes for the family, feelings, forgiveness, and what each person needs to feel loved, with a rule to listen first and not solve.
- **Reconnect prompts after a hard season:** New baby, job change, loss or a move, with gentler cards.
- **Gratitude layer:** One appreciation each at the end of the date ("one thing I loved about tonight").
- **Anniversary and milestone reminders:** A plan, a reminder and a "do something meaningful" suggestion a few weeks ahead.
- **No-screens and no-logistics rule:** A tip that parenting logistics wait until the last 10 minutes.
- **Keep-it-going tracker:** A forgiving streak (dates this quarter, not an unbroken chain) and a private "dates we've had" map.

**Married date ideas by situation:**
- **No sitter, no budget:** Backyard or living-room picnic, after-bedtime walk, cook a recipe from the year you met, stargazing.
- **Two hours with a sitter:** Early dinner, coffee and a walk, a class, a drink at a quiet bar.
- **Half day (kids at school or a grandparent):** Weekday lunch date, hike, museum, spa-style hour.
- **A full evening:** Dinner and live music, a show, a tasting.
- **Overnight:** A local hotel night, a cabin or a small-town trip.
- **Seasonal:** Cider-mill afternoon, holiday-lights walk, spring garden stroll, summer outdoor concert.

**A sample "Reconnect" 12-month pack for married couples:**
1. January: Dreams for the year (Level 4)
2. February: What made us fall for each other (Levels 2 and 5)
3. March: A new skill together (a class)
4. April: How we like to be supported (Level 5)
5. May: Our best memories (Level 2)
6. June: Fears we haven't said out loud (Level 6, with a "pass" option)
7. July: An adventure day
8. August: What each of us needs more of (Level 7)
9. September: Family hopes for the next 5 years (Level 4)
10. October: Forgiveness and fresh starts (Level 6)
11. November: Gratitude letters
12. December: Year in review and next-year plan

---

### Business model by track
- **Dating:** Free tier with a date idea and one card per outing. Paid ($4.99/mo or $39/yr) for date-number guidance, shared planning and the private notes page. Revenue also comes from venues paying for "good first date" slots.
- **Married date nights:** Couples plan ($59/yr) with the standing date, sitter and reservation reminders, the reconnect pack and the anniversary tools. Add the 12-month pack as a $19 one-time purchase, and a gift version.
- **Partners:** Sitter and childcare services (fee per booking from the reminder), restaurants and activity venues (featured date-night slots and bundles), marriage-preparation and enrichment programs, counselors who want an optional "date homework" tool and faith communities that distribute the packs.
- **Employer and wellness benefit:** A "healthy relationships" perk for staff, tested with HR contacts.
- **Gift market:** Wedding and anniversary gifts such as a year of monthly date plans.

### Metrics by track
- **Dating:** Dates per person per month, share reaching date 3, share that continue by mutual yes, skip rate on cards, safety-tool use and conversion to paid.
- **Married:** Dates per couple per month, share with a standing date set, plans locked by Thursday, follow-through, sitter reminders used, 12-month pack completion, couples-plan retention at 6 and 12 months and gratitude-prompt completion.

### Validation
1. **Weeks 1-3:** Offer two free lists, one for dating and one for married couples, each with one date plan and a card per week. Compare reply and "Going" rates.
2. **Weeks 3-6:** Recruit 15 married couples (mostly parents) for a standing-date pilot of 4 dates. Measure how many dates actually happen compared with their previous month.
3. **Weeks 3-6:** Recruit 20 dating people for a guided 3-date trial and ask which cards felt natural.
4. **Weeks 5-8:** Test the $19 12-month pack and the $59 couples plan with the pilot couples.
5. **Gate:** Keep the married track if couples average at least 2 more dates a month than before and half would pay. Keep the dating track if at least 40% reach date 3 and rate the cards as helpful.

### Risks
- **Dating is crowded:** Dating apps dominate matching, so position this as the "what to do on the date" layer, not another matching app.
- **Married couples are hard to reach:** Use warm channels (parents' groups, churches and community groups, marriage-prep classes, employers), as in the marketing plan.
- **Logistics break the habit:** If the sitter cancels, the date dies. Include an at-home fallback every time.
- **Sensitivity:** Marriages in trouble need professional help, not cards. Link to counseling resources on Levels 5-7, and never present the app as treatment.
- **Overly scripted:** Keep the cards optional and let the couple turn them off.

### Link to the rest of the plan
- **Parents marketing plan:** Add the "Reconnect" pack and "5 date nights you can pull off with a sitter" as lead magnets (`2026-11-14-city-explorer-parent-marketing-plan.md`).
- **Matchmaking idea:** The dating track works as the "first dates" experience after an introduction (`2026-11-14-matchmaking-business.md`).

### Open decisions
- Whether to launch married date nights first (stronger paying audience) and add dating after, which this file recommends.
- Whether to sell the 12-month pack as a one-time purchase or include it in the plan.
- Whether to add a faith-aware version of the married pack in version one.
