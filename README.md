# DrinkAid Email Design System

The design system for every email DrinkAid sends. Built for **Klaviyo**, not for the web.

> **Read `brief.md` first.** It carries the brand, the voice, and — critically — the constraints of the medium. This README only explains how the repo is laid out.

---

## What this is

Email clients are twenty years behind browsers. Gmail and Outlook have no flexbox, no CSS grid, no external stylesheets, no SVG, no webfonts. A layout built the way a modern web page is built will visibly break in the inbox.

So this repo does not describe the design system in prose and hope for the best. **It ships the actual markup.** Every component in `components/` is real, Outlook-safe HTML that can be pasted into a Klaviyo template and sent. Compose from these rather than writing new HTML.

---

## Layout

```
brief.md               The design system: brand, voice, colour, type, rules.
tokens.json            The same system, machine-readable.
components/            One file per block. Real email-safe HTML.
  _shell.html          Outer wrapper — doctype, head, media queries, 600px table.
  01…23-*.html         The blocks, in roughly the order they appear in an email.
templates/             Worked examples composing the blocks.
```

## How to build an email

1. Start from `components/_shell.html`.
2. Paste blocks between the `BLOCKS GO HERE` markers, in order.
3. Swap the copy, images and links.
4. Keep the numbering roughly ascending — the library is ordered top-of-email to bottom.

Every block is a `<tr>` (or a pair) inside one 600px table. That is why they can be reordered and deleted freely.

---

## Rules that are not negotiable

**Vertical rhythm is `padding-top` only.** No block sets `padding-bottom`. This is what lets any block be deleted without leaving an orphaned gap. If you add a block, follow the convention.

**Locked blocks** — present on every email including seasonal:
- `02-header-logo-pill` (or `03-header-bar` on letter-style emails)
- `23-footer`, including the `{% unsubscribe %}` tag, which is a legal requirement

**Never**
- `margin` — Outlook drops it. Use `padding` on `<td>`.
- `box-shadow` — Outlook drops it. See `11-cta-outline` for how the lime offset is built instead.
- SVG — unsupported. PNG or JPEG only.
- Text positioned over an image with CSS. If a headline sits on a photo, it must be **baked into the photo**, with the headline repeated in the `alt` attribute.
- More than two columns. Anything 2-up must carry `class="da-stack"` so it collapses below 620px.

**Assume images are off.** Around half of opens block them. Every `<img>` needs real alt text, and the email must still make sense with none of them loaded.

---

## Colour

| Token | Hex | Use |
|---|---|---|
| White | `#FFFFFF` | Default surface |
| Cream | `#F1F0E7` | Alternate surface, cards |
| Forest | `#08230F` | Structure **and all body text** |
| Mint | `#CCFFD9` | Panels, trust bar |
| Lime | `#9AFF1A` | Accent — roughly 1% of the pixels |
| Muted | `#5A6B5E` | Captions, legal only |

Three things people get wrong: this is a **light** brand, body text is **forest and never grey**, and lime is a **spark, not a field**. The only place lime fills a large area is the top announcement bar.

Seasonal emails may leave this palette entirely — see `brief.md` §7.

---

## Type

`'Poppins','Segoe UI',Helvetica,Arial,sans-serif`

Klaviyo strips webfont `<link>` tags, so Poppins renders only where it is already installed. **Design for the Segoe UI / Arial fallback.** Never rely on Poppins' metrics.

The signature move is a headline whose second line turns *italic* — see `07-eyebrow-headline`.

---

## Dynamic blocks

`19-cart-line-items` contains a Klaviyo Django-template loop and **will not render in a browser preview**. That is expected. Klaviyo fills it from the Checkout Started event at send time.

For a static design comp, delete the `{% for %}` / `{% endfor %}` lines and hard-code two example rows. Design the shape of *one* row properly — the loop repeats whatever that row is.

`20-cross-sell-3up` ships static. It can be swapped for a Klaviyo catalogue feed at import.

---

## Assets

Images are served from the Klaviyo CDN and are already live:

```
https://d3k81ch9hvuctc.cloudfront.net/company/VagrHA/images/
```

The full catalogue is listed in `brief.md` §9.

⚠️ **`12-icon-trust-row` references four icons that do not exist yet** — `icon-clinical`, `icon-sg`, `icon-nodrowsy`, `icon-vegan`. The URLs are placeholders. The block is otherwise complete; the icons need designing and uploading before it can ship.

---

## Status

Version 2.0. Rebuilt from 84 of DrinkAid's own sent emails, colour-sampled rather than eyeballed, plus 43 reference emails from Moom Health, Seed, Grüns, Lemme and IM8.

`brief.md` §12 lists everything in here that is a **proposal awaiting client sign-off** rather than established fact — chiefly the standardised type scale and the inferred typeface. Read it before presenting any of this as settled.
