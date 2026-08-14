/* Everbuilt — site-wide interactivity.
   Requires (loaded before this file, all optional at runtime):
   gsap + ScrollTrigger, Lenis. Everything degrades gracefully. */

(function () {
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = window.matchMedia('(pointer: fine)').matches;
  var hasGsap = typeof gsap !== 'undefined';

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
    window.__lenis = lenis; // debug/verification handle
    (function raf(time) { lenis.raf(time); requestAnimationFrame(raf); })(0);
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

  /* ---------- viewfinder cursor (desktop only) ----------
     Four corner brackets orbit the pointer as a rotating diamond; near an
     interactive element they fly out and LOCK onto its corners like a
     camera viewfinder, with a contextual verb label. */
  if (fine && !reduced) {
    document.documentElement.classList.add('has-cursor');
    var curDot = document.createElement('div'); curDot.className = 'cur-dot';
    var curLabel = document.createElement('div'); curLabel.className = 'cur-label';
    var brackets = [];
    for (var bi = 0; bi < 4; bi++) {
      var b = document.createElement('div');
      b.className = 'cur-b cur-b' + bi;
      document.body.appendChild(b);
      brackets.push({ el: b, x: -100, y: -100 });
    }
    document.body.appendChild(curDot);
    document.body.appendChild(curLabel);

    var px = -100, py = -100;       // pointer
    var lockEl = null;              // element the viewfinder is locked onto
    var HOT = 'a, button, summary, input, select, textarea, [data-cursor]';

    function verbFor(el) {
      if (el.dataset.cursor) return el.dataset.cursor;
      var tag = el.tagName;
      if (tag === 'A') return 'OPEN';
      if (tag === 'BUTTON') return el.type === 'submit' ? 'SEND' : 'GO';
      if (tag === 'SUMMARY') return 'READ';
      if (tag === 'SELECT') return 'PICK';
      if (tag === 'INPUT' || tag === 'TEXTAREA') return 'TYPE';
      return 'VIEW';
    }

    window.addEventListener('pointermove', function (e) {
      px = e.clientX; py = e.clientY;
      curDot.style.transform = 'translate(' + px + 'px,' + py + 'px)';
      var hot = e.target.closest ? e.target.closest(HOT) : null;
      if (hot !== lockEl) {
        lockEl = hot;
        if (lockEl) {
          curLabel.textContent = verbFor(lockEl);
          curLabel.classList.add('on');
          curDot.classList.add('locked');
        } else {
          curLabel.classList.remove('on');
          curDot.classList.remove('locked');
        }
      }
    }, { passive: true });

    window.addEventListener('pointerdown', function () {
      curDot.classList.add('pulse');
      setTimeout(function () { curDot.classList.remove('pulse'); }, 260);
    }, { passive: true });

    (function orbit() {
      var t = performance.now() / 1000;
      var targets = [];
      if (lockEl && document.contains(lockEl)) {
        var r = lockEl.getBoundingClientRect();
        var pad = 7;
        // off-screen lock targets? release
        if (r.bottom < 0 || r.top > window.innerHeight) {
          lockEl = null; curLabel.classList.remove('on'); curDot.classList.remove('locked');
        } else {
          targets = [
            [r.left - pad, r.top - pad, 0],
            [r.right + pad, r.top - pad, 90],
            [r.right + pad, r.bottom + pad, 180],
            [r.left - pad, r.bottom + pad, 270],
          ];
          curLabel.style.transform = 'translate(' + (r.right + 14) + 'px,' + (r.top - 10) + 'px)';
        }
      }
      if (!targets.length) {
        // idle: rotating diamond around the pointer
        var rad = 17;
        for (var i = 0; i < 4; i++) {
          var a = t * 1.4 + i * Math.PI / 2;
          targets.push([px + Math.cos(a) * rad, py + Math.sin(a) * rad, (a * 180 / Math.PI) + 135]);
        }
        curLabel.style.transform = 'translate(' + (px + 22) + 'px,' + (py + 18) + 'px)';
      }
      for (var j = 0; j < 4; j++) {
        var bk = brackets[j];
        bk.x += (targets[j][0] - bk.x) * 0.22;
        bk.y += (targets[j][1] - bk.y) * 0.22;
        bk.el.style.transform = 'translate(' + bk.x + 'px,' + bk.y + 'px) rotate(' + targets[j][2] + 'deg)';
      }
      requestAnimationFrame(orbit);
    })();
  }

  /* ---------- scroll progress bar + back-to-top ---------- */
  var prog = document.createElement('div');
  prog.className = 'scroll-progress';
  document.body.appendChild(prog);

  var toTop = document.createElement('button');
  toTop.className = 'to-top';
  toTop.setAttribute('aria-label', 'Back to top');
  toTop.setAttribute('data-cursor', 'Top');
  // progress ring (r=22 → circumference ≈ 138.23) + arrow
  toTop.innerHTML =
    '<svg viewBox="0 0 48 48" aria-hidden="true">' +
    '<circle class="tt-track" cx="24" cy="24" r="22"/>' +
    '<circle class="tt-ring" cx="24" cy="24" r="22" stroke-dasharray="138.23" stroke-dashoffset="138.23"/>' +
    '<path class="tt-arrow" d="M24 30V18M24 18l-6 6M24 18l6 6"/>' +
    '</svg>';
  document.body.appendChild(toTop);
  var ttRing = toTop.querySelector('.tt-ring');
  toTop.addEventListener('click', function () {
    if (window.__lenis) {
      window.__lenis.scrollTo(0);
      // if the animation loop is throttled (background tab), hard-jump
      setTimeout(function () {
        if (window.scrollY > window.innerHeight) window.scrollTo(0, 0);
      }, 2000);
    } else {
      window.scrollTo({ top: 0, behavior: reduced ? 'auto' : 'smooth' });
    }
  });

  window.addEventListener('scroll', function () {
    var max = document.documentElement.scrollHeight - window.innerHeight;
    var p = max > 0 ? window.scrollY / max : 0;
    prog.style.width = (p * 100) + '%';
    ttRing.style.strokeDashoffset = (138.23 * (1 - p)).toFixed(1);
    toTop.classList.toggle('show', window.scrollY > window.innerHeight * 0.8);
  }, { passive: true });

  /* ---------- chapter rail (index only, desktop) ---------- */
  var railSections = [];
  document.querySelectorAll('section[id]').forEach(function (sec) {
    var k = sec.querySelector('.kicker');
    if (k && /^\d\d/.test(k.textContent.trim())) {
      railSections.push({ id: sec.id, num: k.textContent.trim().slice(0, 2), el: sec });
    }
  });
  if (railSections.length >= 4) {
    var rail = document.createElement('nav');
    rail.className = 'rail';
    rail.setAttribute('aria-label', 'Sections');
    railSections.forEach(function (s) {
      var a = document.createElement('a');
      a.href = '#' + s.id;
      a.className = 'rail-dot';
      a.innerHTML = '<span>' + s.num + '</span>';
      a.setAttribute('data-cursor', 'JUMP');
      rail.appendChild(a);
      s.link = a;
    });
    document.body.appendChild(rail);
    var railTick = false;
    function railSync() {
      railTick = false;
      var mid = window.scrollY + window.innerHeight * 0.5;
      var active = railSections[0];
      railSections.forEach(function (s) {
        if (s.el.offsetTop <= mid) active = s;
      });
      railSections.forEach(function (s) {
        s.link.classList.toggle('on', s === active);
      });
    }
    window.addEventListener('scroll', function () {
      if (!railTick) { railTick = true; setTimeout(railSync, 120); }
    }, { passive: true });
    railSync();
  }

  /* ---------- ghost numerals behind section headings ---------- */
  document.querySelectorAll('.section-head').forEach(function (head) {
    var k = head.querySelector('.kicker');
    if (k && /^\d\d/.test(k.textContent.trim())) {
      head.setAttribute('data-num', k.textContent.trim().slice(0, 2));
    }
  });

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
    // safety: if rAF was throttled (background tab), snap the intro complete
    setTimeout(function () { tl.progress(1); }, 3500);
  }

  /* ---------- scroll reveals ----------
     Class-based on purpose: a killed tween can leave an element frozen
     invisible when the user blasts past its trigger zone (scrollbar yank,
     anchor jump). A class + CSS transition can't be interrupted that way. */
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduced) {
    // stagger siblings that arrive in the same frame
    var lastTime = 0, burst = 0;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var now = performance.now();
        burst = (now - lastTime < 120) ? burst + 1 : 0;
        lastTime = now;
        en.target.style.transitionDelay = Math.min(burst * 90, 450) + 'ms';
        en.target.classList.add('in');
        io.unobserve(en.target);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
    reveals.forEach(function (el) { io.observe(el); });
    // belt-and-braces: IO can lag behind fast scrolling in some engines —
    // a throttled position check guarantees nothing stays invisible
    var checking = false;
    function sweep() {
      checking = false;
      reveals.forEach(function (el) {
        if (!el.classList.contains('in')) {
          // anything at or above the viewport line counts as seen —
          // scrolled-past sections must never sit invisible on scroll-up
          if (el.getBoundingClientRect().top < window.innerHeight * 0.98) el.classList.add('in');
        }
      });
    }
    window.addEventListener('scroll', function () {
      if (!checking) { checking = true; setTimeout(sweep, 150); }
    }, { passive: true });
    setTimeout(sweep, 3000);
  } else {
    reveals.forEach(function (el) { el.classList.add('in'); });
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
