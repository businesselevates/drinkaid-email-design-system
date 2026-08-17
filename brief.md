# DrinkAid — Design System Brief for Claude Design
### v2.0 · rebuilt from the client's live emails

Upload or paste this whole file as the design system source. It teaches the brand **and** the medium.

> **What changed from v1.** v1 was extracted from templates sitting in the Klaviyo account that use a dark charcoal surface. Rendering the client's actual sends showed those templates match nothing the brand has ever mailed. v2 is rebuilt from 84 real emails — the palette below was colour-sampled from them, not eyeballed.

---

## 0 · READ THIS FIRST — the medium is email, not web

Everything designed from this system ships as an **HTML email** rendered by Gmail, Outlook, Apple Mail and the Klaviyo preview. Email clients are twenty years behind browsers. A beautiful modern web layout will visibly break.

**Hard constraints. Not stylistic preferences.**

| Required | Forbidden |
|---|---|
| `<table role="presentation">` for all layout | flexbox, CSS grid, `position:absolute/fixed` |
| Inline `style="…"` on every element | external stylesheets, CSS custom properties |
| `padding` on `<td>` for spacing | `margin` (Outlook silently drops it) |
| `<style>` in `<head>` for media queries only | `<style>` as the only styling source |
| Hosted absolute image URLs | local paths, base64, CSS background images |
| Web-safe font stack | `<link>` webfonts (Klaviyo strips them on import) |
| Single column, or 2-up that stacks below 620px | 3+ columns, overlapping elements, absolute layering |
| Real text as HTML | headlines baked into images |

- **Canvas: 600px** wide, `max-width:100%`. Below 620px everything goes single column.
- **No SVG** — unsupported in Outlook and Gmail. PNG or JPEG only.
- **No video, no JS, no forms, no hover-dependent meaning.**
- **Text on top of an image must be baked into the image.** CSS overlays do not survive email clients. The brand's bubble labels ("HATE HANGOVERS?") are part of the photograph, not HTML.
- **Assume images are off.** Roughly half of opens block images. Every image needs real alt text and the email must still make sense without any of them.
- Wrap the 600px table in the Outlook ghost-table conditional:
  `<!--[if mso]><table role="presentation" width="600" align="center"><tr><td><![endif]-->`

> If a layout idea cannot survive those constraints, it is the wrong idea for this channel. Design within them from the start rather than designing freely and repairing after.

---

## 1 · Brand core

**DrinkAid** — Modular Wellness Pte Ltd, Singapore. `drinkaid.co`

> "A modern recovery brand designed for life in motion. From late nights to early starts, we support the moments in between — so you can recover better, feel better, and show up anyway."

**Brand platform: Show Up Anyway.** Life doesn't give ideal conditions, but the meeting still happens and the people still show up for you. Not by pushing harder — by giving your body what it needs to keep going.

| Product | Category | The moment it answers |
|---|---|---|
| **DrinkAid** | Anti-hangover | *Last night happened. Today still matters.* Singapore's OG hangover supplement, clinically proven proprietary formula. Asian flush, fatigue, lost productivity. |
| **Snuu** | Sleep balm | *Your mind can't switch off.* The only topical sleep product with actives beyond aromatherapy. Zero melatonin, zero dependency. |
| **Easy Mode** | Focus supplement | *Your baseline is off.* Zero-caffeine sustained focus, 6–8 hours. No spikes, no crashes. |
| **Gummies** | Anti-hangover, gummy | Flavour "Citrus Zest". A real, launching SKU. Buyers are **almost entirely new customers with no pills crossover**, so gummies copy leans into lifestyle, taste and fun rather than the science. For the first round of flows, treat **1 pouch of gummies ≈ 1 box of pills**. |

**Audience.** Primary: The High Achiever, 25–40 — urban professionals, founders, creators, consultants, finance. Ambitious, packed schedule, travels often, can't afford to lose a day. Secondary: The Survivor, 18–40 — students, parents, long-hours workers who want tangible change, not a supplement regimen.

**Proof points** (use sparingly, never stack all three): 2,000,000+ mornings saved from hangovers · 40,000+ customers · Product of Singapore.

---

## 2 · Voice & tone

