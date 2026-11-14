# Outly: Build the MVP First, Then Test and Pivot

[Overview](../2026-11-14-city-explorer-badges-app.md) | [Manual test playbook](01-focus-and-4-week-plan.md)

**Decision (2026-11-14):** Build the MVP first, put it in front of real parents, then pivot on what the data shows. This file is the plan for that route. The earlier no-code playbook stays as a fallback and as the source of scripts.

**The main risk of build-first:** The thing most likely to fail is not the software. It is whether parents act on a weekly plan. To limit the cost of being wrong, build a thin shell and keep the content (places, plans) hand-made. Time-box the build to 4 weeks. Numbers marked (assumption) are estimates.

---

## MVP scope: Outly v0.1

**One job:** Send each parent one notification a week with one complete weekend plan, and make it one tap to lock in.

### In scope
1. **Sign-up and intake:** Email or phone sign-in, the 10 intake questions, chosen send day and time, preferred channel (email, text, or push if supported).
2. **Admin plan editor (for you):** Create plans from a places table, tag them by age range, cost, indoor/outdoor, season, time of day and neighborhood.
3. **Weekly send:** A scheduled job picks one plan per user (simple rule-based matching) and sends the notification at their chosen time.
4. **Plan page (opened from the notification):** What, where, when, cost, travel time, backup, "checked on [date]." Buttons: **Lock it in, Swap, Invite someone, Not this week.**
5. **Invite link:** A shareable link to the plan that works without an account, with a pre-written text.
6. **Rescue button:** "I have nothing planned" returns 3 open-now places near the user.
7. **After-outing check-in:** One tap on next open ("Did you go?").
8. **Basic analytics:** An events table (sent, opened, locked, swapped, invited, went, opt-out).
9. **Venue code page (minimal):** A code word per venue and a manual count.

### Out of scope for v0.1
Badges and passports, photo hunts, other cohorts, dating and connection cards, Date Night Club, paid listings, badge counts, user-submitted places (a simple form feeding your sheet is fine), payments, native apps.

---

## Suggested stack (a solo, fast build)

| Piece | Option | Why |
|---|---|---|
| App | A web app (installable) built with a framework you know | One codebase, fastest to ship |
| Database and auth | A hosted Postgres with built-in auth | Little setup |
| Scheduled send | A cron job or a scheduled function | Simple and reliable |
| Email | A transactional email service | Cheap, easy to start |
| Text messages | An SMS provider (registration is required in some countries) | Higher open rates, but slower to set up |
| Push | Web push, with platform limits (some phones require the app to be installed to the home screen) | Check current rules before relying on it |
| Hosting | A managed host with a free tier | Low cost to start |
| Maps and place data | Your own hand-checked places table, with a free map for display | No licensing cost at the start |

Verify pricing, limits and registration rules for each service before committing. Use email first, add SMS after the sign-up flow works.

---

## Data model (minimum)

| Table | Key fields |
|---|---|
| users | id, contact, channel, send_day, send_time, neighborhood, kid_age_ranges, budget, energy, interests, created_at |
| places | id, name, address, lat, lng, tags, ages, cost, indoor, stroller_access, changing_table, hours, last_verified |
| plans | id, title, place_ids, steps, duration, cost, season, backup_place_id, notes |
| sends | id, user_id, plan_id, sent_at, channel |
| events | id, user_id, plan_id, type, created_at |
| venues | id, place_id, code_word, status |
| invites | id, plan_id, user_id, token |

Rule for matching v0.1: filter plans by season, age range, budget and distance, exclude plans already sent, pick the highest-rated or least recent. Replace with something smarter only if the data shows it matters.

---

## Build schedule (4 weeks, about 60-80 hours, assumption)

| Week | Build | Done when |
|---|---|---|
| **1** | Project setup, database, auth, intake form, places and plans tables, admin plan editor | You can create a plan and see it |
| **2** | Weekly send job, plan page, Lock it in, Swap, Not this week, invite link | A test user gets a notification and locks a plan |
| **3** | Rescue button, check-in, events table, simple dashboard, venue code page, unsubscribe | Every action logs an event, and you can see rates |
| **4** | Privacy policy and terms, opt-in text, error handling, content fill (60 places, 10 plans), onboard the first 30 parents | 30 real users on the live app |

**Content is part of the build.** Fill the 60-place sheet and 10 plans during weeks 1-3 using the place columns and plan template in the playbook.

---

## Launch and test (weeks 5-10)

1. **Weeks 5-6:** Run the app with 30-50 parents. Send one plan a week. Interview 8 parents. Fix breakages only.
2. **Weeks 7-8:** Add 30 more parents through group admins, preschools and libraries. Start 3-5 venue pilots with code words.
3. **Weeks 9-10:** Test a paid offer ($19-39/yr founding price, assumption) and decide.

### Measures (dashboard)

| Metric | Why it matters | First target (assumption) |
|---|---|---|
| Sign-up to first notification opened | The onboarding works | 80% |
| Weekly open rate | Notification is useful | 50%+ |
| Lock-in rate | Plan is good enough to commit to | 35%+ |
| Went rate (self-reported) | Plan actually gets people out | 50% of locked |
| Weeks active in a row | Habit forming | 4+ for half of users |
| Invites sent | Spreads inside families | 25% of locks |
| Opt-out rate | Annoyance | Under 2% per send |
| Venue visits via code | Revenue case | 20 per venue in 60 days |
| Willingness to pay | Consumer revenue | 40%+ say yes |

---

## Pivot rules (decide in advance)

