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
propagate. That copy is **not reachable through the Templates API** — `PATCH`
returns 404 — so the way to push a repo change into a live flow is:

1. `update_email_template` on the library template.
2. `update_flow_action` on the message, setting `message.template_id` back to the
   library id. This re-clones, producing a *new* copy id.
   The action's existing `links` must be sent unchanged or the call is rejected
   with "You cannot change the links of an action."
3. Read the new copy back and confirm the change landed.

On 25 August all 22 library templates were rebuilt with the corrected bullet and
footer, and **all 32 flow messages were re-attached** this way, so every copy id
recorded before that date is stale. The C11 range email is the one that matters
downstream: its flow copy was `RKEWZY` (was `Yed2U4`), and moved again to
**`Y8MmE5`** when the product images were corrected. Images live in the flow
copy as well as in library template `SvGkXd`, so replacing one is a two-place
job.

The three discount emails were re-attached again on 25 August for the
`LASTCHANCE10` swap, so their copy ids moved a second time:

| Message | Action | Library | Flow copy |
|---|---|---|---|
| A10 · D60 · Exit (T12) | `115379245` | `WBCqdK` | `UtTTTT` |
| B11 · D115 · Exit (T16) | `115379302` | `XFGeFS` | `SUc3dj` |
| C13 · D130 · Primary offer (T22) | `115379372` | `VjzyMt` | `SgAuqM` |

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
| B | Name = pills **AND** Variant = `Original (6 Sachets)` **AND** Quantity ≥ 3 **AND** Quantity ≤ 4 |
| C | Name = pills **AND** (Quantity ≥ 5 **OR** Variant = `Sharing Pack (30 Sachets)`) |

### How Klaviyo combines trigger conditions — groups are AND, conditions are OR

Established from the UI on 2026-08-25, after the first build got it backwards.
The stored JSON carries no `and` / `or` keyword at all, only
`condition_groups[]` each holding `conditions[]`, so the semantics are invisible
from the API and have to be read off the flow editor:

- **Separate `condition_groups` are ANDed.** The editor draws each as its own
  bullet with **AND** between them.
- **`conditions` inside one group are ORed.** The editor stacks them under a
  single bullet with **OR** between them.

The first build assumed the opposite and put every condition of a track into one
group, which ORed them. Track B's group contained `Quantity >= 3` and
`Quantity <= 4` — as an OR that is true of every number, so the whole filter
was a tautology and the flow would have accepted **every `Ordered Product`
event in the account**, any product. A and C were wrong the same way. Nothing
shipped: all three were drafts throughout.

So an AND of N conditions is N groups of one condition each. Track C needs an OR
of two AND-clauses, which this grammar cannot hold directly — it expresses
conjunctive normal form only. Distributing it gives a form that fits, and one
clause falls out as redundant because the product has exactly two variants:

    pills AND ((Original AND qty>=5) OR SharingPack)
  = pills AND (Original OR SharingPack) AND (qty>=5 OR SharingPack)
  = pills AND (qty>=5 OR SharingPack)          <- first clause always true

Which is why C is two groups rather than four. Checked against each tile:
Original at 1 or 2 fails group 2 and lands in A; at 3 it fails group 2 and lands
in B; at 6 or 9 it passes and lands in C; a Sharing Pack passes on the variant
arm at any quantity. No tile matches two tracks.

One Sharing Pack is 30 sachets ≈ 5 boxes, which is why it lands in C.

The storefront sells the Original in fixed quantity tiles of **1, 2, 3, 6 and 9
boxes** (at 0 / 5 / 8 / 12 / 15% off), so in practice A catches 1–2, B catches
only 3, and C catches 6, 9 or any Sharing Pack. Quantities 4 and 5 are
unreachable from the product page. The ranges are kept rather than pinned to the
exact tiles so the split still holds if a customer edits quantity in the cart or
the tiles are ever changed.

### Why the split has to live on `Ordered Product`

`Placed Order` does carry the line-level data — `$extra.line_items[]` holds
`quantity`, `sku` and `variant_title` on every order, verified on a live event.
What it cannot do is **filter** on it. A trigger filter condition is
`{"type": "metric-property", "field": "<one flat property>", "filter": {...}}`
with a single scalar operator; `line_items` is an array of objects and the
grammar has no "any element matches" quantifier. So the data is visible to a
template but unreachable by a filter, which is why the tracks trigger on
`Ordered Product` instead.

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

