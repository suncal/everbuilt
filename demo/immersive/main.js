/* =========================================================
   VOLTA° — scroll IS the camera.
   The page is a corridor in 3D space. Scrolling flies the
   camera down it, straight through solid objects (in → out),
   and every DOM section travels on the same perspective rig.
   three.js vendored in ./vendor — no CDN at runtime.
   ========================================================= */
import * as THREE from 'three';
import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js';
import { UnrealBloomPass } from 'three/addons/postprocessing/UnrealBloomPass.js';
import { OutputPass } from 'three/addons/postprocessing/OutputPass.js';

const REDUCED = matchMedia('(prefers-reduced-motion: reduce)').matches;
const params = new URLSearchParams(location.search);

/* Embed mode: the site is running inside a preview frame on another page. */
const EMBED = params.get('embed') === '1';

/* Phone budget — the site claims 60fps on old hardware, so it has to earn it.
   Preview frames opt in too: they render small, so nobody can see the
   difference, and a page can show two of them at once. */
const MOBILE = innerWidth < 760 || EMBED || matchMedia('(pointer: coarse)').matches;
const DPR_CAP = MOBILE ? 1.3 : 1.75;
const lerp  = (a, b, t) => a + (b - a) * t;
const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
const smoothstep = (e0, e1, x) => { const t = clamp((x - e0) / (e1 - e0), 0, 1); return t * t * (3 - 2 * t); };

/* Depth of the whole corridor, in world units. Scroll maps onto this. */
const DEPTH = 400;
const START_Z = 26;

/* =========================================================
   MONOLITH STYLES — two treatments of the same geometry.

   'corridor' : six monoliths strung down −Z. Scroll flies the camera
                straight through them — in one side, out the other.
   'orbit'    : one monolith held at the origin. Scroll swings the camera
                around and past it on a keyframed path, and the form
                itself spikes and settles as you travel.

   Both drive the DOM depth rig identically — the page always moves in 3D.
   ========================================================= */
const STYLES = ['corridor', 'orbit'];

/* Nothing can scroll a preview frame, so it scrolls itself — a slow ping-pong
   down the page and back, showing the whole effect untouched. */
const EMBED_LEG = 15;            // seconds for one full pass, each direction

/* `&phase=0.5` offsets where in the loop this frame starts. Two previews on
   one page must NOT run in lockstep — side by side showing the same section
   is a worse comparison than either one alone. */
const EMBED_PHASE = parseFloat(params.get('phase')) || 0;

function embedProgress(t) {
  const shifted = t + EMBED_PHASE * EMBED_LEG * 2;
  const phase = (shifted % (EMBED_LEG * 2)) / EMBED_LEG;   // 0→2
  const tri = phase <= 1 ? phase : 2 - phase;        // 0→1→0
  return tri * tri * (3 - 2 * tri);                  // ease the turnarounds
}
let STYLE = params.get('style');
if (!STYLES.includes(STYLE)) {
  try { STYLE = localStorage.getItem('volta:style'); } catch { STYLE = null; }
}
if (!STYLES.includes(STYLE)) STYLE = 'corridor';

/* camera path for 'orbit', sampled by scroll progress */
const ORBIT_KEYS = [
  { at: 0.00, pos: [ 0.0,  0.10, 16.5], morph: 0.05, bloom: 0.34 },
  { at: 0.22, pos: [ 3.4,  1.00, 13.6], morph: 0.50, bloom: 0.50 },
  { at: 0.46, pos: [-3.8, -1.00, 12.2], morph: 0.90, bloom: 0.66 },
  { at: 0.70, pos: [ 2.1,  2.00, 14.4], morph: 0.40, bloom: 0.46 },
  { at: 1.00, pos: [ 0.0,  0.00, 19.0], morph: 0.10, bloom: 0.32 },
];
function sampleOrbit(p) {
  let a = ORBIT_KEYS[0], b = ORBIT_KEYS[ORBIT_KEYS.length - 1];
  for (let i = 0; i < ORBIT_KEYS.length - 1; i++) {
    if (p >= ORBIT_KEYS[i].at && p <= ORBIT_KEYS[i + 1].at) { a = ORBIT_KEYS[i]; b = ORBIT_KEYS[i + 1]; break; }
  }
  const t0 = clamp((p - a.at) / ((b.at - a.at) || 1), 0, 1);
  const t = t0 * t0 * (3 - 2 * t0);
  return {
    pos: [lerp(a.pos[0], b.pos[0], t), lerp(a.pos[1], b.pos[1], t), lerp(a.pos[2], b.pos[2], t)],
    morph: lerp(a.morph, b.morph, t),
    bloom: lerp(a.bloom, b.bloom, t),
  };
}

