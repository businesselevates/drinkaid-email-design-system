# Pills post-purchase nurturing — V4

Built from the client copy doc `13KGYmRN0u21OpRSFJ4i89qDAZIAHzFx-t_aiX0wTvYQ`.
Supersedes the V3 drafts. **V3 was left untouched** — see *What was not changed*.

| | |
|---|---|
| Klaviyo account | `VagrHA` |
| Sender | DrinkAid Team · `hello@drinkaid.co` |
| Email manifest | `nurturing-v4-emails.json` |

## The four flows

Day 0 is its own flow (see *The Day 0 CTA problem*), so the three track flows
open with a two-day delay and carry Day 2 onwards.

| Flow | Klaviyo id | Trigger | Emails | Window |
|---|---|---|---|---|
| Day 0 welcome | `Rg2fJS` | `Placed Order` containing the pills | 1 | D0 |
| Track A · 1–2 boxes | `W2S7G4` | `Ordered Product` | 9 | D2–D60 |
| Track B · 3–4 boxes | `XMSf6n` | `Ordered Product` | 10 | D2–D115 |
| Track C · 5+ / Sharing Pack | `Yu6MWe` | `Ordered Product` | 12 | D2–D130 |

All four are **draft**, and every message now carries subject line, preview text
and an attached template. 34 message slots resolve to **22 unique templates**
and 32 built messages — the Day 0 flow serves A1/B1/C1 from one email.
`nurturing-v4-emails.json` carries the mapping.

**Klaviyo copies the template on attach.** Each flow message owns a private copy
of the library template, with its own id; editing the library template does not
propagate. To change a shipped email, edit it inside the flow — or re-attach.
The three unverified C11 product images live in flow message `Yed2U4`
(Track C, D112), not only in library template `SvGkXd`.

### Superseded flows

`YmGiAb` / `Vt56r5` / `XVHwMq` are the first V4 build: right copy, right
triggers, but Day 0 inline and no templates attached. They are drafts and carry
nothing the new flows do not. **They cannot be renamed through the API** — only
status-changed or deleted — so they are left as-is pending a decision. Deleting
them is safe; leaving them risks someone activating the wrong draft.

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

Shared by all four: profile filter **`Placed Order` at most 1 over all time**,
and re-entry disabled.

That filter changed in this rebuild. The first build used `Placed Order` = 0
*since starting this flow*, which suppresses people who buy again mid-flow but
does **not** restrict entry to first-time buyers — so it did not do what this
document claimed. `<= 1 over all time` does both: it admits only first-time
buyers, and it drops anyone who reorders part-way through, which is what a
restock-nudge sequence wants. It is `<=` rather than `= 1` so that the Day 0
email still sends if the order event has not finished indexing when the filter
is evaluated.

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
5. ~~**Coupon codes are placeholders.**~~ **Decided: Klaviyo dynamic coupon.**
   T12, T16 and T22 now render `{% coupon_code 'PILLS_NURTURE_10OFF' %}`, which
   gives each profile its own code. **The coupon does not exist yet** and has to
   be created in the Klaviyo UI — see *Setup still required in Klaviyo* below.
   Until it exists the tag renders empty, so these three must not send.
   (The doc's B11 contradiction — body `XXXXX`, P.S. `BACKAGAIN10` — is moot now
   that the code is generated, but the P.S. still names `BACKAGAIN10` in the copy
   doc and should be corrected at source.)
5b. **The A6 price table does not match list price.** *Decided: keep the copy
   doc's numbers.* T09 prints "3 boxes = 18 sachets = S$37.02", but three boxes
   at list is 3 x S$14.90 = S$44.70. Every automatic discount in Shopify is
   expired, so the tier comes from the `_aov_bundles` bundle app
   ("Get-More-Save-More") and is not readable through the Admin API. The risk is
   accepted rather than resolved: if that bundle tier is ever switched off, this
   email quotes a price the checkout will not honour. Worth a spot-check at
   seed-test time by actually adding three boxes to a cart.
6. ~~**Broken product URL in the copy.**~~ **Fixed.** The copy doc misspells the
   handle as `complete-alchohol-defence` (4 occurrences); `components/09-cta-primary.html`
   carried the same typo. Shopify confirms the real handle is
   `complete-alcohol-defence`. The component is corrected; the copy doc still
   needs the same fix at source.
7. ~~**Review mechanic undecided.**~~ **Closed.** The review app is Judge.me, and
   T06 links straight to the product's Judge.me review form, as the copy doc
   specifies. Collecting the rating inside the email body was dropped.
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
11. **Decide what to do with the superseded flows** `YmGiAb` / `Vt56r5` /
    `XVHwMq`. They cannot be renamed via the API, only deleted or
    status-changed. See *Superseded flows*.
12. **Three C11 product images are unverified.** The Snuu, Easy Mode and
    Gummies shots in T20 were picked from the Klaviyo image library by name and
    have not been confirmed as the current packshots. Replace inside flow
    message `Yed2U4` as well as library template `SvGkXd`.

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

## The Day 0 CTA problem — resolved

T01's button opens the Shopify order-confirmation page. That URL lives at
`$extra.order_status_url`, which **only `Placed Order` carries** — confirmed
against a live event. The track flows trigger on `Ordered Product`, whose
payload does not have it.

Day 0 is therefore its own flow (`Rg2fJS`), triggered on `Placed Order` filtered
to orders whose `Items` contain the pills. The button renders:

```
{{ event|lookup:'$extra'|lookup:'order_status_url'|default:'https://drinkaid.co/account' }}
```

which now resolves to the real order page, and still degrades to the account
page rather than breaking if the property is ever absent.

T01 was byte-identical across all three tracks, so this also stops the Day 0
email being maintained in triplicate.

## Setup still required in Klaviyo

The **coupon does not exist yet**. Create it before T12, T16 or T22 can send:

Klaviyo → Content → Coupons → Create coupon → Shopify, named exactly
`PILLS_NURTURE_10OFF`, 10% off, expiring 7 days after issue. The name is what the
`{% coupon_code %}` tag resolves against, so it must match character for
character. This cannot be done through the API — `create_coupon` only registers
an external id and can set neither a discount value nor an expiry — so it is a UI
job.
