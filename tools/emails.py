# -*- coding: utf-8 -*-
"""The 22 unique templates, as copy specs.

Copy is transcribed from the client copy doc
(13KGYmRN0u21OpRSFJ4i89qDAZIAHzFx-t_aiX0wTvYQ). Do not rewrite it — Isaac wrote
it himself after rejecting an AI-written round, and paraphrasing is how that
happens again. Structural edits (which block holds which paragraph) are ours;
the words are not.

Keys match the `template` field in flows/nurturing-v4-emails.json.
"""
import archetypes as A
import blocks as B

HI = "Hi {{ first_name|default:'there' }},"
PRODUCT = B.PRODUCT
SHARING = B.SHARING_PACK
SCIENCE = "https://drinkaid.co/pages/science"
FIND_US = "https://drinkaid.co/pages/find-us"
HOME = "https://drinkaid.co"
# Klaviyo mints one unique code per profile at send time from a Shopify dynamic
# coupon of this name. The coupon itself is created in the Klaviyo UI
# (Content > Coupons) — the API cannot set a discount value or an expiry — so
# this tag renders empty until a coupon called exactly this exists.
COUPON_10 = "{% coupon_code 'PILLS_NURTURE_10OFF' %}"

# The Shopify order-status URL lives on Placed Order, not on Ordered Product,
# which is what these flows trigger on. The lookup therefore resolves only if
# this email is moved to a Placed Order trigger; the default keeps the button
# pointing somewhere real either way. See flows/nurturing-v4.md.
ORDER_CONFIRMATION = ("{{ event|lookup:'$extra'|lookup:'order_status_url'"
                      "|default:'https://drinkaid.co/account' }}")

JUDGEME = ("https://judge.me/product_reviews/b3577d33-2024-4571-ac24-28c5287508fe/"
           "new?id=6673927897220&amp;source=shareable-link")

# The comp shipped three CategoryCard images without saying which product each
# one is. Assignment below follows the order they appear in the comp and MUST be
# checked against the real Snuu / Easy Mode / Gummies shots before C11 ships.
IMG_SNUU = B.CDN + "aea45699-2473-42c7-9c79-758c48c2d87f.jpeg"
IMG_EASY_MODE = B.CDN + "93ae336c-c8c8-4585-96eb-f9fd2916365c.png"
IMG_GUMMIES = B.CDN + "6325be8b-636a-48ab-ba5f-5551e464b6c9.jpeg"

EMAILS = {}


EMAILS["T01-welcome"] = lambda: A.welcome(
    "Better mornings start here",
    "A proper thank you, from a small team in Singapore.",
    "BETTER MORNINGS", "Better mornings", "start here.",
    [HI,
     "Thank you for choosing DrinkAid.",
     "As we are a small business, your support means the world to us. Somebody sees it. "
     "Once yours ships, we will send the tracking link straight over.",
     "<b>First time with us?</b>",
     "Welcome to a growing community of 40,000+ people who decided they would rather not "
     "spend their Sundays recovering. Your liver is in good hands.",
     "<b>You are the reason DrinkAid exists.</b>",
     "Since 2020, we have sold over 2,000,000 doses across more than 30 countries, and "
     "almost none of that came from clever advertising.",
     "It came from people trying it, being surprised, and telling somebody else. That is a "
     "slower way to build a company and a much better one.",
     "A handful of emails over the next few weeks, and we will keep them worth opening. The "
     "next one is the one that actually matters: when to take DrinkAid, and why the timing "
     "does more work than anything else we could tell you.",
     "Cheers,<br/>Isaac"],
    "VIEW MY ORDER", ORDER_CONFIRMATION)


