/* Everbuilt — site-wide interactivity.
   Requires (loaded before this file, all optional at runtime):
   gsap + ScrollTrigger, Lenis. Everything degrades gracefully. */

(function () {
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = window.matchMedia('(pointer: fine)').matches;
  var hasGsap = typeof gsap !== 'undefined';
  var hasST = hasGsap && typeof ScrollTrigger !== 'undefined';
  if (hasST) gsap.registerPlugin(ScrollTrigger);

  /* ---------- footer year ---------- */
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ---------- mobile nav ---------- */
  var toggle = document.querySelector('.nav-toggle');
  var links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open);
    });
    links.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') links.classList.remove('open');
    });
  }

  /* ---------- nav: hide on scroll down, show on up ---------- */
  var nav = document.querySelector('.nav');
  var lastY = 0;
  window.addEventListener('scroll', function () {
    var y = window.scrollY;
    if (nav) {
      nav.classList.toggle('nav-hidden', y > lastY && y > 300 && !(links && links.classList.contains('open')));
      nav.classList.toggle('nav-solid', y > 40);
    }
    lastY = y;
  }, { passive: true });

  /* ---------- smooth scrolling (Lenis) ---------- */
  if (!reduced && typeof Lenis !== 'undefined') {
    var lenis = new Lenis({ duration: 1.1, smoothWheel: true });
    if (hasST) {
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add(function (time) { lenis.raf(time * 1000); });
      gsap.ticker.lagSmoothing(0);
    } else {
      (function raf(time) { lenis.raf(time); requestAnimationFrame(raf); })(0);
    }
    // anchor links through Lenis
    document.querySelectorAll('a[href*="#"]').forEach(function (a) {
      a.addEventListener('click', function () {
        var href = a.getAttribute('href');
        var hash = href.slice(href.indexOf('#'));
        var samePage = href.indexOf('#') === 0 ||
          href.split('#')[0].replace(/^\.\//, '') === location.pathname.split('/').pop() ||
          (href.split('#')[0].endsWith('index.html') && (location.pathname.endsWith('/') || location.pathname.endsWith('index.html')));
        var target = samePage && hash.length > 1 && document.querySelector(hash);
        if (target) { lenis.scrollTo(target, { offset: -70 }); }
      });
    });
  }

  /* ---------- custom cursor (desktop only) ---------- */
  if (fine && !reduced) {
    var dot = document.createElement('div'); dot.className = 'cursor-dot';
    var ring = document.createElement('div'); ring.className = 'cursor-ring';
    document.body.appendChild(dot); document.body.appendChild(ring);
    var rx = -100, ry = -100, dx = -100, dy = -100;
    window.addEventListener('pointermove', function (e) {
      dx = e.clientX; dy = e.clientY;
      dot.style.transform = 'translate(' + dx + 'px,' + dy + 'px)';
      var hot = e.target.closest('a, button, summary, input, select, textarea, .aud-card');
      ring.classList.toggle('cursor-hot', !!hot);
    }, { passive: true });
    (function follow() {
      rx += (dx - rx) * 0.16; ry += (dy - ry) * 0.16;
      ring.style.transform = 'translate(' + rx + 'px,' + ry + 'px)';
      requestAnimationFrame(follow);
    })();
  }

  /* ---------- magnetic buttons ---------- */
  if (fine && !reduced) {
    document.querySelectorAll('.btn, .nav-cta').forEach(function (btn) {
      btn.addEventListener('pointermove', function (e) {
        var r = btn.getBoundingClientRect();
        var mx = e.clientX - r.left - r.width / 2;
        var my = e.clientY - r.top - r.height / 2;
        btn.style.transform = 'translate(' + mx * 0.18 + 'px,' + my * 0.28 + 'px)';
      });
      btn.addEventListener('pointerleave', function () {
        btn.style.transform = '';
        btn.style.transition = 'transform 0.35s cubic-bezier(0.22, 1, 0.36, 1)';
        setTimeout(function () { btn.style.transition = ''; }, 360);
      });
    });
  }

  /* ---------- card tilt ---------- */
  if (fine && !reduced) {
    document.querySelectorAll('.aud-card, .price-card, .case').forEach(function (card) {
      card.addEventListener('pointermove', function (e) {
        var r = card.getBoundingClientRect();
        var px = (e.clientX - r.left) / r.width - 0.5;
        var py = (e.clientY - r.top) / r.height - 0.5;
        card.style.transform = 'perspective(900px) rotateX(' + (-py * 4) + 'deg) rotateY(' + (px * 5) + 'deg) translateY(-4px)';
      });
      card.addEventListener('pointerleave', function () {
        card.style.transform = '';
        card.style.transition = 'transform 0.5s cubic-bezier(0.22, 1, 0.36, 1)';
        setTimeout(function () { card.style.transition = ''; }, 520);
      });
    });
  }

  /* ---------- hero intro timeline ---------- */
  var heroH1 = document.querySelector('.hero h1');
  if (hasGsap && !reduced && heroH1) {
    // split headline into word spans
    var split = [];
    heroH1.querySelectorAll('.hw').forEach(function (w) { split.push(w); });
    var tl = gsap.timeline({ defaults: { ease: 'power3.out' } });
    tl.from('.hero .kicker', { y: 24, opacity: 0, duration: 0.7 }, 0.1);
    if (split.length) {
      tl.from(split, { yPercent: 110, opacity: 0, duration: 0.9, stagger: 0.07 }, 0.25);
    } else {
      tl.from(heroH1, { y: 40, opacity: 0, duration: 0.9 }, 0.25);
    }
    tl.from('.hero .lede', { y: 26, opacity: 0, duration: 0.7 }, 0.75);
    tl.from('.hero-ctas', { y: 26, opacity: 0, duration: 0.7 }, 0.9);
    tl.from('.proof-strip > div', { y: 30, opacity: 0, duration: 0.7, stagger: 0.09 }, 1.0);
    tl.from('.scroll-hint', { opacity: 0, duration: 0.6 }, 1.4);
  }

  /* ---------- scroll reveals ---------- */
  var reveals = document.querySelectorAll('.reveal');
  if (hasST && !reduced) {
    reveals.forEach(function (el) { el.classList.add('in'); }); // neutralize CSS fallback
    reveals.forEach(function (el) {
      gsap.from(el, {
        y: 44, opacity: 0, duration: 0.9, ease: 'power3.out',
        scrollTrigger: { trigger: el, start: 'top 86%', once: true },
      });
    });
    // section headers get a little extra
    document.querySelectorAll('.section-head h2').forEach(function (h) {
      gsap.from(h, {
        clipPath: 'inset(0 0 100% 0)', y: 20, duration: 0.8, ease: 'power2.out',
        scrollTrigger: { trigger: h, start: 'top 88%', once: true },
      });
    });
    // compare table rows cascade
    document.querySelectorAll('.compare tbody tr').forEach(function (row, i) {
      gsap.from(row, {
        opacity: 0, x: -24, duration: 0.5, delay: i * 0.06, ease: 'power2.out',
        scrollTrigger: { trigger: '.compare', start: 'top 80%', once: true },
      });
    });
    // process steps draw their top border
    document.querySelectorAll('.step').forEach(function (step, i) {
      gsap.from(step, {
        opacity: 0, y: 30, duration: 0.6, delay: i * 0.12, ease: 'power2.out',
        scrollTrigger: { trigger: '.steps', start: 'top 82%', once: true },
      });
    });
  } else {
    // IntersectionObserver fallback (no GSAP): original behavior
    if ('IntersectionObserver' in window && !reduced) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
        });
      }, { threshold: 0.12 });
      reveals.forEach(function (el) { io.observe(el); });
    } else {
      reveals.forEach(function (el) { el.classList.add('in'); });
    }
  }

  /* ---------- animated counters ---------- */
  // <b data-count="2100" data-prefix="" data-suffix="+">2,100+</b>
  function animateCounter(el) {
    var end = parseFloat(el.getAttribute('data-count'));
    var prefix = el.getAttribute('data-prefix') || '';
    var suffix = el.getAttribute('data-suffix') || '';
    var dur = 1400, start = null;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min(1, (ts - start) / dur);
      p = 1 - Math.pow(1 - p, 3);
      var val = Math.round(end * p);
      el.textContent = prefix + val.toLocaleString('en-US') + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  var counters = document.querySelectorAll('[data-count]');
  if (counters.length && !reduced && 'IntersectionObserver' in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { animateCounter(en.target); cio.unobserve(en.target); }
      });
    }, { threshold: 0.6 });
    counters.forEach(function (el) { cio.observe(el); });
  }

  /* ---------- marquee duplication (seamless loop) ---------- */
  document.querySelectorAll('.marquee-track').forEach(function (track) {
    track.innerHTML += track.innerHTML;
  });

  /* ---------- form redirect targets (FormSubmit needs absolute _next) ---------- */
  var nextVal = location.origin +
    location.pathname.replace(/index\.html$/, '').replace(/\/$/, '') + '/thanks.html';
  document.querySelectorAll('input[name="_next"]').forEach(function (el) {
    el.value = nextVal;
  });
})();
