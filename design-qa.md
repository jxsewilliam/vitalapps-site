# Design QA — Vital Apps product pages

## Scope

- Source URL: https://quittrapp.com
- Source capture: `/Users/jay/Documents/Codex/2026-08-30/you-know-my-site-vital-apps/work/source-capture/`
- Implementation: `/Users/jay/Documents/Codex/2026-08-30/you-know-my-site-vital-apps/work/vitalapps-site/`
- Representative implementation captures: `/Users/jay/Documents/Codex/2026-08-30/you-know-my-site-vital-apps/work/implementation-capture/`
- Routes: `/useby/`, `/dualshot/`, `/maxxr/`, `/relapsr/`, `/swipeclean/`, `/arrowflow/`, `/rise/`

## Viewports and dimensions

- Desktop source and implementation: 1440 × 1024.
- Mobile source and implementation: requested 390 × 844; browser document width was 375 CSS px in both source and implementation.
- Responsive route check: every route reported `scrollWidth === clientWidth` at the mobile breakpoint.

## Fidelity review

- Layout: passed. The implementation follows the source's dark editorial page, transparent top navigation, split hero, product-led artwork, long-form storytelling, alternating feature sections, proof/details band, marquee, FAQs, repeated conversion CTA, and restrained footer.
- Typography: passed. DM Sans provides the closest available open web-font treatment without copying the source's proprietary font. Display scale, compact leading, and tight tracking follow the source hierarchy.
- Color: passed. The near-black source palette is preserved while each page maps the source's purple accent role to the app's real Vital accent color.
- Imagery: passed. Only Vital-owned app icons and Relapsr phone artwork are used. No Quittr imagery, logos, press marks, avatars, ratings, or testimonials are copied or invented.
- Surfaces: passed. Borders, rounded controls, feature panels, section dividers, subdued shadows, and glow levels were checked against the side-by-side desktop and mobile comparison images.
- Content: passed. Pricing, platform, release state, privacy statements, and support links are derived from the existing Vital content. Coming-soon apps retain disabled conversion states.
- Responsiveness: passed at 1440 × 1024 and 390 × 844, with additional visual inspection of hero, story, feature-grid, studio, FAQ, CTA, and footer sections.

## Interaction review

- Desktop navigation anchors: passed.
- Mobile menu open, close, body lock, link close, and resize close: passed.
- FAQ accordion expanded/collapsed state and accessible `aria-expanded`: passed.
- Released-app download links: passed.
- Coming-soon disabled CTAs: passed.
- Scroll reveals, mission word highlighting, and reduced-motion fallback: passed.
- Focus indicators, semantic headings, button labels, and image alt text: passed.

## Runtime and asset checks

- All seven routes returned HTTP 200/304 during browser testing.
- Shared CSS, JavaScript, app icons, Relapsr SVG, and Relapsr phone artwork loaded without a 404.
- Every route reported all document images complete with a non-zero natural width.
- The generator passed `python3 -m py_compile generate_app_pages.py`.
- The patch passed `git diff --check`.

## QA history

1. P2 responsiveness: Relapsr's wide hero artwork extended beyond the mobile document width. Fixed by constraining the real phone artwork and clipping only its stage at the phone breakpoint. Recheck passed at 375/375 CSS px.
2. P2 asset loading: lazy Relapsr SVG story images were not decoded during the route sweep. Removed lazy loading for the small repeated product icons. Recheck passed for every image on every route.
3. P2 fidelity: the first navigation treatment used a visible capsule not present in the captured source. Removed the capsule background/border and matched the source's transparent desktop/mobile header. Side-by-side recheck passed.
4. Final desktop and mobile comparison pass found no remaining P0, P1, or P2 issues.

final result: passed