EMAILS["T02-umbrella"] = lambda: A.education_table(
    "What does DrinkAid have to do with an umbrella?",
    "Before your first drink. Here's exactly how to take DrinkAid.",
    "THE TIMING", "Open it before", "the rain.",
    HI + "<br/><br/>If you're taking DrinkAid, take it before you start drinking."
    "<br/><br/>The best time is 15&ndash;30 minutes before your first drink."
    "<br/><br/>Taking it before you drink means the ingredients are already in your system "
    "when you start drinking.",
    panel=("THE DOSE", "1 sachet = 2 capsules = 1 dose",
           "Take both capsules together. Each box contains 6 sachets, so you get 6 doses per box."),
    table_rows=[
        ("15&ndash;30 min before your first drink", "One sachet (both capsules)"),
        ("After a heavy drinking session", "One more sachet"),
        ("Forgot to take it earlier?", "Take one sachet now. Earlier is better, but late beats never"),
    ],
    bullets=[
        "<b>Eat before you drink.</b> Food can slow the absorption of alcohol into your bloodstream.",
        "<b>Drink water throughout the day.</b> Don't wait until you're at the bar to start hydrating.",
        "<b>Pace yourself.</b> Keep track of how much you're drinking and know your limit.",
        "<b>Get enough sleep.</b> Alcohol can disrupt your sleep, so giving yourself enough time to rest matters.",
    ],
    closing="That's it. No mixing. No measuring. No complicated routine.<br/><br/>"
            "Just <b>take your dose before you drink and get on with your night.</b><br/><br/>"
            "If you are looking to get one when you are outside, you can find DrinkAid at "
            "these locations.<br/><br/>Cheers,<br/>Isaac<br/>CEO, DrinkAid",
    cta="FIND DRINKAID NEAR ME", href=FIND_US)


EMAILS["T03-four-pathways"] = lambda: A.explainer(
    "Curious why DrinkAid works when the last product you've tried didn't?",
    "Most products focus on one part of drinking. DrinkAid takes a broader approach.",
    "THE FORMULA", "One formula,", "four pathways.",
    HI + "<br/><br/>Most hangover products focus on one thing."
    "<br/><br/>Usually, that's DHM, an ingredient that's been widely studied for alcohol "
    "metabolism.<br/><br/>DHM is part of DrinkAid too. But we didn't think one ingredient "
    "was enough.<br/><br/>A night of drinking affects your body in a few different ways:",
    [("Alcohol breakdown",
      "Your body turns alcohol into acetaldehyde as it processes it. DrinkAid includes DHM "
      "to support this process."),
     ("Antioxidant support",
      "Your body uses antioxidants while processing alcohol. That's why our formula includes "
      "ingredients to support your body's antioxidant systems."),
     ("Sleep",
      "Alcohol can affect sleep quality, even if you fall asleep quickly. DrinkAid includes "
      "ingredients selected to support recovery while you sleep."),
     ("Nutrient support",
      "Alcohol can also affect the nutrients your body uses. That's why we include B vitamins "
      "and other supporting ingredients.")],
    closing="That's <b>9 ingredients working together</b>, including <b>three ingredients in "
            "our proprietary Clear2x&trade; blend</b>, which has undergone testing at NUS and "
            "Temasek Polytechnic.<br/><br/>We also develop the formula ourselves rather than "
            "simply using an off-the-shelf OEM formula.<br/><br/>So why might DrinkAid work "
            "differently from the last product you tried?<br/><br/>Because we didn't build it "
            "around one ingredient. We built it around what actually happens when you drink."
            "<br/><br/>Cheers,<br/>Isaac<br/>CEO, DrinkAid")


EMAILS["T04-clinically-tested"] = lambda: A.explainer(
    'What "clinically tested" actually means',
    "We tested the finished formula, not just the ingredients.",
    "THE EVIDENCE", "Tested as sold,", "not as ingredients.",
    HI + '<br/><br/>You\'ve probably seen supplements described as <b>&ldquo;science-backed&rdquo;</b> '
    'or <b>&ldquo;clinically tested.&rdquo;</b><br/><br/>Sometimes, that means one or two '
    "ingredients in the formula have been studied.<br/><br/>That's useful. But it doesn't tell "
    "you what happens when you put all the ingredients together in the finished product."
    "<br/><br/>We wanted to know that too. So we took DrinkAid to NUS and Temasek Polytechnic "
    "and tested the formula and its key ingredients.",
    [("NUS tested the ingredients",
      "NUS tested four key DrinkAid ingredients. Three of them &mdash; DHM, Pyroglutamic Acid "
      "and S-Acetyl Glutathione &mdash; showed a statistically significant increase of roughly "
      "2&times; in ALDH2 gene expression after 24 hours. ALDH2 is one of the enzymes involved "
      "in breaking down acetaldehyde, the toxic byproduct produced when your body processes "
      "alcohol."),
     ("Temasek Polytechnic tested the finished formula",
      "This is where it gets more interesting. Temasek Polytechnic tested the complete DrinkAid "
      "formula, rather than looking at individual ingredients in isolation. The study found that "
      "DrinkAid increased ALDH2 activity, increased glutathione levels by around 2.6&times;, and "
      "reduced markers associated with liver stress.")],
    closing="So we have two different pieces of evidence. NUS looked at what key ingredients can "
            "do. Temasek Polytechnic tested what the finished formula does as a whole. That's the "
            "distinction we care about.<br/><br/>And while we're talking about formulation, we "
            "also chose to use S-Acetyl Glutathione rather than cheaper glutathione alternatives. "
            "It's significantly more expensive, but we chose it because of its bioavailability and "
            "role in the formula.<br/><br/>Nobody sees that decision on the front of the box. We "
            "made it anyway.<br/><br/>Cheers,<br/>Isaac<br/>CEO, DrinkAid",
    cta="READ THE RESEARCH", href=SCIENCE, outline=True)


