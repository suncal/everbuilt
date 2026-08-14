/* Everbuilt — persistent scroll-morphing 3D scene, v2 "ALIVE".
   Fixed full-page canvas behind the content. ~160 instanced blocks morph
   between formations on scroll — and the scene is physically reactive:
   - scroll velocity blows wind through the blocks
   - the cursor casts a ray that repels nearby blocks
   - clicking fires a shockwave through the structure
   - entering a new formation triggers a color activation wave
   - orbital dust field adds depth
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
  scene.fog = new THREE.FogExp2(0x0b0908, 0.026);

  const camera = new THREE.PerspectiveCamera(40, 1, 0.1, 140);

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

  // ---- formations ----
  function fSkyline() {
    const pts = []; seed = 42;
    const COLS = 7, ROWS = 7, GAP = 1.15;
    for (let x = 0; x < COLS; x++) for (let z = 0; z < ROWS; z++) {
      const cx = Math.abs(x - 3), cz = Math.abs(z - 3);
      const h = Math.max(1, Math.round((1 - (cx + cz) / 6) * 5 + rand() * 2.2));
      for (let y = 0; y < h; y++) pts.push([(x - 3) * GAP, y * 0.62 + 0.31, (z - 3) * GAP]);
    }
    return pts;
  }
  function fScatter(n) {
    const pts = []; seed = 7;
    for (let i = 0; i < n; i++) {
      const r = 7 + rand() * 6, th = rand() * Math.PI * 2, ph = Math.acos(2 * rand() - 1);
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
    const X = [-4.4, 0, 4.4], H = [7, 11, 9];
    for (let i = 0; i < n; i++) {
      const t = i % 3, lvl = Math.floor(i / 3);
      const a = (lvl * 2.4 + t) % (Math.PI * 2);
      pts.push([X[t] + Math.cos(a) * 0.75, (lvl * 0.62) % (H[t] * 0.62) + 0.31, Math.sin(a) * 0.75]);
    }
    return pts;
  }
  function fHelix(n) {
    const pts = [];
    for (let i = 0; i < n; i++) {
      const t = i / n, a = t * Math.PI * 6;
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
  const formations = [skyline, fScatter(COUNT), fWall(COUNT), fTowers(COUNT), fHelix(COUNT), fCube(COUNT)];
  const cams = [
    [11, 7.5, 13, 0, 1.6, 0],
    [2, 3.5, 19, 0, 3.2, 0],
    [0, 4.2, 15, 0, 3.6, -2],
    [10, 6, 13, 0, 3, 0],
    [9, 9.5, 10, 0, 5.2, 0],
    [7.5, 4.5, 9.5, 0, 1.8, 0],
  ];
  const STOPS = [0, 0.18, 0.37, 0.56, 0.75, 1];

  // ---- instanced blocks ----
  const geo = new THREE.BoxGeometry(0.92, 0.56, 0.92);
  const mat = new THREE.MeshStandardMaterial({ roughness: 0.5, metalness: 0.18, transparent: true });
  const mesh = new THREE.InstancedMesh(geo, mat, COUNT);
  const cream = new THREE.Color(0xf2ede4);
  const terra = new THREE.Color(0xff5a28);
  const coal = new THREE.Color(0x3a332a);
  const baseColors = new Float32Array(COUNT * 3);
  seed = 7;
  const tmpColor = new THREE.Color();
  for (let i = 0; i < COUNT; i++) {
    const r = rand();
    const c = r < 0.16 ? terra : r < 0.28 ? coal : cream;
    mesh.setColorAt(i, c);
    baseColors[i * 3] = c.r; baseColors[i * 3 + 1] = c.g; baseColors[i * 3 + 2] = c.b;
  }
  mesh.instanceColor.needsUpdate = true;
  const group = new THREE.Group();
  group.add(mesh);
  scene.add(group);

  // ---- orbital dust field ----
  const DUST = 500;
  const dustGeo = new THREE.BufferGeometry();
  const dustPos = new Float32Array(DUST * 3);
  const dustPhase = new Float32Array(DUST);
  seed = 133;
  for (let i = 0; i < DUST; i++) {
    const r = 10 + rand() * 22, th = rand() * Math.PI * 2, ph = Math.acos(2 * rand() - 1);
    dustPos[i * 3] = r * Math.sin(ph) * Math.cos(th);
    dustPos[i * 3 + 1] = 2 + Math.abs(r * Math.cos(ph)) * 0.5;
    dustPos[i * 3 + 2] = r * Math.sin(ph) * Math.sin(th);
    dustPhase[i] = rand() * Math.PI * 2;
  }
  dustGeo.setAttribute('position', new THREE.BufferAttribute(dustPos, 3));
  const dust = new THREE.Points(dustGeo, new THREE.PointsMaterial({
    color: 0xffa07a, size: 0.06, transparent: true, opacity: 0.45,
    blending: THREE.AdditiveBlending, depthWrite: false,
  }));
  scene.add(dust);

  // fly-in starts + per-block phase
  seed = 99;
  const starts = [];
  for (let i = 0; i < COUNT; i++) starts.push([(rand() - 0.5) * 26, 12 + rand() * 16, (rand() - 0.5) * 26]);
  seed = 55;
  const phase = [];
  for (let i = 0; i < COUNT; i++) phase.push(rand());

  const dummy = new THREE.Object3D();
  const easeOut = t => 1 - Math.pow(1 - t, 3);
  const smooth = t => t * t * (3 - 2 * t);
  const lerp = (a, b, t) => a + (b - a) * t;

  // ---- interaction state ----
  const mouse = { x: 0, y: 0, tx: 0, ty: 0 };
  window.addEventListener('pointermove', e => {
    mouse.tx = (e.clientX / window.innerWidth) * 2 - 1;
    mouse.ty = (e.clientY / window.innerHeight) * 2 - 1;
  }, { passive: true });

  // click shockwave (epicenter in group-local space)
  const raycaster = new THREE.Raycaster();
  const ndc = new THREE.Vector2();
  let waveT = -10, waveCenter = new THREE.Vector3();
  window.addEventListener('pointerdown', e => {
    if (reduced) return;
    ndc.set((e.clientX / window.innerWidth) * 2 - 1, -(e.clientY / window.innerHeight) * 2 + 1);
    raycaster.setFromCamera(ndc, camera);
    // epicenter = point on the ray nearest the structure heart (world ~ [0,3,0])
    const heart = new THREE.Vector3(0, 3, 0);
    const toHeart = heart.clone().sub(raycaster.ray.origin);
    const along = toHeart.dot(raycaster.ray.direction);
    waveCenter = raycaster.ray.origin.clone().addScaledVector(raycaster.ray.direction, along);
    group.worldToLocal(waveCenter);
    waveT = performance.now() / 1000;
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

  function segAt(p) {
    let s = 0;
    while (s < STOPS.length - 2 && p > STOPS[s + 1]) s++;
    const span = STOPS[s + 1] - STOPS[s];
    return [s, span > 0 ? (p - STOPS[s]) / span : 0];
  }

  // activation ripple when the formation segment changes
  let lastSeg = 0, rippleT = -10;

  // scratch vectors for the cursor-repulsion ray (group-local space)
  const rayO = new THREE.Vector3(), rayD = new THREE.Vector3();
  const blockPos = new THREE.Vector3(), toBlock = new THREE.Vector3(), closest = new THREE.Vector3();
  const invMat = new THREE.Matrix4();

  let rafId = 0;
  const t0 = performance.now();
  function tick(now) {
    rafId = 0;
    const t = (now - t0) / 1000;
    const tNow = now / 1000;
    const intro = reduced ? 1 : Math.min(1, t / 1.8);

    // scroll easing + velocity ("wind")
    const gap = scrollTarget - scrollP;
    scrollP += gap * 0.075;
    const wind = reduced ? 0 : Math.max(-1, Math.min(1, gap * 14));

    const [s, segRaw] = segAt(scrollP);
    if (s !== lastSeg) { lastSeg = s; rippleT = tNow; }
    const A = formations[s], B = formations[s + 1];
    const camA = cams[s], camB = cams[s + 1];
    const seg = smooth(segRaw);

    // cursor ray in group-local space (for block repulsion)
    ndc.set(mouse.x, -mouse.y);
    raycaster.setFromCamera(ndc, camera);
    invMat.copy(group.matrixWorld).invert();
    rayO.copy(raycaster.ray.origin).applyMatrix4(invMat);
    rayD.copy(raycaster.ray.direction).transformDirection(invMat);

    const rippleAge = tNow - rippleT;
    const waveAge = tNow - waveT;
    let colorsDirty = false;

    for (let i = 0; i < COUNT; i++) {
      const local = smooth(Math.min(1, Math.max(0, (segRaw - phase[i] * 0.22) / 0.78)));
      let px = lerp(A[i][0], B[i][0], local);
      let py = lerp(A[i][1], B[i][1], local);
      let pz = lerp(A[i][2], B[i][2], local);
      if (intro < 1) {
        const ip = easeOut(Math.max(0, Math.min(1, (t - phase[i] * 0.5) / 1.4)));
        px = lerp(starts[i][0], px, ip);
        py = lerp(starts[i][1], py, ip);
        pz = lerp(starts[i][2], pz, ip);
      }
      // idle hover
      py += Math.sin(t * 1.3 + phase[i] * 6.28) * 0.04;
      // wind: fast scroll drags blocks opposite the motion, laggier blocks drift more
      py -= wind * (0.5 + phase[i] * 1.3);

      // cursor repulsion: distance from block to the pointer ray
      let glow = 0;
      if (!reduced && !narrow) {
        blockPos.set(px, py, pz);
        toBlock.copy(blockPos).sub(rayO);
        const along = toBlock.dot(rayD);
        if (along > 0) {
          closest.copy(rayO).addScaledVector(rayD, along);
          toBlock.copy(blockPos).sub(closest);
          const d = toBlock.length();
          const R = 2.4;
          if (d < R && d > 0.0001) {
            const f = (1 - d / R);
            const push = f * f * 1.1;
            toBlock.normalize();
            px += toBlock.x * push;
            py += toBlock.y * push;
            pz += toBlock.z * push;
            glow = Math.max(glow, f);
          }
        }
      }

      // click shockwave: expanding ring displacement
      if (waveAge < 1.6) {
        blockPos.set(px, py, pz);
        const d = blockPos.distanceTo(waveCenter);
        const front = waveAge * 11;
        const band = 1 - Math.min(1, Math.abs(d - front) / 1.6);
        if (band > 0) {
          const amp = band * band * (1 - waveAge / 1.6) * 0.9;
          const dir = d > 0.001 ? 1 / d : 0;
          px += (px - waveCenter.x) * dir * amp;
          py += (py - waveCenter.y) * dir * amp + amp * 0.3;
          pz += (pz - waveCenter.z) * dir * amp;
          glow = Math.max(glow, band * (1 - waveAge / 1.6));
        }
      }

      dummy.position.set(px, py, pz);
      const rot = Math.sin(local * Math.PI) * (0.6 + phase[i]) + wind * (0.4 + phase[i] * 0.6);
      dummy.rotation.set(rot * 0.7, rot, rot * 0.4);
      dummy.updateMatrix();
      mesh.setMatrixAt(i, dummy.matrix);

      // activation ripple: orange wave sweeps outward on formation change
      let mixAmt = glow * 0.85;
      if (rippleAge < 1.4) {
        const d = Math.hypot(px, py - 3, pz);
        const front = rippleAge * 13;
        const band = 1 - Math.min(1, Math.abs(d - front) / 2.2);
        if (band > 0) mixAmt = Math.max(mixAmt, band * (1 - rippleAge / 1.4));
      }
      tmpColor.setRGB(baseColors[i * 3], baseColors[i * 3 + 1], baseColors[i * 3 + 2]);
      if (mixAmt > 0.01) { tmpColor.lerp(terra, Math.min(1, mixAmt)); colorsDirty = true; }
      mesh.setColorAt(i, tmpColor);
    }
    mesh.instanceMatrix.needsUpdate = true;
    if (colorsDirty || rippleAge < 1.6 || waveAge < 1.8) mesh.instanceColor.needsUpdate = true;

    // dust drift + parallax
    dust.rotation.y = t * 0.012 + scrollP * 0.6;
    dust.position.y = -scrollP * 2.5;
    dust.material.opacity = 0.3 + 0.25 * Math.sin(t * 0.4);

    // orbit + camera path + mouse parallax
    group.rotation.y = reduced ? 0.4 : t * 0.05;
    group.rotation.z = wind * -0.03;
    mouse.x += (mouse.tx - mouse.x) * 0.05;
    mouse.y += (mouse.ty - mouse.y) * 0.05;
    camera.position.set(
      lerp(camA[0], camB[0], seg) + mouse.x * 1.1,
      lerp(camA[1], camB[1], seg) - mouse.y * 0.7,
      lerp(camA[2], camB[2], seg)
    );
    camera.lookAt(lerp(camA[3], camB[3], seg), lerp(camA[4], camB[4], seg), lerp(camA[5], camB[5], seg));

    grid.material.opacity = Math.max(0, 1 - scrollP * 5);

    renderer.render(scene, camera);
    if (!document.hidden && !(reduced && t > 2.5)) rafId = requestAnimationFrame(tick);
  }
  rafId = requestAnimationFrame(tick);
  document.addEventListener('visibilitychange', () => {
    if (!document.hidden && !rafId) rafId = requestAnimationFrame(tick);
  });
}