/* =========================================================
   1. RENDERER / SCENE
   ========================================================= */
const canvas = document.getElementById('gl');
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, powerPreference: 'high-performance' });
renderer.setPixelRatio(Math.min(devicePixelRatio, DPR_CAP));
renderer.setSize(innerWidth, innerHeight);
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 0.9;

const scene = new THREE.Scene();
scene.fog = new THREE.FogExp2(0x08080a, 0.021);

const camera = new THREE.PerspectiveCamera(58, innerWidth / innerHeight, 0.1, 400);
camera.position.set(0, 0, START_Z);

/* procedural studio environment — no external HDR file */
function makeEnv() {
  const c = document.createElement('canvas');
  c.width = 512; c.height = 256;
  const g = c.getContext('2d');
  const grad = g.createLinearGradient(0, 0, 0, 256);
  grad.addColorStop(0.00, '#161822');
  grad.addColorStop(0.38, '#5d6070');
  grad.addColorStop(0.50, '#f2ead9');
  grad.addColorStop(0.62, '#7d5f37');
  grad.addColorStop(1.00, '#0a0a0c');
  g.fillStyle = grad; g.fillRect(0, 0, 512, 256);
  for (const [x, col] of [[110, 'rgba(110,168,255,.5)'], [400, 'rgba(201,162,39,.45)']]) {
    const r = g.createRadialGradient(x, 118, 0, x, 118, 130);
    r.addColorStop(0, col); r.addColorStop(1, 'rgba(0,0,0,0)');
    g.fillStyle = r; g.fillRect(x - 130, 0, 260, 256);
  }
  const tex = new THREE.CanvasTexture(c);
  tex.mapping = THREE.EquirectangularReflectionMapping;
  tex.colorSpace = THREE.SRGBColorSpace;
  return tex;
}
const envMap = makeEnv();
scene.environment = envMap;

/* =========================================================
   2. SHARED NOISE + VERTEX DISPLACEMENT
   ========================================================= */
const uniforms = {
  uTime:     { value: 0 },
  uProgress: { value: 0 },
  uMorph:    { value: 0 },
};

const NOISE_GLSL = /* glsl */`
  vec3 mod289(vec3 x){return x-floor(x*(1./289.))*289.;}
  vec4 mod289(vec4 x){return x-floor(x*(1./289.))*289.;}
  vec4 permute(vec4 x){return mod289(((x*34.)+1.)*x);}
  vec4 taylorInvSqrt(vec4 r){return 1.79284291400159-0.85373472095314*r;}
  float snoise(vec3 v){
    const vec2 C=vec2(1./6.,1./3.); const vec4 D=vec4(0.,.5,1.,2.);
    vec3 i=floor(v+dot(v,C.yyy)); vec3 x0=v-i+dot(i,C.xxx);
    vec3 g=step(x0.yzx,x0.xyz); vec3 l=1.-g;
    vec3 i1=min(g.xyz,l.zxy); vec3 i2=max(g.xyz,l.zxy);
    vec3 x1=x0-i1+C.xxx; vec3 x2=x0-i2+C.yyy; vec3 x3=x0-D.yyy;
    i=mod289(i);
    vec4 p=permute(permute(permute(i.z+vec4(0.,i1.z,i2.z,1.))
      +i.y+vec4(0.,i1.y,i2.y,1.))+i.x+vec4(0.,i1.x,i2.x,1.));
    float n_=.142857142857; vec3 ns=n_*D.wyz-D.xzx;
    vec4 j=p-49.*floor(p*ns.z*ns.z);
    vec4 x_=floor(j*ns.z); vec4 y_=floor(j-7.*x_);
    vec4 x=x_*ns.x+ns.yyyy; vec4 y=y_*ns.x+ns.yyyy; vec4 h=1.-abs(x)-abs(y);
    vec4 b0=vec4(x.xy,y.xy); vec4 b1=vec4(x.zw,y.zw);
    vec4 s0=floor(b0)*2.+1.; vec4 s1=floor(b1)*2.+1.; vec4 sh=-step(h,vec4(0.));
    vec4 a0=b0.xzyw+s0.xzyw*sh.xxyy; vec4 a1=b1.xzyw+s1.xzyw*sh.zzww;
    vec3 p0=vec3(a0.xy,h.x); vec3 p1=vec3(a0.zw,h.y);
    vec3 p2=vec3(a1.xy,h.z); vec3 p3=vec3(a1.zw,h.w);
    vec4 norm=taylorInvSqrt(vec4(dot(p0,p0),dot(p1,p1),dot(p2,p2),dot(p3,p3)));
    p0*=norm.x;p1*=norm.y;p2*=norm.z;p3*=norm.w;
    vec4 m=max(.6-vec4(dot(x0,x0),dot(x1,x1),dot(x2,x2),dot(x3,x3)),0.); m=m*m;
    return 42.*dot(m*m,vec4(dot(p0,x0),dot(p1,x1),dot(p2,x2),dot(p3,x3)));
  }
`;