EMAILS["T05-isaac-reply"] = lambda: A.founder_letter(
    "A quick note from Isaac",
    "Plain text, no marketing. I read every reply.",
    [HI.replace("Hi ", "Hi ").rstrip(","),
     "I'm Isaac, CEO of DrinkAid. You have had your order for a couple of weeks now, so I "
     "wanted to check in personally.",
     "How has it actually worked for you?",
     "I hope you have found yourself noticeably fresher the next morning than you would "
     "otherwise have been, more or less regardless of what the night looked like.",
     "One thing that tends to get lost behind all the hangover talk: DrinkAid is not only "
     "about Asian flush or a better Sunday.",
     "It is also about protecting your liver from alcohol-induced damage over the longer run. "
     "That is the part you don't feel immediately, and it is the reason this has been in my "
     "own routine for years now whenever I drink.",
     "There are just <b>two things I'd love to hear from you</b>.",
     "First, your honest feedback on your experience. Even if it's brutal. We want you to have "
     "the best time with DrinkAid. If there's anything we can do to improve, we'd love to hear "
     "from you directly, rather than read a frustrated review months later.",
     "Second, what would you like to know more about when it comes to DrinkAid? We'd love to "
     "make these emails as valuable as possible, so they are worth opening every time.",
     "When you're ready, just hit reply. I read every response personally."])


EMAILS["T06-review"] = lambda: A.review_request(
    "Are you still getting hungover?",
    "Genuinely asking. Plus a small favour.",
    "A SMALL FAVOUR", "Are you still", "getting hungover?",
    [HI,
     "Genuine question: <b>are you still getting hungover?</b> Or have you stopped losing half "
     "the next day to a night out?",
     "Either way, we'd love to hear how DrinkAid has been working for you.",
     "You might be wondering why we're asking. Reviews are how many of our 40,000+ customers "
     "found us in the first place. And the most useful reviews aren't always the five-star ones.",
     "<b>We'd rather have honest feedback than a perfect rating.</b>",
     "If something didn't work for you, tell us. If something surprised you, tell us that too.",
     "We actually read the reviews and use them to improve DrinkAid. Customer feedback even "
     "helped us identify problems with our Philippines logistics, which we've since fixed.",
     "So if you have a minute, we'd really appreciate hearing from you."],
    "SHARE YOUR EXPERIENCE", JUDGEME,
    closing="Cheers,<br/>Isaac<br/>CEO, DrinkAid")


