# City Explorer MVP Playbook: Get It Done in 28 Days

[Overview](../2026-11-14-city-explorer-badges-app.md)

> **Note (2026-11-14):** The chosen route is to build the MVP first. See `12-build-mvp-first-plan.md`. This manual playbook stays as a fallback and as the source of scripts, place-sheet columns and the plan template.

**Product:** One notification a week with a complete weekend plan for parents of kids 0-8. One tap locks it in and texts the other parent.

**Goal of the MVP:** Prove that parents go out more when they get a finished plan than when they get an idea. Nothing else.

**Budget:** About $100 and 40-50 hours over 4 weeks. **No app code in this phase.**

Numbers marked (assumption) are estimates. Verify any tool pricing and message-registration rules before relying on them.

---

## Definition of done (day 28)

- 30 parents on the list, 20+ active every week
- 3 weekly plans sent to everyone
- 8 parent interviews done
- 3 venues told about a free 60-day pilot
- A written decision: build, fix or stop

---

## The stack (all manual, no code)

| Job | Tool | Cost |
|---|---|---|
| Sign-up and intake form | Tally or Google Forms | Free |
| Place sheet, plans, parent list, results | Google Sheets or Airtable | Free |
| Weekly message | Email tool (free tier) or personal texts to under 30 people | $0-20 |
| Replies and "lock it in" | A dedicated phone number or shared inbox | $0-15 |
| Landing page | One page in Tally, Carrd or a Google Site | $0-20 |
| Venue visit counting | A code word in the message, counted by hand | Free |

Rule: if a task takes under 10 minutes by hand, do it by hand. Automate only after week 4.

---

## Day-by-day

### Week 1: Build the assets (12-15 hours)

| Day | Do this | Output |
|---|---|---|
| 1 | Pick the cluster: 3-4 adjacent neighborhoods you know well. Write the one-line promise: "One text a week with a finished weekend plan for families with little kids." | Cluster and promise |
| 2 | Build the intake form with the 10 questions from the overview, plus "who would you want to invite?" | Live form |
| 3-4 | Fill the place sheet (below) with 60 places. Visit or call every one. Skip anything you cannot verify. | 60 verified places |
| 5 | Write 10 complete plans (below). Write 3 weeks of messages. | 10 plans, 3 messages |
| 6 | Build the one-page site: promise, 3 bullets, sign-up button. | Live page |
| 7 | Message 40 parents (script below). | 20 sign-ups by day 10 |

**Place sheet columns:** Name, address, neighborhood, type, ages (0-2, 3-5, 6-8), cost, indoor/outdoor, best time, stay length, stroller access, changing table, parking, quiet or loud, food available, rainy-day safe, hours, last verified date, notes.

**Plan template (copy for each plan):**
```
Title: Saturday morning at the market, then the playground
When: Sat 9:30-12:00
Stop 1: [place] - 9:30, 60 min, $0-10, stroller ok
Stop 2: [place] - 11:00, 45 min, free, 4 min away
Travel: 12 min from [cluster center]
Nap-friendly: yes, home by 12:15
Rainy backup: [indoor place], same area
Checked: hours and access verified [date]
Reply GOING to lock it in
```

### Week 2: First send and the A/B split (10-12 hours)

| Day | Do this |
|---|---|
| 8 | Split sign-ups at random into **Group A (idea only)** and **Group B (full plan)**. |
| 9 | Send Thursday 10am: A gets one line ("Try the Eastside farmers market Saturday"). B gets the full plan. Both get one message only. |
| 10 | Answer every reply within 2 hours. For B, when someone replies GOING, send a pre-written text they can forward to their partner. |
| 11 | Friday morning, B only: if nothing locked, send the three open-now options when the parent texts RESCUE. |
| 12 | Sunday evening: send both groups the same text: "Did you go anywhere this weekend? Reply Y or N." |
| 14 | Log results in the sheet. |

### Week 3: Second send, interviews, more parents (10-12 hours)

| Day | Do this |
|---|---|
| 15 | Send plan 2 to both groups, same split. |
| 16-18 | Interview 8 parents, 4 from each group, 15 minutes each (questions below). |
| 19-21 | Ask 2 parent-group admins and 3 preschool or library contacts to share the sign-up link. Aim for 10 more parents. |
| 21 | Visit or call 10 venues and pitch the pilot (script below). |

### Week 4: Third send and the decision (8-10 hours)

