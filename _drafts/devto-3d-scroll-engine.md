<!-- PUBLISH TO: dev.to (DR ~90). Tags: threejs, javascript, webdev, showdev.
     Paste as-is; dev.to renders this markdown directly.
     This is the piece with Hacker News / r/webdev potential — post it there
     AFTER it's live on dev.to, linking the dev.to article or the site itself. -->

# I built a scroll-morphing 3D website with no framework, no build step, and $0/month hosting

Our studio needed a website that *was* the portfolio piece. The result is [everbuiltstudio.com](https://everbuiltstudio.com): ~160 blocks that assemble into a skyline, then reform into a wall, three towers, a helix, and finally a cube as you scroll — with the camera flying between formations. One `scene.js`, Three.js from a CDN, static files on free hosting.

Here's the architecture, and the three bugs that taught me the most.

## One InstancedMesh, six formations

Everything is a single `THREE.InstancedMesh` — one draw call for all blocks. A "formation" is just an array of target positions:

```js
const formations = [skyline, scatter, wall, towers, helix, cube];
const STOPS = [0, 0.18, 0.37, 0.56, 0.75, 1]; // scroll fractions
```

Each frame, map scroll progress to a segment between two formations and lerp every block — with a per-block phase offset so blocks travel as a staggered swarm instead of one rigid object:

```js
const local = smooth(clamp((segRaw - phase[i] * 0.22) / 0.78));
px = lerp(A[i][0], B[i][0], local);
```

Blocks also tumble in transit (`sin(local * π)` peaks mid-flight), which sells the physicality for free.

## The scene reacts to you

Three cheap tricks that make it feel "alive":

- **Wind:** I don't smooth scroll position separately — the easing gap `scrollTarget - scrollP` *is* the velocity signal. Fast scrolling drags blocks against the motion.
- **Cursor repulsion:** unproject the pointer into a ray, compute each block's distance to it, push blocks out radially. On ~160 instances this is nothing per frame.
- **Click shockwave:** an expanding spherical front displaces blocks as it passes. Band-pass on `abs(dist - front)`, decay over 1.6s.

## Bug 1: `scroll-behavior: smooth` froze the entire page

We use Lenis for inertial scrolling. Lenis writes `scrollTop` every frame; CSS `scroll-behavior: smooth` told the browser to *animate* each of those one-frame writes. Result: the page could not scroll at all. If you use any JS smooth-scroll library, that CSS line must go.

## Bug 2: scroll-triggered tweens can die mid-flight

Our reveals were GSAP tweens with `once: true` ScrollTriggers. Yank the scrollbar fast enough to blast *past* an element's whole trigger zone and the trigger killed a half-played tween — leaving the section frozen at opacity 0 forever. The fix that can't fail: IntersectionObserver adds a class, CSS transition does the animation. A class, once added, can't be killed mid-flight. I kept GSAP only for the load-time hero intro, which has no scroll dependency.

## Bug 3: `position: sticky` table columns silently don't stick

Mobile comparison table, sticky first column. Two separate landmines: sticky cells don't pin under `border-collapse: collapse` (Chrome), and they also don't pin if the table itself has `overflow: hidden` (we had it for border-radius). Both had to change, mobile-only.

## Performance notes

- `setPixelRatio(min(devicePixelRatio, 2))` desktop, `1.5` on phones
- Pause the rAF loop when the tab is hidden; on narrow screens, dim and shrink the scene so text always wins
- The whole page is static files on GitHub Pages — the hosting bill is genuinely $0/month, which happens to be our studio's entire pitch

Full site: [everbuiltstudio.com](https://everbuiltstudio.com) · repo: [github.com/suncal/everbuilt](https://github.com/suncal/everbuilt)

*Questions about the formation math or the cursor system? Ask below — happy to go deeper.*