EMAILS["T07-nights-we-built-for"] = lambda: A.nudge(
    "The nights we built DrinkAid for",
    "Nothing to sell today",
    "NO OFFER TODAY", "The nights we", "built this for.",
    [HI,
     "It started as a joke in a group chat, but it's become a pretty good reminder of who we're "
     "building DrinkAid for.",
     "The nights we built it for:"],
    bullets=[
        "The company D&amp;D where the boss orders another bottle for the table and saying no isn't really an option.",
        "The wedding banquet. Eight courses, and a yum seng at most of them.",
        "&ldquo;Just one drink&rdquo; at 7 pm. Kopi at 7 am.",
        "The client who's quietly testing whether you can keep up, and the 9 am meeting where they'll find out.",
        "The business trip where dinner is also the meeting.",
        "CNY, where turning down a drink becomes a negotiation with an auntie you're probably going to lose.",
        "The glass on the sofa after the kids are asleep. Not a big night. Still enough to affect tomorrow.",
    ],
    closing="None of these are problems we think need fixing. They're just part of life here."
            "<br/><br/>We're not here to tell you whether you should drink or not. Plenty of "
            "brands will happily do that. We just wanted to make something that helps you enjoy "
            "the night without giving up the next day.<br/><br/>That's all for today. No offer. "
            "No CTA. Just a reminder of why we built DrinkAid in the first place."
            "<br/><br/>Cheers,<br/>Isaac<br/>CEO, DrinkAid")


EMAILS["T08-A5-first-nudge"] = lambda: A.nudge(
    "What has DrinkAid actually changed?",
    "Three weeks in. How has your experience been?",
    "THREE WEEKS IN", "What has DrinkAid", "actually changed?",
    [HI,
     "Three weeks in.",
     "Genuine question: what has being hangover-free actually changed for you?",
     "Maybe it's enjoying the night without worrying about tomorrow. Being present the next day "
     "instead of feeling like you need the whole day to recover. Or simply having a normal weekend.",
     "You've now had a few weeks to see what DrinkAid can do for you.",
     "So, less philosophically: how's the drawer looking?",
     "A box of six can go faster than you'd think. A couple of dinners, a birthday, and a Friday "
     "night out can leave you with only a sachet or two.",
     "If you're running low, now's probably a good time to restock."],
    "RESTOCK MY SACHETS", PRODUCT,
    closing="If you're still stocked up, ignore this one. We'll check in again soon."
            "<br/><br/>Cheers,<br/>Isaac<br/>CEO, DrinkAid")


EMAILS["T09-A6-primary-offer"] = lambda: A.offer_compare(
    "Running low on DrinkAid?",
    "If it worked for you, there's a better way to stock up.",
    "TIME TO RESTOCK", "Running low", "on DrinkAid?",
    HI + "<br/><br/>When you bought your first pack, you probably weren't completely sure it "
    "would work.<br/><br/>Fair enough. There's a lot of marketing in the hangover category, and "
    "it's hard to know what actually makes a difference. Hopefully, DrinkAid surprised you."
    "<br/><br/>And if you're nearly through your first box, there's probably a simple reason:"
    "<br/><br/><b>Once you know it works for you, you stop saving it for special occasions.</b>"
    "<br/><br/>Dinner with friends. A few drinks after work. Friday night out. You take a sachet, "
    "wake up feeling good, and it becomes part of the routine.<br/><br/>So if you're ready to "
    "restock, here are the two recommended options for you:",
    left={"kicker": "OPTION ONE", "name": "3 Boxes", "price": "S$37.02",
          "detail": ["18 sachets", "S$2.06 per session", "Roughly 2&ndash;3 months of supply"],
          "cta": "CHOOSE THIS", "href": PRODUCT},
    right={"kicker": "OPTION TWO", "name": "Sharing Pack", "price": "S$59.80",
           "detail": ["30 sachets", "S$1.99 per session", "FREE SHIPPING"],
           "cta": "CHOOSE THIS", "href": SHARING},
    closing="Three boxes keeps you stocked for roughly 2&ndash;3 months, depending on how often "
            "you drink. If you're drinking a couple of times a week, the Sharing Pack probably "
            "makes more sense.<br/><br/>And despite the name, you don't actually have to share it. "
            "Some customers just like not having to worry about running out.",
    cta="GET THE SHARING PACK", href=SHARING)


