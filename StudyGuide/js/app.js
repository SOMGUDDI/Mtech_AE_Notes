/**
 * M.Tech Automotive Engineering Study Guide — Core Application Engine
 * Offline-First: Theme Controller, Smart Token Search, Bookmarks, Local Notes & Progress.
 */

(function () {
  'use strict';

  // 1. Theme Controller
  window.toggleTheme = function () {
    const isDark = document.body.classList.toggle('dark');
    const theme = isDark ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('sg-theme', theme);
    localStorage.setItem('mtech_theme', theme);
    updateThemeToggleIcons(isDark);
  };

  function updateThemeToggleIcons(isDark) {
    const buttons = document.querySelectorAll('.theme-toggle-btn, #themeToggle, #themeBtn');
    buttons.forEach(btn => {
      const textSpan = btn.querySelector('span:not(.icon)');
      if (textSpan) {
        textSpan.textContent = isDark ? 'Light' : 'Dark';
      }
    });
  }

  function initTheme() {
    const saved = localStorage.getItem('sg-theme') || localStorage.getItem('mtech_theme') || 'light';
    if (saved === 'dark') {
      document.body.classList.add('dark');
      document.documentElement.setAttribute('data-theme', 'dark');
      updateThemeToggleIcons(true);
    } else {
      document.body.classList.remove('dark');
      document.documentElement.setAttribute('data-theme', 'light');
      updateThemeToggleIcons(false);
    }
  }

  // 2. Search Engine & Modal Controller
  let currentSubjectFilter = 'all';

  function getRelativeRootPrefix() {
    const path = window.location.pathname.replace(/\\/g, '/');
    if (path.includes('/topics/')) return '../../';
    if (path.includes('/subjects/') || path.includes('/semesters/') || path.includes('/sem-1/')) return '../';
    return './';
  }

  function htmlEscape(str) {
    return String(str || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  window.openSearchModal = function () {
    const modal = document.getElementById('searchModal');
    if (modal) {
      modal.classList.add('open');
      const input = document.getElementById('searchInput');
      if (input) {
        input.focus();
        if (input.value) window.handleSearch(input.value);
      }
    }
  };

  window.closeSearchModal = function (event) {
    if (event && event.target && event.target.id !== 'searchModal' && !event.target.classList.contains('search-modal-close')) {
      return;
    }
    const modal = document.getElementById('searchModal');
    if (modal) {
      modal.classList.remove('open');
    }
  };

  window.setSearchFilter = function (subject) {
    currentSubjectFilter = subject;
    document.querySelectorAll('.search-filter-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.subject === subject);
    });
    const input = document.getElementById('searchInput');
    if (input) window.handleSearch(input.value);
  };

  // Robust Search Token Matcher & Scorer
  window.handleSearch = async function (query) {
    const resultsContainer = document.getElementById('searchResults');
    if (!resultsContainer) return;

    query = (query || '').trim();
    if (!query) {
      resultsContainer.innerHTML = '<div class="search-empty-state"><span>Type keywords to search across 33+ comprehensive M.Tech topics...</span></div>';
      return;
    }

    // Ensure search index is available
    let index = window.SEARCH_INDEX;
    if (!index || !Array.isArray(index) || index.length === 0) {
      try {
        const rootPrefix = getRelativeRootPrefix();
        const res = await fetch(rootPrefix + 'data/search-index.json');
        index = await res.json();
        window.SEARCH_INDEX = index;
      } catch (err) {
        console.warn('Failed to load search index JSON:', err);
      }
    }

    if (!index || !Array.isArray(index) || index.length === 0) {
      resultsContainer.innerHTML = '<div class="search-empty-state"><span>Search index is loading, please try again...</span></div>';
      return;
    }

    const rootPrefix = getRelativeRootPrefix();

    // Extract clean tokens (letters & digits)
    const rawTokens = query.toLowerCase().match(/[a-z0-9]+/g) || [];
    if (rawTokens.length === 0) {
      resultsContainer.innerHTML = '<div class="search-empty-state"><span>Please enter valid search terms.</span></div>';
      return;
    }

    const scoredResults = [];
    const queryLower = query.toLowerCase();

    for (const item of index) {
      const itemSubject = (item.subject || '').toLowerCase();
      if (currentSubjectFilter !== 'all' && itemSubject !== currentSubjectFilter) {
        continue;
      }

      const title = (item.title || '').toLowerCase();
      const moduleName = (item.module || '').toLowerCase();
      const summary = (item.summary || '').toLowerCase();
      const keywords = (typeof item.keywords === 'string' ? item.keywords : (item.keywords || []).join(' ')).toLowerCase();
      const subjectTitle = (item.subject_title || '').toLowerCase();

      let score = 0;

      // Exact phrase match bonus
      if (title.includes(queryLower)) score += 120;
      if (keywords.includes(queryLower)) score += 50;
      if (summary.includes(queryLower)) score += 40;

      // Token-level scoring
      let matchedTokens = 0;
      for (const token of rawTokens) {
        let tokenFound = false;
        if (title.includes(token)) {
          score += 35;
          tokenFound = true;
        }
        if (moduleName.includes(token)) {
          score += 20;
          tokenFound = true;
        }
        if (subjectTitle.includes(token)) {
          score += 15;
          tokenFound = true;
        }
        if (keywords.includes(token)) {
          score += 10;
          tokenFound = true;
        }
        if (summary.includes(token)) {
          score += 8;
          tokenFound = true;
        }
        if (tokenFound) matchedTokens++;
      }

      // If at least half of tokens match, or at least 1 token for short queries
      if (score > 0 && (matchedTokens >= Math.ceil(rawTokens.length / 2) || rawTokens.length === 1)) {
        scoredResults.push({ item, score });
      }
    }

    // Sort by score descending
    scoredResults.sort((a, b) => b.score - a.score);

    if (scoredResults.length === 0) {
      resultsContainer.innerHTML = `<div class="search-empty-state"><span>No matching topics found for "<strong>${htmlEscape(query)}</strong>". Try broader keywords.</span></div>`;
      return;
    }

    const topResults = scoredResults.slice(0, 10);
    resultsContainer.innerHTML = topResults.map(({ item }) => {
      const itemUrl = item.url ? (rootPrefix + item.url) : `${rootPrefix}topics/${item.subject}/${item.id}.html`;
      const subjTitle = item.subject_title || item.subject_code || item.subject;
      const snippet = (item.summary || '').slice(0, 160);

      return `
        <div class="search-result-item">
          <a class="search-result-title" href="${itemUrl}">${htmlEscape(item.title)}</a>
          <div class="search-result-meta">${htmlEscape(subjTitle)} &bull; ${htmlEscape(item.module || '')}</div>
          <div class="search-result-snippet">${htmlEscape(snippet)}...</div>
        </div>
      `;
    }).join('');
  };

  // Keyboard shortcut Ctrl+K or '/'
  window.addEventListener('keydown', (e) => {
    if ((e.key === '/' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') ||
        ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k')) {
      e.preventDefault();
      window.openSearchModal();
    } else if (e.key === 'Escape') {
      const modal = document.getElementById('searchModal');
      if (modal && modal.classList.contains('open')) {
        modal.classList.remove('open');
      }
    }
  });

  // 3. Topic Progress Controller
  window.setTopicStatus = function (topicSlug, status) {
    const progress = JSON.parse(localStorage.getItem('sg_topic_progress') || '{}');
    progress[topicSlug] = status;
    localStorage.setItem('sg_topic_progress', JSON.stringify(progress));
    updateTopicStatusUI(topicSlug, status);
  };

  function updateTopicStatusUI(topicSlug, status) {
    ['statusNotStarted', 'statusInProgress', 'statusCompleted'].forEach(id => {
      const btn = document.getElementById(id);
      if (btn) btn.classList.remove('active');
    });

    if (status === 'completed') {
      const btn = document.getElementById('statusCompleted');
      if (btn) btn.classList.add('active');
    } else if (status === 'in_progress') {
      const btn = document.getElementById('statusInProgress');
      if (btn) btn.classList.add('active');
    } else {
      const btn = document.getElementById('statusNotStarted');
      if (btn) btn.classList.add('active');
    }
  }

  // 4. Bookmarks Controller
  window.toggleBookmark = function (topicSlug) {
    let bookmarks = JSON.parse(localStorage.getItem('sg_bookmarks') || '[]');
    const btn = document.getElementById('bookmarkBtn');
    if (bookmarks.includes(topicSlug)) {
      bookmarks = bookmarks.filter(s => s !== topicSlug);
      if (btn) {
        btn.classList.remove('active');
        btn.textContent = '★ Bookmark for Revision';
      }
    } else {
      bookmarks.push(topicSlug);
      if (btn) {
        btn.classList.add('active');
        btn.textContent = '★ Bookmarked ✓';
      }
    }
    localStorage.setItem('sg_bookmarks', JSON.stringify(bookmarks));
  };

  // 5. Personal Notepad Controller
  window.savePersonalNote = function (topicSlug, noteText) {
    const notes = JSON.parse(localStorage.getItem('sg_personal_notes') || '{}');
    notes[topicSlug] = noteText;
    localStorage.setItem('sg_personal_notes', JSON.stringify(notes));
    const tag = document.getElementById('notesSavedTag');
    if (tag) {
      tag.style.opacity = '1';
      setTimeout(() => { tag.style.opacity = '0.7'; }, 1500);
    }
  };

  // 6. Code block copy
  window.copyCodeBlock = function (elementId) {
    const el = document.getElementById(elementId);
    if (!el) return;
    navigator.clipboard.writeText(el.innerText).then(() => {
      alert('Code copied to clipboard.');
    });
  };

  // DOM Init
  document.addEventListener('DOMContentLoaded', () => {
    initTheme();

    const body = document.body;
    const currentTopic = body.dataset.topicId;
    if (currentTopic) {
      const progress = JSON.parse(localStorage.getItem('sg_topic_progress') || '{}');
      const status = progress[currentTopic] || 'not_started';
      updateTopicStatusUI(currentTopic, status);

      const bookmarks = JSON.parse(localStorage.getItem('sg_bookmarks') || '[]');
      const btn = document.getElementById('bookmarkBtn');
      if (btn && bookmarks.includes(currentTopic)) {
        btn.classList.add('active');
        btn.textContent = '★ Bookmarked ✓';
      }

      const notes = JSON.parse(localStorage.getItem('sg_personal_notes') || '{}');
      const notePad = document.getElementById('personalNotePad');
      if (notePad && notes[currentTopic]) {
        notePad.value = notes[currentTopic];
      }
    }
  });

})();
