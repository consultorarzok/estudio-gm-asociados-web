(function () {
  var d = document, root = d.documentElement;
  var quieto = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Apertura: solo una vez por sesión y sin reduced-motion
  // (la clase .anim la pone el script en línea del <head> antes de pintar, para que no parpadee)
  if (root.classList.contains('anim')) {
    try { sessionStorage.setItem('gm-intro', '1'); } catch (e) {}
    {
      var go = function () { requestAnimationFrame(function () { requestAnimationFrame(function () { root.classList.add('listo'); }); }); };
      var img = d.querySelector('.hero .fondo img');
      if (img && !img.complete) { img.addEventListener('load', go, { once: true }); setTimeout(go, 900); } else go();
    }
  }


  // Header: sólido al bajar, se esconde al bajar rápido, vuelve al subir
  var top = d.querySelector('.top'), wa = d.querySelector('.wa'), last = 0, tick = false;
  var hero = d.querySelector('.hero');
  function onScroll() {
    var y = window.scrollY, h = hero ? hero.offsetHeight : 400;
    if (top && !top.classList.contains('abierto')) {
      top.classList.toggle('solid', y > h - 90);
      top.classList.toggle('oculto', y > h && y > last + 4);
      if (y < last - 4) top.classList.remove('oculto');
    }
    if (wa) wa.classList.toggle('ver', y > h * 0.6);
    // parallax suave en fotos
    if (!quieto) {
      var bg = d.querySelector('.hero .fondo img');
      if (bg && y < h) bg.style.setProperty('--py', (y * 0.25).toFixed(1) + 'px');
      d.querySelectorAll('.para img').forEach(function (im) {
        var r = im.parentNode.getBoundingClientRect();
        if (r.bottom > 0 && r.top < innerHeight) {
          var c = (r.top + r.height / 2 - innerHeight / 2) / innerHeight;
          im.style.setProperty('--py', (c * -36).toFixed(1) + 'px');
        }
      });
    }
    manifiesto();
    last = y; tick = false;
  }
  addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(onScroll); } }, { passive: true });

  // Menú móvil
  var btn = d.querySelector('.abrir');
  if (btn) btn.addEventListener('click', function () {
    var o = top.classList.toggle('abierto');
    btn.setAttribute('aria-expanded', o);
    d.body.style.overflow = o ? 'hidden' : '';
  });
  d.querySelectorAll('nav.menu a').forEach(function (a) {
    a.addEventListener('click', function () { top.classList.remove('abierto'); if (btn) btn.setAttribute('aria-expanded', false); d.body.style.overflow = ''; });
  });
  d.addEventListener('keydown', function (e) { if (e.key === 'Escape' && top && top.classList.contains('abierto')) btn.click(); });

  // Manifiesto: palabras que se encienden con el scroll
  var man = d.querySelector('.manifiesto p.frase'), palabras = [];
  if (man) {
    man.innerHTML = man.textContent.trim().split(/\s+/).map(function (w) { return '<span class="w">' + w + '</span>'; }).join(' ');
    palabras = man.querySelectorAll('.w');
  }
  function manifiesto() {
    if (!man || quieto) return;
    var r = man.getBoundingClientRect();
    var prog = (innerHeight * 0.85 - r.top) / (r.height + innerHeight * 0.35);
    var n = Math.round(Math.max(0, Math.min(1, prog)) * palabras.length);
    palabras.forEach(function (w, i) { w.classList.toggle('on', i < n); });
  }

  // Revelados al entrar en pantalla
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('visto'); io.unobserve(e.target); } });
  }, { rootMargin: '0px 0px -12% 0px', threshold: 0.12 });
  d.querySelectorAll('.revela,.sube,.pasos').forEach(function (el) { io.observe(el); });

  // Mapas: se cargan sólo si la persona los pide (página más liviana)
  d.querySelectorAll('.mapa .cargar').forEach(function (b) {
    b.addEventListener('click', function () {
      var f = d.createElement('iframe');
      f.src = b.dataset.src; f.title = b.dataset.title; f.loading = 'lazy'; f.referrerPolicy = 'no-referrer-when-downgrade';
      b.replaceWith(f);
    });
  });

  onScroll();
})();