EMAILS["T10-A8-showing-up"] = lambda: A.nudge(
    "Who are you showing up for today?",
    "The reason any of this exists.",
    "SHOW UP ANYWAY", "Who are you showing", "up for today?",
    [HI,
     "Beyond supplements where you can actually feel the difference, here's what we're actually selling.",
     "Not the absence of a hangover, calm focus, or good sleep. <b>The ability to show up anyway.</b>",
     "Life is relentless enough, and we could all use some support.",
     "Which is also why we've created more than one product. We've built supplements for those "
     "who show up for everything.",
     "<b>DrinkAid Complete Alcohol Defence</b>, the sachets you already have. The toxin, the "
     "antioxidants, the tank.",
     "<b>Snuu</b>, a sleep balm. Alcohol wrecks the back half of the night even when you get "
     "your eight hours, and no hangover formula fixes that, ours included. Apply on your skin; "
     "it works in about 20 minutes, no morning grogginess and no 4 am bathroom trip.",
     "<b>Easy Mode</b>, caffeine-free focus. We call it your cheat code to getting things done.",
     "Nothing you need to do today. But if one of those is your particular problem, it exists."],
    "EXPLORE THE RANGE", HOME,
    closing="Cheers,<br/>Isaac<br/>CEO, DrinkAid")


EMAILS["T11-A9-remember"] = lambda: A.nudge(
    "Remember when you first got hungover?",
    "The part you don't feel is worth thinking about too.",
    "THE PART YOU DON'T FEEL", "Remember when you", "used to get hungover?",
    [HI,
     "Remember your last hangover?",
     "The nausea. The headache that starts in the middle of the night. Waking up already knowing "
     "your whole day is going to be a write-off.",
     "Nobody misses that.",
     "But there's another part of drinking that you don't necessarily feel.",
     "Your body still has to process the alcohol long after your last drink.",
     "But what matters even more is how your liver responds every time you drink. It works "
     "overtime to clear a toxin 20&times; worse than alcohol itself.",
     "<b>DrinkAid was built to support and protect your liver.</b> It was never just about the "
     "hangover or the Asian flush.",
     "If you choose to drink, use DrinkAid. Anything else just isn't worth the risk."],
    "RESTOCK MY SACHETS", PRODUCT,
    closing="Cheers,<br/>Isaac<br/>CEO, DrinkAid")


EMAILS["T12-A10-exit"] = lambda: A.nudge(
    "Last one from us for a while",
    "Adults can make their own decisions",
    "LAST ONE FOR A WHILE", "Adults can make", "their own decisions.",
    [HI,
     "If you've stopped drinking altogether, we're genuinely happy for you. That's obviously the "
     "healthiest option, and we're not going to pretend otherwise.",
     "But if you do drink, there will always be a reason.",
     "Weddings. Birthdays. Anniversaries. Work dinners. Festive seasons. Or just Tuesday.",
     "So if you're going to drink, DrinkAid is an easy thing to keep in the drawer.",
     "And before we leave you alone for a while, <b>here's 10% off your next order.</b>"],
    "RESTOCK NOW", PRODUCT,
    code=(COUPON_10, "10% off your next order &mdash; expires in 7 days"),
    closing="With the Sharing Pack, each sachet already works out to under S$2 per drinking "
            "session. With 10% off, it's even less.<br/><br/>We'll leave you alone after this. "
            "See you whenever you need us.<br/><br/>P.S. The 10% code is just for this last "
            "restock reminder. Use it while it's available for the next 7 days.<br/><br/>"
            "Cheers,<br/>Isaac<br/>CEO, DrinkAid")


EMAILS["T13-B8-first-nudge"] = lambda: A.nudge(
    "How's the drawer looking?",
    "No pressure if not.",
    "TWO AND A HALF MONTHS IN", "A box of six goes", "quicker than it reads.",
    [HI,
     "Coming up on two and a half months, so this is worth a check.",
     "Six sachets sounds like a lot until you count how a normal month actually goes. Two client "
     "dinners, a birthday you had already agreed to, and the Friday that was not planned, and the "
     "box is open and nearly done.",
     "It is rarely because anyone is drinking more. It is that nights arrive unannounced. The "
     "D&amp;D that got moved up. The night-in to drink because work was a write-off.",
     "If you are near the end of the box, now is the easy time to sort it. If you are not, ignore "
     "this one completely, and we will talk later."],
    "RESTOCK MY SACHETS", PRODUCT,
    closing="Cheers,<br/>Isaac<br/>CEO, DrinkAid")