function displace(shader) {
  shader.uniforms.uTime = uniforms.uTime;
  shader.uniforms.uProgress = uniforms.uProgress;
  shader.uniforms.uMorph = uniforms.uMorph;
  shader.vertexShader = shader.vertexShader
    .replace('#include <common>', `#include <common>
       uniform float uTime; uniform float uProgress; uniform float uMorph;
       ${NOISE_GLSL}`)
    .replace('#include <begin_vertex>', `#include <begin_vertex>
       float n  = snoise(normal * 1.25 + uTime * 0.14);
       float n2 = snoise(normal * 2.7  - uTime * 0.19);
       float amp = 0.34 + uMorph * 0.70;
       transformed += normal * (n * amp + n2 * amp * 0.26);`);
}

/* =========================================================
   3. THE CORRIDOR
   Six monolith "stations" the camera flies straight through,
   linked by gate rings and a particle tunnel.
   ========================================================= */
const corridor = new THREE.Group();
scene.add(corridor);

/* --- 3a. monoliths: camera passes inside, then out --- */
const LOOKS = [
  { r: 6.0, hue: 0.11, spin:  0.9 },
  { r: 6.8, hue: 0.58, spin: -0.7 },
  { r: 6.2, hue: 0.03, spin:  1.1 },
  { r: 7.2, hue: 0.42, spin: -0.6 },
  { r: 6.5, hue: 0.14, spin:  0.8 },
  { r: 7.6, hue: 0.52, spin: -0.9 },
];

const monoGeo = new THREE.IcosahedronGeometry(1, MOBILE ? 12 : 24);
const shellGeo = new THREE.IcosahedronGeometry(1, 3);
const monoliths = LOOKS.map(s => {
  const g = new THREE.Group();

  const mat = new THREE.MeshStandardMaterial({
    color: new THREE.Color().setHSL(s.hue, 0.18, 0.72),
    metalness: 1.0, roughness: 0.22,
    envMap, envMapIntensity: 1.0,
    flatShading: true,
    side: THREE.DoubleSide,       // so the inside is a real place when we fly through
    transparent: true, opacity: 1,
  });
  mat.onBeforeCompile = displace;
  const core = new THREE.Mesh(monoGeo, mat);
  core.scale.setScalar(s.r);
  g.add(core);

  const wireMat = new THREE.MeshBasicMaterial({
    color: 0xc9a227, wireframe: true, transparent: true, opacity: 0.16,
  });
  wireMat.onBeforeCompile = displace;
  const wire = new THREE.Mesh(shellGeo, wireMat);
  wire.scale.setScalar(s.r * 1.42);
  g.add(wire);

  corridor.add(g);
  return { group: g, core, wire, mat, wireMat, data: s, z: 0 };
});

/* Park each monolith in the GAP between two content sections, so the
   punch-through always happens during a transition — never on top of
   something you were trying to read. */
