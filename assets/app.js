/* Vital Apps · shared app-page behaviour */
(function () {
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Scroll reveals */
  var revealed = document.querySelectorAll('.rv');
  if (!reduced && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('in');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    revealed.forEach(function (el) { io.observe(el); });
  } else {
    revealed.forEach(function (el) { el.classList.add('in'); });
  }

  /* Mission text: words light up as you scroll through the section */
  var mission = document.querySelector('.mission p');
  if (mission && !mission.dataset.split) {
    var accentWords = (mission.getAttribute('data-accent') || '').toLowerCase().split('|').filter(Boolean);
    var words = mission.textContent.trim().split(/\s+/);
    mission.textContent = '';
    words.forEach(function (word, i) {
      var span = document.createElement('span');
      span.className = 'w';
      var clean = word.toLowerCase().replace(/[^a-z0-9']/g, '');
      if (accentWords.indexOf(clean) !== -1) span.className += ' accent';
      span.textContent = word;
      mission.appendChild(span);
      if (i < words.length - 1) mission.appendChild(document.createTextNode(' '));
    });
    mission.dataset.split = '1';

    var spans = mission.querySelectorAll('.w');
    if (reduced) {
      spans.forEach(function (s) { s.classList.add('lit'); });
    } else {
      var ticking = false;
      var section = mission.closest('.mission') || mission;
      var update = function () {
        ticking = false;
        var rect = section.getBoundingClientRect();
        var vh = window.innerHeight;
        /* progress across the tall sticky region: 0 as it pins, 1 before it releases */
        var total = rect.height - vh;
        var progress = total > 0 ? (-rect.top + vh * 0.25) / total : 1;
        progress = Math.max(0, Math.min(1, progress));
        var litCount = Math.round(progress * spans.length);
        spans.forEach(function (s, i) { s.classList.toggle('lit', i < litCount); });
      };
      var onScroll = function () {
        if (!ticking) { ticking = true; requestAnimationFrame(update); }
      };
      window.addEventListener('scroll', onScroll, { passive: true });
      update();
    }
  }
})();
