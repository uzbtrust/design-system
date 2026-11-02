#!/usr/bin/env python3
"""uzbtrust — dist/ fayllarini yig‘adi.

tokens.json            → dist/tokens.css   (CSS o‘zgaruvchilar, mavzular, type klasslari)
tokens.css + bundle.css → dist/uzbtrust.css (sahifaga ulanadigan bitta fayl)

Ishga tushirish (repo ildizidan):  python3 scripts/build.py
Faqat standart kutubxona ishlatiladi.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = ROOT / "tokens.json"
BUNDLE = ROOT / "components" / "bundle.css"
DIST = ROOT / "dist"

HEADER = "/* uzbtrust — generated from tokens.json */\n"


def css_value(value):
    """"{boshqa-token}" → var(--boshqa-token), qolgani o‘zgarishsiz."""
    m = re.fullmatch(r"\{(.+)\}", value)
    return f"var(--{m.group(1)})" if m else value


def theme_value(token, theme, first):
    value = token["value"]
    if isinstance(value, str):
        return value
    return value.get(theme, value.get(first))


def build_tokens_css(tokens):
    themes = [t["id"] for t in tokens["color"]["themes"]]
    first = themes[0]
    themed = tokens["color"]["tokens"] + tokens.get("shadow", {}).get("tokens", [])
    out = [HEADER]

    # Shrift fayllari dist/ dan bir pog‘ona yuqorida (fonts/) — yo‘l CSS fayliga nisbatan
    for font in tokens["type"].get("fonts", []):
        out.append(
            "@font-face {\n"
            f"  font-family: {font['family']};\n"
            f"  font-style: {font.get('style', 'normal')};\n"
            f"  font-weight: {font.get('weight', '400')};\n"
            "  font-display: swap;\n"
            f"  src: url(\"../{font['file']}\") format(\"woff2\");\n"
            "}\n"
        )

    for theme in themes:
        if theme == first:
            selector = f':root,\n[data-theme="{theme}"]'
        elif theme == "dark":
            selector = f'[data-theme="{theme}"],\n.dark'
        else:
            selector = f'[data-theme="{theme}"]'
        lines = [f"  --{t['name']}: {css_value(theme_value(t, theme, first))};" for t in themed]
        out.append(selector + " {\n" + "\n".join(lines) + "\n}\n")

    lines = []
    for family, body in tokens.items():
        if family in ("color", "shadow", "type") or not isinstance(body, dict) or "tokens" not in body:
            continue
        lines += [f"  --{t['name']}: {t['value']};" for t in body["tokens"]]
    lines += [f"  --font-{key}: {stack};" for key, stack in tokens["type"]["families"].items()]
    out.append(":root {\n" + "\n".join(lines) + "\n}\n")

    props = (("fontSize", "font-size"), ("lineHeight", "line-height"), ("fontWeight", "font-weight"),
             ("letterSpacing", "letter-spacing"), ("fontStyle", "font-style"))
    for group in tokens["type"]["groups"]:
        for style in group["styles"]:
            family = style.get("family", group.get("family", "sans"))
            decl = [f"  font-family: var(--font-{family});"]
            decl += [f"  {css}: {style[key]};" for key, css in props if key in style]
            out.append(f".{style['name']} {{\n" + "\n".join(decl) + "\n}\n")

    return "\n".join(out)


def main():
    tokens = json.loads(TOKENS.read_text(encoding="utf-8"))
    tokens_css = build_tokens_css(tokens)
    bundle = BUNDLE.read_text(encoding="utf-8")
    DIST.mkdir(exist_ok=True)
    (DIST / "tokens.css").write_text(tokens_css, encoding="utf-8")
    (DIST / "uzbtrust.css").write_text(tokens_css + "\n" + bundle, encoding="utf-8")
    print(f"dist/tokens.css   {len(tokens_css):>7} bayt")
    print(f"dist/uzbtrust.css {len(tokens_css) + len(bundle) + 1:>7} bayt")


if __name__ == "__main__":
    main()
