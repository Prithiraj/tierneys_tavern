# Tierney's Tavern Website Concept

A mobile-first, future-heritage website concept for Tierney's Tavern in Montclair, New Jersey.

## Public outreach site

[`index.html`](index.html) is now the business-facing outreach experience. It contains:

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

## Passwordless Netlify deployment

The previous anonymous Netlify workflow was removed because anonymous deployments are temporary and protected. The production workflow is now:

```text
.github/workflows/netlify-production.yml
```

It validates the public-only bundle on every relevant push. To enable deployment, add these GitHub repository secrets:

```text
NETLIFY_AUTH_TOKEN
NETLIFY_SITE_ID
```

Then set the connected Netlify project's visitor access to **Public**:

```text
Project configuration
→ General
→ Visitor access
→ Project visibility
→ Public
```

Once connected, pushes to `main` deploy the passwordless production site. The workflow deliberately does not fall back to `--allow-anonymous`.

## Local production build

```bash
bash scripts/build_netlify.sh
```

The command creates `dist/`, generates the original social card, rejects research-only content, validates the HTML and PNG output, and writes deployment metadata.

## Venue point

```text
Tierney's Tavern
138 Valley Road
Montclair, New Jersey 07042
40.822509225043, -74.219748973846
(862) 596-5986
```

## Private research archive

The repository still retains the full creative direction, attributed image references, rights notes, and machine-readable location research for development use:

- [Complete website design plan](WEBSITE_DESIGN_PLAN.md)
- [Image and rights manifest](ASSET_MANIFEST.md)
- [Machine-readable venue location](location/tierneys-tavern.json)
- [GeoJSON point](location/tierneys-tavern.geojson)
- [Reference-asset collector](scripts/fetch_reference_assets.py)

These research files are not copied into the public Netlify bundle.
