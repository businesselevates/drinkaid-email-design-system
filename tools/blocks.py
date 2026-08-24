"""Email-safe block builders.

Each function returns one or more <tr> rows for the 600px table in
components/_shell.html. The markup mirrors components/ exactly — if you change a
component, change it here too, and vice versa.

House rules that the builders enforce so callers cannot break them:
  - vertical rhythm is padding-top only, never padding-bottom
  - no margin, no box-shadow, no SVG
  - anything 2-up carries class="da-stack"
"""

FONT = "'Poppins','Segoe UI',Helvetica,Arial,sans-serif"
FOREST, CREAM, MINT, LIME = "#08230F", "#F1F0E7", "#CCFFD9", "#9AFF1A"
MUTED, HAIRLINE, WHITE = "#5A6B5E", "#DCDCD2", "#FFFFFF"
CDN = "https://d3k81ch9hvuctc.cloudfront.net/company/VagrHA/images/"
LOGO = CDN + "8dbd6bfe-5f24-4f5d-910f-efb8c527f5b6.png"
STARS = CDN + "8b43610a-398f-4c58-8d64-b1a33b9e42da.png"
# Flat forest social set, lifted from the approved comp and uploaded to Klaviyo.
# The comp explicitly hides the design system's own 2-icon row and puts this
# 4-icon row in its place — see flows/nurturing-v4.md.
SOCIAL = [
    ("Facebook",  "https://www.facebook.com/drinkaid.co",     CDN + "7dea48e8-1577-4103-a621-b7fa7e535420.png"),
    ("Instagram", "https://www.instagram.com/drinkaid.co",    CDN + "e80dc936-31d2-4369-8939-f7694a6cde1b.png"),
    ("TikTok",    "https://www.tiktok.com/@drinkaid.co",      CDN + "20781481-a9f2-400c-9ed7-85164df7fcdf.png"),
    ("LinkedIn",  "https://www.linkedin.com/company/drinkaid", CDN + "f957394c-40d4-4148-a2b3-b8ed1cb999a8.png"),
]
PRODUCT = "https://drinkaid.co/products/complete-alcohol-defence"
SHARING_PACK = PRODUCT + "?variant=51911310508164"


def header_logo_pill():
    return f"""<tr>
  <td align="center" style="padding:28px 20px 0 20px;">
    <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr>
      <td align="center" bgcolor="{FOREST}" style="background-color:{FOREST}; border-radius:999px; padding:16px 34px;">
        <a href="https://drinkaid.co" target="_blank" style="text-decoration:none;"><img src="{LOGO}" width="180" alt="DrinkAid" style="display:block; width:180px; height:auto; border:0;"/></a>
      </td>
    </tr></table>
  </td>
</tr>"""


def header_bar():
    return f"""<tr>
  <td align="center" bgcolor="{FOREST}" style="background-color:{FOREST}; padding:22px 20px;">
    <a href="https://drinkaid.co" target="_blank" style="text-decoration:none;"><img src="{LOGO}" width="180" alt="DrinkAid" style="display:block; width:180px; height:auto; border:0;"/></a>
  </td>
</tr>"""


def eyebrow_headline(eyebrow, line1, line2_italic=None):
    head = line1 if not line2_italic else f'{line1}<br/><em style="font-style:italic;">{line2_italic}</em>'
    return f"""<tr>
  <td align="center" class="da-gut" style="padding:34px 40px 0 40px; font-family:{FONT}; font-size:13px; line-height:18px; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:{FOREST};">{eyebrow}</td>
</tr>
<tr>
  <td align="center" class="da-h1 da-gut" style="padding:12px 40px 0 40px; font-family:{FONT}; font-size:38px; line-height:44px; font-weight:800; color:{FOREST};">{head}</td>
</tr>"""


def body(html, align="center", top=20):
    cls = "da-body da-gut"
    return f"""<tr>
  <td align="{align}" class="{cls}" style="padding:{top}px 48px 0 48px; font-family:{FONT}; font-size:19px; line-height:30px; font-weight:400; color:{FOREST};">{html}</td>
</tr>"""


def hero_inset(src, alt):
    return f"""<tr>
  <td align="center" class="da-gut" style="padding:28px 40px 0 40px;">
    <img src="{src}" width="520" alt="{alt}" style="display:block; width:100%; max-width:520px; height:auto; border:0; border-radius:16px;"/>
  </td>
</tr>"""