EMAILS["T14-B9-faq"] = lambda: A.explainer(
    "Straight answers, including the awkward ones",
    "Six questions, no marketing.",
    "STRAIGHT ANSWERS", "Six questions,", "no marketing.",
    HI + "<br/><br/>After 6 years and 40,000+ customers, we keep getting the same questions."
    "<br/><br/>So instead of sending you to the FAQ page, we thought we'd bring the answers to you.",
    [("&ldquo;Will DrinkAid stop my flush completely?&rdquo;",
      "Not necessarily. DrinkAid is designed to help your body clear acetaldehyde, which is one "
      "of the things that causes flushing. Some people see a significant reduction, while others "
      "see less of a difference. Everyone responds differently, so we won't promise that it will "
      "stop your flush completely."),
     ("&ldquo;Can I take it after drinking?&rdquo;",
      "You can, but we recommend taking it 15&ndash;30 minutes before your first drink. That's "
      "when you want the formula working before you start drinking."),
     ("&ldquo;Why is there less DHM in DrinkAid than some other brands?&rdquo;",
      "This is one of the biggest misconceptions in the category. More DHM isn't necessarily "
      "better. DHM has a bioavailability of only 4.02%, so after a certain point, simply adding "
      "more isn't the most effective way to build a formula. After a year of R&amp;D, we chose to "
      "dose DHM optimally and use the remaining formula space for other ingredients, including "
      "S-Acetyl Glutathione and Pyroglutamic Acid. The idea is to have the ingredients work "
      "together rather than relying on one ingredient."),
     ("&ldquo;Can I take more than one sachet?&rdquo;",
      "Yes. Take one sachet 15&ndash;30 minutes before your first drink. For a heavier session, "
      "you can take another sachet after your last drink."),
     ("&ldquo;Is DrinkAid safe to take regularly?&rdquo;",
      "DrinkAid is made with natural ingredients, is third-party tested, and is produced in a "
      "GMP-certified facility. As with any supplement, follow the recommended serving instructions."),
     ("&ldquo;Does DrinkAid let me drink more?&rdquo;",
      "No. DrinkAid isn't a free pass to drink more alcohol. It's designed to support your body "
      "while it processes alcohol. It doesn't change the fact that drinking too much is still "
      "drinking too much.")],
    closing="Still have a question? Hit reply. We read them.",
    cta="SHOP DRINKAID SACHETS", href=PRODUCT)


EMAILS["T15-B10-primary-offer"] = lambda: A.offer_compare(
    "It was never only for the big nights",
    "The maths nobody does before they buy",
    "THE MATHS", "It runs out faster", "than you'd think.",
    HI + "<br/><br/>Most people buy DrinkAid for the big nights.<br/><br/>The D&amp;D. The client "
    "dinner. The wedding. The Friday that was supposed to be one drink.<br/><br/>Then something "
    "usually changes. You start taking it for the smaller nights too.<br/><br/>Dinner with "
    "friends. Friday drinks. That glass of wine at home on a Tuesday.<br/><br/>Because once "
    "DrinkAid becomes part of your drinking routine, you stop saving it for special occasions."
    "<br/><br/>And that's when the maths changes. A box has 6 sachets. If you drink twice a week, "
    "that's around 8 sachets a month.",
    left={"kicker": "OPTION ONE", "name": "3 Boxes", "price": "18 sachets",
          "detail": ["Roughly 10 weeks", "at two sessions a week"],
          "cta": "CHOOSE THIS", "href": PRODUCT},
    right={"kicker": "OPTION TWO", "name": "Sharing Pack", "price": "S$59.80",
           "detail": ["30 sachets", "S$1.99 each, FREE SHIPPING",
                      "Roughly four months of supply"],
           "cta": "CHOOSE THIS", "href": SHARING},
    closing="So if you're drinking regularly, it makes sense to buy enough that you're not "
            "checking the drawer before every night out.",
    cta="SEE THE SHARING PACK", href=SHARING)


