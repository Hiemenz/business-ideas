# E-Ink Flight Display: A Silent Paper-Look Desk Tracker for the Plane Overhead (2026-11-14)

A small desk or shelf display that shows the flight nearest your window, or a specific flight you are following, in a calm paper-like e-ink style. Inspired by a photo of a color LCD flight tracker (a 3D-printed case labeled "SKYTILE" showing route map, plane photo, airline, aircraft type, altitude, speed and arrival time). This idea is the e-ink version.

## Who this is for
A 29-year-old software engineer with data and hardware-tinkering skills who wants to build solo in evenings and weekends with no outside funding. **Honest note up front:** hardware is lumpy and low-margin, so this is better treated as a side-income or niche business than as a full salary replacement. The income math below shows why.

## Lens: Alex Hormozi
- **Value equation:** Dream outcome is a beautiful, always-on window to the sky that makes people smile. Effort is low (plug in, connect Wi-Fi, done). Time delay is short (first flight shows within minutes).
- **Grand Slam Offer:** "Plug it in and see your first plane in 10 minutes, or return it for a full refund within 60 days."
- **Own the audience:** Aviation fans are tight communities. Sell through them first (warm), then content, then retail.

## What I found about the photo and the market
- I searched for "Skytile" and **found no product by that name**, so it may be a DIY build, a prototype or a very new or regional product. I could not confirm it.
- **Existing desk flight trackers** are common: JetClock Desk (small round display), a $400 desk radar, LED matrix flight boards and an iPad-based app called Skyty Wall. See the sources in the chat message that accompanies this file.
- **E-ink versions exist as hobby builds** (Raspberry Pi with an e-ink badge or an Inky panel, or an ePaper "closest flight" project), but I did not find a polished, ready-to-buy e-ink flight tracker. That gap is the opportunity, but it may only look empty because few people have tried selling one.
- **A builder noted e-ink refresh felt too slow and flickered** for a desk display, so the design must be built around slow refresh, not fight it.

## Why e-ink
- **Silent and glare-free:** No glowing screen in the bedroom or on a shelf.
- **Looks like a printed card,** which suits a living room or office better than a bright LCD.
- **Very low power:** The image holds without power, so it can run on USB for pennies or even a battery for a "follow a flight" card.
- **Readable in daylight** near windows.
- **Drawbacks:** Slow refresh (seconds, with a flash on some panels), limited colors, no smooth animation. Design for a card that updates every 30-60 seconds, not a live moving map.

## The product

### Core: "Overhead" card
Shows the closest aircraft in range, refreshed every 30-60 seconds:
- Airline and flight number, route (from and to), aircraft type and registration
- Altitude, speed and estimated arrival
- A small route line or map drawn in e-ink style
- Aircraft silhouette or illustration (see the rights note about photos)
- A "nothing overhead" screen with a calm message and a daily count

