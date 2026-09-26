# Energy story — scroll-driven product page

A rebuild of the *principles* behind a battery-storage website concept (not a copy of its brand or assets).
Everything is a single `index.html`: no build step and no dependencies apart from a Google Font.
Open it in a browser.

## How it works

| Stage | What happens | Where in code |
|---|---|---|
| 1. Loader | Maroon screen → hero fades in behind a logo + 0→100% counter, slow camera push-in | `Loader sequence` (JS), `.loader` (CSS) |
| 2. Hero | Full-bleed aerial scene, pill nav, big headline bottom-left, CTAs bottom-right, lines slide up | `buildHero()`, `.hero*`, `.nav` |
| 3. Reveal | Sticky paragraph; words go from 20% → 100% opacity as you scroll | `.reveal`, `words` in `update()` |
| 4. Build-up | Pinned section, 7 steps from raw material to full system. Orange line art draws itself in (`stroke-dashoffset`), outgoing step shrinks and fades, labels alternate left and right | `STEPS`, `draw*()` functions, `buildProgress()` |
| 5. Closing | Light section with stats + CTA | `.closing` |

## Customising

- **Brand**: colors and font are CSS variables at the top of `<style>`; the logo is the `#mark` symbol; search "halden" for the name.
- **Hero image**: `buildHero()` draws an SVG placeholder. To use a real photo or video, replace the `<svg id="heroScene">` inside `.hero__media` with an `<img>`/`<video>` (`object-fit: cover`) and remove the `buildHero()` call.
- **Steps**: edit the `STEPS` array. Each step has text plus a `draw(add, addCircle)` function that emits SVG paths; drawings are auto-fitted to the same box. The isometric helpers (`iso`, `boxEdges`, `ribsX/Y`) make boxes and containers quick to sketch.
- **Pacing**: `build.style.height` sets scroll length per step; `LEAD`/`HOLD` control how early the first drawing starts and how long the last one holds.
