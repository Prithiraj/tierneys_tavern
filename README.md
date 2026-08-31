# Tierney's Tavern Website Concept

A mobile-first, future-heritage website concept for Tierney's Tavern in Montclair, New Jersey.

## Public outreach site

[`index.html`](index.html) is the business-facing outreach experience. It contains:

- A responsive, thumb-friendly layout
- An optional Three.js architectural Tavern scene with an SVG fallback
- Current published bar and kitchen hours with an Eastern Time status indicator
- Real menu categories and the required kitchen/allergen notice
- Actual upstairs rental terms and capacity information
- Tierney's family timeline
- Exact Google Maps and Apple Maps directions
- Deferred map loading for mobile performance and privacy
- An original 1200 × 630 social card for WhatsApp and link previews
- Clear independent-concept labeling

The customer-facing build does **not** publish the design-research section, source manifest, dated prototype events, collected editorial photographs, lorem ipsum, fabricated pricing, or placeholders.

## GitHub Pages deployment

The active deployment workflow is:

```text
.github/workflows/pages.yml
```

It builds the public-only bundle, validates the outreach constraints, uploads the Pages artifact, and publishes from the `github-pages` environment. The expected passwordless address is:

```text
https://prithiraj.github.io/tierneys_tavern/
```

No Netlify token, site ID, visitor password, or external hosting account is required. The old Netlify workflow and configuration have been removed.

If Pages has not previously been enabled for this repository, select:

```text
Repository Settings
→ Pages
→ Build and deployment
→ Source: GitHub Actions
```

The repository is private, so the GitHub account must have a plan that supports Pages for private repositories. The published site remains marked `noindex` because it is an independent outreach concept rather than Tierney's official website.

## Local production build

```bash
PUBLIC_SITE_URL="https://prithiraj.github.io/tierneys_tavern" \
  bash scripts/build_site.sh
```

The command creates `dist/`, generates the original social card, rejects research-only content, validates the HTML and PNG output, writes deployment metadata, and adds `.nojekyll` for static publishing.

## Venue point

```text
Tierney's Tavern
138 Valley Road
Montclair, New Jersey 07042
40.822509225043, -74.219748973846
(862) 596-5986
```

## Private research archive

The repository retains the full creative direction, attributed image references, rights notes, and machine-readable location research for development use:

- [Complete website design plan](WEBSITE_DESIGN_PLAN.md)
- [Image and rights manifest](ASSET_MANIFEST.md)
- [Machine-readable venue location](location/tierneys-tavern.json)
- [GeoJSON point](location/tierneys-tavern.geojson)
- [Reference-asset collector](scripts/fetch_reference_assets.py)

These research files are not copied into the public GitHub Pages artifact.
