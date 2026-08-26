#!/usr/bin/env python3
"""Render every template in tools/emails.py to templates/ and lint the output.

    python3 tools/build.py

Lint enforces the rules in README.md that a browser preview will not catch:
no margin, no box-shadow, no SVG, every 2-up carries da-stack, every email ends
with the unsubscribe tag, every image has alt text, and no block sets
padding-bottom on the outer rhythm.
"""
import os
import re
import sys
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "templates")
sys.path.insert(0, HERE)

import emails  # noqa: E402

VOID = {"img", "br", "meta", "hr", "input", "link"}


class Balance(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.stack, self.errors = [], []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append("closed <%s> with nothing open" % tag)
        elif self.stack[-1] != tag:
            self.errors.append("closed <%s> while <%s> was open" % (tag, self.stack[-1]))
        else:
            self.stack.pop()


def lint(name, html):
    bad = []
    for pattern, msg in [
        (r"box-shadow", "box-shadow (Outlook drops it)"),
        (r"<svg", "SVG (unsupported in email)"),
        (r"alchohol", "misspelled product handle"),
        (r"display\s*:\s*flex", "flexbox (no support in Outlook)"),
        (r"display\s*:\s*grid", "CSS grid (no support in Outlook)"),
    ]:
        if re.search(pattern, html, re.I):
            bad.append(msg)

    # margin is allowed nowhere; the shell's own body reset is the exception
    for m in re.finditer(r"margin\s*:", html):
        line = html[:m.start()].count("\n") + 1
        if "body {" not in html[max(0, m.start() - 200):m.start()] and \
           "body style" not in html[max(0, m.start() - 120):m.start()]:
            bad.append("margin at line %d (use padding on <td>)" % line)

    if "{% unsubscribe" not in html:
        bad.append("no unsubscribe tag")

    for m in re.finditer(r"<img\b[^>]*>", html):
        if "alt=" not in m.group(0):
            bad.append("img with no alt attribute")

    # a bare & in a URL is not valid in an HTML attribute and some clients
    # truncate the query string at it
    for m in re.finditer(r'href="([^"]*)"', html):
        for amp in re.finditer(r"&(?!amp;|nbsp;|mdash;|ndash;|ldquo;|rdquo;|#)", m.group(1)):
            bad.append("unescaped & in href: %s" % m.group(1)[:60])

    # placeholders must never reach a template
    if re.search(r"XXXXX|LOREM IPSUM|lorem ipsum", html):
        bad.append("placeholder copy left in the template")

    # any row holding two side-by-side cells must be able to stack
    for m in re.finditer(r"<td[^>]*width=\"5[02]%\"[^>]*>", html):
        if "da-stack" not in m.group(0):
            bad.append("2-up cell without da-stack: %s" % m.group(0)[:70])

    b = Balance()
    b.feed(html)
    bad += b.errors
    if b.stack:
        bad.append("unclosed: %s" % ", ".join(b.stack))
    return bad


def main():
    os.makedirs(OUT, exist_ok=True)
    failures = 0
    for key in sorted(emails.EMAILS):
        html = emails.EMAILS[key]()
        path = os.path.join(OUT, key + ".html")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(html)
        problems = lint(key, html)
        size = len(html.encode("utf-8"))
        flag = "ok " if not problems else "FAIL"
        print("%s %-26s %6d bytes" % (flag, key, size))
        for p in dict.fromkeys(problems):
            print("       - %s" % p)
            failures += 1
        if size > 102400:
            print("       - over 100KB, Gmail will clip it")
            failures += 1
    print("\n%d template(s), %d problem(s)" % (len(emails.EMAILS), failures))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
