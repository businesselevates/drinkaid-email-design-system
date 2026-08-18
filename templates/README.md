# Templates

Worked examples composing `components/`. Each one is a real, send-ready email.

| File | Flow | Email | Ask |
|---|---|---|---|
| `a2-day2-umbrella.html` | Post-purchase nurture · Track A | A2 · Day 2 | none |

Copy source for the nurture flow: the client's Google Doc *DrinkAid Email
Nurturing Flow* (Track A / B / C). Copy in these templates is **verbatim** from
that doc. Where a word was added by the agency for the design — an eyebrow, a
panel label — it is flagged in a comment at the top of the file so Isaac and
Rachel can approve or kill it. Do not paraphrase doc copy: see `brief.md` §2.1.

---

## Archetype map — 34 emails, 8 layouts

The flow does not need 34 designs. Every email in Track A, B and C is one of
these eight, which is the "building blocks" approach the client asked for on
14 August. Approve the eight and the rest is assembly.

| # | Archetype | Blocks | Track A examples |
|---|---|---|---|
| 1 | Welcome / thank-you | 02 · 06 · 07 · 08 · 14 · 09 · 22 · 23 | A1 |
| 2 | **Educational + spec table** | 02 · 06 · 07 · 08 · 14 · **24** · 15 · 08 · 22 · 23 | **A2 ← built** |
| 3 | Long-form explainer | 02 · 07 · 08 · 15 (numbered) · 08 · 22 · 23 | A3, A9 |
| 4 | Founder letter, plain | 03 · 08 · 08 · 23 | A4 |
| 5 | Nudge + single CTA | 02 · 07 · 08 · 09 · 22 · 23 | A5, A9, A10 |
| 6 | Offer + price comparison | 02 · 07 · 08 · **24** · 09 · 18 · 22 · 23 | A6 |
| 7 | Review request | 02 · 07 · 08 · 17 · 09 · 22 · 23 | A7 |
| 8 | Range / cross-sell | 02 · 07 · 08 · 20 · 09 · 22 · 23 | A8 |

Block `24-spec-table` was added for this flow — archetypes 2 and 6 both need a
label/value table and the library had none.

---

## Open against the nurture flow

1. **Copy is still in review.** Rachel's comments on the doc are dated 18 August
   and all still open — including one calling A1's *"an order is not an
   abstraction here"* AI-sounding. Anything built off Track A copy may move.
2. **Product name.** Rachel: always "DrinkAid" in front — *DrinkAid Complete
   Alcohol Defence*, never "Complete Alcohol Defence" alone.
3. **Merge tag case.** The doc writes `{{ First_Name|default:'there' }}`;
   `brief.md` §11 and these templates use lowercase `first_name`, which is the
   standard Klaviyo attribute. Confirm against the account before import.
4. **A2 has no CTA** — that is the doc's decision (Ask = none), not an omission.
   The button style is shown in archetype 5.