EMAILS["T16-B11-exit"] = lambda: A.nudge(
    "Go big once instead of reordering four times",
    "Last one from us for a while.",
    "LAST ONE FOR A WHILE", "Go big once instead of", "reordering four times.",
    [HI,
     "As the calendar fills up, so do the nights.",
     "More weddings. More company dinners. CNY. Year-end parties. And the occasional "
     "&ldquo;quick catch-up&rdquo; that turns into a full night out.",
     "If you're going to be drinking regularly over the next few months, the Sharing Pack is "
     "probably the one for you.",
     "<b>30 sachets for S$59.80, with FREE SHIPPING.</b>",
     "That's enough to keep you covered without having to think about reordering every few weeks.",
     "And if you already know the next few months are going to be particularly busy, you can "
     "double up: 2 Sharing Packs = 60 sachets for S$113.62.",
     "Before we leave you alone for a while, here's 10% off your next order."],
    "STOCK UP NOW", SHARING,
    code=(COUPON_10, "10% off your next order &mdash; expires in 7 days"),
    closing="If you only drink occasionally, stick with the smaller pack. We'd rather you buy "
            "what you'll actually use.<br/><br/>Otherwise, stock up now and forget about it for "
            "a while. That's it from us. We'll only be back when we have something worth sharing."
            "<br/><br/>Cheers,<br/>Isaac<br/>CEO, DrinkAid")


# Archetype 6 reused as a two-answer qualifier: the CTAs are replies, not
# purchases, so both go to mailto with the answer pre-filled as the subject.
EMAILS["T17-C5-qualifier"] = lambda: A.offer_compare(
    "Quick question, and it changes what we send you",
    "Two very different situations, and we can't tell which is yours.",
    "ONE QUESTION", "That was a big", "first order.",
    HI + "<br/><br/>Most first orders here are a box or two. Somebody testing whether a hangover "
    "product can possibly be real.<br/><br/>Yours was not that.<br/><br/>So before we keep sending "
    "you things, one question, because the honest answer changes what is actually useful to you."
    "<br/><br/><b>Is this for you, or is it for something?</b><br/><br/>Both are common, and they "
    "are completely different situations.",
    left={"kicker": "ANSWER ONE", "name": "For me", "price": "&nbsp;",
          "detail": ["Your calendar genuinely runs like that",
                     "We carry on as we are. There is a fair amount we only tell people at your end of things."],
          "cta": "FOR ME",
          "href": "mailto:hello@drinkaid.co?subject=For%20me"},
    right={"kicker": "ANSWER TWO", "name": "For an event", "price": "&nbsp;",
           "detail": ["A wedding, a company D&amp;D, a party, a big gift",
                      "We do a proper version of that rather than you buying retail boxes and hoping there are enough."],
           "cta": "FOR AN EVENT",
           "href": "mailto:hello@drinkaid.co?subject=For%20an%20event"},
    closing="DrinkAid Customs is custom-printed sachet sleeves. Your names on it, your company on "
            "it, whatever you want on it. We have done weddings, and we have done corporate nights "
            "for Unilever, Bain &amp; Co, Zouk, Mothership and Foodpanda.<br/><br/>It works for a "
            "fairly unglamorous reason: it is the only party favour anyone actually uses, and your "
            "guests remember it the next morning precisely because the morning went fine."
            "<br/><br/>Just hit reply and say &ldquo;for me&rdquo; or &ldquo;for an event&rdquo;. "
            "If it is an event, tell us roughly when and roughly how many, and we will come back "
            "with real numbers rather than a brochure.")


EMAILS["T18-C9-what-next"] = lambda: A.founder_letter(
    "What should we make next?",
    "You've told us what you like. Now tell us what's missing",
    [HI.rstrip(","),
     "We've spent the last few years making DrinkAid better.",
     "And honestly, a lot of the changes have come from customers telling us what they want.",
     "So now we're asking you directly: <b>what would you like to see from DrinkAid next?</b>",
     "Maybe it's a bigger pack, so you don't have to restock as often. Maybe it's a different "
     "format that's easier to take on the go. Maybe it's something completely new that we "
     "haven't thought of yet.",
     "Or maybe you think the product is already pretty good and you'd rather we leave it alone.",
     "We want to hear all of it.",
     "You can reply to this email and tell us. One sentence is enough.",
     "We read every reply, and we'll use the feedback to decide what we work on next. After all, "
     "you're the ones actually using DrinkAid.",
     "Thanks for being part of the journey."])


