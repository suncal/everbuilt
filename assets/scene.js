/* Everbuilt — persistent scroll-morphing 3D scene.
   A fixed full-page canvas behind the content. ~160 instanced blocks morph
   between formations as the user scrolls:
   skyline → scattered field → wall → three towers → helix → cube.
   Degrades gracefully: no WebGL / reduced-motion → static, dimmed. */

import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js';

const canvas = document.getElementById('scene-canvas');
if (canvas) init();

function init() {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  let renderer;
  try {
    renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
  } catch (e) { canvas.remove(); return; }
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  const scene = new THREE.Scene();
  scene.fog = new THREE.FogExp2(0x0b0908, 0.028);

  const camera = new THREE.PerspectiveCamera(40, 1, 0.1, 120);

  // ---- lights ----
  scene.add(new THREE.AmbientLight(0xf2ede4, 0.5));
  const key = new THREE.DirectionalLight(0xfff1dd, 1.6);
  key.position.set(6, 14, 8);
  scene.add(key);
  const rim = new THREE.DirectionalLight(0xff5a28, 1.1);
  rim.position.set(-9, 4, -7);
  scene.add(rim);
  const fill = new THREE.PointLight(0xff5a28, 26, 36);
  fill.position.set(0, 7, -5);
  scene.add(fill);

  // ---- ground grid, fades out after the hero ----
  const grid = new THREE.GridHelper(80, 80, 0x4a4234, 0x231e17);
  grid.material.transparent = true;
  grid.position.y = -0.01;
  scene.add(grid);

  // ---- deterministic rng ----
  let seed = 42;
  const rand = () => (seed = (seed * 16807) % 2147483647) / 2147483647;

  // ---- formation generators (all must yield >= COUNT points) ----
  function fSkyline() {
    const pts = [];
    seed = 42;
    const COLS = 7, ROWS = 7, GAP = 1.15;
    for (let x = 0; x < COLS; x++) for (let z = 0; z < ROWS; z++) {
      const cx = Math.abs(x - 3), cz = Math.abs(z - 3);
      const h = Math.max(1, Math.round((1 - (cx + cz) / 6) * 5 + rand() * 2.2));
      for (let y = 0; y < h; y++) {
        pts.push([(x - 3) * GAP, y * 0.62 + 0.31, (z - 3) * GAP]);
      }
    }
    return pts;
  }
  function fScatter(n) {
    const pts = []; seed = 7;
    for (let i = 0; i < n; i++) {
      const r = 7 + rand() * 6;
      const th = rand() * Math.PI * 2;
      const ph = Math.acos(2 * rand() - 1);
      pts.push([r * Math.sin(ph) * Math.cos(th), 3.5 + r * Math.cos(ph) * 0.55, r * Math.sin(ph) * Math.sin(th) * 0.7]);
    }
    return pts;
  }
  function fWall(n) {
    const pts = []; const W = 16;
    for (let i = 0; i < n; i++) {
      const col = i % W, row = Math.floor(i / W);
      pts.push([(col - (W - 1) / 2) * 1.05, row * 0.72 + 0.4, -2 - (row % 2) * 0.15]);
    }
    return pts;
  }
  function fTowers(n) {
    const pts = []; seed = 21;
    const X = [-4.4, 0, 4.4], H = [7, 11, 9]; // mirror the 3 pricing tiers
    for (let i = 0; i < n; i++) {
      const t = i % 3;
      const lvl = Math.floor(i / 3);
      const a = (lvl * 2.4 + t) % (Math.PI * 2);
      pts.push([X[t] + Math.cos(a) * 0.75, (lvl * 0.62) % (H[t] * 0.62) + 0.31, Math.sin(a) * 0.75]);
    }
    return pts;
  }
  function fHelix(n) {
    const pts = [];
    for (let i = 0; i < n; i++) {
      const t = i / n;
      const a = t * Math.PI * 6;
      pts.push([Math.cos(a) * 4.2, t * 11 + 0.3, Math.sin(a) * 4.2]);
    }
    return pts;
  }
  function fCube(n) {
    const pts = []; const S = Math.ceil(Math.cbrt(n));
    for (let i = 0; i < n; i++) {
      const x = i % S, y = Math.floor(i / S) % S, z = Math.floor(i / (S * S));
      pts.push([(x - (S - 1) / 2) * 1.0, y * 0.64 + 0.32, (z - (S - 1) / 2) * 1.0]);
    }
    return pts;
  }

  const skyline = fSkyline();
  const COUNT = skyline.length;
  const formations = [
    skyline,
    fScatter(COUNT),
    fWall(COUNT),
    fTowers(COUNT),
    fHelix(COUNT),
    fCube(COUNT),
  ];
  // camera [pos..., lookAt...] per formation
  const cams = [
    [11, 7.5, 13, 0, 1.6, 0],
    [2, 3.5, 19, 0, 3.2, 0],
    [0, 4.2, 15, 0, 3.6, -2],
    [10, 6, 13, 0, 3, 0],
    [9, 9.5, 10, 0, 5.2, 0],
    [7.5, 4.5, 9.5, 0, 1.8, 0],
  ];
  const STOPS = [0, 0.18, 0.37, 0.56, 0.75, 1];

  // ---- instanced mesh ----
  const geo = new THREE.BoxGeometry(0.92, 0.56, 0.92);
  const mat = new THREE.MeshStandardMaterial({ roughness: 0.5, metalness: 0.18, transparent: true });
  const mesh = new THREE.InstancedMesh(geo, mat, COUNT);
  const cream = new THREE.Color(0xf2ede4);
  const terra = new THREE.Color(0xff5a28);
  const coal = new THREE.Color(0x3a332a);
  seed = 7;
  for (let i = 0; i < COUNT; i++) {
    const r = rand();
    mesh.setColorAt(i, r < 0.16 ? terra : r < 0.28 ? coal : cream);
  }
  mesh.instanceColor.needsUpdate = true;
  const group = new THREE.Group();
  group.add(mesh);
  scene.add(group);

  // fly-in start positions for the load intro
  seed = 99;
  const starts = [];
  for (let i = 0; i < COUNT; i++) {
    starts.push([(rand() - 0.5) * 26, 12 + rand() * 16, (rand() - 0.5) * 26]);
  }
  // per-block phase offsets for organic morphs
  seed = 55;
  const phase = [];
  for (let i = 0; i < COUNT; i++) phase.push(rand());

  const dummy = new THREE.Object3D();
  const easeOut = t => 1 - Math.pow(1 - t, 3);
  const smooth = t => t * t * (3 - 2 * t);
  const lerp = (a, b, t) => a + (b - a) * t;

  // ---- state ----
  const mouse = { x: 0, y: 0, tx: 0, ty: 0 };
  window.addEventListener('pointermove', e => {
    mouse.tx = (e.clientX / window.innerWidth) * 2 - 1;
    mouse.ty = (e.clientY / window.innerHeight) * 2 - 1;
  }, { passive: true });

  let scrollP = 0, scrollTarget = 0;
  function onScroll() {
    const max = document.documentElement.scrollHeight - window.innerHeight;
    scrollTarget = max > 0 ? Math.min(1, window.scrollY / max) : 0;
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  let narrow = false;
  function resize() {
    const w = window.innerWidth, h = window.innerHeight;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    narrow = camera.aspect <= 1.05;
    if (!narrow) camera.setViewOffset(w, h, -w * 0.18, h * 0.02, w, h);
    else camera.clearViewOffset();
    mat.opacity = narrow ? 0.42 : 0.95;
    group.scale.setScalar(narrow ? 0.66 : 1);
    camera.updateProjectionMatrix();
  }
  window.addEventListener('resize', resize);
  resize();

  // segment lookup for a given scroll position
  function segAt(p) {
    let s = 0;
    while (s < STOPS.length - 2 && p > STOPS[s + 1]) s++;
    const span = STOPS[s + 1] - STOPS[s];
    return [s, span > 0 ? (p - STOPS[s]) / span : 0];
  }

  let rafId = 0;
  const t0 = performance.now();
  function tick(now) {
    rafId = 0;
    const t = (now - t0) / 1000;
    const intro = reduced ? 1 : Math.min(1, t / 1.8);

    // scroll easing (buttery follow)
    scrollP += (scrollTarget - scrollP) * 0.075;
    const [s, segRaw] = segAt(scrollP);
    const A = formations[s], B = formations[s + 1];
    const camA = cams[s], camB = cams[s + 1];
    const seg = smooth(segRaw);

    for (let i = 0; i < COUNT; i++) {
      // per-block staggered morph inside the segment
      const local = smooth(Math.min(1, Math.max(0, (segRaw - phase[i] * 0.22) / 0.78)));
      let px = lerp(A[i][0], B[i][0], local);
      let py = lerp(A[i][1], B[i][1], local);
      let pz = lerp(A[i][2], B[i][2], local);
      // load intro: fly in from scattered sky
      if (intro < 1) {
        const ip = easeOut(Math.max(0, Math.min(1, (t - phase[i] * 0.5) / 1.4)));
        px = lerp(starts[i][0], px, ip);
        py = lerp(starts[i][1], py, ip);
        pz = lerp(starts[i][2], pz, ip);
      }
      // idle hover
      py += Math.sin(t * 1.3 + phase[i] * 6.28) * 0.04;
      dummy.position.set(px, py, pz);
      // tumble while in transit between formations
      const transit = Math.sin(local * Math.PI) * (1 - intro < 0.01 ? 1 : 1);
      const rot = Math.sin(local * Math.PI) * (0.6 + phase[i]);
      dummy.rotation.set(rot * 0.7, rot, rot * 0.4);
      dummy.updateMatrix();
      mesh.setMatrixAt(i, dummy.matrix);
    }
    mesh.instanceMatrix.needsUpdate = true;

    // slow orbit + camera path
    group.rotation.y = reduced ? 0.4 : t * 0.05;
    mouse.x += (mouse.tx - mouse.x) * 0.05;
    mouse.y += (mouse.ty - mouse.y) * 0.05;
    camera.position.set(
      lerp(camA[0], camB[0], seg) + mouse.x * 1.1,
      lerp(camA[1], camB[1], seg) - mouse.y * 0.7,
      lerp(camA[2], camB[2], seg)
    );
    camera.lookAt(lerp(camA[3], camB[3], seg), lerp(camA[4], camB[4], seg), lerp(camA[5], camB[5], seg));

    // floor grid only belongs to the skyline
    grid.material.opacity = Math.max(0, 1 - scrollP * 5);

    renderer.render(scene, camera);
    if (!document.hidden && !(reduced && t > 2.5)) rafId = requestAnimationFrame(tick);
  }
  rafId = requestAnimationFrame(tick);
  document.addEventListener('visibilitychange', () => {
    if (!document.hidden && !rafId) rafId = requestAnimationFrame(tick);
  });
}