def cta_primary(label, href):
    return f"""<tr>
  <td align="center" class="da-btn" style="padding:30px 40px 0 40px;">
    <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr>
      <td align="center" bgcolor="{FOREST}" style="background-color:{FOREST}; border-radius:999px;">
        <a href="{href}" target="_blank" style="display:inline-block; padding:18px 44px; font-family:{FONT}; font-size:17px; line-height:22px; font-weight:800; letter-spacing:0.5px; text-transform:uppercase; color:{LIME}; text-decoration:none; border-radius:999px;">{label}</a>
      </td>
    </tr></table>
  </td>
</tr>"""


def cta_outline(label, href):
    return f"""<tr>
  <td align="center" class="da-btn" style="padding:22px 40px 0 40px;">
    <table role="presentation" border="0" cellpadding="0" cellspacing="0">
      <tr>
        <td align="center" bgcolor="{WHITE}" style="background-color:{WHITE}; border:2px solid {FOREST}; border-radius:999px;">
          <a href="{href}" target="_blank" style="display:inline-block; padding:17px 42px; font-family:{FONT}; font-size:16px; line-height:21px; font-weight:800; letter-spacing:0.5px; text-transform:uppercase; color:{FOREST}; text-decoration:none; border-radius:999px;">{label}</a>
        </td>
      </tr>
      <tr><td style="padding:0 6px;">
        <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
          <tr><td height="4" bgcolor="{LIME}" style="background-color:{LIME}; font-size:0; line-height:0; border-radius:0 0 999px 999px;">&nbsp;</td></tr>
        </table>
      </td></tr>
    </table>
  </td>
</tr>"""


def mint_panel(eyebrow, heading, text):
    return f"""<tr>
  <td align="center" class="da-gut" style="padding:30px 40px 0 40px;">
    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" bgcolor="{MINT}" style="background-color:{MINT}; border-radius:20px;">
      <tr><td align="center" style="padding:28px 28px 0 28px; font-family:{FONT}; font-size:13px; line-height:18px; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:{FOREST};">{eyebrow}</td></tr>
      <tr><td align="center" class="da-h2" style="padding:10px 28px 0 28px; font-family:{FONT}; font-size:28px; line-height:36px; font-weight:800; color:{FOREST};">{heading}</td></tr>
      <tr><td align="center" style="padding:12px 28px 28px 28px; font-family:{FONT}; font-size:17px; line-height:27px; color:{FOREST};">{text}</td></tr>
    </table>
  </td>
</tr>"""


def bullet_list(items):
    """Marker is the comp's 8px lime dot, not an icon image.

    border-radius is ignored by Outlook's Word engine, so the dot degrades to an
    8px lime square there. That is deliberate: a bgcolor cell stays visible with
    images turned off, which an image marker would not.
    """
    rows = []
    for i, text in enumerate(items):
        pad = "0" if i == len(items) - 1 else "14px"
        rows.append(f"""      <tr>
        <td width="30" valign="top" style="padding:5px 12px {pad} 0;">
          <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="8">
            <tr><td height="8" bgcolor="{LIME}" style="background-color:{LIME}; width:8px; height:8px; border-radius:999px; font-size:0; line-height:0;">&nbsp;</td></tr>
          </table>
        </td>
        <td valign="top" style="padding:0 0 {pad} 0; font-family:{FONT}; font-size:17px; line-height:26px; color:{FOREST};">{text}</td>
      </tr>""")
    return f"""<tr>
  <td align="left" class="da-gut" style="padding:30px 48px 0 48px;">
    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
{chr(10).join(rows)}
    </table>
  </td>
</tr>"""


def spec_table(rows):
    out = []
    for i, (label, value) in enumerate(rows):
        border = "" if i == len(rows) - 1 else f" border-bottom:1px solid {HAIRLINE};"
        out.append(f"""          <tr>
            <td class="da-stack" width="34%" valign="top" style="width:34%; padding:18px 16px 18px 0;{border} font-family:{FONT}; font-size:13px; line-height:19px; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; color:{FOREST};">{label}</td>
            <td class="da-stack" valign="top" style="padding:18px 0;{border} font-family:{FONT}; font-size:16px; line-height:24px; color:{FOREST};">{value}</td>
          </tr>""")
    return f"""<tr>
  <td align="center" class="da-gut" style="padding:30px 40px 0 40px;">
    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" bgcolor="{CREAM}" style="background-color:{CREAM}; border-radius:20px;">
      <tr><td style="padding:6px 28px;">
        <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
{chr(10).join(out)}
        </table>
      </td></tr>
    </table>
  </td>
</tr>"""