**Personality: a well-intentioned, knowledgeable friend.** Honest · Direct · Practical · Confident · Sometimes funny.

- **Honest + direct** — no overpromising, no preaching.
- **Warm + supportive** — a friend who gets it, not a brand talking at you.
- **Real + relatable** — imperfect moments, authentic situations.
- **Empathetic, not pressuring** — "we've got you", never "push harder".
- **Sometimes funny** — light humour when it fits, never forced.

**The signature copy move.** Headlines break across two lines and the second turns *italic*:

> **Something's missing.** Oh right, *your order.*
> **Your "I do"** shouldn't turn into *"I don't feel so good!"*

Use it often. It is the most recognisable thing the brand does in words.

**Lean in** — real people in recognisable situations · moments of quiet relief, not triumph · the early morning after a late night · the work trip where skipping drinks isn't an option · Friday plans when you're already exhausted · the parent who has to be "on" every morning · the 6am flight after a big night.

**Avoid — these read as a different brand:** preachy wellness · before/after transformation tropes · luxury or aspirational perfection imagery · guilt-tripping about alcohol or sleep · "keep grinding" bro-culture · countdown timers and fake scarcity.

**Mechanics.** Open with the situation they recognise, not the product. Short paragraphs, one idea each. CTA is a verb in first person — `LEARN THE SCIENCE HERE`, `FINISH MY ORDER` — not "Shop now". Sign off **The DrinkAid Team** for broadcasts, **Isaac** (CEO) for founder notes.

**If the user supplies copy, use it verbatim.** Only write copy when explicitly asked.

### 2.1 · Do not sound like AI

The client rejected an entire round of EDM copy for reading as machine-written, and rewrote it himself. This is the single most sensitive thing about the account. Copy that trips these wires gets thrown out regardless of how good the design is.

**Banned constructions**
- Opening on abstraction: "In today's fast-paced world…", "Life moves fast, and…", "We all know that feeling…"
- Rule-of-three padding: "smarter nights, smoother mornings, and better days"
- Verbs from the AI dictionary: elevate · unlock · transform · empower · seamless · effortless · journey · embrace · dive in · game-changer · revolutionise · curated
- Em-dash-heavy rhythm where every sentence hinges on a dash
- "Whether you're X, Y, or Z…" openers
- Restating the headline in the first line of body copy
- Symmetrical paragraphs that all run the same length
- A closing line that summarises what was just said

**What good looks like here** — actual brand copy:

> "Most brands would use the last email in a series to talk you into the biggest bundle on the shelf. This is not that email."

> "Heads up: these aren't Haribo. DHM has a naturally bitter edge and if you can't taste it, you're probably not getting enough of it to do its job."

> "If everything's fine and you just got distracted (relatable), you can jump right back into checkout here."

Note what those do: uneven sentence lengths, a parenthetical aside, an admission against interest, no summary close. Write like someone typing to a friend who is slightly short on time.

---

## 3 · Colour

Sampled from live sends. Percentages are share of rendered pixels.

| Token | Hex | Share | Use |
|---|---|---|---|
| **White** | `#FFFFFF` | 22–45% | Default email surface. Most campaigns are white. |
| **Cream** | `#F1F0E7` | 9–13% | Alternate surface — letter/founder notes, calm section bands. |
| **Forest** | `#08230F` | 10–12% | The structural colour. Logo pill, header bar, primary buttons, **all headline and body text**, footer icons. |
| **Mint** | `#CCFFD9` | 5–10% | Soft panels, quote and explainer cards, the footer trust bar. |
| **Lime** | `#9AFF1A` | 0.5–1.2% | Accent. Announcement bars, button text on forest, bullet glyphs, stars, the logo dot, the offset shadow under outline buttons. |
| Forest soft | `#123424` | — | Lighter forest for large fills and gradients. |
| Warm cream | `#FAF0D8` | — | Occasional warm card fill in seasonal sends. |
| Hairline | `#DCDCD2` | — | Dividers and card borders. |

**Three things to get right:**

1. **This is a light brand.** White or cream body, forest ink. Do not build on a dark surface.
2. **Body text is forest `#08230F`, not grey.** The brand has no grey body copy anywhere.
3. **Lime is roughly 1% of the pixels.** It is a spark, not a field. The only place it fills a large area is the top announcement bar.

