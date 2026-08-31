# Tierney's Tavern Website

Creative direction and source research for a futuristic, motion-rich redesign of Tierney's Tavern in Montclair, New Jersey.

## Start here

- [Complete website design plan](WEBSITE_DESIGN_PLAN.md)
- [Image and rights manifest](ASSET_MANIFEST.md)
- [Machine-readable venue location](location/tierneys-tavern.json)
- [GeoJSON point](location/tierneys-tavern.geojson)
- [Standalone exact-location map](location/tierneys-map.html)

## Venue point

```text
Tierney's Tavern
138 Valley Road
Montclair, New Jersey 07042
40.822509225043, -74.219748973846
(862) 596-5986
```

## Repository policy

The project does not use fake business information, lorem ipsum, fabricated menu pricing, generic image placeholders, or invented customer quotations. Collected third-party photographs are stored only as attributed design references; public-site use requires the rights status described in [ASSET_MANIFEST.md](ASSET_MANIFEST.md).

## Asset collection

The workflow at `.github/workflows/collect-reference-assets.yml` downloads the exact files listed in `ASSET_SOURCES.json`, validates that every response is a real image above the configured minimum size, creates SHA-256 checksums, and fails the job if any required asset is unavailable. It never generates or substitutes a placeholder.
