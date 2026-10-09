/* ============================================================
   Happy & Hop — site.js
   Meniu mobil, reveal la scroll, contoare, lightbox galerie.
   Fără dependențe. Tot conținutul funcționează și fără JS.
   ============================================================ */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- An curent în footer ---------- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  /* Fundalul unui overlay modal nu trebuie sa ramana accesibil cititoarelor de ecran. */
  /* Doar `inert`: nu atingem aria-hidden, ca sa nu stergem valorile deja puse in HTML
     (sprite-ul SVG). Impreuna cu aria-modal pe overlay, e suficient. */
  function setBackgroundInert(on, keep) {
    Array.prototype.forEach.call(document.body.children, function (el) {
      if (el === keep || el.tagName === 'SCRIPT') return;
      if (on) el.setAttribute('inert', '');
      else el.removeAttribute('inert');
    });
  }

  /* ---------- Meniu mobil ---------- */
  var toggle = document.querySelector('[data-nav-toggle]');
  var panel = document.getElementById('mobile-panel');
  var closeBtn = document.querySelector('[data-nav-close]');

  function openPanel() {
    if (!panel || !panel.hidden) return;
    panel.hidden = false;
    setBackgroundInert(true, panel);
    /* daca headerul era ascuns de scroll, il readucem — altfel ramane ascuns dupa inchidere */
    var hdr = document.querySelector('.site-header');
    if (hdr) hdr.classList.remove('is-hidden');
    document.body.classList.add('is-locked');
    toggle.setAttribute('aria-expanded', 'true');
    var first = panel.querySelector('a, button');
    if (first) first.focus();
    document.addEventListener('keydown', onPanelKey);
  }
  function closePanel(restoreFocus) {
    if (!panel || panel.hidden) return;
    panel.hidden = true;
    setBackgroundInert(false, panel);
    document.body.classList.remove('is-locked');
    toggle.setAttribute('aria-expanded', 'false');
    /* offsetParent e null cand butonul e display:none (desktop) — focusul s-ar pierde. */
    if (restoreFocus !== false && toggle.offsetParent !== null) toggle.focus();
    document.removeEventListener('keydown', onPanelKey);
  }
  function onPanelKey(e) {
    if (e.key === 'Escape') { closePanel(); return; }
    if (e.key !== 'Tab') return;
    var f = panel.querySelectorAll('a[href], button:not([disabled])');
    if (!f.length) return;
    var first = f[0], last = f[f.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  }
  if (toggle && panel) {
    toggle.addEventListener('click', openPanel);
    if (closeBtn) closeBtn.addEventListener('click', closePanel);
    panel.addEventListener('click', function (e) {
      if (e.target.closest('a')) closePanel();
    });
    window.addEventListener('resize', function () {
      if (window.innerWidth >= 1024) closePanel(false);
    });
  }

  /* ---------- Header care se ascunde la scroll (doar mobil) ---------- */
  var header = document.querySelector('.site-header');
  if (header) {
    var lastY = window.pageYOffset || 0;
    var ticking = false;
    var DELTA = 6;          /* ignora micro-scroll / bounce */
    var SHOW_ABOVE = 80;    /* langa varf headerul ramane mereu vizibil */

    function onScrollFrame() {
      ticking = false;
      var y = window.pageYOffset || 0;
      if (y < 0) y = 0;

      /* desktop sau meniu deschis: header mereu vizibil */
      if (window.innerWidth >= 1024 || document.body.classList.contains('is-locked')) {
        header.classList.remove('is-hidden');
        lastY = y;
        return;
      }
      if (Math.abs(y - lastY) < DELTA) return;

      if (y > lastY && y > SHOW_ABOVE) header.classList.add('is-hidden');
      else header.classList.remove('is-hidden');

      lastY = y;
    }

    window.addEventListener('scroll', function () {
      if (ticking) return;
      ticking = true;
      window.requestAnimationFrame(onScrollFrame);
    }, { passive: true });
  }

  /* ---------- Butoane fixe de contact ---------- */
  /* Bara de jos (mobil) si butonul flotant de WhatsApp (desktop) se ascund cat timp pe ecran
     se vede deja o zona cu aceleasi butoane: banda CTA, footer-ul, formularul de contact. */
  var zones = document.querySelectorAll('.cta-band, .site-footer, [data-contact-zone]');
  if (zones.length && 'IntersectionObserver' in window) {
    var visibleZones = [];
    var zio = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var i = visibleZones.indexOf(entry.target);
        if (entry.isIntersecting && i < 0) visibleZones.push(entry.target);
        else if (!entry.isIntersecting && i >= 0) visibleZones.splice(i, 1);
      });
      document.body.classList.toggle('contact-in-view', visibleZones.length > 0);
    });
    zones.forEach(function (el) { zio.observe(el); });
  }

  /* ---------- Reveal la scroll ---------- */
  var revealables = document.querySelectorAll('.reveal');
  if (revealables.length) {
    if (reduceMotion || !('IntersectionObserver' in window)) {
      revealables.forEach(function (el) { el.classList.add('is-visible'); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            io.unobserve(entry.target);
          }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
      revealables.forEach(function (el) { io.observe(el); });
    }
  }

  /* ---------- Contoare animate ---------- */
  var counters = document.querySelectorAll('[data-count]');
  if (counters.length && 'IntersectionObserver' in window && !reduceMotion) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        cio.unobserve(el);
        var target = parseFloat(el.dataset.count);
        var decimals = (el.dataset.count.split('.')[1] || '').length;
        var dur = 1100, t0 = performance.now();
        function step(now) {
          var p = Math.min((now - t0) / dur, 1);
          var eased = 1 - Math.pow(1 - p, 3);
          el.textContent = (target * eased).toFixed(decimals).replace('.', ',');
          if (p < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
      });
    }, { threshold: 0.4 });
    counters.forEach(function (el) { cio.observe(el); });
  }

  /* ---------- Baloane: animatie doar cat timp hero-ul e pe ecran ---------- */
  var hero = document.querySelector('.hero');
  var floaties = document.querySelectorAll('.floaty');
  if (hero && floaties.length && 'IntersectionObserver' in window) {
    var fio = new IntersectionObserver(function (entries) {
      var visible = entries[0].isIntersecting;
      floaties.forEach(function (el) { el.classList.toggle('is-paused', !visible); });
    }, { threshold: 0 });
    fio.observe(hero);
  }

  /* ---------- Lightbox galerie ---------- */
  var gallery = document.querySelector('[data-gallery]');
  var box = document.getElementById('lightbox');
  if (gallery && box) {
    /* Overlay-ul trebuie sa fie frate cu restul continutului, altfel `inert` pus pe <main>
       l-ar dezactiva chiar pe el. */
    if (box.parentNode !== document.body) document.body.appendChild(box);

    var items = Array.prototype.slice.call(gallery.querySelectorAll('button[data-full]'));
    var boxImg = box.querySelector('img');
    var boxCap = box.querySelector('.lightbox__cap');
    var index = 0;
    var lastFocused = null;

    function show(i) {
      index = (i + items.length) % items.length;
      var btn = items[index];
      boxImg.src = btn.dataset.full;
      boxImg.alt = btn.dataset.caption || '';
      boxCap.textContent = (index + 1) + ' / ' + items.length + ' · ' + (btn.dataset.caption || '');
    }
    function openBox(i) {
      lastFocused = document.activeElement;
      show(i);
      box.classList.add('is-open');
      box.removeAttribute('hidden');
      setBackgroundInert(true, box);
      document.body.classList.add('is-locked');
      box.querySelector('.lightbox__close').focus();
      document.addEventListener('keydown', onBoxKey);
    }
    function closeBox() {
      box.classList.remove('is-open');
      box.setAttribute('hidden', '');
      setBackgroundInert(false, box);
      document.body.classList.remove('is-locked');
      document.removeEventListener('keydown', onBoxKey);
      if (lastFocused) lastFocused.focus();
    }
    function onBoxKey(e) {
      if (e.key === 'Escape') closeBox();
      else if (e.key === 'ArrowRight') show(index + 1);
      else if (e.key === 'ArrowLeft') show(index - 1);
      else if (e.key === 'Tab') {
        var f = box.querySelectorAll('button');
        var first = f[0], last = f[f.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    }

    items.forEach(function (btn, i) {
      btn.addEventListener('click', function () { openBox(i); });
    });
    box.querySelector('.lightbox__close').addEventListener('click', closeBox);
    box.querySelector('.lightbox__prev').addEventListener('click', function () { show(index - 1); });
    box.querySelector('.lightbox__next').addEventListener('click', function () { show(index + 1); });
    box.addEventListener('click', function (e) {
      if (e.target === box) closeBox();
    });

    /* swipe pe mobil */
    var x0 = null;
    box.addEventListener('touchstart', function (e) { x0 = e.changedTouches[0].clientX; }, { passive: true });
    box.addEventListener('touchend', function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 55) show(index + (dx < 0 ? 1 : -1));
      x0 = null;
    }, { passive: true });
  }

  /* ---------- Formular contact -> WhatsApp ---------- */
  var waForm = document.querySelector('[data-wa-form]');
  if (waForm) {
    /* Formularul are `novalidate`: bulele native ale browserului apar in limba
       interfetei lui (deseori engleza). Le inlocuim cu mesaje proprii, in romana. */
    var campuri = Array.prototype.slice.call(waForm.querySelectorAll('[data-eroare]'));

    function eroareEl(camp) {
      return document.getElementById(camp.getAttribute('aria-describedby'));
    }

    function aratăEroare(camp, mesaj) {
      var el = eroareEl(camp);
      if (!el) return;
      el.textContent = mesaj;
      el.hidden = false;
      camp.setAttribute('aria-invalid', 'true');
    }

    function ștergeEroare(camp) {
      var el = eroareEl(camp);
      if (el) { el.textContent = ''; el.hidden = true; }
      camp.removeAttribute('aria-invalid');
    }

    campuri.forEach(function (camp) {
      var eveniment = camp.type === 'checkbox' ? 'change' : 'input';
      camp.addEventListener(eveniment, function () {
        if (camp.checkValidity()) ștergeEroare(camp);
      });
    });

    waForm.addEventListener('submit', function (e) {
      e.preventDefault();

      var primulInvalid = null;
      campuri.forEach(function (camp) {
        if (camp.checkValidity()) {
          ștergeEroare(camp);
        } else {
          aratăEroare(camp, camp.dataset.eroare);
          if (!primulInvalid) primulInvalid = camp;
        }
      });
      if (primulInvalid) { primulInvalid.focus(); return; }

      var nume = waForm.elements.nume.value.trim();
      var subiect = waForm.elements.subiect.value;
      var mesaj = waForm.elements.mesaj.value.trim();
      var text = 'Bună ziua! Sunt ' + nume + '.\n' + subiect + ': ' + mesaj;
      var base = (waForm.dataset.waUrl || '').split('?')[0];
      if (!base) return;
      window.open(base + '?text=' + encodeURIComponent(text), '_blank', 'noopener');
    });
  }

  /* ---------- Slider recenzii ---------- */
  document.querySelectorAll('[data-slider]').forEach(function (slider) {
    var track = slider.querySelector('[data-slider-track]');
    var prev = slider.querySelector('[data-slider-prev]');
    var next = slider.querySelector('[data-slider-next]');
    if (!track || !prev || !next) return;

    function step(dir) {
      var card = track.querySelector('.review-card');
      var gap = parseFloat(getComputedStyle(track).columnGap) || 0;
      var amount = card ? card.getBoundingClientRect().width + gap : track.clientWidth;
      track.scrollBy({ left: dir * amount, behavior: reduceMotion ? 'auto' : 'smooth' });
    }

    prev.addEventListener('click', function () { step(-1); });
    next.addEventListener('click', function () { step(1); });
  });
})();