function placeStations() {
  if (STYLE === 'orbit') {
    /* one hero form at the origin; the rest sit out this style */
    monoliths.forEach((m, i) => {
      m.group.visible = i === 0;
      if (i === 0) { m.z = 0; m.group.position.set(0, 0, 0); m.group.scale.setScalar(0.34); }
    });
    rings.forEach(r => { r.visible = false; });
    return;
  }

  monoliths.forEach(m => { m.group.visible = true; m.group.scale.setScalar(1); });
  rings.forEach(r => { r.visible = true; });

  const blocks = [...document.querySelectorAll('main > section, main > .marquee, main > .foot')];
  const max = Math.max(1, document.body.scrollHeight - innerHeight);
  const seams = blocks.slice(1).map(b => {
    const y = b.getBoundingClientRect().top + scrollY;      // seam in document space
    return clamp((y - innerHeight / 2) / max, 0, 1);        // scroll ratio at the seam
  });

  /* keep the opening screen clear, and never stack two punch-throughs
     on top of each other however the page reflows */
  /* LAST stops short of the contact block — the conversion screen never
     gets a monolith parked on top of it. */
  const FIRST = 0.17, MIN_GAP = 0.115, LAST = 0.78;
  let prev = FIRST - MIN_GAP;
  monoliths.forEach((m, i) => {
    const seam = seams[i] ?? (i + 1) / (monoliths.length + 1);
    const ratio = clamp(Math.max(seam, prev + MIN_GAP), FIRST, LAST);
    prev = ratio;
    m.z = START_Z - ratio * DEPTH;
    m.group.position.set(Math.sin(i * 1.9) * 2.6, Math.cos(i * 1.4) * 1.9, m.z);
  });
}

/* --- 3b. gate rings streaming past --- */
const ringGeo = new THREE.TorusGeometry(1, 0.008, 5, 110);
const RING_GAP = 15;
const rings = [];
for (let i = 0; i < (MOBILE ? 16 : 26); i++) {
  const m = new THREE.Mesh(ringGeo, new THREE.MeshBasicMaterial({
    color: i % 3 === 0 ? 0xc9a227 : 0x9fb6d8,
    transparent: true, opacity: 0.12, blending: THREE.AdditiveBlending, depthWrite: false,
  }));
  m.position.z = 10 - i * RING_GAP;
  m.position.x = Math.sin(i * 0.7) * 2.2;
  m.position.y = Math.cos(i * 0.55) * 1.6;
  m.scale.setScalar(7 + Math.sin(i * 0.9) * 2.6);
  m.rotation.z = i * 0.31;
  corridor.add(m);
  rings.push(m);
}

/* --- 3c. particle tunnel --- */
const P_COUNT = MOBILE ? 1500 : 3400;
const pPos = new Float32Array(P_COUNT * 3);
const pSeed = new Float32Array(P_COUNT);
for (let i = 0; i < P_COUNT; i++) {
  const a = Math.random() * Math.PI * 2;
  const rad = 5 + Math.pow(Math.random(), 0.6) * 26;
  pPos[i * 3]     = Math.cos(a) * rad;
  pPos[i * 3 + 1] = Math.sin(a) * rad * 0.8;
  pPos[i * 3 + 2] = 24 - Math.random() * (DEPTH + 60);
  pSeed[i] = Math.random();
}
const pGeo = new THREE.BufferGeometry();
pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
pGeo.setAttribute('aSeed', new THREE.BufferAttribute(pSeed, 1));

const particles = new THREE.Points(pGeo, new THREE.ShaderMaterial({
  transparent: true, depthWrite: false, blending: THREE.AdditiveBlending,
  uniforms: { uTime: uniforms.uTime },
  vertexShader: /* glsl */`
    uniform float uTime;
    attribute float aSeed; varying float vA;
    void main(){
      vec3 p = position;
      float a = uTime * (0.05 + aSeed * 0.07);
      p.xy = mat2(cos(a), -sin(a), sin(a), cos(a)) * p.xy;
      vec4 mv = modelViewMatrix * vec4(p, 1.0);
      gl_PointSize = (aSeed * 2.4 + 0.7) * (30.0 / max(1.0, -mv.z));
      gl_Position = projectionMatrix * mv;
      vA = smoothstep(90.0, 8.0, -mv.z) * (0.2 + aSeed * 0.8);
    }`,
  fragmentShader: /* glsl */`
    varying float vA;
    void main(){
      float d = length(gl_PointCoord - 0.5);
      if (d > 0.5) discard;
      gl_FragColor = vec4(vec3(0.93, 0.91, 0.87), vA * smoothstep(0.5, 0.0, d));
    }`,
}));
scene.add(particles);

