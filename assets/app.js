/* Vital Apps · product page interactions */
(function () {
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var menuButton = document.querySelector('.menu-button');
  var mobileMenu = document.getElementById('mobile-menu');

  function closeMenu() {
    if (!menuButton || !mobileMenu) return;
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.setAttribute('aria-label', 'Open menu');
    mobileMenu.hidden = true;
    document.body.classList.remove('menu-open');
  }

  if (menuButton && mobileMenu) {
    menuButton.addEventListener('click', function () {
      var open = menuButton.getAttribute('aria-expanded') === 'true';
      if (open) return closeMenu();
      menuButton.setAttribute('aria-expanded', 'true');
      menuButton.setAttribute('aria-label', 'Close menu');
      mobileMenu.hidden = false;
      document.body.classList.add('menu-open');
    });
    mobileMenu.querySelectorAll('a').forEach(function (link) { link.addEventListener('click', closeMenu); });
    window.addEventListener('resize', function () { if (window.innerWidth > 980) closeMenu(); });
  }

  var revealed = document.querySelectorAll('.rv');
  if (!reduced && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: .11, rootMargin: '0px 0px -7% 0px' });
    revealed.forEach(function (el) { io.observe(el); });
  } else {
    revealed.forEach(function (el) { el.classList.add('in'); });
  }

  var mission = document.querySelector('.mission p');
  if (mission && !mission.dataset.split) {
    var accentWords = (mission.getAttribute('data-accent') || '').toLowerCase().split('|').filter(Boolean);
    var words = mission.textContent.trim().split(/\s+/);
    mission.textContent = '';
    words.forEach(function (word, index) {
      var span = document.createElement('span');
      var clean = word.toLowerCase().replace(/[^a-z0-9']/g, '');
      span.className = 'w' + (accentWords.indexOf(clean) !== -1 ? ' accent' : '');
      span.textContent = word;
      mission.appendChild(span);
      if (index < words.length - 1) mission.appendChild(document.createTextNode(' '));
    });
    mission.dataset.split = '1';
    var spans = mission.querySelectorAll('.w');
    if (reduced) {
      spans.forEach(function (span) { span.classList.add('lit'); });
    } else {
      var section = mission.closest('.mission');
      var ticking = false;
      var update = function () {
        ticking = false;
        var rect = section.getBoundingClientRect();
        var available = rect.height - window.innerHeight;
        var progress = available > 0 ? (-rect.top + window.innerHeight * .2) / available : 1;
        progress = Math.max(0, Math.min(1, progress));
        var lit = Math.round(progress * spans.length);
        spans.forEach(function (span, index) { span.classList.toggle('lit', index < lit); });
      };
      window.addEventListener('scroll', function () {
        if (!ticking) { ticking = true; requestAnimationFrame(update); }
      }, { passive: true });
      update();
    }
  }

  document.querySelectorAll('.faq-question').forEach(function (button) {
    button.addEventListener('click', function () {
      var answer = button.closest('.faq-item').querySelector('.faq-answer');
      var open = button.getAttribute('aria-expanded') === 'true';
      button.setAttribute('aria-expanded', String(!open));
      answer.hidden = open;
    });
  });
})();