| Day | Do this |
|---|---|
| 22 | Send plan 3. |
| 23 | Offer founding membership: "$19 for the first year. Reply YES." |
| 24-25 | Call 10 more venues. Offer the 60-day pilot with a code word. |
| 26 | Count results and fill in the decision table. |
| 27 | Write one page: what worked, what didn't, what to do next. |
| 28 | Decide. |

---

## Scripts

**Outreach to a parent you know:**
> Hi [name], I'm testing a free weekly text for parents of little kids. One finished weekend plan, hours and stroller access already checked. Can I send you this week's? Takes 2 minutes to sign up: [link]. I'd love your honest feedback.

**Ask a group admin:**
> Hi [name], I live in [neighborhood] and I'm building a free weekly weekend-plan text for families. Would you be open to sharing the sign-up link in the group? I'll send you the plans first and credit the group.

**Weekly message (Group B):**
> Saturday plan: [title]. [Stop 1, time, cost]. Then [Stop 2]. Home by [time]. Rainy backup: [place]. Reply GOING and I'll send a text you can forward to your partner. Reply RESCUE any Friday night for last-minute options.

**Forwardable invite (sent after GOING):**
> Saturday 9:30, farmers market then the playground, home by 12. Want to come? I'll bring snacks.

**Parent interview (15 minutes):**
1. What did you do last weekend? Who decided, and when?
2. Did you use the plan? If not, what got in the way?
3. What was missing: details, timing, distance, cost, someone to go with?
4. Would you want this every week? What would you pay, if anything?
5. Who else should get it?

**Venue pitch (2 minutes):**
> I send local parents a weekly plan. I'd like to feature you for 60 days, free. Parents will say a code word, [word], at the counter, and I'll send you the count of visits. If it's under 20, you owe nothing. After that, it's $99 a month if you want to keep it.

---

## What to track (one sheet, one row per parent per week)

Parent, group (A or B), week, plan sent, reply, locked in (Y/N), went (Y/N), would repeat (Y/N), code word used, notes.

**Weekly numbers:** sign-ups, active parents, lock-in rate, went rate by group, replies, interviews done, venues contacted, venues interested.

---

## Decision table (assumption)

| Result at day 28 | Do this |
|---|---|
| B went at least 1.5x as often as A and 40%+ locked in | Build the simple web app (below) and start paid venue pilots |
| B beat A by less | Keep the weekly send, change the plan format, run 3 more weeks |
| No difference or under 15 active parents | Stop or change cluster or audience before building |
| 50%+ say they would pay $19-39/yr | Open the paid plan in week 5 |
| 3+ venues agree to a paid slot after the pilot | Start counting redeemed codes monthly |

---

## After the gate: the first build (weeks 5-10)

Build only what the test proved people use.

**Version 1 of the app (web, installable):**
1. Sign-in by email or phone number
2. Intake screens (the same 10 questions)
3. A plan screen with Lock it in, Swap, Invite and Not this week
4. A weekly send at the user's chosen day and time
5. A rescue button that lists open-now places
6. A venue page with listing details and a visit-code count

**Data tables:** users, places, plans, plan_sends, replies, venues, visit_codes.

**Notifications:** Start with email and text. Web push on phones has platform limits (for example, some phones require installing the web app to the home screen), so check the current rules before relying on it. A native app is a later decision.

**Build order:** (1) places and plans admin sheet, (2) intake and sign-in, (3) weekly send job, (4) plan screen, (5) lock-in and invite, (6) venue code tracking.

---

## Do not build yet

Badges and passports, photo hunts, other cohorts, dating and connection cards, Date Night Club, paid listings, badge counts and leaderboards. They live in the other files. Start any of them only when its trigger is met:

| Later | Trigger |
|---|---|
| Other cohorts | 12-week retention above 50% |
| Badges | Parents ask for something to collect, or retention dips |
| Photo hunts | Place list goes stale |
| Paid listings | 30+ venues and 300+ users |
| Native app | The web version retains users for 3 months |

---

## Before the first send

- Get opt-in for every text or email, with a clear way to stop.
- Write a short privacy policy. Collect no children's names or photos.
- Say only what you checked, with the date.
- Check local rules on business texting and registration before sending at volume.
- Have a lawyer review the terms before taking money.

---

## Costs and time

| Item | Cost |
|---|---|
| Tools and page | $0-60 |
| Phone number or inbox | $0-15 |
| Small thank-you gifts | $25-50 |
| **Total** | **$25-125** |

Time: 12-15 hours in week 1, then 8-12 a week. Keep your day job until the business covers half your target income for 3 months in a row.

## Write down now

What result at day 28 makes you stop? What makes you continue? Put both in one sentence each before you start.