---

## 4 · Typography

Stack: `'Poppins','Segoe UI',Helvetica,Arial,sans-serif`

⚠️ The brand brief supplied is a **strategy** document and names no typeface. Live emails use a geometric sans with a true italic; Poppins is the closest widely-available match. Confirm the official face with the client. For email it barely matters — Klaviyo strips webfonts and most clients fall back to Segoe UI / Arial, so **design for the fallback.**

| Role | Size / line | Weight | Notes |
|---|---|---|---|
| Announcement bar | 15 / 20 | 700 | Forest on lime, full bleed, centred |
| Eyebrow | 13 / 18 | 700 | 2px tracking, UPPERCASE, forest |
| Display | 46 / 52 | 800 | Seasonal & event heroes |
| H1 | 38 / 44 | 800 | Forest |
| H1 italic | 38 / 44 | 800 *italic* | The signature second line |
| H2 | 28 / 36 | 800 | Section heads |
| H3 | 22 / 30 | 700 | Card titles |
| Body LG | 19 / 30 | 400 | **Default.** Letter copy, forest |
| Body | 17 / 27 | 400 | Dense sections, cards |
| Caption | 13 / 19 | 400 | Muted |
| Legal | 11 / 16 | 400 | Address, unsubscribe |
| Button | 17 / 22 | 800 | 0.5px tracking, UPPERCASE |
| Trust stat | 22 / 26 | 800 | "2,000,000+" |
| Trust label | 11 / 14 | 700 | "MORNINGS SAVED FROM HANGOVERS" |

Mobile (≤620px): Display 34/40 · H1 29/36 · H2 24/31 · Body LG 17/27.

---

## 5 · Layout & rhythm

- **600px** canvas. **40px** outer gutter, **48px** for left-aligned body copy, **24px** both on mobile.
- Radii: **16px** images · **20px** cards · **fully rounded** buttons and the logo pill.
- **Vertical rhythm is `padding-top` only. No block sets `padding-bottom`.** This is what makes blocks deletable without orphaned gaps.
- Steps: `12` eyebrow→H1 · `20` H1→body · `30` block→block · `44` section→section · `56` before footer.
- Tap targets never below 44px.

**Signature marks — on every email, seasonal included:**
1. The **forest logo pill** at the top (or the full-width forest header bar on letter emails).
2. The **mint trust bar** and legal footer at the bottom.
3. Fully-rounded buttons.
4. Forest as the ink colour.

---

## 6 · Component vocabulary

The block library, grouped by where it sits. Blocks marked ★ appear in nearly every reference email (Moom, Grüns, Seed, Lemme, IM8) — they are table stakes, not optional flourishes.

### Top zone
| Block | Notes |
|---|---|
| ★ **Announcement bar** | Lime, full bleed, forest text, centred. Offer or code. Sits *above* the logo. Max one. |
| ★ **Logo pill / header bar** | Forest pill on white, or full-width forest band. Locked. |
| **Nav row** | 3–4 text links under the logo — `Shop · The Science · Bundles · Reviews`. Moom and Lemme both run this. Optional but it lifts perceived polish. |

### Hero zone
| Block | Notes |
|---|---|
| ★ **Full-bleed hero with overlaid headline** | The most common opener in the references. **The headline must be baked into the image** — CSS text-over-image does not survive email. Supply an image-off fallback via alt text. |
| **Inset hero** | 520px, 16px radius, headline as live HTML below it. Safer when copy changes often. |
| ★ **Eyebrow + headline + body** | Eyebrow, then the headline with its italic second line, then 2–4 lines centred. |

