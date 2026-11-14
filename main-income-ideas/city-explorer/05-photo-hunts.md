# City Explorer: Scavenger Hunts and Photo Proof

[Back to the City Explorer overview](../2026-11-14-city-explorer-badges-app.md) | [Focus and 4-week plan](01-focus-and-4-week-plan.md)

Photo-based badges that prove a visit and keep place data fresh. Build only after the core weekly plan works.

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
