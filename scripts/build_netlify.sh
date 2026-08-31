#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST="$ROOT/dist"

required=(
  "index.html"
  "WEBSITE_DESIGN_PLAN.md"
  "ASSET_MANIFEST.md"
  "location/tierneys-tavern.json"
  "location/tierneys-tavern.geojson"
  "location/tierneys-map.html"
  "assets/reference/tierneys-exterior-montclair-girl.jpg"
  "assets/reference/tierney-family-northjersey.jpg"
  "assets/reference/buddy-burger-mike-eats-nyc-burgers.jpg"
  "assets/reference/upstairs-performance-bizzboard.jpg"
  "assets/reference/guinness-mural-mike-eats-nyc-burgers.jpg"
  "assets/location/tierneys-location-card.svg"
  "assets/location/tierneys-directions-qr.svg"
)

for relative in "${required[@]}"; do
  file="$ROOT/$relative"
  if [[ ! -s "$file" ]]; then
    printf 'Missing or empty required deployment asset: %s\n' "$relative" >&2
    exit 1
  fi
done

rm -rf "$DIST"
mkdir -p "$DIST/assets" "$DIST/location"

cp "$ROOT/index.html" "$DIST/index.html"
cp "$ROOT/WEBSITE_DESIGN_PLAN.md" "$DIST/WEBSITE_DESIGN_PLAN.md"
cp "$ROOT/ASSET_MANIFEST.md" "$DIST/ASSET_MANIFEST.md"
cp -R "$ROOT/assets/reference" "$DIST/assets/reference"
cp -R "$ROOT/assets/brand" "$DIST/assets/brand"
cp -R "$ROOT/assets/location" "$DIST/assets/location"
cp "$ROOT/location/tierneys-tavern.json" "$DIST/location/tierneys-tavern.json"
cp "$ROOT/location/tierneys-tavern.geojson" "$DIST/location/tierneys-tavern.geojson"
cp "$ROOT/location/tierneys-map.html" "$DIST/location/tierneys-map.html"

cat > "$DIST/robots.txt" <<'ROBOTS'
User-agent: *
Disallow: /
ROBOTS

cat > "$DIST/404.html" <<'HTML'
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="robots" content="noindex,nofollow,noarchive">
  <meta name="theme-color" content="#070908">
  <title>Signal not found // TT-1934</title>
  <style>
    :root{color-scheme:dark}*{box-sizing:border-box}body{margin:0;min-height:100svh;display:grid;place-items:center;background:#070908;color:#f0ebdd;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;padding:1.5rem}main{width:min(760px,100%);border:1px solid rgba(98,255,157,.34);padding:clamp(1.5rem,6vw,4rem);background:radial-gradient(circle at 85% 10%,rgba(13,81,52,.35),transparent 38%)}small{color:#62ff9d;letter-spacing:.12em;text-transform:uppercase}h1{font-family:system-ui,sans-serif;font-size:clamp(3rem,12vw,8rem);line-height:.85;letter-spacing:-.07em;margin:1.4rem 0}p{color:#a6aea9;line-height:1.7;max-width:56ch}a{display:inline-block;margin-top:1.5rem;padding:.8rem 1rem;background:#62ff9d;color:#070908;text-decoration:none;font-weight:700;text-transform:uppercase;letter-spacing:.08em;font-size:.75rem}
  </style>
</head>
<body><main><small>Error 404 // signal absent</small><h1>NOT<br>FOUND.</h1><p>The requested route is not part of the Tierney's future-heritage design dossier.</p><a href="/">Return to the dossier →</a></main></body>
</html>
HTML

python - "$DIST" <<'PY'
from html.parser import HTMLParser
from pathlib import Path
import json
import sys

class Parser(HTMLParser):
    pass

root = Path(sys.argv[1])
for page in (root / "index.html", root / "404.html", root / "location" / "tierneys-map.html"):
    parser = Parser()
    parser.feed(page.read_text(encoding="utf-8"))

meta = {
    "project": "Tierney's Tavern future-heritage design dossier",
    "venue": "138 Valley Road, Montclair, NJ 07042",
    "coordinates": [40.822509225043, -74.219748973846],
    "source_commit": "${COMMIT_SHA:-local}",
    "deployment_type": "noindex design preview"
}
(root / "deploy-meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
print(f"Validated and staged {sum(1 for p in root.rglob('*') if p.is_file())} files in {root}")
PY
