# Tierney's Tavern Website Concept

A mobile-first, future-heritage website concept for Tierney's Tavern in Montclair, New Jersey.

## Public outreach site

[`index.html`](index.html) is the business-facing experience. It now uses real Tierney's imagery instead of illustrated stand-ins:

- Real Valley Road exterior photograph with a transparent Three.js scan overlay
- Real Buddy Burger and classic cheeseburger photography
- Real upstairs performance photograph with an optional layout guide
- Real Tierney family photograph beside the verified history timeline
- Real mural and stair image in the inside-the-tavern gallery
- Current published hours with an Eastern Time open/closed indicator
- Official menu categories and kitchen/allergen notice
- A clearly dated official legacy price snapshot for demonstrating the menu interface
- Actual upstairs rental terms and capacity information
- Exact Google Maps and Apple Maps directions
- Deferred map loading for mobile performance and privacy
- A photographic 1200 × 630 WhatsApp/Open Graph card
- Clear independent-concept labeling and image credits

The customer-facing build does **not** publish the research dossier, source manifest, fabricated prices, generic stock photography, lorem ipsum, or the previous SVG burger.

## Important source status

The public concept uses attributed real photographs already collected in the repository. Those images remain the property of their respective photographers and publishers. They are suitable for this noncommercial design concept, but an official Tierney's launch should replace them with owner-supplied originals or obtain written commercial permission.

The displayed numeric menu prices are not represented as current. They come from Tierney's official legacy menu, which marks them as **February 2014**. Current prices should be supplied or approved by Tierney's before an official release. The Buddy Burger price is deliberately omitted rather than guessed.

See:

- [Real-image and menu replacement plan](REAL_IMAGE_AND_MENU_REPLACEMENT_PLAN.md)
- [Image and rights manifest](ASSET_MANIFEST.md)

## GitHub Pages deployment

The active deployment workflow is:

```text
.github/workflows/pages.yml
```

It builds optimized JPEG/WebP derivatives from the real reference files, creates the photographic sharing card, validates the outreach constraints, uploads the Pages artifact, and publishes from the `github-pages` environment.

Expected passwordless address:

```text
https://prithiraj.github.io/tierneys_tavern/
```

If Pages has not yet been enabled:

```text
Repository Settings
→ Pages
→ Build and deployment
→ Source: GitHub Actions
```

Then run **Deploy Tierney's concept to GitHub Pages** from the Actions tab, or push another change to `main`.

The site remains marked `noindex` because it is an independent outreach concept rather than Tierney's official website.

## Local production build

```bash
PUBLIC_SITE_URL="https://prithiraj.github.io/tierneys_tavern" \
  bash scripts/build_site.sh
```

The command creates `dist/`, generates optimized real-photo assets, creates the photographic social card, rejects research-only and illustrated-stand-in content, validates the HTML and image output, writes deployment metadata, and adds `.nojekyll`.

## Venue point

```text
Tierney's Tavern
138 Valley Road
Montclair, New Jersey 07042
40.822509225043, -74.219748973846
(862) 596-5986
```

## Private development archive

The repository also retains:

- [Complete website design plan](WEBSITE_DESIGN_PLAN.md)
- [Machine-readable venue location](location/tierneys-tavern.json)
- [GeoJSON point](location/tierneys-tavern.geojson)
- [Reference-asset collector](scripts/fetch_reference_assets.py)

These development files are not copied into the GitHub Pages artifact.