def numbered_explainer(items):
    out = []
    for i, (heading, text) in enumerate(items, 1):
        pad = "0" if i == len(items) else "26px"
        out.append(f"""      <tr>
        <td width="58" valign="top" style="padding:0 18px {pad} 0;">
          <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="40">
            <tr><td align="center" height="40" bgcolor="{FOREST}" style="background-color:{FOREST}; border-radius:999px; width:40px; height:40px; font-family:{FONT}; font-size:16px; line-height:40px; font-weight:800; color:{LIME};">{i}</td></tr>
          </table>
        </td>
        <td valign="top" style="padding:0 0 {pad} 0;">
          <div style="font-family:{FONT}; font-size:19px; line-height:26px; font-weight:700; color:{FOREST};">{heading}</div>
          <div style="font-family:{FONT}; font-size:16px; line-height:25px; color:{FOREST}; padding-top:4px;">{text}</div>
        </td>
      </tr>""")
    return f"""<tr>
  <td align="left" class="da-gut" style="padding:34px 48px 0 48px;">
    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
{chr(10).join(out)}
    </table>
  </td>
</tr>"""


def letter(paragraphs, signoff="Cheers,", name="Isaac", title="CEO, DrinkAid"):
    """One <tr> per paragraph. The comp used <p style="margin:...">, but Outlook
    drops margin, so the spacing is rebuilt as padding-top per row."""
    rows = []
    for i, p in enumerate(paragraphs):
        top = 34 if i == 0 else 20
        rows.append(f"""<tr>
  <td align="left" class="da-body da-gut" style="padding:{top}px 48px 0 48px; font-family:{FONT}; font-size:19px; line-height:30px; font-weight:400; color:{FOREST};">{p}</td>
</tr>""")
    rows.append(f"""<tr>
  <td align="left" class="da-body da-gut" style="padding:20px 48px 0 48px; font-family:{FONT}; font-size:19px; line-height:30px; font-weight:400; color:{FOREST};">{signoff}<br/>{name}<br/><span style="font-size:15px; line-height:22px; color:{MUTED};">{title}</span></td>
</tr>""")
    return "\n".join(rows)


def offer_compare(left, right):
    """left / right are dicts: kicker, name, price, detail, cta, href."""
    def lines(detail):
        return "<br/><br/>".join(detail)
    return f"""<tr>
  <td align="center" class="da-gut" style="padding:30px 40px 0 40px;">
    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
      <tr>
        <td class="da-stack" width="50%" valign="top" style="width:50%; padding-right:8px;">
          <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" bgcolor="{CREAM}" style="background-color:{CREAM}; border-radius:20px;">
            <tr><td align="center" style="padding:24px 20px 0 20px; font-family:{FONT}; font-size:12px; line-height:16px; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; color:{MUTED};">{left['kicker']}</td></tr>
            <tr><td align="center" style="padding:6px 20px 0 20px; font-family:{FONT}; font-size:22px; line-height:28px; font-weight:800; color:{FOREST};">{left['name']}</td></tr>
            <tr><td align="center" style="padding:2px 20px 0 20px; font-family:{FONT}; font-size:15px; line-height:22px; color:{MUTED};">{left['price']}</td></tr>
            <tr><td align="center" style="padding:16px 20px 0 20px; font-family:{FONT}; font-size:14px; line-height:20px; color:{FOREST};">{lines(left['detail'])}</td></tr>
            <tr><td align="center" style="padding:14px 20px 24px 20px;">
              <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr>
                <td align="center" bgcolor="{CREAM}" style="background-color:{CREAM}; border:2px solid {FOREST}; border-radius:999px;">
                  <a href="{left['href']}" target="_blank" style="display:inline-block; padding:13px 26px; font-family:{FONT}; font-size:14px; line-height:19px; font-weight:800; letter-spacing:0.5px; text-transform:uppercase; color:{FOREST}; text-decoration:none; border-radius:999px;">{left['cta']}</a>
                </td>
              </tr></table>
            </td></tr>
          </table>
        </td>
        <td class="da-stack da-stack-2" width="50%" valign="top" style="width:50%; padding-left:8px;">
          <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" bgcolor="{MINT}" style="background-color:{MINT}; border-radius:20px;">
            <tr><td align="center" style="padding:24px 20px 0 20px; font-family:{FONT}; font-size:12px; line-height:16px; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; color:{FOREST};">{right['kicker']}</td></tr>
            <tr><td align="center" style="padding:6px 20px 0 20px; font-family:{FONT}; font-size:22px; line-height:28px; font-weight:800; color:{FOREST};">{right['name']}</td></tr>
            <tr><td align="center" style="padding:2px 20px 0 20px; font-family:{FONT}; font-size:15px; line-height:22px; color:{FOREST};">{right['price']}</td></tr>
            <tr><td align="center" style="padding:16px 20px 0 20px; font-family:{FONT}; font-size:14px; line-height:20px; color:{FOREST};">{lines(right['detail'])}</td></tr>
            <tr><td align="center" style="padding:14px 20px 24px 20px;">
              <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr>
                <td align="center" bgcolor="{FOREST}" style="background-color:{FOREST}; border-radius:999px;">
                  <a href="{right['href']}" target="_blank" style="display:inline-block; padding:15px 28px; font-family:{FONT}; font-size:14px; line-height:19px; font-weight:800; letter-spacing:0.5px; text-transform:uppercase; color:{LIME}; text-decoration:none; border-radius:999px;">{right['cta']}</a>
                </td>
              </tr></table>
            </td></tr>
          </table>
        </td>
      </tr>
    </table>
  </td>
</tr>"""


