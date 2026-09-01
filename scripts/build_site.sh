#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST="$ROOT/dist"
VENV="$ROOT/.public-build-venv"

export PUBLIC_SITE_URL="${PUBLIC_SITE_URL:-}"
export COMMIT_SHA="${COMMIT_SHA:-local}"

required=(
  "index.html"
  "scripts/generate_public_assets.py"
  "assets/site.css"
  "assets/site.js"
  "assets/reference/tierneys-exterior-montclair-girl.jpg"
  "assets/reference/buddy-burger-mike-eats-nyc-burgers.jpg"
  "assets/reference/classic-cheeseburger-mike-eats-nyc-burgers.jpg"
  "assets/reference/upstairs-performance-bizzboard.jpg"
  "assets/reference/tierney-family-northjersey.jpg"
  "assets/reference/guinness-mural-mike-eats-nyc-burgers.jpg"
)

for relative in "${required[@]}"; do
  file="$ROOT/$relative"
  if [[ ! -s "$file" ]]; then
    printf 'Missing or empty required public-build file: %s\n' "$relative" >&2
    exit 1
  fi
done

rm -rf "$DIST" "$VENV"
mkdir -p "$DIST/assets"
cp "$ROOT/index.html" "$DIST/index.html"
cp "$ROOT/assets/site.css" "$DIST/assets/site.css"
cp "$ROOT/assets/site.js" "$DIST/assets/site.js"

if python3 -c 'import PIL' >/dev/null 2>&1; then
  python3 "$ROOT/scripts/generate_public_assets.py" "$ROOT" "$DIST"
else
  python3 -m venv "$VENV"
  "$VENV/bin/python" -m pip install --disable-pip-version-check --quiet "Pillow==12.3.0"
  "$VENV/bin/python" "$ROOT/scripts/generate_public_assets.py" "$ROOT" "$DIST"
  rm -rf "$VENV"
fi

# GitHub Pages receives a prebuilt static artifact; prevent an unintended Jekyll pass.
touch "$DIST/.nojekyll"

cat > "$DIST/robots.txt" <<'ROBOTS'
User-agent: *
Disallow: /
ROBOTS

if [[ -n "$PUBLIC_SITE_URL" ]]; then
  HOME_HREF="${PUBLIC_SITE_URL%/}/"
else
  HOME_HREF="./"
fi

cat > "$DIST/404.html" <<HTML
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="robots" content="noindex,nofollow,noarchive">
  <meta name="theme-color" content="#050806">
  <title>Page not found // Tierney's concept</title>
  <style>
    :root{color-scheme:dark}*{box-sizing:border-box}body{margin:0;min-height:100svh;display:grid;place-items:center;background:#050806;color:#f2eddf;font-family:system-ui,sans-serif;padding:1.25rem}main{width:min(760px,100%);border:1px solid rgba(98,255,157,.34);padding:clamp(1.5rem,6vw,4rem);background:radial-gradient(circle at 85% 10%,rgba(13,81,52,.35),transparent 38%)}small{color:#62ff9d;letter-spacing:.12em;text-transform:uppercase;font-family:ui-monospace,monospace}h1{font-size:clamp(3rem,12vw,8rem);line-height:.85;letter-spacing:-.07em;margin:1.4rem 0}p{color:#a9b3ad;line-height:1.7;max-width:56ch}a{display:inline-block;margin-top:1.5rem;padding:.8rem 1rem;background:#62ff9d;color:#050806;text-decoration:none;font-weight:750;text-transform:uppercase;letter-spacing:.08em;font-size:.75rem}
  </style>
</head>
<body><main><small>Error 404 // signal absent</small><h1>NOT<br>FOUND.</h1><p>This route is not part of the Tierney's Tavern concept.</p><a href="$HOME_HREF">Return home →</a></main></body>
</html>
HTML

python3 - "$DIST" <<'PY'
from html.parser import HTMLParser
from pathlib import Path
from PIL import Image
import json
import os
import sys

class Parser(HTMLParser):
    pass

root = Path(sys.argv[1])
index = root / "index.html"
source = index.read_text(encoding="utf-8")
public_url = os.environ.get("PUBLIC_SITE_URL", "").strip().rstrip("/")

if public_url:
    social_url = f"{public_url}/assets/public/tierneys-social-card.jpg"
    source = source.replace(
        'content="assets/public/tierneys-social-card.jpg"',
        f'content="{social_url}"',
    )
    source = source.replace(
        "  <title>Tierney's Tavern // Where Friends Meet</title>",
        "  <title>Tierney's Tavern // Where Friends Meet</title>\n"
        f'  <link rel="canonical" href="{public_url}/">\n'
        f'  <meta property="og:url" content="{public_url}/">',
    )
    index.write_text(source, encoding="utf-8")

for forbidden in (
    "RESEARCH BEFORE RENDER",
    "REAL ASSET BOARD",
    "<svg class=\"burger\"",
    "Stylized stacked burger illustration",
    "WEBSITE_DESIGN_PLAN.md",
    "ASSET_MANIFEST.md",
):
    if forbidden.lower() in source.lower():
        raise SystemExit(f"Public index contains forbidden dossier or stand-in content: {forbidden}")

for required_text in (
    "assets/images/exterior-hero.webp",
    "assets/images/buddy-burger.webp",
    "assets/images/upstairs-performance.webp",
    "assets/images/family-behind-bar.webp",
    "Price provenance:",
    "February 2014",
):
    if required_text not in source:
        raise SystemExit(f"Public index is missing required real-photo/menu content: {required_text}")

for page in (index, root / "404.html"):
    parser = Parser()
    parser.feed(page.read_text(encoding="utf-8"))

expected = {
    "assets/images/exterior-hero.jpg": (1600, 1200),
    "assets/images/exterior-hero.webp": (1600, 1200),
    "assets/images/buddy-burger.jpg": (1200, 1200),
    "assets/images/buddy-burger.webp": (1200, 1200),
    "assets/images/classic-cheeseburger.jpg": (1200, 1200),
    "assets/images/classic-cheeseburger.webp": (1200, 1200),
    "assets/images/upstairs-performance.jpg": (1400, 1050),
    "assets/images/upstairs-performance.webp": (1400, 1050),
    "assets/images/family-behind-bar.jpg": (1400, 933),
    "assets/images/family-behind-bar.webp": (1400, 933),
    "assets/images/mural-stairs.jpg": (1200, 1200),
    "assets/images/mural-stairs.webp": (1200, 1200),
    "assets/public/tierneys-social-card.jpg": (1200, 630),
}
for relative, dimensions in expected.items():
    path = root / relative
    if not path.is_file() or path.stat().st_size == 0:
        raise SystemExit(f"Missing generated public image: {relative}")
    with Image.open(path) as image:
        if image.size != dimensions:
            raise SystemExit(f"Unexpected dimensions for {relative}: {image.size}")

meta = {
    "project": "Tierney's Tavern real-photo mobile outreach concept",
    "venue": "138 Valley Road, Montclair, NJ 07042",
    "coordinates": [40.822509225043, -74.219748973846],
    "source_commit": os.environ.get("COMMIT_SHA", "local"),
    "public_site_url": public_url or None,
    "deployment_type": "github-pages, passwordless, noindex, independent concept",
    "real_photos_published": True,
    "photo_usage": "attributed noncommercial concept references; owner/licensor approval required for official launch",
    "menu_price_status": "archived official price snapshot marked February 2014; not represented as current",
}
(root / "deploy-meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
print(f"Validated and staged {sum(1 for p in root.rglob('*') if p.is_file())} public files in {root}")
PY