EMAILS["T19-C10-advocacy"] = lambda: A.nudge(
    "How most people find DrinkAid",
    "Usually, it's just one person telling another",
    "A SMALL FAVOUR", "How most people", "find DrinkAid.",
    [HI,
     "One small favour to ask from you.",
     "Most of our customers found DrinkAid because someone they knew recommended it.",
     "A friend handed them a sachet before a wedding. Someone dropped it into the group chat "
     "before a big night out. Or a colleague said, &ldquo;Try this before you drink.&rdquo;",
     "That's the kind of recommendation we like. Not because someone gets something out of it, "
     "but because they actually thought it would help.",
     "So if DrinkAid has become part of your drinking routine and you know someone who might "
     "find it useful, send them our way.",
     "<b>You don't need a code.</b> Just send them the link."],
    "SHARE DRINKAID", PRODUCT,
    closing="And thank you for being one of the people who helped us get here.")


EMAILS["T20-C11-range"] = lambda: A.range_crosssell(
    "What the sachet doesn't do",
    "Yes, this is a range email. It's also true.",
    "DIFFERENT JOBS", "What the sachet", "doesn't do.",
    HI + "<br/><br/>DrinkAid does what it's designed to do: support your body while it processes "
    "alcohol and help you feel better the next day.<br/><br/>But it doesn't fix everything.",
    [{"image": IMG_SNUU, "eyebrow": "SLEEP BALM", "name": "Snuu",
      "text": "You can still sleep badly. Alcohol can disrupt the second half of your sleep, even "
              "if you fall asleep quickly. A topical sleep balm designed to help you wind down "
              "without the grogginess associated with some oral sleep aids. We reformulated it "
              "after customers told us the first version wasn't quite right &mdash; the current "
              "version is the one we stand behind.",
      "cta": "SEE SNUU", "href": HOME},
     {"image": IMG_EASY_MODE, "eyebrow": "CAFFEINE-FREE FOCUS", "name": "Easy Mode",
      "text": "You can also still feel tired. Feeling less rough isn't necessarily the same as "
              "feeling sharp. Caffeine-free and formulated with theacrine and acetyl-L-carnitine "
              "to support alertness without adding more caffeine to your system.",
      "cta": "SEE EASY MODE", "href": HOME},
     {"image": IMG_GUMMIES, "eyebrow": "CHEWABLE", "name": "DrinkAid Gummies",
      "text": "And if you're caught without water, there's the same Clear2x&trade; formula in a "
              "chewable format that's easy to keep in your bag.",
      "cta": "SEE GUMMIES", "href": HOME}],
    closing="Different products, different jobs.<br/><br/>Cheers,<br/>Isaac<br/>CEO, DrinkAid")


EMAILS["T21-C12-first-nudge"] = lambda: A.nudge(
    "Five months in. How's the supply?",
    "First time we've mentioned it, and we'll be quick.",
    "FIVE MONTHS IN", "Even a big box", "ends.",
    [HI,
     "We have deliberately not mentioned restocking until now, because you bought enough that it "
     "would have been a silly thing to ask.",
     "But five months is about the point where even a large order starts looking thin, so: how is "
     "it going?",
     "If there is still plenty, ignore this entirely. You will not hear about it again for a while.",
     "If you are down to the last few sachets, it is worth sorting before the next thing lands on "
     "the calendar rather than the morning after you notice."],
    "RESTOCK MY SACHETS", PRODUCT)


EMAILS["T22-C13-primary-offer"] = lambda: A.nudge(
    "Same again?",
    "No pitch. Just the easy version.",
    "WHENEVER YOU'RE READY", "Same", "again?",
    [HI,
     "Coming up on six months, which is usually about when the drawer starts looking thin.",
     "One thing worth saying: you don't need to buy more than you actually need.",
     "Your first order was a guess. By now, you know how often you drink and how quickly you go "
     "through DrinkAid.",
     "So if you want the simple option:"],
    "REORDER WITH 10% OFF", SHARING,
    panel=("THE SIMPLE OPTION", "1 Sharing Pack. 30 sachets. S$59.80.",
           "That's S$1.99 per session and roughly four months of supply for most people."),
    code=(COUPON_10, "10% off &mdash; brings the Sharing Pack down to S$53.82"),
    closing="If you'd rather repeat exactly what you ordered last time, that's fine too. Same "
            "formula either way.<br/><br/>And if you're still well stocked, ignore this one "
            "completely. We'd much rather you buy when you actually need it than because an email "
            "turned up.<br/><br/>Cheers,<br/>Isaac<br/>CEO, DrinkAid")
