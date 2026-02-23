(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    initFilters();
    initSearch();
    initCards();
  });

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
    var cards = document.querySelectorAll('.tcard');

    cards.forEach(function (card) {
      var matchCat = (category === 'all' || card.dataset.category === category);
      var matchSearch = true;
      if (searchTerm) {
        matchSearch = (card.dataset.name || '').includes(searchTerm) ||
                      (card.dataset.desc || '').includes(searchTerm);
      }
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
    var stages = document.querySelectorAll('.stage');

    stages.forEach(function (stage) {
      var visible = stage.querySelectorAll('.tcard:not(.is-hidden)');
      var allCards = stage.querySelectorAll('.tcard');
      var filteredEmpty = stage.querySelector('.stage-empty--filtered');

      if (filteredEmpty) {
        var hasCards = allCards.length > 0;
        var noneVisible = visible.length === 0;
        filteredEmpty.style.display = (hasCards && noneVisible) ? 'flex' : 'none';
        filteredEmpty.setAttribute('aria-hidden', String(!(hasCards && noneVisible)));
      }
    });
  }

  /* ------------------------------------------------------------------
     Expand / collapse cards
  ------------------------------------------------------------------ */
  function initCards() {
    var cards = document.querySelectorAll('.tcard');

    cards.forEach(function (card) {
      var desc = card.querySelector('.tcard-desc');
      if (!desc) return;

      card.addEventListener('click', function () {
        var expanded = this.getAttribute('aria-expanded') === 'true';
        this.setAttribute('aria-expanded', String(!expanded));
      });
    });
  }

})();
