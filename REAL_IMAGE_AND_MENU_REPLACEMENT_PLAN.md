# Tierney's Tavern — Real Image and Menu Replacement Plan

**Project:** `Prithiraj/tierneys_tavern`  
**Public target:** `https://prithiraj.github.io/tierneys_tavern/`  
**Purpose:** replace illustration-led presentation with real, owner-approved Tierney's photography and a verified current menu while retaining the futuristic interaction system.

---

## 1. Final creative rule

The public experience will follow this order:

1. **Real Tierney's photograph first**
2. **Futuristic interface treatment second**
3. **Three.js only as an enhancement layer**
4. **Text and controls remain useful without animation**

The finished public site must not use an SVG burger, an opaque procedural building, a generic stock pub, or an AI-generated food image where genuine Tierney's photography can be used.

The Three.js façade, scan lines, grids, glow, depth movement, and structural labels can remain, but they must sit over or transition from a real photograph rather than replace it.

---

## 2. Image-rights rule

Real does not automatically mean reusable. Images downloaded from Google Maps, editorial articles, review sites, or social accounts may still belong to the photographer or platform contributor.

### Approved production-source order

1. Original files supplied directly by Tierney's Tavern
2. Photographs taken for this project with a signed usage release
3. Files from Tierney's official accounts that the business explicitly approves for reuse
4. Licensed third-party photographs with written commercial permission

### Research-only images already in the repository

The following are real Tierney's references, but they must not enter the public Pages bundle until their rights are cleared:

| Candidate use | Existing reference path | Current status |
|---|---|---|
| Exterior hero | `assets/reference/tierneys-exterior-montclair-girl.jpg` | Editorial reference; permission required |
| Family story | `assets/reference/tierney-family-northjersey.jpg` | Editorial reference; permission required |
| Buddy Burger | `assets/reference/buddy-burger-mike-eats-nyc-burgers.jpg` | Review photograph; permission required |
| Secondary food image | `assets/reference/classic-cheeseburger-mike-eats-nyc-burgers.jpg` | Review photograph; permission required |
| Rear mural and stairs | `assets/reference/guinness-mural-mike-eats-nyc-burgers.jpg` | Review photograph; permission required |
| Upstairs live room | `assets/reference/upstairs-performance-bizzboard.jpg` | Provenance must be confirmed |
| Current visual mark | `assets/brand/current-tierneys-mark.png` | Confirm owner approval before public use |

These files are composition and content references, not automatic production assets.

---

## 3. Required final public asset set

The build should require these real, approved images before the real-photo release is published:

```text
assets/public/images/
├── exterior-hero-desktop.avif
├── exterior-hero-desktop.webp
├── exterior-hero-mobile.avif
├── exterior-hero-mobile.webp
├── buddy-burger-main.avif
├── buddy-burger-main.webp
├── buddy-burger-detail.webp
├── upstairs-live.webp
├── upstairs-empty.webp
├── family-behind-bar.webp
├── bar-interior-wide.webp
├── mural-and-stairs.webp
├── accessible-entrance.webp
├── parking-lot.webp
└── tierneys-social-card.jpg
```

The full-resolution camera originals should be retained outside the public repository. The repository should contain only approved, web-optimized derivatives.

### Crop requirements

| Image | Desktop crop | Mobile crop | Minimum useful source |
|---|---:|---:|---:|
| Exterior hero | 16:10 | 4:5 | 2400 px wide |
| Buddy Burger | 4:3 | 4:5 | 1800 px wide |
| Upstairs live | 16:10 | 4:3 | 2000 px wide |
| Upstairs empty | 16:10 | 4:3 | 2000 px wide |
| Family | 3:2 | 4:5 | 1800 px wide |
| Bar interior | 16:9 | 4:3 | 2200 px wide |
| Mural/stairs | 4:5 | 4:5 | 1600 px wide |
| Access/parking | 3:2 | 4:3 | 1600 px wide |
| Social card | 1200 × 630 | Same file | 1200 × 630 |