/* --- 3d. lights --- */
scene.add(new THREE.AmbientLight(0xffffff, 0.4));
const key = new THREE.DirectionalLight(0xfff2d8, 2.2); key.position.set(4, 5, 6); scene.add(key);
const rim = new THREE.DirectionalLight(0x6ea8ff, 1.5); rim.position.set(-6, -2, -4); scene.add(rim);
const travel = new THREE.PointLight(0xffe9c4, 3.2, 42, 2);   // rides with the camera
scene.add(travel);

/* =========================================================
   4. POST
   ========================================================= */
const composer = new EffectComposer(renderer);
composer.setPixelRatio(Math.min(devicePixelRatio, DPR_CAP));
composer.setSize(innerWidth, innerHeight);
composer.addPass(new RenderPass(scene, camera));
const bloom = new UnrealBloomPass(new THREE.Vector2(innerWidth, innerHeight), 0.42, 0.7, 0.5);
composer.addPass(bloom);
composer.addPass(new OutputPass());

/* =========================================================
   5. SCROLL + POINTER
   ========================================================= */
const S = { raw: 0, smooth: 0, vel: 0 };
const M = { x: 0, y: 0, sx: 0, sy: 0 };

function readScroll() {
  const max = Math.max(1, document.body.scrollHeight - innerHeight);
  S.raw = clamp(scrollY / max, 0, 1);
}
addEventListener('scroll', readScroll, { passive: true });
addEventListener('pointermove', e => {
  M.x = (e.clientX / innerWidth) * 2 - 1;
  M.y = (e.clientY / innerHeight) * 2 - 1;
}, { passive: true });

/* =========================================================
   6. DOM DEPTH RIG
   Every section (and tagged child) rides the same perspective
   camera: far away below the fold, flat while you read it,
   then rushing past the viewer as you scroll on.
   ========================================================= */
const DEAD = 0.30;                 // readable dead-zone around screen centre
const depthEls = [...document.querySelectorAll('[data-depth]')];

/* Anything already on screen at load has "arrived" — it must never be
   pushed down the corridor, only fly past once you scroll beyond it. */
function measureFirstScreen() {
  for (const el of depthEls) {
    const prev = el.style.transform;
    el.style.transform = 'none';
    el.__arrived = el.getBoundingClientRect().top + scrollY < innerHeight * 0.98;
    el.style.transform = prev;
  }
}

function easeOut(p) {              // 0 inside the dead zone, ±1 at the edges
  const s = Math.sign(p);
  return s * clamp((Math.abs(p) - DEAD) / (1 - DEAD), 0, 1);
}

function driveDOM() {
  if (REDUCED) return;
  const vh = innerHeight;
  for (const el of depthEls) {
    const f = +el.dataset.depth || 1;
    const r = el.getBoundingClientRect();
    if (r.bottom < -vh * 0.6 || r.top > vh * 1.9) { el.style.visibility = 'hidden'; continue; }
    el.style.visibility = '';

    const p = ((r.top + r.height / 2) - vh / 2) / vh;
    let e = easeOut(p);
    if (e > 0 && el.__arrived) e = 0;          // no "incoming" for the opening screen

    /* Outgoing panels scale up as they pass the lens, so they have to
       clear out fast — a few translucent slabs stacked at 2x will
       otherwise black out the whole viewport. */
    const out = e < 0;
    const z = -e * (out ? 400 : 660) * f;
    const rx = -e * 9 * f;
    const op = 1 - clamp(Math.abs(e) * (out ? 1.55 : 1.15), 0, 1);

    if (op <= 0.02) { el.style.visibility = 'hidden'; continue; }
    el.style.transform = `translate3d(0,0,${z.toFixed(1)}px) rotateX(${rx.toFixed(2)}deg)`;
    el.style.opacity = op.toFixed(3);
  }
}

/* =========================================================
   7. LOOP
   ========================================================= */
const clock = new THREE.Clock();

function frame() { requestAnimationFrame(frame); step(); }

