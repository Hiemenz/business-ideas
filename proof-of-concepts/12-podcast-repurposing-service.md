# PoC 12 — "One Recording, Ten Posts" — Podcast/Video Repurposing Service for B2B Thought Leaders

**Date:** 2026-07-09
**Fit:** software/technical + sales/marketing/ops · needs cash in weeks · near-$0 budget

## The Opportunity

B2B founders, consultants, and executives who host or appear on podcasts (their own show, guest appearances, or recorded webinars/talks) sit on a pile of long-form content that almost never gets repurposed into the shorter-form posts that actually drive reach — LinkedIn posts, Twitter/X threads, short video clips, newsletter blurbs. They know repurposing is valuable ("content flywheel" is a well-worn phrase in this exact buyer segment) but doing it themselves takes hours they don't have, and most existing repurposing tools produce generic, low-quality output that still needs heavy editing. This service sits directly adjacent to PoC 06 (LinkedIn ghostwriting) but solves a different bottleneck: instead of generating content from nothing, you're extracting and reformatting content that already exists, which is faster to produce and easier to prove ROI on since the source material is already validated (it got recorded/published once already).

## Who It's For

B2B podcast hosts, frequent podcast guests, and executives who record webinars/talks but don't systematically repurpose them — same buyer profile as PoC 06 (consultants, coaches, fractional execs, agency founders) but specifically those already producing long-form audio/video content, which is an easy-to-verify signal (just check if they have a podcast or recent recorded talk).

## How It Makes Money

- Flat per-episode fee: $150–$400 per episode, delivering a bundle of 5-8 LinkedIn posts, 1 Twitter/X thread, 3-5 short video clip scripts with suggested cut points, and a newsletter blurb — priced by episode so the client can start with a single trial episode.
- Monthly retainer for active podcasters: $500–$1,200/mo covering weekly episode repurposing on an ongoing show schedule.
- Video clipping upsell: +$100–$200/episode if you also handle the actual video editing/clipping (using free/low-cost tools) rather than just providing cut-point scripts and captions for the client's own editor.
- Natural cross-sell into PoC 06's LinkedIn ghostwriting retainer — repurposed posts fill part of the content calendar, original ghostwritten posts fill the rest, same buyer, same content operation.

## MVP — Buildable in Days, ~$0 Cost

1. **Week 1, no code required:**
   - Client sends a recent episode (audio/video file or a link to where it's published).
   - Transcribe using a free tool (YouTube's auto-captions if video is posted there, or a free tier of a transcription tool) — no paid transcription service needed at low volume.
   - Feed the transcript into an LLM with a prompt template per output type (LinkedIn post extraction, thread-worthy insight extraction, clip-worthy moment identification) to draft the repurposed content bundle, then edit for voice and accuracy.
   - Deliver via Google Doc, organized by content type and ready to copy/paste and post.
2. **Software layer (build once 2–3 clients are live, funded by early per-episode fees):**
   - Reusable prompt library per content type (same pattern as PoC 06's voice-profile config) so each new episode runs through a consistent, refined extraction process rather than being rebuilt from scratch.
   - Simple script to automate the transcription step (free/low-cost speech-to-text API) so you're not manually running each file through a web tool — cuts turnaround time as volume grows.
   - Per-client voice/style config (reused directly from a PoC 06 engagement if the client is on both services) ensuring repurposed posts match the client's established tone.

## Tools/Stack

- Free transcription options: YouTube auto-captions (if video is public), or free tiers of transcription tools — no paid tooling required to start.
- Claude/Gemini API for content extraction and drafting across formats.
- Free/low-cost video clipping tools (e.g., a simple ffmpeg script for cutting clips at specified timestamps, consistent with a scriptable/technical approach) if offering the video-clipping upsell.
- Google Docs for delivery.
- Stripe/invoice for per-episode or retainer billing.

## Go-to-Market — First 5 Customers, Zero Ad Spend

1. Identify B2B podcast hosts and frequent guests via podcast directories (Apple Podcasts/Spotify search by category) and LinkedIn (people who regularly post "new episode out" links) — a highly identifiable, easily-listed prospect pool.
2. Free-sample hook: pick one of their recent episodes, repurpose it into 2-3 sample LinkedIn posts, and send as a DM: "Loved your episode on [topic] — pulled 3 LinkedIn posts out of it, free to use if you want them." This is the strongest version of the free-sample tactic used throughout this folder, since the source material (their own words) makes the output feel obviously valuable and low-risk to use.
3. Podcast guest-swap and podcast-host communities (there are active online communities specifically for B2B podcasters) are a dense, on-topic venue where this exact pain point is constantly discussed.
4. Cross-sell directly into any existing PoC 06 (LinkedIn ghostwriting) client relationships — if they also host or appear on podcasts, this is a same-call upsell, not a new outreach cycle.
5. Once a client sees engagement on a repurposed post, ask them to mention on their own podcast or LinkedIn that they're now repurposing content — podcasters talk shop with other podcasters, making this a strong word-of-mouth loop within a tight community.

## Time to First Dollar

- Day 1–2: identify 15–20 active B2B podcast hosts/guests, select one recent episode per prospect for the free-sample treatment.
- Day 2–4: produce and send free-sample repurposed posts to the first 10.
- Day 4–9: close 3–5 clients on the per-episode fee ($150–$400), collected upfront for the trial episode.
- **First dollar within 1–2 weeks** — no build dependency, source material already exists so turnaround on the free sample itself can be same-day.

## Why This, Why Now

- Zero build required to start, and turnaround is faster than most content services in this folder since the underlying material already exists — you're extracting and reformatting, not generating from a blank page.
- Free-sample conversion is unusually strong here because the sample is built from the prospect's own already-validated content, making the value obvious without requiring them to imagine a hypothetical.
- Natural bundling with PoC 06 creates a combined content-operation offer for the same buyer, increasing deal size without a second outreach motion.
- Podcasting as a B2B marketing channel continues to grow, and the repurposing bottleneck is a widely and openly discussed pain point within podcaster communities, making prospecting and messaging unusually straightforward.

## Risks / Open Questions

- **Overlap/cannibalization with PoC 06:** if pursuing both simultaneously, be clear internally about which service is being pitched first to avoid confusing positioning — recommend leading with whichever pain point is more visible for a given prospect (active podcast → lead with repurposing; inconsistent posting with no podcast → lead with ghostwriting).
- **Transcription quality varies:** free auto-captions can be inaccurate for accented speech, cross-talk, or poor audio — budget manual correction time before running the transcript through the LLM extraction step, or clients may see the free-sample quality dip.
- **Video clipping upsell requires more technical setup** (basic video editing capability) than the text-only repurposing tier — validate demand for the text-only bundle first before investing time in the video-editing workflow.
- **Deal size is moderate**, similar to PoC 06 — volume of clients matters more than any single high-ticket close, so outreach efficiency is a bigger lever here than in the audit/research-based PoCs.

## Validation Signal to Watch

If 3+ of your first 10 free-sample DMs get a reply expressing genuine interest in using the posts, the hook is working — scale outreach into podcaster communities next. If interest is tepid even with a strong free sample, test whether the issue is targeting (are these prospects actually posting content regularly at all?) before concluding the offer itself needs rework — this service depends on the prospect already having an active publishing habit, unlike PoC 06 where inconsistency itself is the opener.