---

# 4. Section-by-section replacement plan

## Section 0 — Page metadata and WhatsApp preview

### Current implementation

The build generates an original illustrated social card.

### Replacement

Use a real blue-hour or early-evening exterior photograph of Tierney's. The steep gable and sign must remain clearly recognizable when the image is cropped inside WhatsApp.

### Composition

- Exterior occupies the right 55–60% of the frame.
- Left side contains `TIERNEY'S // 1934 → ∞` and `WHERE FRIENDS MEET`.
- Preserve a 90-pixel safe margin around all text.
- Apply only a subtle green scan line and amber window glow.
- Do not turn the photograph into a fully synthetic render.

### Final files

```text
assets/public/images/tierneys-social-card.jpg
```

### Metadata

```html
<meta property="og:image" content="https://prithiraj.github.io/tierneys_tavern/assets/public/images/tierneys-social-card.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Tierney's Tavern on Valley Road in Montclair, a family tavern founded in 1934">
```

### Acceptance condition

The social image must be based on a real approved exterior photograph and must render at 1200 × 630.

---

## Section 1 — Header and identity

### Current implementation

The header uses a custom `TT 1934` geometric symbol and the word `TIERNEY'S`.

### Replacement

Use the approved Tierney's wordmark if the family authorizes it. If the current official mark is not approved for this concept, use a clean text wordmark reading `TIERNEY'S TAVERN`; a text wordmark is an intentional identity treatment, not an image placeholder.

### Recommended behavior

- Keep the compact sticky header.
- Preserve the live open/closed indicator.
- Do not place a photographic background behind navigation.
- On mobile, the identity must remain readable at 320 pixels wide.

### Candidate reference

```text
assets/brand/current-tierneys-mark.png
```

### Acceptance condition

No unapproved logo artwork is published. The header remains lightweight and legible.

---

## Section 2 — Hero / Valley Road landmark

### Current implementation

Selector group:

```text
.scene-card
.facade-fallback
#facade-scene
#scene-toggle
```

The section currently displays a procedural Three.js building and an SVG architectural fallback.

### Replacement

The real exterior photograph becomes the primary visual and the largest-contentful-paint asset. The canvas becomes transparent and renders only architectural line work, scanner light, particles, and optional depth movement over the photograph.

### Required media

```text
assets/public/images/exterior-hero-desktop.avif
assets/public/images/exterior-hero-desktop.webp
assets/public/images/exterior-hero-mobile.avif
assets/public/images/exterior-hero-mobile.webp
```

### Candidate composition reference

```text
assets/reference/tierneys-exterior-montclair-girl.jpg
```

### Revised DOM structure

```html
<div class="scene-card" id="scene-card">
  <picture class="hero-photo">
    <source media="(max-width: 699px)" type="image/avif" srcset="assets/public/images/exterior-hero-mobile.avif">
    <source media="(max-width: 699px)" type="image/webp" srcset="assets/public/images/exterior-hero-mobile.webp">
    <source type="image/avif" srcset="assets/public/images/exterior-hero-desktop.avif">
    <img
      src="assets/public/images/exterior-hero-desktop.webp"
      alt="Tierney's Tavern's Tudor-style exterior on Valley Road in Montclair"
      width="1600"
      height="1000"
      fetchpriority="high"
      decoding="async">
  </picture>
  <canvas id="facade-scene" aria-hidden="true"></canvas>
  <!-- existing labels and actions -->
</div>
```

### Three.js treatment

Retain:

- roofline wireframe
- one scanner pass
- subtle pointer depth on desktop
- amber highlight around real windows
- structural labels such as `LEVEL 01 // BAR + GRILL` and `LEVEL 02 // UPSTAIRS`

Remove:

- opaque procedural walls and roof
- the 3D model as the only visible building
- the SVG façade as the standard visual
- continuous movement that obscures the photo

### Button copy

Replace `EXPLODE VIEW` with one of these business-friendly labels:

```text
SCAN THE TAVERN
VIEW LEVELS
EXPLORE THE BUILDING
```

`SCAN THE TAVERN` is preferred. The active state can read `RETURN TO PHOTO`.

### Mobile behavior

- Show the real mobile crop immediately.
- Load Three.js only after the photo is visible.
- Disable pointer tracking.
- Use a single 600–800 millisecond scan effect.
- Keep the CTA buttons above the fold on common 390 × 844 screens.

### Acceptance conditions

- The real exterior remains visible if JavaScript or WebGL fails.
- No architectural SVG is shown as the primary building.
- Hero image remains under approximately 300 KB in AVIF and 450 KB in WebP.

---

## Section 3 — Live status rail

### Current implementation

The status rail shows bar hours, kitchen hours, seating policy, and a calculated Eastern Time status.

### Replacement

No photograph is needed. Keep this section data-first. Adding an image would reduce scanability.

### Improvement

Add a small `Last checked against published hours` label and allow an owner-controlled temporary notice such as:

```text
KITCHEN CLOSING EARLY TONIGHT
UPSTAIRS PRIVATE EVENT
HOLIDAY HOURS
```

### Acceptance condition

The rail remains immediately readable and never relies on photography or animation to communicate open/closed state.

---

## Section 4 — Kitchen signature visual

### Current implementation

Selector group:

```text
#food
.burger-stage
.burger
```

The current section uses an animated inline SVG burger.

### Replacement

Remove the SVG burger completely. Use a real Tierney's Buddy Burger photograph as the main visual.

### Required media

```text
assets/public/images/buddy-burger-main.avif
assets/public/images/buddy-burger-main.webp
assets/public/images/buddy-burger-detail.webp
```

### Candidate composition references

```text
assets/reference/buddy-burger-mike-eats-nyc-burgers.jpg
assets/reference/classic-cheeseburger-mike-eats-nyc-burgers.jpg
```

### Revised presentation

- Main frame: full burger with enough context to feel like Tierney's rather than a studio stock image.
- Secondary close-up: fried onions, bacon, cheese, and patty texture.
- Preserve `SCAN // BUDDY BURGER` as a small interface label.
- Use a mild image-mask reveal or thermal scan overlay.
- Do not animate food into separated layers unless a genuine multi-shot sequence is photographed for that purpose.

### Suggested overlay copy

```text
THE BUDDY BURGER
A Tierney's favorite with bacon, fried onions and American cheese.
```

The final ingredient wording must be confirmed with Tierney's before publication.

### Alt text

```text
Tierney's Buddy Burger with bacon, fried onions and melted American cheese
```

### Acceptance conditions

- No inline burger SVG remains in `index.html`.
- The photograph is a real Tierney's food image with usage approval.
- Mobile crop does not cut off the bun or plate.

---

## Section 5 — Full menu and current pricing

### Current implementation

The page currently lists eight broad menu categories without prices and links to the official kitchen page.

### Replacement

Build a proper in-page menu with real item names and owner-verified current prices. Keep the external official menu link as a secondary source, not the primary experience.

### Source status

- The current official kitchen page publishes item categories but not prices.
- The legacy official menu includes prices explicitly marked `Prices as of February 2014`; those numbers are historical and must not be reused as current prices.
- Recent directory and review pages may surface other values, but they are verification leads rather than an owner-approved price source.
- Google Maps menu data should be transcribed only after Tierney's confirms that the listing is current.

### Required verification workflow

1. Capture the current Google Business menu and any current menu photographs.
2. Ask Grace or Sarah Tierney for the latest printed or digital menu.
3. Compare every item name and price.
4. Send a one-page verification table to Tierney's.
5. Record who approved it and the approval date.
6. Publish only rows marked `verified: true`.

### Data file

Create:

```text
data/menu.json
```

Recommended structure:

```json
{
  "currency": "USD",
  "verified_on": "YYYY-MM-DD",
  "verified_by": "Tierney's Tavern",
  "source_note": "Owner-approved current menu",
  "categories": [
    {
      "name": "From the Grill",
      "items": [
        {
          "name": "Hamburger",
          "description": "",
          "price": null,
          "featured": false,
          "verified": false
        }
      ]
    }
  ]
}
```

`null` is a data-review state and must not render as `$0.00`, `TBD`, or placeholder dashes. An unverified row is omitted from the priced production menu.

### Production categories

The official current kitchen page supports these real groups:

- From the Grill
- Sandwiches
- Sides

The current item inventory includes burgers, cheeseburgers, grilled chicken, pastrami, corned beef, cheesesteak, grilled cheese, wings, chicken fingers, hot dog, Taylor ham, chicken salad, tuna salad, turkey, turkey club, BLT, roast beef, roast beef club, ham, liverwurst, fries, onion rings, pickles, deli salads, and chili.

### UI plan

Desktop:

- Two-column menu board.
- Category label, item, optional description, right-aligned price.
- Featured Buddy Burger strip with its real image.

Mobile:

- One-column category accordion.
- Item and price remain on one line where possible.
- Minimum 16-pixel body type.
- Sticky `Call` and `Directions` actions remain accessible.

### Pricing disclosure

```text
Menu and prices verified with Tierney's on [date]. Prices and availability may change.
```

### Acceptance conditions

- No price is sourced solely from an old directory or the 2014 page.
- Every displayed price has an approval date.
- No fabricated, inferred, or placeholder prices appear.

---

## Section 6 — Upstairs room

### Current implementation

Selector group:

```text
#upstairs
.room
.room-plan
.room-toolbar
```

The current primary visual is a CSS room diagram.

### Replacement

Make real upstairs photography the default visual. Keep the interactive room diagram as a secondary planning tab.

### Required media

```text
assets/public/images/upstairs-live.webp
assets/public/images/upstairs-empty.webp
```

### Candidate reference

```text
assets/reference/upstairs-performance-bizzboard.jpg
```

### Tab structure

```text
LIVE ROOM
EMPTY ROOM
LAYOUT GUIDE
```

- `LIVE ROOM`: real performance photograph.
- `EMPTY ROOM`: real wide-angle photograph showing stage, bar, seating, exits, and floor proportions.
- `LAYOUT GUIDE`: existing schematic, clearly labeled as conceptual.

### Animation

- Crossfade between the two real photographs.
- The floor-plan markers animate only inside `LAYOUT GUIDE`.
- No faux 3D room should appear before the real room photos.

### Content retained

- $60 per hour
- two-hour minimum
- bartender included
- gratuity not included
- approximately 55–60 current seats
- up to 100 seated with additional furniture
- up to 135 standing
- no second kitchen upstairs
- outside catering recommendation
- no elevator

All operating details should be reconfirmed before a formal launch.

### Acceptance conditions

- A real room photograph is the first visible upstairs asset.
- The layout graphic is clearly secondary and conceptual.
- The no-elevator notice is visible before the booking CTA.

---

## Section 7 — Story and family history

### Current implementation

The story section is a text-only timeline for the 1890s, 1934, and today.

### Replacement

Use a real Tierney family photograph as the anchor and combine it with owner-supplied archival material.

### Required media

```text
assets/public/images/family-behind-bar.webp
```

Recommended optional archive:

```text
assets/public/images/archive/
├── tierneys-1930s.webp
├── historic-sign.webp
├── early-family-photo.webp
└── old-menu-or-license.webp
```

### Candidate reference

```text
assets/reference/tierney-family-northjersey.jpg
```

### Layout

Desktop:

- Large family photograph on the left.
- Timeline on the right.
- Years activate as the user scrolls.

Mobile:

- Family photo first.
- Three compact timeline cards underneath.
- No sideways scroll requirement.

### Copy rule

Keep the story focused on:

- family connection to the property since the 1890s
- tavern founded in 1934
- fifth generation involved today

Do not add invented family anecdotes or unverified archival dates.