function step() {
  const t = clock.getElapsedTime();
  const prev = S.smooth;

  /* In a preview frame, drive the document scroll ourselves so the WebGL
     camera AND the DOM depth rig both animate exactly as they would for a
     real visitor — no special-cased "demo" motion path to drift out of sync. */
  if (EMBED && !REDUCED) {
    S.raw = embedProgress(t);
    scrollTo(0, S.raw * Math.max(1, document.body.scrollHeight - innerHeight));
  }

  S.smooth = lerp(S.smooth, S.raw, REDUCED ? 1 : 0.08);
  S.vel = S.smooth - prev;
  M.sx = lerp(M.sx, M.x, 0.045);
  M.sy = lerp(M.sy, M.y, 0.045);

  uniforms.uTime.value = t;
  uniforms.uProgress.value = S.smooth;

  const orbit = STYLE === 'orbit';
  const k = orbit ? sampleOrbit(S.smooth) : null;

  /* --- camera: down the corridor, or around the hero form --- */
  let camZ, lookZ;
  if (orbit) {
    camZ = k.pos[2];
    lookZ = 0;
    camera.position.x = k.pos[0] + M.sx * 1.5;
    camera.position.y = k.pos[1] - M.sy * 1.1;
  } else {
    camZ = START_Z - S.smooth * DEPTH;
    lookZ = camZ - 30;
    camera.position.x = Math.sin(S.smooth * 5.2) * 2.4 + M.sx * 2.2;
    camera.position.y = Math.cos(S.smooth * 4.1) * 1.7 - M.sy * 1.6;
  }
  camera.position.z = camZ;
  camera.lookAt(
    orbit ? M.sx * 0.5 : Math.sin(S.smooth * 5.2 + 0.6) * 1.2 + M.sx * 0.9,
    orbit ? -M.sy * 0.4 : Math.cos(S.smooth * 4.1 + 0.6) * 0.9 - M.sy * 0.7,
    lookZ
  );
  camera.rotation.z += Math.sin(S.smooth * 3.4) * (orbit ? 0.05 : 0.09) + S.vel * 2.2;  // roll, after lookAt
  travel.position.set(camera.position.x, camera.position.y, camZ - (orbit ? 2 : 4));

  /* --- how "inside" the form we are: proximity in corridor, keyframed in orbit --- */
  let insideAny = 0;
  for (const m of monoliths) {
    if (!m.group.visible) continue;
    const near = orbit
      ? k.morph * 0.55
      : clamp(1 - Math.abs(camZ - m.z) / 46, 0, 1);
    insideAny = Math.max(insideAny, near);

    m.group.rotation.y = t * 0.07 * m.data.spin + S.smooth * (orbit ? 3.1 : 2.2) * m.data.spin;
    m.group.rotation.x = Math.sin(t * 0.16 + m.z) * 0.22;
    m.wire.rotation.y = -t * 0.05 * m.data.spin;
    m.wire.scale.setScalar(m.data.r * (1.42 + near * 0.34));

    // dissolve the skin as we punch through it, so "inside" is a place
    m.mat.opacity = 1 - near * (orbit ? 0.30 : 0.62);
    m.mat.envMapIntensity = 1.0 + near * 1.4;
    m.wireMat.opacity = 0.12 + near * 0.34;
    m.core.scale.setScalar(m.data.r * (1 + near * 0.1));
  }
  uniforms.uMorph.value = lerp(
    uniforms.uMorph.value,
    orbit ? k.morph : 0.25 + insideAny * 0.9,
    0.09
  );

  /* --- rings recycle so the tunnel never ends (corridor only) --- */
  if (!orbit) {
    const span = rings.length * RING_GAP;
    for (const r of rings) {
      let rel = r.position.z - camZ;
      while (rel > 18)          { r.position.z -= span; rel -= span; }
      while (rel < -span + 18)  { r.position.z += span; rel += span; }
      r.rotation.z += 0.0016;
      const ahead = -rel;                                  // distance in front of camera
      const band = clamp(1 - Math.abs(ahead - 90) / 130, 0, 1);
      const nearFade = smoothstep(6, 40, ahead);           // don't smear across the lens
      r.material.opacity = 0.26 * band * nearFade;
    }
  }

  /* --- atmosphere responds to depth --- */
  scene.fog.density = orbit ? 0.030 + insideAny * 0.020 : 0.019 + insideAny * 0.030;
  bloom.strength = (orbit ? k.bloom : 0.34 + insideAny * 0.75) + Math.abs(S.vel) * 6;
  renderer.toneMappingExposure = 0.9 - insideAny * 0.18;

  driveDOM();
  composer.render();
}

function syncSize() {
  const w = Math.max(1, innerWidth), h = Math.max(1, innerHeight);
  camera.aspect = w / h;
  camera.updateProjectionMatrix();
  renderer.setSize(w, h);
  composer.setSize(w, h);
  measureFirstScreen();
  placeStations();
  readScroll();
}
addEventListener('resize', syncSize, { passive: true });