### Modes
1. **Overhead:** Nearest plane to your location.
2. **Follow a flight:** Enter a flight number (for example a family member's flight) and the card tracks it from departure to landing, with a proper arrival alert. This is the emotional hook: "Mom's flight is 40 minutes out."
3. **Airport board:** Departures or arrivals for a chosen airport, in a classic split-flap style on e-ink.
4. **Plane log:** A running list of the planes you have seen, with a "first seen" count (a simple badge collection for fans).
5. **Quiet hours:** Pause updates overnight to avoid flicker.

### Setup
Plug in, scan a QR code, choose Wi-Fi and enter your location. No receiver required in the base version (data comes over the internet). An optional **local receiver mode** reads aircraft directly with a small radio dongle for fans who want their own feed.

## How to get it done (MVP)
1. **Week 1:** Prototype with a Raspberry Pi Zero 2 W and a 5-7 inch e-ink panel. Pull nearby flights from a public ADS-B data source and draw the card.
2. **Week 2:** Add the follow-a-flight mode and a simple phone setup page.
3. **Week 3:** Design and 3D-print a case (the photo shows a clean printed case with a front lip and screws). Photograph it well.
4. **Week 4:** Build 5 units. Give 3 to aviation fans for feedback and put 2 up for pre-order.
5. **Weeks 5-8:** Run a pre-order test of 20 units before buying parts in bulk.

**Bill of materials (assumption, verify prices):** Computer board $15-20, e-ink panel $60-100 depending on size and color, case and screws $5-10, power supply and cable $8-10, packaging $5. About $95-145 per unit at small volume.

## Pricing and income math (honest)
| Item | Price (assumption) |
|---|---|
| DIY kit (parts, case file, software) | $129 |
| Assembled unit | $179-199 |
| Optional "follow a flight" subscription | $2.99/mo or $24/yr |
| Business or lobby unit | $249 + $9/mo |

- At $189 assembled with about $120 cost plus shipping and fees, **gross profit is about $45-55 a unit.**
- 100 units a year is about **$5,000 a year**, which is small. 400 units a year is about $20,000 a year.
- A subscription helps: 500 subscribers at $24/yr is $12,000 a year, but only if enough people value follow-a-flight.
- **So the ceiling is realistic side income of $500-2,000/mo.** Full-salary scale would need a much larger market or a higher-priced B2B angle.

## Who buys
- **Aviation fans and spotters** (the easiest first buyers, active in forums and communities).
- **People who live under flight paths or near airports.**
- **Families with a traveler:** Follow-a-flight for grandparents, partners and kids.
- **Gifts:** Pilots, flight attendants, frequent flyers, travel fans.
- **Small businesses:** Hotel lobbies, flight schools, cafes near airports, aviation museums and offices, with a branded version.
- **Kids' rooms and classrooms:** A calm science-and-geography display.

## Competition and differentiation
- **Competitors:** LED matrix boards, small round desk displays, a $400 radar-style desk unit, tablet apps, and DIY hobby builds.
- **Your edge:** Silent paper look, plug-and-play (most builds are DIY), follow-a-flight for family, and a calmer design.
- **Their edge:** Faster refresh, bigger brands, more features and lower prices at scale.

## Rights and sales flags (confirm before selling)
- **Aircraft photos are copyrighted.** The photo shows a credit to a plane-spotting site. Do not ship someone else's photos. Use silhouettes, your own illustrations, or licensed images with permission and credit.
- **Flight data terms:** Free or paid flight-data sources have terms about commercial use and request limits. Read them and price the data cost per unit or per month. Using your own receiver avoids this but adds setup effort.
- **Naming:** Do not use another company's name or logo, or imply a link to flight-tracking brands. Check trademarks before choosing a name.
- **Selling electronics:** Selling a powered device usually brings product-safety, labeling, radio and shipping rules that vary by country. Check what applies before selling beyond friends, and consider selling a DIY kit first.
- **Not for navigation:** Add a clear note that the display is for fun and is not aviation equipment.

## Name ideas
Overhead, Flyby, Contrail, Paper Plane, Gate Keeper, Skyline Card, Runway, Nearest Plane (check for existing names before using any).

## Risks
- **Thin margins and small market** for a single-purpose gadget.
- **Slow refresh** may disappoint people expecting a live map. Set expectations and design for cards.
- **Data costs and limits** can erode margin or break the product.
- **Support burden:** Wi-Fi and setup problems. Make setup a single scan and keep the manual short.
- **Parts and shipping:** Panel prices change, and shipping electronics costs money and time.
- **Copycats:** Hobbyists can build the same thing for less. Sell convenience, design and follow-a-flight.

## Validation (before bulk purchase)
1. Post a build thread with photos in 3 aviation and Raspberry Pi communities and collect replies and email sign-ups.
2. Take 20 paid pre-orders ($25 deposit, refundable) for the DIY kit or assembled unit.
3. Interview 10 people about follow-a-flight: would they pay a subscription to track a family member's flight?
4. Check 3 businesses (a hotel lobby, a flight school, a cafe near an airport) for willingness to pay $249.
5. **Gate:** 20 pre-orders or 100 sign-ups with at least 5 interested businesses. If not, keep it as a hobby project or build a software-only version.

## Software-only variant (lower risk)
Skip the hardware: a web page or tablet "ambient card" in an e-ink style that runs on a spare tablet or an e-reader. It tests demand and the follow-a-flight idea with no inventory, and you can add hardware later.

## Open decisions
- Kit versus assembled first (this file suggests a kit, to limit shipping and safety exposure).
- Photos versus silhouettes (this file suggests silhouettes).
- Whether follow-a-flight is the main product (family angle) or overhead is (fan angle).
- Whether to pursue business units or stay consumer-only.