### Acceptance condition

At least one owner-approved family or archival photograph must appear; otherwise the section remains text-only rather than using a fake historical image.

---

## Section 8 — New business section: Inside Tierney's

### Purpose

This section replaces any developer-facing or research-facing content. It should show what visiting the tavern actually feels like.

### Heading

```text
INSIDE TIERNEY'S
THE BAR, THE GRILL, THE ROOM UPSTAIRS.
```

### Required media

```text
assets/public/images/bar-interior-wide.webp
assets/public/images/mural-and-stairs.webp
assets/public/images/buddy-burger-detail.webp
assets/public/images/upstairs-live.webp
```

### Candidate references

```text
assets/reference/guinness-mural-mike-eats-nyc-burgers.jpg
assets/reference/classic-cheeseburger-mike-eats-nyc-burgers.jpg
assets/reference/upstairs-performance-bizzboard.jpg
```

### Layout

Desktop:

- Asymmetric four-image editorial grid.
- Wide bar interior as the dominant image.
- Mural/stairs as the tall vertical image.
- Food and upstairs images as supporting cards.

Mobile:

- Horizontal snap gallery with visible next-card edge.
- Real captions under each image.
- No automatic carousel.

### Captions

Examples:

```text
THE MAIN BAR
THE BUDDY BURGER
UPSTAIRS LIVE
THE REAR MURAL + STAIRS
```

### Acceptance condition

No development language, source manifest, rights explanation, or design-process commentary appears in the customer journey.

---

## Section 9 — Events / Tonight

### Current implementation

The public outreach build links to the official calendar but does not show current events inline.

### Replacement

Add an owner-maintained current-events strip between the status rail and kitchen section.

### Media rule

Use real event posters or venue-supplied performer images. Do not download random social or event-listing artwork without permission.

### Behavior

- Show only future events.
- Hide the entire section when there are no published events.
- Each event includes date, time, room, cover charge where applicable, and a link to the official calendar or ticket source.
- Never retain old demonstration events after their dates pass.

### Suggested data file

```text
data/events.json
```

### Card fallback

When a real poster does not exist, use a deliberate typographic event card with the actual event name and date. Do not show an empty image frame or a generic concert stock image.

### Acceptance condition

Every displayed event is current and linked to an owner-controlled or performer-controlled source.

---

## Section 10 — Visit, accessibility, parking, and map

### Current implementation

The Visit section contains operational facts and a deferred Google Maps embed, but no real access or parking photography.

### Replacement

Keep the live map and add two practical real photographs:

```text
assets/public/images/accessible-entrance.webp
assets/public/images/parking-lot.webp
```

### Image use

- Accessible entrance photo: show the actual sidewalk approach and doorway.
- Parking photo: show the customer lot entrance and relationship to the building.
- Do not use a downloaded Google Street View screenshot as a substitute.

### Map

Retain the on-demand iframe at:

```text
40.822509225043, -74.219748973846
```

The map remains an interactive embed rather than a static image.

### Mobile layout

1. Address
2. Current hours
3. Directions buttons
4. Access and parking photos
5. `Load interactive map`

This keeps the most important actions ahead of the heavier third-party map.

### Acceptance conditions

- The exact address and coordinate point remain unchanged.
- Parking and accessible-entry claims are supported by actual venue photographs and owner confirmation.
- Map loading remains user initiated.

---

## Section 11 — Final call to action and footer

### Current implementation

The final CTA is text-only and the footer identifies the site as an independent concept.

### Replacement

Use a real night exterior photograph as a low-opacity background only if a separate suitable image is available. Otherwise keep the section text-only; a text-only CTA is intentional and preferable to reusing the same image excessively.

### Copy

```text
SEE YOU AT TIERNEY'S.
Come for a burger and a game, check the calendar for live events, or call to plan something upstairs.
```

### Acceptance condition

The independent-concept notice remains visible until Tierney's formally adopts or authorizes the site.

---

