"""The eight layout archetypes the client approved, as composable functions.

Each takes the copy for one email and returns the finished HTML. Every one of
the 22 templates in flows/nurturing-v4-emails.json is built from one of these —
see the mapping table in flows/nurturing-v4.md.

Copy in the approved comp is lorem ipsum; what was signed off is the system.
The words come from the client copy doc, not from here.
"""
import blocks as B
from shell import render

HERO_PLACEHOLDER = B.CDN + "65882579-a21a-4528-bf15-d8db23f999b9.jpeg"


def _tail(extra=None):
    return (extra or []) + [B.support_line(), B.footer()]


def welcome(title, preheader, eyebrow, h1, h1_italic, paras, cta=None, href=None,
            hero=None, hero_alt=""):
    rows = [B.header_logo_pill(), B.eyebrow_headline(eyebrow, h1, h1_italic)]
    if hero:
        rows.append(B.hero_inset(hero, hero_alt))
    rows.append(B.body("<br/><br/>".join(paras)))
    if cta:
        rows.append(B.cta_primary(cta, href))
    return render(title, preheader, rows + _tail())


def education_table(title, preheader, eyebrow, h1, h1_italic, intro,
                    panel=None, table_rows=None, bullets=None, closing=None,
                    cta=None, href=None, hero=None, hero_alt=""):
    rows = [B.header_logo_pill(), B.eyebrow_headline(eyebrow, h1, h1_italic)]
    if hero:
        rows.append(B.hero_inset(hero, hero_alt))
    rows.append(B.body(intro))
    if panel:
        rows.append(B.mint_panel(*panel))
    if table_rows:
        rows.append(B.spec_table(table_rows))
    if bullets:
        rows.append(B.bullet_list(bullets))
    if closing:
        rows.append(B.body(closing, top=30))
    if cta:
        rows.append(B.cta_primary(cta, href))
    return render(title, preheader, rows + _tail())


def explainer(title, preheader, eyebrow, h1, h1_italic, intro, items,
              closing=None, cta=None, href=None, outline=False,
              hero=None, hero_alt=""):
    rows = [B.header_logo_pill(), B.eyebrow_headline(eyebrow, h1, h1_italic)]
    if hero:
        rows.append(B.hero_inset(hero, hero_alt))
    rows += [B.body(intro), B.numbered_explainer(items)]
    if closing:
        rows.append(B.body(closing, top=6))
    if cta:
        rows.append((B.cta_outline if outline else B.cta_primary)(cta, href))
    return render(title, preheader, rows + _tail())


def founder_letter(title, preheader, paras, signoff="Cheers,", name="Isaac",
                   role="CEO, DrinkAid"):
    """No CTA button. The ask is a reply, and a button undoes that."""
    rows = [B.header_bar(), B.letter(paras, signoff, name, role)]
    return render(title, preheader, rows + _tail())


def nudge(title, preheader, eyebrow, h1, h1_italic, paras, cta=None, href=None,
          panel=None, closing=None, code=None, bullets=None):
    rows = [B.header_logo_pill(), B.eyebrow_headline(eyebrow, h1, h1_italic),
            B.body("<br/><br/>".join(paras))]
    if panel:
        rows.append(B.mint_panel(*panel))
    if bullets:
        rows.append(B.bullet_list(bullets))
    if code:
        rows.append(B.offer_code(*code))
    if cta:
        rows.append(B.cta_primary(cta, href))
    if closing:
        rows.append(B.body(closing, top=26))
    return render(title, preheader, rows + _tail())


def offer_compare(title, preheader, eyebrow, h1, h1_italic, intro, left, right,
                  closing=None, cta=None, href=None, code=None):
    rows = [B.header_logo_pill(), B.eyebrow_headline(eyebrow, h1, h1_italic),
            B.body(intro), B.offer_compare(left, right)]
    if code:
        rows.append(B.offer_code(*code))
    if closing:
        rows.append(B.body(closing, top=30))
    if cta:
        rows.append(B.cta_primary(cta, href))
    return render(title, preheader, rows + _tail())


def review_request(title, preheader, eyebrow, h1, h1_italic, paras, cta, href,
                   review=None, closing=None):
    rows = [B.header_logo_pill(), B.eyebrow_headline(eyebrow, h1, h1_italic),
            B.body("<br/><br/>".join(paras))]
    if review:
        rows.append(B.review_card(*review))
    rows.append(B.cta_primary(cta, href))
    if closing:
        rows.append(B.body(closing, top=26))
    return render(title, preheader, rows + _tail())


def range_crosssell(title, preheader, eyebrow, h1, h1_italic, intro, cards,
                    closing=None):
    rows = [B.header_logo_pill(), B.eyebrow_headline(eyebrow, h1, h1_italic), B.body(intro)]
    for c in cards:
        rows.append(B.category_card(**c))
    if closing:
        rows.append(B.body(closing, top=30))
    return render(title, preheader, rows + _tail())