/* A page opened in a background tab can report 0×0 and never fire a resize
   when it's finally shown — which would leave the canvas blank. Re-sync on
   the way back to visible. */
addEventListener('visibilitychange', () => {
  if (document.visibilityState === 'visible') syncSize();
});

/* =========================================================
   8. LOADER
   ========================================================= */
const loaderEl = document.getElementById('loader');
const barEl = document.getElementById('loaderBar');
const pctEl = document.getElementById('loaderPct');

function openTheDoors() {
  loaderEl.classList.add('is-done');
  document.body.classList.remove('is-loading');
  document.querySelectorAll('.hero .line, .hero .reveal, .hero__title')
    .forEach((el, i) => setTimeout(() => el.classList.add('in'), i * 90));
  startCounters();
}

if (EMBED) {
  /* A preview frame has no time to spend on a loading bar — and every
     reveal must be resolved, because the frame starts mid-page. */
  openTheDoors();
  document.querySelectorAll('.reveal, .line').forEach(el => el.classList.add('in'));
} else {

document.body.classList.add('is-loading');

let pct = 0;
const tick = setInterval(() => {
  pct = Math.min(100, pct + Math.random() * 13 + 5);
  barEl.style.width = pct + '%';
  pctEl.textContent = Math.round(pct);
  if (pct >= 100) {
    clearInterval(tick);
    setTimeout(openTheDoors, 360);
  }
}, 130);

}   // end !EMBED

/* debug handle — lets a background tab (where rAF is throttled) render a
   deterministic, fully-settled frame for screenshot verification */
window.__volta = {
  camera, monoliths, S, DEPTH, START_Z,
  settle() { readScroll(); S.smooth = S.raw; for (let i = 0; i < 3; i++) step(); },
};

syncSize();
driveDOM();
renderer.compile(scene, camera);
frame();

/* =========================================================
   9. DOM INTERACTION
   ========================================================= */
const io = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
}, { threshold: 0.15, rootMargin: '0px 0px -6% 0px' });
document.querySelectorAll('.reveal, .line').forEach(el => io.observe(el));

/* manifesto words light as they cross the middle */
const mws = [...document.querySelectorAll('.mw')];
function litManifesto() {
  const mid = innerHeight * 0.62;
  mws.forEach(w => w.classList.toggle('lit', w.getBoundingClientRect().top < mid));
}

const nav = document.getElementById('nav');
let lastY = 0;
function navState() {
  const y = scrollY;
  nav.classList.toggle('is-stuck', y > 40);
  nav.classList.toggle('is-hidden', y > lastY && y > 320);
  lastY = y;
}
addEventListener('scroll', () => { navState(); litManifesto(); }, { passive: true });
litManifesto();

/* =========================================================
   MONOLITH STYLE SWITCH
   Swaps the treatment live — no reload, no scroll jump — and
   remembers the choice so a shared ?style= link lands right.
   ========================================================= */
const switchEl = document.getElementById('styleSwitch');

function applyStyle(name, persist = true) {
  if (!STYLES.includes(name)) return;
  STYLE = name;
  placeStations();
  switchEl?.querySelectorAll('button').forEach(b =>
    b.classList.toggle('is-on', b.dataset.style === name));
  document.documentElement.dataset.sceneStyle = name;
  if (persist) {
    try { localStorage.setItem('volta:style', name); } catch { /* private mode */ }
    const u = new URL(location.href);
    u.searchParams.set('style', name);
    history.replaceState(null, '', u);
  }
}

switchEl?.addEventListener('click', e => {
  const b = e.target.closest('button[data-style]');
  if (b) applyStyle(b.dataset.style);
});

applyStyle(STYLE, false);        // reflect the resolved style in the UI at boot

/* depth indicator in the footer/nav rail */
const railEl = document.getElementById('railFill');
addEventListener('scroll', () => {
  if (railEl) railEl.style.transform = `scaleY(${S.raw.toFixed(3)})`;
}, { passive: true });

function startCounters() {
  document.querySelectorAll('[data-count]').forEach(el => {
    const target = +el.dataset.count;
    const t0 = performance.now();
    (function step(now) {
      const p = clamp((now - t0) / 1600, 0, 1);
      el.textContent = Math.round(target * (1 - Math.pow(1 - p, 3)));
      if (p < 1) requestAnimationFrame(step);
    })(t0);
  });
}