def review_card(quote, text, attribution):
    return f"""<tr>
  <td align="center" class="da-gut" style="padding:30px 40px 0 40px;">
    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="border:1px solid {HAIRLINE}; border-radius:20px;">
      <tr><td align="center" style="padding:28px 28px 0 28px;"><img src="{STARS}" width="92" alt="Five stars" style="display:block; width:92px; height:auto; border:0;"/></td></tr>
      <tr><td align="center" style="padding:16px 28px 0 28px; font-family:{FONT}; font-size:20px; line-height:30px; font-weight:700; color:{FOREST};">&ldquo;{quote}&rdquo;</td></tr>
      <tr><td align="center" style="padding:10px 28px 0 28px; font-family:{FONT}; font-size:16px; line-height:26px; color:{FOREST};">{text}</td></tr>
      <tr><td align="center" style="padding:14px 28px 28px 28px; font-family:{FONT}; font-size:12px; line-height:16px; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:{MUTED};">&mdash; {attribution}</td></tr>
    </table>
  </td>
</tr>"""


def category_card(image, eyebrow, name, text, cta, href):
    return f"""<tr>
  <td align="center" class="da-gut" style="padding:30px 40px 0 40px;">
    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" bgcolor="{CREAM}" style="background-color:{CREAM}; border-radius:20px;">
      <tr><td style="padding:0; font-size:0; line-height:0;"><img src="{image}" width="520" alt="{name}" style="display:block; width:100%; max-width:520px; height:auto; border:0; border-radius:20px 20px 0 0;"/></td></tr>
      <tr><td align="center" style="padding:22px 28px 0 28px; font-family:{FONT}; font-size:12px; line-height:16px; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:{FOREST};">{eyebrow}</td></tr>
      <tr><td align="center" style="padding:8px 28px 0 28px; font-family:{FONT}; font-size:26px; line-height:32px; font-weight:800; color:{FOREST};">{name}</td></tr>
      <tr><td align="center" style="padding:10px 28px 0 28px; font-family:{FONT}; font-size:16px; line-height:25px; color:{FOREST};">{text}</td></tr>
      <tr><td align="center" style="padding:20px 28px 28px 28px;">
        <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr>
          <td align="center" bgcolor="{FOREST}" style="background-color:{FOREST}; border-radius:999px;">
            <a href="{href}" target="_blank" style="display:inline-block; padding:14px 32px; font-family:{FONT}; font-size:14px; line-height:19px; font-weight:800; letter-spacing:0.5px; text-transform:uppercase; color:{LIME}; text-decoration:none; border-radius:999px;">{cta}</a>
          </td>
        </tr></table>
      </td></tr>
    </table>
  </td>
</tr>"""


