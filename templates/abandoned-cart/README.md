# Abandoned cart · four sends

The client-approved layout for the cart-recovery flow, built from `components/` and
carrying the copy from the approved copy doc verbatim. Live in Klaviyo as draft.

Approved layout: https://claude.ai/code/artifact/8dd4062f-fed1-42ad-b1fc-eebe836dca4b
Flow: https://www.klaviyo.com/flow/WVmBZQ/edit (`[DrinkAid] Cart recovery email (clone)`, status **draft**)

| # | File | Delay | Subject | Master template | Flow copy |
|---|---|---|---|---|---|
| 1 | `01-recovery-30min.html` | 30 min | You left your mornings in the cart | `RnZhBf` | `YAKvRJ` |
| 2 | `02-recovery-10h.html` | +9 h 30 | Still thinking it over? | `T8zETq` | `WycBhC` |
| 3 | `03-recovery-16h-offer.html` | +6 h | A little something before your cart expires | `S9BQM4` | `Vg9vTR` |
| 4 | `04-recovery-3d-proof.html` | +56 h | Still not sure if DrinkAid is for you? | `W6LpiE` | `WVV8Ur` |

**Master vs flow copy.** Klaviyo clones a template into the flow message the moment it is
assigned, so each email exists twice. The master (`[Cart v2] R0n · …` in the template
library) is the one to edit and re-assign; the flow copy is what actually sends. Editing
the flow copy in the flow editor is fine too, it just drifts from the master.

The four previous dark templates (`WuzYZR`, `WYWM8z`, `RpMeaY`, `TfrKtb`) are no longer
referenced by the flow. They are left in the library untouched.

## How each one is built

Every email: `02-header-logo-pill` → blocks → `22-support-line` (not on #4) → `23-footer`.

| # | Blocks between header and footer |
|---|---|
| 1 | `07-eyebrow-headline` · `08-body-copy` · `19-cart-line-items` · `09-cta-primary` · sign-off |
| 2 | `07` · `08` · `24-tick-list` (4) · `08` · `25-review-stack` (3) · `08` guarantee · `09` · section label + `19` · sign-off |
| 3 | `07` · `08` · `18-offer-code-panel` · expiry caption · `09` · `08` · section label + `19` · sign-off |
| 4 | `07` · `08` · `08` · `24-tick-list` (5) · `08` · `17-review-card` · `08` guarantee · `09` · section label + `19` · brand sign-off line |

Headlines use the signature italic second line. Eyebrows are the ones already in the
old flow (`YOUR CART IS SAVED`, `STILL DECIDING?`, `YOUR CART EXPIRES SOON`,
`THE HONEST ANSWER`). Body copy, ticks, reviews, CTA labels and sign-offs are the copy
doc's words, unchanged.

## Dynamic content

`19-cart-line-items` loops `event.extra.line_items` from the Shopify **Checkout Started**
event:

```
{{ item.product.images.0.src }}      thumbnail
{{ item.product.title }}             linked to https://drinkaid.co/products/{{ item.product.handle }}
{{ item.product.variant.title }}     shown only when set and not "Default Title"
{{ item.quantity }}
{{ item.line_price_set.shop_money.amount }}         price, as S$, when presentment_currency is SGD or unset
{{ item.line_price_set.presentment_money.amount }}  price + currency code otherwise (VND, MYR...)
{{ event.extra.checkout_url }}       every CTA
```

Two things learned from a real event (4 Sep): Shopify sends `product.url` as **null**, so
the link is built from `handle`; and `line_price` is in the shopper's *presentment*
currency (a checkout from Vietnam came through as 1048000 VND), so the price reads
`line_price_set` and switches format on `presentment_currency`.

Verified with the Klaviyo render API against a two-item sample cart (one with a variant,
one without). **The Klaviyo web-view / plain preview renders the list empty** because it
has no Checkout Started event behind it; use *Preview with event data* in the flow editor,
or a seed test, to see rows. Still needs a **seed test through the flow** in Gmail and Outlook before the
flow goes live; a browser preview is not an inbox.

## Mobile

Two things overflowed the 375px canvas in the first build and are now fixed in the
shared blocks, so they apply to every future email:

- the footer social row (domain · four icons · handle) was a six-cell table that could
  not shrink below ~420px. It is now inline text and images inside one cell, so it
  wraps naturally. `components/23-footer.html`.
- the discount code at 32px did not fit. `.da-code` in `_shell.html` drops it to 22px
  below 620px. `components/18-offer-code-panel.html`.

## Still open

- **Review attributions.** The approved layout shows an attribution line under each
  quote (`— J.W. TAN`). The copy doc has none, so none are shown. Add them once the
  client supplies real names or initials; never invent one.
- **Discount code.** `DRINKAIDEMAIL12` is carried over from the previous version of
  email 3. The copy doc says 10%; the code's actual value could not be checked (Shopify
  connector was not authorised in this session). Confirm before the flow goes live.
- **Email 1 copy still says "gummies"** in two places, as the copy doc does. If the flow
  serves the pills SKU too, that line needs a variant or a conditional.
