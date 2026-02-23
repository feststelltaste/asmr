(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    initPhaseNav();
    initFilters();
    initSearch();
  });

  /* ------------------------------------------------------------------
     Phase nav — scroll to stage + highlight active
  ------------------------------------------------------------------ */
  function initPhaseNav() {
    var navBtns = document.querySelectorAll('.phase-nav-btn');
    var scroll  = document.querySelector('.roadmap-scroll');

    navBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var target = document.getElementById(this.dataset.target);
        if (!target || !scroll) return;
        scroll.scrollTo({ left: target.offsetLeft - scroll.offsetLeft, behavior: 'smooth' });
      });
    });

    if (!scroll) return;

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        navBtns.forEach(function (btn) {
          btn.classList.toggle('is-active', btn.dataset.target === entry.target.id);
        });
      });
    }, { root: scroll, threshold: 0.5 });

    document.querySelectorAll('.stage[id]').forEach(function (s) { observer.observe(s); });
  }

  /* ------------------------------------------------------------------
     Filter chips
  ------------------------------------------------------------------ */
  function initFilters() {
    var chips = document.querySelectorAll('.chip');
    chips.forEach(function (chip) {
      chip.addEventListener('click', function () {
        chips.forEach(function (c) { c.classList.remove('active'); });
        this.classList.add('active');
        applyFilters(getSearchTerm(), this.dataset.category);
      });
    });
  }

  /* ------------------------------------------------------------------
     Search
  ------------------------------------------------------------------ */
  function initSearch() {
    var input = document.getElementById('tech-search');
    if (!input) return;
    input.addEventListener('input', function () {
      applyFilters(this.value.trim().toLowerCase(), getActiveCategory());
    });
  }

  /* ------------------------------------------------------------------
     Shared filter logic
  ------------------------------------------------------------------ */
  function applyFilters(term, category) {
    document.querySelectorAll('.tcard').forEach(function (card) {
      var matchCat    = category === 'all' || card.dataset.category === category;
      var matchSearch = !term ||
                        (card.dataset.name || '').includes(term) ||
                        (card.dataset.desc || '').includes(term);
      card.classList.toggle('is-hidden', !(matchCat && matchSearch));
    });
    updateEmptyStates();
  }

  function getActiveCategory() {
    var a = document.querySelector('.chip.active');
    return a ? a.dataset.category : 'all';
  }

  function getSearchTerm() {
    var i = document.getElementById('tech-search');
    return i ? i.value.trim().toLowerCase() : '';
  }

  function updateEmptyStates() {
    document.querySelectorAll('.stage').forEach(function (stage) {
      var all     = stage.querySelectorAll('.tcard');
      var visible = stage.querySelectorAll('.tcard:not(.is-hidden)');
      var el      = stage.querySelector('.stage-empty--filtered');
      if (!el) return;
      var show = all.length > 0 && visible.length === 0;
      el.style.display = show ? 'flex' : 'none';
      el.setAttribute('aria-hidden', String(!show));
    });
  }

})();