def offer_code(code, caption):
    return f"""<tr>
  <td align="center" class="da-gut" style="padding:30px 40px 0 40px;">
    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" bgcolor="{CREAM}" style="background-color:{CREAM}; border:2px dashed {FOREST}; border-radius:16px;">
      <tr><td align="center" style="padding:26px 24px 0 24px; font-family:{FONT}; font-size:13px; line-height:18px; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:{FOREST};">USE CODE</td></tr>
      <tr><td align="center" style="padding:8px 24px 0 24px;"><span style="display:inline-block; background-color:{LIME}; border-radius:8px; padding:6px 16px; font-family:{FONT}; font-size:32px; line-height:40px; font-weight:800; letter-spacing:1px; color:{FOREST};">{code}</span></td></tr>
      <tr><td align="center" style="padding:10px 24px 26px 24px; font-family:{FONT}; font-size:16px; line-height:24px; color:{FOREST};">{caption}</td></tr>
    </table>
  </td>
</tr>"""


def support_line():
    return f"""<tr>
  <td align="center" class="da-gut" style="padding:34px 48px 0 48px; font-family:{FONT}; font-size:14px; line-height:22px; color:{MUTED};">
    Got questions? Check our <a href="https://drinkaid.co" target="_blank" style="color:{FOREST}; text-decoration:underline;">FAQs</a> or just reply to this email &mdash; a human reads it.
  </td>
</tr>"""


def footer():
    """LOCKED. Carries {% unsubscribe %}, which the approved comp omits and which
    is a legal requirement, so it ships whether or not the comp shows it.

    The social row is the comp's 4-icon flat forest set at 22px. The design
    system's own 2-icon row is NOT shipped — the comp hides it.
    """
    icons = "\n".join(
        f"""      <td style="padding:0 9px;"><a href="{href}" target="_blank"><img src="{src}" width="22" alt="{label}" style="display:block; width:22px; height:22px; border:0;"/></a></td>"""
        for label, href, src in SOCIAL
    )
    return f"""<tr><td style="padding:0 0 40px 0; font-size:0; line-height:0;">&nbsp;</td></tr>

<tr>
  <td align="center" style="padding:0 30px 0 30px;">
    <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr>
      <td style="padding:0 9px; font-family:{FONT}; font-size:14px; line-height:20px; font-weight:700; color:{FOREST};"><a href="https://drinkaid.co" target="_blank" style="color:{FOREST}; text-decoration:none;">www.drinkaid.co</a></td>
{icons}
      <td style="padding:0 9px; font-family:{FONT}; font-size:14px; line-height:20px; font-weight:700; color:{FOREST};"><a href="https://www.instagram.com/drinkaid.co" target="_blank" style="color:{FOREST}; text-decoration:none;">@drinkaid.co</a></td>
    </tr></table>
  </td>
</tr>

<tr>
  <td style="padding:24px 0 0 0;">
    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" bgcolor="{MINT}" style="background-color:{MINT};">
      <tr><td align="center" style="padding:20px 24px;">
        <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%"><tr>
          <td align="left" class="da-stack" valign="middle" width="52%" style="width:52%;">
            <img src="{STARS}" width="88" alt="Five stars" style="display:block; width:88px; height:auto; border:0;"/>
            <div style="font-family:{FONT}; font-size:22px; line-height:26px; font-weight:800; color:{FOREST}; padding-top:4px;">2,000,000+</div>
            <div style="font-family:{FONT}; font-size:11px; line-height:14px; font-weight:700; letter-spacing:0.3px; text-transform:uppercase; color:{FOREST};">Mornings saved from hangovers</div>
          </td>
          <td align="left" class="da-stack da-stack-2" valign="middle" width="48%" style="width:48%;">
            <div style="font-family:{FONT}; font-size:12px; line-height:16px; font-weight:700; text-transform:uppercase; color:{FOREST};">Product of Singapore.</div>
            <div style="font-family:{FONT}; font-size:11px; line-height:15px; color:{FOREST}; padding-top:2px;">Modular Wellness Pte. Ltd.<br/>3 Lorong Bakar Batu, #03-03, Singapore 348741</div>
          </td>
        </tr></table>
      </td></tr>
    </table>
  </td>
</tr>

<tr>
  <td align="center" class="da-gut" style="padding:18px 40px 30px 40px; font-family:{FONT}; font-size:11px; line-height:16px; color:{MUTED};">
    No longer want to receive these emails? {{% unsubscribe 'Unsubscribe' %}}
  </td>
</tr>"""
