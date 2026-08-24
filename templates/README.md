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

- **Coupon codes read `XXXXX`** in T12, T16 and T22. Real codes, or Klaviyo
  dynamic coupons, have to go in before those three send.
- **T09 prices come from the copy doc** and do not match Shopify list price.
  See open item 5b in `flows/nurturing-v4.md`.
- **T20's three product images are a guess.** The approved comp shipped three
  CategoryCard images without labelling which is Snuu, Easy Mode or Gummies;
  they are assigned here in the order the comp used them and must be checked.
- **T01's CTA points at the homepage.** The copy asks for the order confirmation
  page, but these flows trigger on `Ordered Product`, whose payload carries no
  `order_status_url`.
