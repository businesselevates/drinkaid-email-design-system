# Pills post-purchase nurturing — V4

Built from the client copy doc `13KGYmRN0u21OpRSFJ4i89qDAZIAHzFx-t_aiX0wTvYQ`.
Supersedes the V3 drafts. **V3 was left untouched** — see *What was not changed*.

| | |
|---|---|
| Klaviyo account | `VagrHA` |
| Sender | DrinkAid Team · `hello@drinkaid.co` |
| Email manifest | `nurturing-v4-emails.json` |

## The three flows

| Track | Segment | Klaviyo flow | Emails | Window | First nudge | Primary offer |
|---|---|---|---|---|---|---|
| A | 1–2 boxes | `YmGiAb` | 10 | 60 days | D20 | D27 |
| B | 3–4 boxes | `Vt56r5` | 11 | 115 days | D70 | D95 |
| C | 5+ boxes | `XVHwMq` | 13 | 135 days | D122 | D130 |

All three are **draft**, every message carries subject line and preview text, and
**no template is attached yet** — hence `TEMPLATES PENDING` in the flow names.

34 message slots resolve to **22 unique templates**: the top-of-funnel emails are
byte-identical across tracks. `nurturing-v4-emails.json` carries the mapping.

## How the tracks are split

`Placed Order` cannot carry the split. Its `Item Count` property counts **line
items, not units** — an observed order of 2 boxes reports `Item Count: 1` — and
its `Items` property holds only the product title, so the pack size is invisible.

The flows therefore trigger on **`Ordered Product`** (`Y669Xq`), which does carry
`Quantity`, `Variant Name` and `SKU`.

| Track | Trigger filter |
|---|---|
| A | Name = pills **AND** Variant = `Original (6 Sachets)` **AND** Quantity ≤ 2 |
| B | Name = pills **AND** Variant = `Original (6 Sachets)` **AND** Quantity 3–4 |
| C | (Name = pills **AND** Variant = `Original (6 Sachets)` **AND** Quantity ≥ 5) **OR** (Name = pills **AND** Variant = `Sharing Pack (30 Sachets)`) |

One Sharing Pack is 30 sachets ≈ 5 boxes, which is why it lands in C.

Shared by all three: profile filter `Placed Order` = 0 before flow start
(first-time buyers only), and re-entry disabled.

## Open items before these can go live

1. ~~**Confirm the full variant list.**~~ **Closed.** Shopify shows the product
   has exactly two variants — `Original (6 Sachets)` / `DACAD01` / S$14.90 and
   `Sharing Pack (30 Sachets)` / `DASP1` / S$59.80. The track filters cover the
   whole catalogue; no flow change needed.
2. **Decide what happens to subscription orders.** Orders placed through
   `subscription_contract_checkout_one` carry a selling plan and replenish
   automatically; a "you're running low, restock" sequence is wrong for them.
   They are not excluded yet.
3. **Mixed carts trigger twice.** An order containing both variants fires two
   `Ordered Product` events and can enter two tracks. Needs a precedence rule.
4. **Turn off the live V3 flow at cutover.** `TLYSwU`
   ("[DrinkAid] Nurturing Email (new EDM)") is live on `Placed Order` with no
   product filter, for first-time buyers. Left running, it double-sends.
5. **Coupon codes are placeholders.** A10, B11 and C13 promise 10% off and print
   `XXXXX`. B11 also contradicts itself — body says `XXXXX`, the P.S. says
   `BACKAGAIN10`. Klaviyo dynamic coupons would satisfy the 7-day expiry the
   copy promises.
5b. **The A6 price table does not match list price.** The copy prints
   "3 boxes = 18 sachets = S$37.02", but three boxes at list is
   3 x S$14.90 = S$44.70. Every automatic discount in Shopify is expired, so the
   tier comes from the `_aov_bundles` bundle app ("Get-More-Save-More") and is
   not readable through the Admin API. Someone has to confirm the live tier
   before that email ships — otherwise it quotes a price the checkout will not
   honour.
6. ~~**Broken product URL in the copy.**~~ **Fixed.** The copy doc misspells the
   handle as `complete-alchohol-defence` (4 occurrences); `components/09-cta-primary.html`
   carried the same typo. Shopify confirms the real handle is
   `complete-alcohol-defence`. The component is corrected; the copy doc still
   needs the same fix at source.
7. **Review mechanic undecided.** A7/B6/C7 ask to collect the review inside the
   email rather than sending people to Shopify. Whether that is possible depends
   on the review app in use.
8. **Hero photography.** The approved comp ships a placeholder lifestyle shot
   whose own alt text reads "real product/lifestyle photography to come". Needed
   from the client before any archetype carrying a hero ships.
   Two former asset gaps are now closed: no approved archetype uses a trust-icon
   row, so the four missing icons in `components/12-icon-trust-row.html` are not
   blocking; and A3's "four pathways" needs no infographic because archetype 3
   renders it as live numbered text, which also survives images-off.
9. **Day-number conflicts in the source doc.** The Track C summary table says
   D100 and D135; the per-email headings say D110 and D130. The headings were
   treated as canonical. The Track A "Updated Ideas 12/8" table likewise
   disagrees with the A1–A10 headings.
10. **C10 → C11 is a 2-day gap** (D110 → D112) against 16–22 day gaps either
    side. Faithful to the doc; worth a second look.

## What was not changed

The V3 drafts `Rwcjte` / `S692Vg` / `TpnCpK` and every `[Pills]` template from
12–13 August are untouched. Note that those templates — including everything
suffixed `— DESIGNED` and the master `Y4USkr` — are the dark, off-brand set that
`HANDOFF.md` warns about. None of them should be attached to a V4 flow.

## Design → template mapping

The client-approved comp (`DrinkAid Post-Purchase Nurture - Layout Comp.dc.html`)
is a layout approval: all copy in it is lorem ipsum, and what was signed off is
the system — colour, type, spacing and block vocabulary. It defines **8 layout
archetypes** covering all 34 sends.

| Archetype | Templates it carries |
|---|---|
| 1 · Welcome / thank-you | T01 |
| 2 · Education + table | T02 |
| 3 · Long-form explainer | T03, T04, T14 |
| 4 · Founder letter | T05, T18, T19 |
| 5 · Nudge + single CTA | T08, T10, T11, T12, T13, T16, T21 |
| 6 · Offer + price comparison | T09, T15, T22 |
| 7 · Review request | T06 |
| 8 · Range / cross-sell | T20 |

T17 (C5, the Day 28 qualifier) has no exact archetype — it asks one question with
two possible situations. Archetype 6's two-card layout is being reused for it
with the CTAs relabelled as the two answers, rather than commissioning a ninth.

The comp's component library maps 1:1 onto `components/`: `LogoPill` → 02,
`HeaderBar` → 03, `EyebrowHeadline` → 07, `MintPanel` → 14, `CtaPrimary` → 09,
`CtaOutline` → 11, `ReviewCard` → 17, `CategoryCard` → 16, `SupportLine` → 22,
`Footer` → 23. Four blocks in the comp had no repo equivalent and were added:
`24-spec-table`, `25-numbered-explainer`, `26-letter-body`, `27-offer-compare-2up`.

**The comp's footer has no unsubscribe link.** `components/23-footer.html` does,
and that is the one being shipped — the tag is a legal requirement. The built
emails therefore carry one line the client did not see in the comp.
