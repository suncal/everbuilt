/* Everbuilt hero — "The Build": instanced blocks assemble into a structure.
   Loaded as an ES module. Renders into #hero-canvas, degrades gracefully:
   no WebGL / reduced-motion / small screens → static CSS hero remains. */

import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js';

const canvas = document.getElementById('hero-canvas');
const heroEl = document.querySelector('.hero');
if (canvas && heroEl) init();

function init() {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  let renderer;
  try {
    renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
  } catch (e) {
    canvas.remove();
    return;
  }
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  const scene = new THREE.Scene();
  scene.fog = new THREE.Fog(0x12100c, 18, 42);

  const camera = new THREE.PerspectiveCamera(38, 1, 0.1, 100);
  const camBase = new THREE.Vector3(11, 7.5, 13);
  camera.position.copy(camBase);
  camera.lookAt(0, 1.2, 0);

  // ---- lights ----
  scene.add(new THREE.AmbientLight(0xf5f1e8, 0.55));
  const key = new THREE.DirectionalLight(0xfff4e0, 1.5);
  key.position.set(6, 12, 8);
  scene.add(key);
  const rim = new THREE.DirectionalLight(0xc2481b, 0.9);
  rim.position.set(-8, 4, -6);
  scene.add(rim);
  const fill = new THREE.PointLight(0xc2481b, 18, 30);
  fill.position.set(0, 6, -4);
  scene.add(fill);

  // ---- ground grid (blueprint floor) ----
  const grid = new THREE.GridHelper(60, 60, 0x3a342a, 0x241f18);
  grid.position.y = -0.01;
  scene.add(grid);

  // ---- the structure: a skyline of blocks on a grid ----
  const COLS = 7, ROWS = 7, GAP = 1.15;
  const targets = [];
  const heightMap = [];
  // deterministic pseudo-random so the build is stable
  let seed = 42;
  const rand = () => (seed = (seed * 16807) % 2147483647) / 2147483647;

  for (let x = 0; x < COLS; x++) {
    for (let z = 0; z < ROWS; z++) {
      const cx = Math.abs(x - (COLS - 1) / 2), cz = Math.abs(z - (ROWS - 1) / 2);
      const centrality = 1 - (cx + cz) / ((COLS - 1) / 2 + (ROWS - 1) / 2);
      const h = Math.max(1, Math.round(centrality * 5 + rand() * 2.2));
      heightMap.push(h);
      for (let y = 0; y < h; y++) {
        targets.push({
          x: (x - (COLS - 1) / 2) * GAP,
          y: y * 0.62 + 0.31,
          z: (z - (ROWS - 1) / 2) * GAP,
          delay: (x + z) * 0.055 + y * 0.12 + rand() * 0.15,
          phase: rand() * Math.PI * 2,
        });
      }
    }
  }

  const COUNT = targets.length;
  const geo = new THREE.BoxGeometry(0.92, 0.56, 0.92);
  const mat = new THREE.MeshStandardMaterial({ roughness: 0.55, metalness: 0.15, transparent: true });
  const mesh = new THREE.InstancedMesh(geo, mat, COUNT);

  const cream = new THREE.Color(0xf5f1e8);
  const terra = new THREE.Color(0xc2481b);
  const ink = new THREE.Color(0x2a251d);
  seed = 7;
  for (let i = 0; i < COUNT; i++) {
    const r = rand();
    mesh.setColorAt(i, r < 0.14 ? terra : r < 0.24 ? ink : cream);
  }
  mesh.instanceColor.needsUpdate = true;

  const group = new THREE.Group();
  group.add(mesh);
  scene.add(group);

  // scattered start positions (blocks "fly in")
  seed = 99;
  const starts = targets.map(t => ({
    x: t.x * (2.5 + rand() * 2),
    y: t.y + 8 + rand() * 14,
    z: t.z * (2.5 + rand() * 2),
    rot: (rand() - 0.5) * Math.PI * 2,
  }));

  const dummy = new THREE.Object3D();
  const easeOutCubic = t => 1 - Math.pow(1 - t, 3);

  // ---- interaction state ----
  const mouse = { x: 0, y: 0, tx: 0, ty: 0 };
  window.addEventListener('pointermove', (e) => {
    mouse.tx = (e.clientX / window.innerWidth) * 2 - 1;
    mouse.ty = (e.clientY / window.innerHeight) * 2 - 1;
  }, { passive: true });

  let scrollP = 0; // 0 at top → 1 when hero scrolled past
  const onScroll = () => {
    const h = heroEl.offsetHeight || 1;
    scrollP = Math.min(1, Math.max(0, window.scrollY / h));
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // ---- sizing ----
  // Wide screens: shift the structure right so it lives beside the copy.
  // Narrow screens: shrink + dim it and push it below the copy.
  function resize() {
    const w = heroEl.clientWidth, h = heroEl.clientHeight;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    if (camera.aspect > 1.05) {
      camera.setViewOffset(w, h, -w * 0.22, h * 0.04, w, h);
      group.scale.setScalar(1);
      mat.opacity = 1;
    } else {
      camera.setViewOffset(w, h, 0, -h * 0.2, w, h);
      group.scale.setScalar(0.62);
      mat.opacity = 0.38;
    }
    camera.updateProjectionMatrix();
  }
  window.addEventListener('resize', resize);
  resize();

  // ---- render loop (paused when hero off-screen or tab hidden) ----
  let visible = true, rafId = 0;
  new IntersectionObserver((en) => {
    visible = en[0].isIntersecting;
    if (visible && !rafId) rafId = requestAnimationFrame(tick);
  }).observe(heroEl);
  document.addEventListener('visibilitychange', () => {
    if (!document.hidden && visible && !rafId) rafId = requestAnimationFrame(tick);
  });

  const t0 = performance.now();
  function tick(now) {
    rafId = 0;
    const t = (now - t0) / 1000;

    for (let i = 0; i < COUNT; i++) {
      const tg = targets[i], st = starts[i];
      let p = reduced ? 1 : Math.min(1, Math.max(0, (t - tg.delay) / 1.6));
      p = easeOutCubic(p);
      const hover = p >= 1 ? Math.sin(t * 1.4 + tg.phase) * 0.035 : 0;
      // scroll gently lifts the structure apart again
      const lift = scrollP * scrollP * (2.5 + (i % 5));
      dummy.position.set(
        st.x + (tg.x - st.x) * p,
        st.y + (tg.y - st.y) * p + hover + lift * (tg.y / 4),
        st.z + (tg.z - st.z) * p
      );
      const r = st.rot * (1 - p);
      dummy.rotation.set(r, r, r * 0.6);
      dummy.updateMatrix();
      mesh.setMatrixAt(i, dummy.matrix);
    }
    mesh.instanceMatrix.needsUpdate = true;

    group.rotation.y = reduced ? 0.5 : t * 0.07 + scrollP * 0.9;

    // mouse parallax (lerped)
    mouse.x += (mouse.tx - mouse.x) * 0.05;
    mouse.y += (mouse.ty - mouse.y) * 0.05;
    camera.position.x = camBase.x + mouse.x * 1.2;
    camera.position.y = camBase.y - mouse.y * 0.8 + scrollP * 3;
    camera.lookAt(0, 1.2 - scrollP * 1.5, 0);

    renderer.render(scene, camera);
    if (visible && !document.hidden && !(reduced && t > 2)) {
      rafId = requestAnimationFrame(tick);
    }
  }
  rafId = requestAnimationFrame(tick);
}
