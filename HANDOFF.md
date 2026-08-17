# Handoff — context that isn't in the code

`README.md` explains *how* the repo works. This file explains *why it looks the way it does*, and what is still unresolved. Read it before changing anything structural or presenting any of this to the client.

Last updated: 17 August 2026.

---

## Where this sits

DrinkAid (Modular Wellness Pte Ltd, Singapore) engaged the agency for paid media and email. In the 14 August campaign review, the client rejected the "email by email" approach and asked for **building blocks** instead — a reusable system, reviewed once, then applied.

Kennedy committed to: revised copy Mon/Tue, **templates and design by Wednesday 19 August**.

The client also named reference brands to match for craft: **Moom Health**, **Seed**, **Grüns**. (The meeting transcript renders Grüns as "Grants" — it is `gruns.co`, a gummy greens brand.)

---

## The one thing most likely to trip up whoever picks this up

**Version 1 of this system was built on the wrong source and thrown away.**

There is a set of templates in the Klaviyo account named `[Pills][Track A/B/C] … — DESIGNED`, created 13 August. v1 was extracted from those: dark charcoal `#0D0D0D` surface, lime accent, Poppins, an editorial look.

Rendering the client's actual sent emails showed those templates **match nothing the brand has ever mailed**. DrinkAid's real emails are light — white and cream surfaces with forest-green ink. The dark templates were the agency's own work-in-progress, not client-approved; the 14 August transcript confirms they were still pending review.

v2 was rebuilt from the real sends. If you find yourself looking at a dark DrinkAid email template, it is stale.

> ⚠️ Template `Y4USkr` in Klaviyo — `★ MASTER · DrinkAid EDM System v1.0` — is still live and still dark. Anyone who clones it will send an off-brand email. It should be renamed `[DEPRECATED]` or deleted. **Not yet done.**

---

## How the palette was derived

Not eyeballed. The client supplied two PDFs — `Welcome Flow EDM.pdf` (14 emails) and `DrinkAid EDM.pdf` (70 emails). Both were rendered to bitmaps and colour-sampled across a spread of standard-length emails. The percentages in `README.md` and `brief.md` §3 are share of rendered pixels.

That method settled three things that prose kept getting wrong:

1. **It is a light brand.** White 22–45%, cream 9–13%. Not dark.
2. **Body text is forest `#08230F`, not grey.** There is no grey body copy anywhere in the brand.
3. **Lime is 0.5–1.2% of pixels.** A spark, not a field. The only large lime area is the top announcement bar.

One reconciliation worth knowing: v1's lime `#9BFF1A` and footer `#08230F` were *correct* — those came from the real brand. v1's error was inverting the surface. Hence "hybrid": keep forest, lime and mint, put them back on light ground.

---

## Decisions taken, and who took them

| Decision | Status |
|---|---|
| Rebuild on the client's real sends, tightening where they're inconsistent | Agreed with Kennedy |
| Standardise the type scale and spacing (live sends vary a lot) | **Agency proposal — needs client sign-off** |
| Poppins as the typeface | **Inferred, not specified.** The supplied brand brief is a *strategy* document with no visual identity section. Confirm with client. |
| Seasonal emails may leave the palette entirely | Observed behaviour — Valentine's is deep red, NYE is green foil with white script serif. Encoded as permitted. |
| Take structure and craft from reference brands, not their palette | **Agency proposal.** See below. |
| Gummies: round 1 reuses the pills flows, 1 pouch ≈ 1 box | Agreed in the 14 Aug review (Isaac + Rachel) |

### On the reference brands

Moom is a soft cream-and-pastel wellness aesthetic. DrinkAid's own brand brief lists *"preachy wellness messaging"* and *"luxury or aspirational perfection imagery"* under things to **avoid**. Copying Moom's look would walk DrinkAid into exactly what its own strategy warns against.

So the rule in `brief.md` §10 is: take block architecture, section rhythm, image-to-copy ratio and level of finish. Do not take palette or mood. Grüns is the closest match in *energy* — bold and punchy rather than serene — and should be weighted most heavily, especially for the Gummies SKU.

Isaac's phrasing was *"different yet similar"*. The take-structure-not-palette split is the agency's reading of that. It has not been put to the client explicitly.

---

## The copy landmine

Isaac rejected an entire round of EDM copy for sounding AI-generated and rewrote it himself with Rachel. This is the most sensitive thing about the account.

`brief.md` §2.1 encodes the specific constructions to avoid. Copy that trips those wires gets thrown out regardless of how good the design is. If you only read one section of the brief before writing, read that one.

---

## Workflow

```
brief.md + components/  →  Claude Design (design system)
                        →  prompt per email type
                        →  client reviews the design
                        →  HTML handed back
                        →  convert + wire dynamic content + upload images
                        →  import to Klaviyo  →  seed test in Gmail + Outlook
```

Order agreed with the client: **welcome and abandoned cart first**, then newsletter, holiday and seasonal.

Two things to hold on to:

- **Preview in a browser is not preview in an inbox.** Always seed-test through Klaviyo before anything ships.
- **Cart line items and cross-sell are dynamic.** A static comp is approvable but not functional. `components/19-cart-line-items.html` carries the real Klaviyo loop; it will look broken in a browser, which is expected.

---

## Account facts

| | |
|---|---|
| Klaviyo account | `VagrHA` |
| Image CDN | `https://d3k81ch9hvuctc.cloudfront.net/company/VagrHA/images/` |
| Sender | DrinkAid Team · `hello@drinkaid.co` |
| Stale v1 template | `Y4USkr` — see warning above |
| Flow segmentation | Track A = 1–2 boxes · Track B = 2–4 · Track C = 5+ |

---

## Open items

1. **Four trust-row icons do not exist.** `components/12-icon-trust-row.html` references `icon-clinical`, `icon-sg`, `icon-nodrowsy`, `icon-vegan`. The URLs are placeholders and will render as broken images. The block is otherwise complete. Design, upload to the CDN, update the file.
2. **Deprecate Klaviyo template `Y4USkr`.**
3. **Confirm the typeface with the client.** Matters for print and web; barely matters for email, since Klaviyo strips webfonts.
4. **Get client sign-off on the standardised type scale** — `brief.md` §12 lists everything in this category.
5. **UGC folder is unusable as-is.** The local `Asset/` folder holds candid customer photos of the Gummies SKU. All are phone screenshots — several still carry the iOS status bar and Instagram story UI, and six are rotated 90°. They need cropping, rotating and uploading before any of them can appear in an email. Do not feed them to a design tool in their current state.

---

## Source material

Not in this repo — it is large and client-confidential. Held locally alongside it.

| | |
|---|---|
| `DrinkAid_Brand Brief_May 2026.pdf` | Strategy: personality, audience, "Show Up Anyway", tone guardrails. No visual identity section. |
| `Welcome Flow EDM.pdf` | 14 real emails |
| `DrinkAid EDM.pdf` | 70 real emails |
| `EDM reference/` | 43 competitor emails from Moom, Seed, Grüns, Lemme, IM8, sorted by funnel stage |
| `DrinkAid-own-emails/` | 13 of the client's real emails exported as PNGs, for feeding to design tools |