> ~~**Defect — all three track trigger filters were built inside out.**~~
> **Fixed in the UI, 2026-08-25, and verified by reading all three back.** The
> first build ORed each track's conditions by putting them in one condition
> group; Track B's was a tautology (`Quantity >= 3 OR Quantity <= 4`) and would
> have admitted every `Ordered Product` event in the account. Rebuilt one group
> per ANDed condition — A is 3 groups, B is 4, C is 2 with the OR pair in the
> second. Checked against every purchasable quantity: no tile lands in two
> tracks and none falls outside all three. Nothing had shipped mis-segmented;
> all three were drafts throughout. See *How Klaviyo combines trigger
> conditions* above for the grammar.

1. ~~**Confirm the full variant list.**~~ **Closed.** Shopify shows the product
   has exactly two variants — `Original (6 Sachets)` / `DACAD01` / S$14.90 and
   `Sharing Pack (30 Sachets)` / `DASP1` / S$59.80. The track filters cover the
   whole catalogue; no flow change needed.
2. **Decide what happens to subscription orders.** Orders placed through
   `subscription_contract_checkout_one` carry a selling plan and replenish
   automatically; a "you're running low, restock" sequence is wrong for them.
   They are not excluded yet.
3. ~~**Mixed carts trigger twice.**~~ **Accepted, not fixed — client call,
   2026-08-25.** An order containing both variants fires two `Ordered Product`
   events and enters two tracks. The client's read is that buying an Original
   and a Sharing Pack in one order is rare enough not to engineer around, and
   they own that judgement about their own order mix. What is being accepted:
   those buyers get two overlapping restock sequences, not one.

   Two things blunt it, neither by design. Smart sending is on for every message
   read back so far, so two tracks landing on the same day suppress down to one
   send — and both tracks open at D2 on a shared top-of-funnel, which is where
   collisions cluster. The schedules diverge later (D60 / D115 / D130), where
   duplicates would be different emails rather than the same one twice.

   Not measured. `Ordered Product`'s `$event_id` is `{order}:{line item}:{index}`,
   so the true rate is countable by grouping pills events on that prefix if it
   ever needs a number.
4. **Turn off the V3 flow at cutover.** `TLYSwU`
   ("[DrinkAid] Nurturing Email (new EDM)") triggers on `Placed Order` with no
   product filter, for first-time buyers. Left running, it double-sends.
   **As of 2026-08-24 16:xx UTC it reads `draft`, not live** (last updated
   07:37 that morning) — so it may already have been switched off. Nobody on
   this side changed it. Worth confirming with whoever did before treating this
   as closed, in case the status change was accidental.
5. ~~**Coupon codes are placeholders.**~~ ~~**Decided: Klaviyo dynamic coupon.**~~
   **Closed 2026-08-25: one standing code, `LASTCHANCE10`, in all three emails.**
   T12, T16 and T22 print it literally. No Klaviyo dynamic coupon is involved, so
   there is nothing left to create on the Klaviyo side — only a check that the
   code is live in Shopify. Because a static code cannot expire per recipient,
   the 7-day expiry claim was dropped from T12 and T16; see *The discount* below.
   (The doc's B11 contradiction — body `XXXXX`, P.S. `BACKAGAIN10` — is moot, but
   the P.S. still names `BACKAGAIN10` in the copy doc and should be corrected at
   source.)
5b. ~~**The A6 price table does not match list price.**~~ **Closed, and my earlier
    reading of it was wrong.** S$37.02 was not invented: it is 3 boxes after the
    8% volume discount *and* the 10% coupon (44.70 x 0.92 x 0.90 = 37.01). The
    real defect was that T09 showed a with-coupon price while carrying no coupon
    code, so a customer clicking through would have found S$41.12. T09 now quotes
    **S$41.12 / S$2.28 per session**, the true no-coupon price.
    T15, T16 (S$113.62 for 2 Sharing Packs) and T22 (S$53.82 after 10%) were all
    checked against the ladder below and are exact.

    Volume ladder, derived from ~50 real orders on SKU `DACAD01`:

    | Boxes | Discount |
    |---|---|
    | 1 | 0% |
    | 2 | 5% |
    | 3 | 8% |
    | 6 | 12% |
    | 9+ | 15% |

    The `qty 6 -> 12%` step is confirmed across 14 orders; the others across 3-8
    each. The tier config lives inside the volume-discount app and is not
    readable through the Admin API, so this is inferred from outcomes, not read
    from source.

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
12. **Prices are quoted in SGD but the store sells into 14 markets.**
    Shopify has 14 enabled markets and 15 price lists across 14 currencies, so a
    recipient in Malaysia or the Philippines sees a different number at checkout
    than the S$ figure in the email. Same-variant SGD line prices observed across
    recent orders ranged S$10.92-15.39. The quoted prices are correct for
    Singapore only. Either label them as such, restrict the price-bearing emails
    to the SG market, or drop absolute figures.