### Body zone
| Block | Notes |
|---|---|
| ★ **Icon trust row** | 4–6 small icons with one-word labels in a row — Moom runs `VEGAN · HALAL · NATURAL · NON-GMO · SUGAR-FREE`, Lemme runs a 4-icon credential row. For DrinkAid: `CLINICALLY TESTED · MADE IN SG · NO DROWSINESS · VEGAN`. Highest-value block we are currently missing. |
| **Stat grid** | 2×2 or 4-across percentages with captions (IM8: `95% / 85% / 80% / 75%`). Strong for the science story. |
| **Credibility row** | Circular headshots + name + credential. Moom uses five experts. Only with real people and real titles. |
| ★ **Mint panel** | Explainer, quote, or "the honest bit". |
| ★ **Bullet list** | Lime sparkle glyph + forest text. |
| **Category card stack** | Repeating unit: image + heading + 2 lines + pill CTA. Lemme stacks four. This is how you present DrinkAid / Snuu / Easy Mode / Gummies without a wall of text. |
| **Product line-item list** | Thumbnail + name link + price, stacked. Moom uses it for recommendations, both brands use it for cart contents. |
| **Cross-sell 3-up** | Thumbnail + name + price + small `Buy Now` each. Moom's "You might also like…". |
| ★ **Review card** | Stars, quote, attribution. Real customers only. |
| **Offer / code panel** | Tinted box, code in large lime type. Or inline — Lemme highlights `10% OFF!` mid-sentence with a lime background span. |
| **Full-bleed image band with inline CTA** | Photo, headline baked in, pill button below. Good mid-email reset. |

### Bottom zone
| Block | Notes |
|---|---|
| **Stacked outline nav buttons** | 2–3 full-width outline pills — `SHOP PRODUCTS` / `THE SCIENCE` / `OUR STORY`. Lemme's; a clean way to end. |
| **Logo marquee strip** | Repeated wordmark with a divider glyph across a thin band. Lemme's. Pure texture, cheap to build, reads expensive. |
| **Support line** | "Got questions? Check our FAQs or reply to this email." Moom runs it on every send. Cheap trust. |
| ★ **Mint trust bar** | Stars + `2,000,000+` + `PRODUCT OF SINGAPORE` + address. Locked. |
| ★ **Social row · Legal · Unsubscribe** | Locked. |

**Button detail worth getting right:** the outline button sits on white with a 2px forest border and a **4px lime bar offset directly below it, no blur.** It reads as a printed sticker. Build it as a two-row table, not a CSS `box-shadow` — Outlook drops shadows.

**Per-email limits:** one primary CTA · one announcement bar, and only above the logo · max 2 columns · never two blocks of the same shape back to back.

### 6.1 · Blocks that need Klaviyo dynamic content

These cannot be finished as static HTML. Design them with placeholder products; they get wired up at import.

| Block | What it becomes |
|---|---|
| Cart line-item list | `{% for item in event.extra.line_items %}` over the abandoned-cart event |
| Cross-sell 3-up | A Klaviyo product-feed or catalogue block |
| Personalised recommendations | Catalogue feed, not hand-written HTML |
| First name, cart total, product names | Merge tags |

Design the *shape* of one row properly — thumbnail size, spacing, where the price sits, what the button looks like. The loop repeats whatever that one row is.

---

## 7 · Seasonal & event — what may change

The brand **deliberately leaves its palette** for seasonal moments. This is intended behaviour, not a violation. Real examples:

| Moment | Treatment |
|---|---|
| Valentine's | Deep red `#6B0F16` ground, cream card, red serif italic headline. No lime at all. |
| New Year | Green foil photography, white script serif headline, mint accents. |
| Wedding / events | Mid-green `#8FDD8A` ground, white sans + white serif italic. |

**Free to change:** surface colour, accent colour, headline typeface (script or serif is fine), hero treatment, section order, photographic mood.

**Still locked:** the forest logo pill at the top · the mint trust bar and legal footer at the bottom · fully-rounded buttons · 600px canvas · the unsubscribe line.

So: a seasonal email can look like almost anything in the middle, as long as it opens and closes like DrinkAid.

---

## 8 · Imagery

**How this brand shoots.** Composed product sets — boxes on white plinths with soft shadows, product arranged in a green basket, sachets beside a wine glass on a wooden table. Real hands, real rooms, natural light. Playful staging (hands punching through paper, confetti, foil curtains) for seasonal. Bubble labels in lime sit **on** the photograph.

**Never generate:**
- Product shots. A DrinkAid sachet, box, gummy, Snuu tube or Easy Mode bottle must be a real photograph. A generated one is a fabricated product image.
- Anything showing a logo, label, supplement facts panel or packaging copy.
- Faces or scenes presented as real customers or real reviews.
- Anything containing readable text — generators mangle it and it can't be edited later.