## Section 12 — Mobile dock

### Current implementation

```text
Home · Food · Upstairs · Directions
```

### Replacement

Use the more task-oriented set:

```text
Tonight · Menu · Directions · Call
```

No imagery is required.

### Acceptance condition

Every target is a real action; no dock item opens a design or research page.

---

# 5. Photography capture list

The fastest clean production path is a single controlled shoot at Tierney's.

## Exterior

- Blue-hour front three-quarter view
- Straight-on façade and sign
- Daytime mobile crop
- Night exterior with windows lit
- Parking-lot entrance
- Accessible sidewalk entrances

## Food

- Buddy Burger hero: 45-degree angle
- Buddy Burger side profile
- Burger cut or detail shot
- Fries and onion rings
- Wings or chicken fingers
- Cheesesteak or Taylor ham sandwich
- Beer pour beside burger, where appropriate

## Interior

- Empty main bar before service
- Main bar with natural activity and signed appearance releases where required
- TVs and sports atmosphere
- Jukebox, darts, signs, taps, and small details
- Mural and exterior stairs

## Upstairs

- Empty room from rear to stage
- Empty room from stage to rear/bar
- Live band
- Comedy or seated configuration
- Birthday/private-event configuration
- Access stairs and entrance

## Family and history

- Current family/staff portrait behind the bar
- Historical photographs scanned flat and evenly lit
- Original signs, menus, licenses, or memorabilia

---

# 6. Menu-price collection sheet

Before editing the public menu, prepare this exact owner-review table:

| Category | Item | Google listing price | Printed/menu-photo price | Owner-confirmed price | Verified date | Publish? |
|---|---|---:|---:|---:|---|---|
| From the Grill | Hamburger |  |  |  |  | No |
| From the Grill | Cheeseburger |  |  |  |  | No |
| From the Grill | Buddy Burger |  |  |  |  | No |
| From the Grill | Grilled Chicken |  |  |  |  | No |
| From the Grill | Wings |  |  |  |  | No |
| From the Grill | Chicken Fingers |  |  |  |  | No |
| From the Grill | Pastrami |  |  |  |  | No |
| From the Grill | Corned Beef |  |  |  |  | No |
| From the Grill | Cheesesteak |  |  |  |  | No |
| From the Grill | Grilled Cheese |  |  |  |  | No |
| From the Grill | Hot Dog |  |  |  |  | No |
| From the Grill | Taylor Ham |  |  |  |  | No |
| Sandwiches | Chicken Salad |  |  |  |  | No |
| Sandwiches | Tuna Salad |  |  |  |  | No |
| Sandwiches | Turkey |  |  |  |  | No |
| Sandwiches | Turkey Club |  |  |  |  | No |
| Sandwiches | BLT |  |  |  |  | No |
| Sandwiches | Roast Beef |  |  |  |  | No |
| Sandwiches | Roast Beef Club |  |  |  |  | No |
| Sandwiches | Ham |  |  |  |  | No |
| Sandwiches | Liverwurst |  |  |  |  | No |
| Sides | French Fries |  |  |  |  | No |
| Sides | Cheese Fries |  |  |  |  | No |
| Sides | Chili Fries |  |  |  |  | No |
| Sides | Chili and Cheese Fries |  |  |  |  | No |
| Sides | Onion Rings |  |  |  |  | No |
| Sides | Pickles |  |  |  |  | No |
| Sides | Macaroni Salad |  |  |  |  | No |
| Sides | Potato Salad |  |  |  |  | No |
| Sides | Cole Slaw |  |  |  |  | No |
| Sides | Chili Cup / Bowl |  |  |  |  | No |

Blank cells are review fields in this internal planning document; they must never render on the public site.

---

# 7. Code-change checklist

## Remove or demote

