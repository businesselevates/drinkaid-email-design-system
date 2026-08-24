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

1. **Confirm the full variant list.** Only two variants were observable from
   event data — `Original (6 Sachets)` and `Sharing Pack (30 Sachets)`. Any
   third pack size currently matches no track and the buyer receives nothing.
   Needs a look at the live Shopify product.
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
6. **Broken product URL in the copy.** `drinkaid.co/products/complete-alchohol-defence`
   appears 4 times — the handle is misspelled.
7. **Review mechanic undecided.** A7/B6/C7 ask to collect the review inside the
   email rather than sending people to Shopify. Whether that is possible depends
   on the review app in use.
8. **Missing assets.** A3 calls for a "four pathways" infographic that does not
   exist, and the four trust-row icons in `components/12-icon-trust-row.html`
   are still placeholders.
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
