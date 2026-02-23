(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    initPhaseNav();
    initFilters();
    initSearch();
    initCards();
  });

  /* ------------------------------------------------------------------
     Phase nav — scroll to stage + highlight active
  ------------------------------------------------------------------ */
  function initPhaseNav() {
    var navBtns = document.querySelectorAll('.phase-nav-btn');
    var scroll  = document.querySelector('.roadmap-scroll');

    // Click → scroll stage into view
    navBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var target = document.getElementById(this.dataset.target);
        if (!target || !scroll) return;

        // Scroll the roadmap container so the stage left-edge is visible
        var scrollLeft = target.offsetLeft - scroll.offsetLeft;
        scroll.scrollTo({ left: scrollLeft, behavior: 'smooth' });
      });
    });

    // Highlight whichever stage is most visible in the scroll container
    if (!scroll) return;

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var stageId = entry.target.id; // "stage-hold-on" etc.
        navBtns.forEach(function (btn) {
          btn.classList.toggle('is-active', btn.dataset.target === stageId);
        });
      });
    }, {
      root: scroll,
      threshold: 0.5
    });

    document.querySelectorAll('.stage[id]').forEach(function (stage) {
      observer.observe(stage);
    });
  }

  /* ------------------------------------------------------------------
     Filter chips
  ------------------------------------------------------------------ */
  function initFilters() {
    var chips = document.querySelectorAll('.chip');

    chips.forEach(function (chip) {
      chip.addEventListener('click', function () {
        var cat = this.dataset.category;
        chips.forEach(function (c) { c.classList.remove('active'); });
        this.classList.add('active');
        applyFilters(getSearchTerm(), cat);
      });
    });
  }

  /* ------------------------------------------------------------------
     Search box
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
  function applyFilters(searchTerm, category) {
    document.querySelectorAll('.tcard').forEach(function (card) {
      var matchCat    = (category === 'all' || card.dataset.category === category);
      var matchSearch = !searchTerm ||
                        (card.dataset.name || '').includes(searchTerm) ||
                        (card.dataset.desc || '').includes(searchTerm);
      card.classList.toggle('is-hidden', !(matchCat && matchSearch));
    });
    updateEmptyStates();
  }

  function getActiveCategory() {
    var active = document.querySelector('.chip.active');
    return active ? active.dataset.category : 'all';
  }

  function getSearchTerm() {
    var input = document.getElementById('tech-search');
    return input ? input.value.trim().toLowerCase() : '';
  }

  /* ------------------------------------------------------------------
     Empty states per stage
  ------------------------------------------------------------------ */
  function updateEmptyStates() {
    document.querySelectorAll('.stage').forEach(function (stage) {
      var allCards    = stage.querySelectorAll('.tcard');
      var visibleCards = stage.querySelectorAll('.tcard:not(.is-hidden)');
      var filteredEmpty = stage.querySelector('.stage-empty--filtered');
      if (!filteredEmpty) return;

      var showEmpty = allCards.length > 0 && visibleCards.length === 0;
      filteredEmpty.style.display = showEmpty ? 'flex' : 'none';
      filteredEmpty.setAttribute('aria-hidden', String(!showEmpty));
    });
  }

  /* ------------------------------------------------------------------
     Expand / collapse cards
  ------------------------------------------------------------------ */
  function initCards() {
    document.querySelectorAll('.tcard').forEach(function (card) {
      if (!card.querySelector('.tcard-desc')) return;
      card.addEventListener('click', function () {
        var expanded = this.getAttribute('aria-expanded') === 'true';
        this.setAttribute('aria-expanded', String(!expanded));
      });
    });
  }

})();