| What the data shows | Pivot to |
|---|---|
| Open and lock rates are high, but people don't go | Fix plan quality and details (travel time, timing), or add the Friday reminder |
| People open but never lock | Shorten the plan, show a single stop, or simplify the lock step |
| Plans work but parents won't pay | Make it free for parents and charge venues, or sell to schools, employers or parent groups |
| Parents of young kids are lukewarm, couples or older adults respond more | Switch the lead cohort (see the cohorts file) |
| Venues respond more than parents | Venue-first: a local-business marketing tool that sends traffic by the same weekly plan |
| Text works much better than email or push | Move to text-first, and budget for registration and cost |
| Weekly is too often or too rare | Test every other week or twice a month |
| Engagement is strong only in one neighborhood | Narrow to that neighborhood and go deep |
| Nobody uses it after 6 weeks | Stop or restart with a different idea, using the interviews |

**Stop rule:** Fewer than 25 active parents after 6 weeks of live use, or lock-in under 15%, means stop or change the audience before building anything more.

---

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Spending weeks on software before testing demand | Time-box to 4 weeks, cut scope hard, keep content manual |
| Content takes more time than code | Plan for 15-20 hours of place checking and plan writing |
| Notification delivery and message rules | Start with email, add text after registration, check push limits |
| Low sign-ups after launch | Line up 20 parents and 3 group admins before launch day |
| Privacy and children's data | Collect only age ranges, no names or photos of children, short policy, opt-in |
| Name conflicts (Outly is used by other apps) | Trademark, domain and app-store checks before any paid launch |

---

## Pre-launch checklist

- [ ] 60 places verified, 10 plans written
- [ ] 30 parents committed to try it
- [ ] Terms, privacy policy and opt-in text live
- [ ] Unsubscribe works on every message
- [ ] Events logging checked end to end
- [ ] A test send to yourself and 3 friends
- [ ] Interview script and results sheet ready
- [ ] Trademark and domain check done, or a plan to rename

---

## Build-first versus manual-first (why the playbook still matters)

| | Build first (this plan) | Manual first (playbook) |
|---|---|---|
| Time to first real user feedback | About 5 weeks | About 1-2 weeks |
| Cost | 60-80 hours of build | 10-15 hours of setup |
| Risk | Building something nobody wants | Less polished, harder to scale |
| Good if | You enjoy building, and the code is reusable | You want fast proof before investing |

**A middle path you can still use:** Send the first plan to 10 friends by text in week 1 while you build. It costs almost nothing and tests the idea long before the app is ready.

---

## What's Working: The Weekly Review

How to tell, week by week, whether Outly is doing its job. Measure what people do, not what they say. Numbers marked (assumption) are starting targets to adjust with real data.

### The five numbers to check each week

| Question | Number | Healthy sign (assumption) |
|---|---|---|
| Do they open it? | Weekly notification open rate | 50%+ |
| Is the plan good enough to commit to? | Lock-in rate | 35%+ |
| Does it get them out the door? | Went rate among locked plans | 50%+ |
| Is it becoming a habit? | Users active 4 weeks in a row | Half of users |
| Is it annoying? | Opt-out rate per send | Under 2% |

If you track only one, track **"went."** It is the only number that shows the app does its job. The others explain why it is not.

### 30-minute weekly review

1. Update the five numbers and compare them with last week.
2. Pick the **weakest** number. Ignore the rest this week.
3. Look at the 5 plans with the highest and lowest lock-in. What do the good ones share (cost, distance, time of day, age range)?
4. Read every reply and swap reason. "Too far" and "wrong age" are free product direction.
5. Call or text 2 users who went and 2 who did not. Ask one question: "What decided it?"
6. Write one change for next week, and only one, so you can tell if it worked.

### Cuts to look at

- Plan type: outdoor vs. indoor, free vs. paid, morning vs. afternoon
- Child age range and neighborhood
- Channel: email vs. text vs. push
- Send day and time
- Venue: visits through each code word

### Signals that it is working

- Parents forward the invite link without being asked
- They reply GOING on their own, or ask for more
- Users in week 4 do at least as well as users in week 1
- A venue asks to be featured again

### Signals that it is not, even if sign-ups look good

| Pattern | What it usually means |
|---|---|
| High opens, low lock-ins | Plans look good but are not actionable |
| High lock-ins, low went rate | Plans fall apart on the day (timing, weather, distance) |
| Sign-ups from one group post, then silence | Curiosity, not need |
| Many swaps of the same type | The matching rule is off for that audience |
| Opt-outs jump after a certain plan | That plan type or send time is wrong |

### Results sheet (one row per user per week)

| Column | Example |
|---|---|
| user_id | 014 |
| week | 2026-W49 |
| cohort tag | parent, kids 3-5, Eastside |
| channel | email |
| plan_id | 7 |
| opened | Y |
| action | locked |
| invited | Y |
| went | Y |
| would repeat | Y |
| code word used | N |
| swap reason | |
| notes | "loved the playground, a bit far" |

### Weekly summary block (fill in every Monday)

```
Week: ____    Active users: ___    Sends: ___
Open rate: __%    Lock-in: __%    Went: __%    Opt-outs: __%
Weakest number: ______
Best plan: ______ (why: ______)
Worst plan: ______ (why: ______)
What users said: ______
One change for next week: ______
Pivot trigger hit? (see pivot rules)  Y / N
```

### Caveats

- **Small numbers mislead.** With 30 users, 3 people move a rate by 10 points. Look at 3-4 week trends and use interviews to explain the numbers.
- **"Went" is self-reported.** Compare it with venue code counts when you have them.
- **One change at a time.** Changing several things per week hides what worked.