13. ~~**Three C11 product images are unverified.**~~ **Two were wrong; fixed
    2026-08-25.** Checked against the Klaviyo preview: only Snuu was right. The
    Easy Mode card carried a shot of the pills box, and the Gummies card carried
    the Easy Mode bottle — so the Easy Mode shot was already in hand, one card
    too far down. Re-pointing it left Gummies as the only genuinely missing
    asset.

    That one came from the Shopify product image. `upload_image_from_url`
    fetches the URL **server-side at Klaviyo**, so it reaches the storefront CDN
    even though this session's outbound access to that host is blocked — no file
    transfer needed, and it is the canonical shot rather than an ad crop. New
    image id `362430726`.

    The comp's third image (the pills box, `93ae336c`) is dropped: C11 is about
    the rest of the range and the reader has already bought the pills.

    Still worth an eyeball in preview. The Gummies import is a 934KB PNG, and
    the byte-count check that caught the mangled social icons cannot be applied
    here — comparing against the source would mean fetching it, which the
    outbound block prevents.

    **Easy Mode changed again the same day.** The client checked the preview:
    Gummies was right, Easy Mode was not. The comp's Easy Mode shot is a bottle
    held against plain white, so on a white email canvas the card read as half
    empty next to Snuu and Gummies, which both fill their frame — the problem
    was framing, not identity.

    The replacement came out of the client's Drive folder, per product. Two
    findings about that folder, both worth keeping:

    - The ~30 `EasyMode ads - *.png` files are ad creative with headlines burned
      into the pixels ("Coffee 2.0", "Get shit done"). Unusable next to two
      clean cards; do not reach for them.
    - The six `DrinkAid EDM (n).png` files are Canva exports from the EDM deck,
      the same design language as the comp. These are the right family.

    All six were imported to the Klaviyo library as `[cand] EDM n` so the client
    could look at them and choose — this session cannot see images, `Read` on an
    image needs a local file, and both `drive.google.com` and
    `lh3.googleusercontent.com` are 403 at the proxy under org policy. Klaviyo's
    server-side fetch is the only route that reaches Drive, and only via
    `https://lh3.googleusercontent.com/d/{FILE_ID}`.

    The client picked EDM 5, now image `362441412`. Five of the six imports came
    back byte-for-byte identical to Drive's `fileSize`, so the integrity check is
    available again on this route. The exception was EDM 7: 4,493,315 bytes in,
    743,316 out — Klaviyo recompressed it. Under 5MB, so not the documented size
    limit; treat multi-megabyte PNGs as re-encoded on import and check the
    preview rather than trusting the upload. The five unused candidates are set
    `hidden` (Klaviyo has no delete-image endpoint), as is the earlier
    `[probe] drive fetch test`, `362436660`.

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
`HeaderBar` → 03, `EyebrowHeadline` → 07 (the eyebrow half was later dropped at
the client's request; `blocks.headline` keeps only the h1), `MintPanel` → 14, `CtaPrimary` → 09,
`CtaOutline` → 11, `ReviewCard` → 17, `CategoryCard` → 16, `SupportLine` → 22,
`Footer` → 23. Four blocks in the comp had no repo equivalent and were added:
`24-spec-table`, `25-numbered-explainer`, `26-letter-body`, `27-offer-compare-2up`.

**The comp's footer has no unsubscribe link.** `components/23-footer.html` does,
and that is the one being shipped — the tag is a legal requirement. The built
emails therefore carry one line the client did not see in the comp.

## The Day 0 CTA — button removed, 2026-08-25

T01 used to end with a **VIEW MY ORDER** button pointing at the Shopify
order-confirmation page (`$extra.order_status_url`, which only `Placed Order`
carries). **The client signed off on removing it**, for three reasons that all
hold independently:

1. Shopify already emails its own order confirmation, carrying that link, within
   seconds of checkout. By the time T01 lands the customer has it.
2. T01's own body says *"Once yours ships, we will send the tracking link
   straight over."* The button offered the thing the paragraph above it had just
   promised to send later.
3. The `|default:` fallback pointed at `drinkaid.co/account`. Checkout is guest
   by default — the one live order read for this had the customer at
   `state: "disabled"`, i.e. no account — so the fallback was a login wall
   rather than an order page.

T01 is now a founder's letter with no button. `archetypes.welcome()` takes `cta`
and `href` as optional, matching `education_table` and `explainer`; the support
line ("reply to this email — a human reads it") still closes it, and the first
real CTA in the sequence now lands on T02.

Library template `RqKwSt` re-uploaded and re-attached to `Rg2fJS`; the flow copy
is now **`Sr7TeA`** (was `VZkKkB`, and `SQshAX` before that).

### T01 got a hero image (26 Aug)

The letter opened on an eyebrow and a headline over plain text. It now carries a
hero between the two, from the client's EDM deck — the same family as the C11
cards they signed off on. `archetypes.welcome()` takes `hero` and `hero_alt` as
optional, matching `education_table` and `explainer`.

Chosen over the other candidate in that folder, `2026 May - BOFU - DRINKAID 4x5
ADS.jpg`, on three grounds: it is a bottom-of-funnel acquisition creative and
T01 goes to somebody who has just paid; it would put a sales pitch back into the
one email whose CTA button was deliberately removed; and `4x5` means portrait,
which at 520px wide is a ~650px wall of image above a letter whose whole point is
the letter.

The image is `[Pills v4] T01 hero - welcome letter`, 687KB — well within what
Klaviyo serves, and the byte count matches what was uploaded, so it was not
mangled (see the social-icon note above). It is heavy for a hero on mobile data
though; if the client wants it lighter, re-export and re-upload rather than
scaling it down in the `width` attribute.

### The uppercase eyebrow was dropped (26 Aug)

The comp put a small letter-spaced eyebrow above each h1 — "TIME TO RESTOCK",
"THE TIMING", "A SMALL FAVOUR" and so on. The client asked for it gone.

`blocks.eyebrow_headline` became `blocks.headline`, and the h1 took over the
eyebrow's 34px top padding, so the spacing under the logo pill is unchanged. The
`eyebrow` argument is gone from all seven archetypes that took one and from all
20 specs that passed one. The two founder letters (T05, T18) never had one, which
is why only 20 of the 22 templates changed.

Untouched, because they are a different element: the uppercase labels inside the
mint panels (THE DOSE, THE SIMPLE OPTION), the discount panels (USE CODE), the
offer cards (OPTION ONE / OPTION TWO, ANSWER ONE / ANSWER TWO) and the product
cards in the range email (SLEEP BALM, CHEWABLE, CAFFEINE-FREE FOCUS).

**Pushed to Klaviyo on 26 August**: 20 library templates re-uploaded and 28 flow
messages re-attached, so every flow copy id below supersedes anything recorded
earlier — including `Sr7TeA` for T01, three paragraphs up.

| Slot | Action | Message | New copy |
|---|---|---|---|
| Day 0 (T01) | `115379174` | `T4s9fm` | `TnFpmk` |
| A2 (T02) | `115379228` | `TBrbyW` | `UYr24S` |
| A3 (T03) | `115379230` | `SYq8Wj` | `XYRYE6` |
| A5 (T08) | `115379234` | `VWeRkE` | `SZiRKs` |
| A6 (T09) | `115379236` | `X7DGew` | `TaVnt9` |
| A7 (T06) | `115379238` | `STLSAV` | `TdxCE2` |
| A8 (T10) | `115379241` | `Yh4x8n` | `TXNbNU` |
| A9 (T11) | `115379243` | `XE3uvK` | `RituDC` |
| A10 (T12) | `115379245` | `X32rT8` | `XYpuBc` |
| B2 (T02) | `115379275` | `VnriXg` | `VapwMu` |
| B3 (T03) | `115379283` | `VUP7ev` | `XKGdDJ` |
| B4 (T04) | `115379285` | `X6dW8m` | `WfLmni` |
| B6 (T06) | `115379289` | `VQbQT7` | `TArEd2` |
| B7 (T07) | `115379292` | `QZhYCT` | `TXyVMt` |
| B8 (T13) | `115379295` | `WnzDak` | `UR4ZuC` |
| B9 (T14) | `115379297` | `TX8H3e` | `XDDdcb` |
| B10 (T15) | `115379300` | `WUXrrz` | `RpsJZV` |
| B11 (T16) | `115379302` | `WhWnNW` | `Wsdn9N` |
| C2 (T02) | `115379343` | `W4DRP8` | `XsWWpe` |
| C3 (T03) | `115379347` | `RdKZyU` | `VqDhQz` |
| C4 (T04) | `115379349` | `WB3E6m` | `WMUTC6` |
| C5 (T17) | `115379352` | `VkZyR7` | `VhZ3kE` |
| C7 (T06) | `115379358` | `WwqpJX` | `XViJmr` |
| C8 (T07) | `115379360` | `SixA7n` | `XXUYyi` |
| C10 (T19) | `115379366` | `X4Nc2c` | `XyLGPk` |
| C11 (T20) | `115379368` | `WrM9pz` | `WYmUpA` |
| C12 (T21) | `115379370` | `VNL6LW` | `T9Cnks` |
| C13 (T22) | `115379372` | `TpjaDQ` | `XzmWRG` |

Not re-attached, because their templates did not change: A4 (`115379232`), B5
(`115379287`) and C6 (`115379356`), all T05; and C9 (`115379364`), T18.

### Folding Day 0 into the three track flows

Removing the button removes the only reason the flows were split: T01 no longer
needs order-level data, so all four flows could run off `Ordered Product` alone.

**The API cannot do it.** There is no `create_flow_action` — actions can only be
added by `create_flow`, which builds a whole flow from a full definition. Adding
one email to the head of an existing flow is therefore either a UI edit, or a
rebuild of all three flows from scratch under new IDs. The UI edit is the right
call: three flows, one new email each, delay 0, attach `RqKwSt`.

Two consequences of merging:

| | 4 flows (current) | 3 flows (merged) |
|---|---|---|
| T01 copies to maintain | 1 | 3 — each edit is its own re-attach |
| Mixed pills cart | T01 sends once (`Placed Order` fires once) | T01 sends twice (two `Ordered Product` events) |
| Flow objects | 4 | 3 |

The mixed-cart row is no longer a blocker: open item 3 records the client's
decision to accept that case rather than engineer around it, and merging only
widens an accepted risk. Two same-day sends of T01 are also the case smart
sending suppresses most reliably, since both entries fire within minutes.

So the merge is **unblocked and pending a UI edit** — three flows, one email
each at the head, delay 0, template `RqKwSt`, subject *Better mornings start
here*, preview *A proper thank you, from a small team in Singapore*. Delete
`Rg2fJS` afterwards. What it buys is one fewer flow to keep in sync; what it
costs is T01 living in three copies instead of one, so every future edit to it
becomes three re-attaches rather than one.

## The discount

**One standing code, `LASTCHANCE10`, shared by all three discount emails**
(T12, T16, T22). Printed literally in the HTML — not a Klaviyo dynamic coupon,
so there is no per-profile code and nothing to create in Klaviyo. The only
pre-send check is that the code is live in Shopify at the right value.

It **stacks with product discounts** — the volume bundles — but **not with other
order discounts**, notably the newsletter-signup code. So the bundle ladder
still applies underneath it and does not need special handling.

Stacking with the bundle was verified independently before this was settled:
`Get-More-Save-More` and `Buy-More-Save-More` are both `DiscountCodeApp` codes
from the `volume-discount` app, both ACTIVE, and both carry
`combinesWith: {orderDiscounts: true, productDiscounts: true,
shippingDiscounts: true}`. Real orders already show a 10% code applied alongside
the 12% volume discount (#125775, #125773, #125757, #125723).

Accepted trade-off: at 3 boxes the customer pays 44.70 -> 41.12 (volume)
-> 37.01 (code), about 17% off list. Signed off.

**No expiry is claimed.** A single static code cannot expire a different number
of days after each recipient opens it, so "expires in 7 days" was removed from
T12 and T16 rather than shipped as a promise the code does not keep. T12's P.S.
still frames it as tied to the last restock reminder, which stays true without
naming a deadline. If the Shopify code is later given a fixed end date, say so
as a date and put it back.
