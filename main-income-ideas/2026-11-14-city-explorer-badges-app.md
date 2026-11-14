# City Explorer: A Badge-Collecting App That Gets You Out of the House (2026-11-14)

**App name:** Outly (chosen 2026-11-14; trademark, domain and app-store checks still to do, and other apps use this name). **Tagline (proposed):** Hang up and hang out. See `city-explorer/11-name-and-tagline.md`.

## Core product (one sentence)
**An app that sends you one notification a week with a ready weekend plan.** You pick the day and time (default Thursday late morning). The notification holds one complete, seasonal plan matched to what you said you like at signup. One tap locks it in. Badges, cohorts, listings and the rest of the files are extras that only matter if this one notification gets people out of the house.

**Rules for the core product:**
- **One notification a week.** No daily pings, no nagging. Anything else is sent only after the user does something (taps "lock it in," asks for a reminder).
- **One plan, not a feed.** The notification shows a single plan with what, where, when, cost and travel time. Two alternates sit one tap away inside the app.
- **Open the app to act.** Tapping the notification opens the plan with Lock it in, Swap, Invite someone and Not this week.
- **Rescue is pull, not push.** A button in the app ("I have nothing planned") returns open-now options on demand, so the Friday problem is solved without sending another notification.

Users also collect badges for doing different things in their own city, alone, with friends or with a partner.

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

### The weekly rhythm: one notification, everything else on request

| When | What happens | Sent by the app? |
|---|---|---|
| **Weekly, user's chosen day (default Thursday late morning)** | **The one notification:** a complete plan ("Saturday 11am, farmers market, then coffee next door, 12 min away") with **Lock it in** | Yes, the only unprompted message |
| **On "Lock it in"** | Add to the calendar, invite a person in one tap with a pre-written message, confirm hours | After the user's tap |
| **Day before a locked plan** | One reminder with address, hours, travel time and a weather swap if needed | Only if the user locked a plan (can be turned off) |
| **Friday evening, nothing locked** | **Rescue mode,** pulled by the user: "I have nothing planned" shows 3 open-now options within 20 minutes | No, the user opens it |
| **After the outing** | "How was it?" one-tap check-in for the badge, shown the next time the app opens | No push by default |

Earlier drafts had Wednesday, Thursday, Friday, Saturday and Sunday messages. Those are replaced by this single weekly notification to avoid fatigue.

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
- **Rescue use:** Share of users with no plan who open rescue mode on Friday and go out (target 30%+).
- **Notification health:** Open rate of the weekly notification (target 50%+) and opt-out rate under 2% per send (assumption).
- **Follow-through rate:** Locked plans that end in a check-in (target 60%+).
- **Weekends out per month** per active user (the main outcome, target 3+).

### Updated validation test
For the free Thursday list, test the two versions side by side with 50 subscribers each:
- **A:** Idea only.
- **B:** One weekly notification with a complete plan, one-tap lock-in and invite, and an in-app rescue button.
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

## Where Everything Lives

This overview is the short version. Detail sits in separate files under `city-explorer/`.

| File | What it covers | Priority |
|---|---|---|
| [01-focus-and-4-week-plan.md](city-explorer/01-focus-and-4-week-plan.md) | The one launch product and a 4-week test | **Start here** |
| [12-build-mvp-first-plan.md](city-explorer/12-build-mvp-first-plan.md) | **Chosen route:** build Outly v0.1 first, then test and pivot | **Start here (build-first)** |
| [02-gaps-and-solutions.md](city-explorer/02-gaps-and-solutions.md) | Economics, data, venues, privacy, safety | Read before building |
| [03-cohorts.md](city-explorer/03-cohorts.md) | Life-stage cohorts and missing cohorts | Later |
| [04-older-adults-cohort.md](city-explorer/04-older-adults-cohort.md) | Adults 55+ | Later |
| [05-photo-hunts.md](city-explorer/05-photo-hunts.md) | Scavenger hunts and photo proof | Later |
| [06-connection-cohort.md](city-explorer/06-connection-cohort.md) | Guided conversation for couples | Later |
| [07-date-ideas-bank.md](city-explorer/07-date-ideas-bank.md) | Date ideas by stage, season and budget | Content source |
| [08-date-tracks-and-club.md](city-explorer/08-date-tracks-and-club.md) | Dating, married date nights, Date Night Club | Later |
| [09-business-listings-and-badge-counts.md](city-explorer/09-business-listings-and-badge-counts.md) | Paid listings and badge analytics | Venue revenue |
| [10-host-locations-and-idea-submissions.md](city-explorer/10-host-locations-and-idea-submissions.md) | Host venues for matchmaking and a way for anyone to submit places and ideas | Submission form is cheap, start in week 1 |
| [11-name-and-tagline.md](city-explorer/11-name-and-tagline.md) | Name shortlist and the tagline "Hang up and hang out" | Decide before printing anything |
| [archive-date-spots.md](city-explorer/archive-date-spots.md) | Superseded date-spots idea | Archive |

Related: [parent marketing plan](2026-11-14-city-explorer-parent-marketing-plan.md) and [matchmaking business](2026-11-14-matchmaking-business.md).
