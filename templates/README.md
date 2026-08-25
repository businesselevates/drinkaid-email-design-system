# templates/

Generated. Do not hand-edit — run `python3 tools/build.py` instead.

One file per unique template. 34 message slots across the three nurture tracks
resolve to these 22, because the top-of-funnel emails are shared between tracks.
`flows/nurturing-v4-emails.json` maps slot → template.

| Source | What it holds |
|---|---|
| `tools/blocks.py` | email-safe block builders, mirroring `components/` |
| `tools/archetypes.py` | the 8 layouts the client approved |
| `tools/emails.py` | the copy, transcribed from the client copy doc |
| `tools/shell.py` | the 600px Outlook-safe wrapper |
| `tools/build.py` | renders + lints everything here |

`build.py` fails on anything a browser preview would not catch: `margin`,
`box-shadow`, SVG, flex, grid, a 2-up cell without `da-stack`, an `<img>` with no
`alt`, a missing `{% unsubscribe %}`, unbalanced tags, or a body over 100KB
(where Gmail clips).

A clean build is not a send test. Preview in a browser is not preview in an
inbox — seed-test through Klaviyo into Gmail and Outlook before anything ships.

## Known gaps in what is generated here

- **The discount is one standing code, `LASTCHANCE10`.** T12, T16 and T22 print
  it literally — no Klaviyo dynamic coupon, no per-profile code. It stacks with
  product discounts (the volume bundles) but not with other order discounts, so
  the bundle ladder still applies underneath it. Confirm the code is live in
  Shopify before sending; a static code cannot carry a per-recipient expiry, so
  the emails make no expiry claim.
- **T09 prices come from the copy doc** and do not match Shopify list price.
  See open item 5b in `flows/nurturing-v4.md`.
- **T20's three product images are a guess.** The approved comp shipped three
  CategoryCard images without labelling which is Snuu, Easy Mode or Gummies;
  they are assigned here in the order the comp used them and must be checked.
- **T01's CTA falls back to the account page.** It looks up
  `$extra.order_status_url`, which exists on `Placed Order` but not on
  `Ordered Product` — the trigger these flows use. See "The Day 0 CTA problem" in
  `flows/nurturing-v4.md`.