/* custom cursor */
const cur = document.getElementById('cursor');
const curLabel = document.getElementById('cursorLabel');
const C = { x: innerWidth / 2, y: innerHeight / 2, tx: innerWidth / 2, ty: innerHeight / 2 };
addEventListener('pointermove', e => { C.tx = e.clientX; C.ty = e.clientY; }, { passive: true });
(function curLoop() {
  C.x = lerp(C.x, C.tx, 0.18); C.y = lerp(C.y, C.ty, 0.18);
  cur.style.transform = `translate(${C.x}px, ${C.y}px) translate(-50%, -50%)`;
  requestAnimationFrame(curLoop);
})();
document.querySelectorAll('[data-cursor], a, button').forEach(el => {
  el.addEventListener('pointerenter', () => {
    cur.classList.add('is-active');
    curLabel.textContent = el.dataset.cursor || '';
  });
  el.addEventListener('pointerleave', () => {
    cur.classList.remove('is-active');
    curLabel.textContent = '';
  });
});

/* =========================================================
   10. PROCEDURAL PROJECT THUMBNAILS (no stock, no network)
   ========================================================= */
document.querySelectorAll('.proj__canvas').forEach(cv => {
  const cs = getComputedStyle(cv.closest('.proj'));
  const a = cs.getPropertyValue('--a').trim() || '#e8dcc8';
  const b = cs.getPropertyValue('--b').trim() || '#8a6a3f';
  const seed = +cv.dataset.seed || 1;
  const W = 1280, H = 800;
  cv.width = W; cv.height = H;
  const g = cv.getContext('2d');

  const grad = g.createLinearGradient(0, 0, W, H);
  grad.addColorStop(0, b); grad.addColorStop(1, '#0a0a0c');
  g.fillStyle = grad; g.fillRect(0, 0, W, H);

  const rg = g.createRadialGradient(W * (0.3 + seed * 0.12), H * 0.32, 0, W * 0.4, H * 0.4, W * 0.7);
  rg.addColorStop(0, a + 'cc'); rg.addColorStop(1, 'rgba(0,0,0,0)');
  g.globalCompositeOperation = 'screen';
  g.fillStyle = rg; g.fillRect(0, 0, W, H);
  g.globalCompositeOperation = 'source-over';

  g.strokeStyle = 'rgba(255,255,255,.16)'; g.lineWidth = 1.2;
  for (let i = 0; i < 34; i++) {
    g.beginPath();
    for (let x = 0; x <= W; x += 8) {
      const y = H * 0.5
        + Math.sin(x * 0.006 + i * 0.42 + seed) * (52 + i * 5)
        + Math.cos(x * 0.013 - i * 0.3 + seed * 2) * 26
        + (i - 17) * 21;
      x === 0 ? g.moveTo(x, y) : g.lineTo(x, y);
    }
    g.stroke();
  }

  const vg = g.createRadialGradient(W / 2, H / 2, H * 0.28, W / 2, H / 2, H * 0.86);
  vg.addColorStop(0, 'rgba(0,0,0,0)'); vg.addColorStop(1, 'rgba(0,0,0,.62)');
  g.fillStyle = vg; g.fillRect(0, 0, W, H);
  const img = g.getImageData(0, 0, W, H), d = img.data;
  for (let i = 0; i < d.length; i += 4) {
    const n = (Math.random() - 0.5) * 16;
    d[i] += n; d[i + 1] += n; d[i + 2] += n;
  }
  g.putImageData(img, 0, 0);
});

/* =========================================================
   11. FORM (demo only — nothing leaves the browser)
   ========================================================= */
const form = document.getElementById('form');
const note = document.getElementById('formNote');
form.addEventListener('submit', e => {
  e.preventDefault();
  if (!form.checkValidity()) { note.textContent = 'Please complete every field.'; return; }
  const name = new FormData(form).get('name');
  note.textContent = `Thanks ${name} — brief received. We reply within one business day. (Demo: not sent anywhere.)`;
  form.reset();
});

const clockEl = document.getElementById('clock');
setInterval(() => {
  clockEl.textContent = new Date().toLocaleTimeString('en-US',
    { timeZone: 'America/New_York', hour: '2-digit', minute: '2-digit', second: '2-digit' }) + ' ATL';
}, 1000);