**Fine to generate:** abstract backgrounds, gradients, textures, seasonal motifs; clearly-illustrative hero art; placeholder comps for client review — **labelled as placeholders**, swapped for real assets before send.

**When generating,** respect the stated avoids: no luxury gloss, no before/after, no stock-photo perfection. Real, imperfect, warm. Light surfaces, forest ink, lime spark.

---

## 9 · Assets

All URLs below are live on the Klaviyo CDN.
Base: `https://d3k81ch9hvuctc.cloudfront.net/company/VagrHA/images/`

| Asset | File |
|---|---|
| Logo, white (on forest) | `8dbd6bfe-5f24-4f5d-910f-efb8c527f5b6.png` |
| Logo, cream | `c07fe091-544e-4f37-b200-ee86288e9307.png` |
| Logotype, dark green (on white/cream) | `6ec08cb8-a66e-4b02-b3ca-e754203db0e0.png` |
| Primary logo mark | `9407bbec-39c6-490c-89af-1f1e23593d2f.png` |
| Five stars, lime | `8b43610a-398f-4c58-8d64-b1a33b9e42da.png` |
| Icon · Instagram | `66928843-1f6f-4634-9d55-c1de33b1f691.png` |
| Icon · TikTok | `eb6b8462-2978-41cb-a8f4-c1abb7313e91.png` |
| Icon · Website | `b6e824c8-1920-4f2b-9842-36ceccda44e5.png` |
| Icon · Plus divider | `bd2d69c6-a2ef-46de-a481-053989348db8.png` |
| Product family (all three) | `65882579-a21a-4528-bf15-d8db23f999b9.jpeg` |
| Boxes on plinths | `5b1f423e-56b7-4e03-b741-3a1802a8049f.jpeg` |
| Multibox | `98e6c6c1-5074-4622-a4f0-985dcb667c27.png` |
| Sachet box in hand | `93ae336c-c8c8-4585-96eb-f9fd2916365c.png` |
| Capsules in palm | `280f2890-4735-4321-a84b-50466a9a458c.png` |
| Gummies pack | `73f77285-91a9-49d3-82ee-27a152f05360.jpeg` |
| Dosage guide | `2c9e07ea-7eb1-4807-8963-f7b633bab6e6.png` |
| Supplement facts | `3883c145-279b-41c6-aa1a-ef6062414746.png` |
| Snuu — sleep | `aea45699-2473-42c7-9c79-758c48c2d87f.jpeg` |
| Snuu — ingredients | `276221c2-274e-4971-8f6e-7986080403d2.png` |
| Easy Mode — in palm | `6325be8b-636a-48ab-ba5f-5551e464b6c9.jpeg` |
| Friends with sachets | `c9a77d6a-9c3d-4298-99a8-6950af1adf7c.jpeg` |
| Friends group | `48ce008f-d1f3-4b9e-bc94-6424003e44e1.jpeg` |
| Whisky + sachets | `cc825c91-2fa8-40a2-87e8-81e5fb1eb38a.jpeg` |
| Club grin | `bc7fb17c-1b97-4d82-804d-a4d144e25f42.jpeg` |
| Hen party | `dec0f92e-9c67-43d4-bab5-5248dc265bd2.jpeg` |
| Groomsmen | `b06fc835-8fc2-453d-a7f1-ca80b7b7c75b.jpeg` |
| Destination wedding | `c93b9b69-c0f5-4780-af88-1c8af74cd647.jpeg` |
| Couples | `db338bce-a380-4831-b567-28f44413d4a8.jpeg` |
| Family | `599b71d7-bc76-49aa-b1d5-ccdc0aae62d9.png` |
| Open bar breakfast | `bd406459-571e-44c2-bbc4-f383f6c0ac9d.jpeg` |
| Toast / recovery | `25da6c86-cdf5-4d96-b354-d7cdc0b4b91f.jpeg` |
| Slow week — bed | `6ae82447-4cc7-4984-a384-043dcb587acb.jpeg` |
| NYE | `63a7463e-559f-4d41-860a-b2723c5f0e65.jpeg` |
| New Year hero | `5bb9af29-0181-4867-8a25-f5ee305631ea.jpeg` |

