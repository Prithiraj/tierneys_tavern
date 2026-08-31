# Tierney's Tavern Website

Creative direction and source research for a futuristic, motion-rich redesign of Tierney's Tavern in Montclair, New Jersey.

## Netlify design preview

- **Preview:** https://papaya-daffodil-140b69.netlify.app/
- **Access password:** `My-Drop-Site`
- **Mode:** noindex, password-protected, independent design dossier
- **Deployment run:** GitHub Actions run `33438515723`

The anonymous project must be claimed in Netlify before its one-hour claim window expires. The claim credential is intentionally not committed to Git history. After claiming it, connect `Prithiraj/tierneys_tavern` to the Netlify project for durable continuous deployment.

## Start here

- [Deployable dossier](index.html)
- [Complete website design plan](WEBSITE_DESIGN_PLAN.md)
- [Image and rights manifest](ASSET_MANIFEST.md)
- [Machine-readable venue location](location/tierneys-tavern.json)
- [GeoJSON point](location/tierneys-tavern.geojson)
- [Standalone exact-location map](location/tierneys-map.html)
- [Netlify configuration](netlify.toml)

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

## Builds and deployment

- `.github/workflows/collect-reference-assets.yml` downloads and validates the exact files declared in `ASSET_SOURCES.json`, normalizes supported image responses, creates SHA-256 checksums, and fails rather than generating a placeholder.
- `scripts/build_netlify.sh` validates all deployment-critical assets and stages a controlled `dist/` bundle.
- `.github/workflows/netlify-preview.yml` builds the dossier and creates a claimable Netlify preview without storing a Netlify account token in GitHub.
- `netlify.toml` defines the publish directory, redirects, cache behavior, security headers, and noindex policy.