- [ ] Remove the inline `<svg class="burger">` from `index.html`.
- [ ] Remove `.burger .layer` and burger-separation animation CSS.
- [ ] Remove the visible `.facade-fallback` SVG as the normal hero.
- [ ] Convert the Three.js building renderer into a transparent overlay.
- [ ] Make `.room-plan` a secondary tab rather than the initial upstairs view.
- [ ] Remove the generated illustrated OG card from the final real-photo release.

## Add

- [ ] Add responsive `<picture>` markup for the exterior hero.
- [ ] Add responsive `<picture>` markup for the Buddy Burger.
- [ ] Add real upstairs live and empty-room tabs.
- [ ] Add family photography beside the timeline.
- [ ] Add the `Inside Tierney's` image gallery.
- [ ] Add practical access and parking photography.
- [ ] Add `data/menu.json` and render only owner-verified prices.
- [ ] Add `data/events.json` or an owner-managed equivalent.
- [ ] Generate the WhatsApp card from the approved real exterior photo.

---

# 8. Build protections

Update `scripts/build_site.sh` so the real-photo release fails when a mandatory image is missing or empty.

Required checks:

```bash
test -s dist/assets/public/images/exterior-hero-mobile.webp
test -s dist/assets/public/images/exterior-hero-desktop.webp
test -s dist/assets/public/images/buddy-burger-main.webp
test -s dist/assets/public/images/upstairs-live.webp
test -s dist/assets/public/images/family-behind-bar.webp
! grep -R -i '<svg class="burger"' dist
! grep -R -i 'research before render' dist
```

Add an internal approval file that is not copied into `dist`:

```text
PUBLIC_MEDIA_APPROVALS.md
```

For each asset, record:

- filename
- photographer or owner
- date supplied
- permitted uses
- attribution requirement
- approval evidence location

---

# 9. Performance requirements

- Hero image is the LCP asset and must not wait for Three.js.
- Use AVIF first, WebP fallback.
- Include intrinsic width and height on every image.
- Use `fetchpriority="high"` only for the hero.
- Lazy-load all images below the hero.
- Cap desktop hero at roughly 300 KB AVIF / 450 KB WebP.
- Cap below-fold images at roughly 180–250 KB each.
- Pause WebGL while off-screen or while the tab is hidden.
- Respect `prefers-reduced-motion`.
- Preserve the tested 390-pixel mobile layout without horizontal overflow.

---

# 10. Implementation order

## Release A — Highest visual impact

1. Real exterior hero
2. Real Buddy Burger
3. Real upstairs live-room photo
4. Real family photo
5. Real-photo WhatsApp card

## Release B — Business completeness

6. Owner-verified menu and prices
7. Real upstairs empty-room photo
8. Inside Tierney's gallery
9. Entrance and parking images
10. Current event posters

## Release C — Enhanced interaction

11. Photo-aware Three.js scan overlay
12. Photo transitions and hotspot labels
13. Event and menu data administration
14. Automated image optimization and integrity checks

---

# 11. Definition of done

The replacement is complete only when:

- The hero shows the real Tierney's exterior before any WebGL loads.
- The kitchen section shows a real Tierney's burger.
- The upstairs section opens on a real photograph.
- The story section contains an approved family or archive image.
- The customer-facing gallery contains only real Tierney's imagery.
- Every public image has documented permission.
- Every displayed menu price is owner-confirmed and date-stamped.
- No SVG burger or opaque procedural building substitutes for available real photography.
- The site remains usable with images disabled, JavaScript disabled, and reduced motion enabled.
- The GitHub Pages build contains no research-only assets or developer-facing sections.

---

## Source pages used for menu planning

- Current official kitchen page: `https://www.tierneystavern1934.com/kitchen`
- Current official site: `https://www.tierneystavern1934.com/`
- Legacy menu, explicitly marked with February 2014 pricing: `https://tierneystavern.com/cookin.php`
- Google Maps destination: `https://www.google.com/maps/search/?api=1&query=Tierney%27s%20Tavern%2C%20138%20Valley%20Road%2C%20Montclair%2C%20NJ%2007042`

The owner-approved current menu must override all third-party directories and historical menu pages.