⚠️ **The local `Asset/` folder** holds 6 candid customer photos of the Gummies SKU. They are **not on the Klaviyo CDN** and **all 6 are rotated 90°**. They must be rotated and uploaded before they can be used in an email. Treat them as reference for now.

---

## 10 · Structure — and reference discipline

### Not a wall of text, and not a blog post

The client named both failure modes directly. An email must not be a slab of paragraphs, **and** it must not be the lazy fix of *bold header → paragraph → bold header → paragraph* repeated down the page. That pattern reads as a blog post pasted into an inbox.

Build with **alternating block types** instead. A good email changes texture every screen: full-bleed image → short copy → mint panel → bullet list → product card → review → CTA. The reader should never scroll past two blocks of the same shape in a row.

Practical targets:
- No more than ~90 words of unbroken body copy before something visual interrupts.
- At least three distinct block types in any email longer than one screen.
- One idea per block. If a block needs a sub-heading to stay coherent, it should have been two blocks.

**Length is not the problem.** Every reference email runs long — Moom's welcome is 5,100px, Lemme's is 6,800px, Grüns' newsletters are 4,300–5,800px. They stay readable because the texture changes every screen, not because they are short. Do not compress a DrinkAid email to feel "clean". Vary it instead.

### Reference brands

The client points to **Moom Health**, **Seed**, and **Grüns** (`gruns.co` — noted as "Grants" in the meeting). The reference folder also contains **Lemme** and **IM8**. Material lives in `EDM reference/`, sorted into `Welcome`, `Cart abandoned`, `Newsletter`, `Promotion`, `Product News, education`, `Bottom of Funnel`, `IRL + Community`.

**Grüns is the closest match in energy** — a gummy supplement brand, bold and punchy rather than serene. Weight it most heavily, especially for the Gummies SKU. Moom and Seed are the reference for *craft and structure*; Grüns is the reference for *tone of design*.

Take from them: block architecture, section rhythm, the image-to-copy ratio, how they build review / ingredient / comparison modules, and the overall level of finish.

**Do not take their palette or their mood.** Moom in particular is a soft cream-and-pastel wellness aesthetic — and DrinkAid's own brand brief lists *"preachy wellness messaging"* and *"luxury or aspirational perfection imagery"* under things to avoid. Copying Moom's look would walk DrinkAid straight into what its own strategy warns against.

DrinkAid keeps white / forest / lime, the friend's voice, and the italic second line. The brief the client gave is *"different yet similar"* — same standard of craft, different personality.

> If a design starts drifting cream, pastel, or spa-like, it has copied the wrong layer of the reference.

---

## 11 · Output contract

Return a **single self-contained HTML file** that:

1. Uses table layout with fully inline CSS, per section 0.
2. Is 600px wide with the Outlook ghost-table wrapper.
3. Opens with a hidden preheader div, 50–90 characters, not a repeat of the subject line.
4. Carries the four signature marks from section 5.
5. Ends with the mint trust bar, legal footer, and this exact tag: `{% unsubscribe 'Unsubscribe' %}`
6. Uses `{{ first_name|default:'there' }}` for personalisation — always with the default.
7. Gives every image real alt text.
8. Uses only the asset URLs in section 9, or clearly-flagged generated placeholders.
9. Includes a `<style>` block in `<head>` with the ≤620px media query only.

Also return a **plaintext version** — written, not auto-stripped.

---

## 12 · Where this brief is a proposal, not a fact

Flagged honestly so nothing gets presented to the client as established when it isn't:

- **Type scale and spacing are standardised here.** Live sends vary a lot; this file picks one scale. Client should sign off.
- **The typeface is inferred**, not specified — see section 4.
- **`#5A6B5E` muted text is derived**, not sampled. Everything else in section 3 came from real pixels.
- **Poppins vs the real face** — worth one question to the client before anything goes to print or web.
- **Reference discipline (section 10) is my recommendation**, not a client instruction. The client said "different yet similar"; the take-structure-not-palette split is how I read that. Worth confirming.

*Resolved since v2.0: the Gummies SKU is real and launching — confirmed in the 14 Aug campaign review.*
