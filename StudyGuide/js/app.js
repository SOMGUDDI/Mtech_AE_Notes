/**
 * M.Tech Automotive Engineering Study Guide — Technical Application Engine
 * Offline-First: Theme, Progress Tracking, Bookmarks, Local Notes & Instant Search.
 */

(function () {
  'use strict';

  // 1. Theme Controller
  window.toggleTheme = function () {
    const isDark = document.body.classList.toggle('dark');
    localStorage.setItem('sg-theme', isDark ? 'dark' : 'light');
  };

  function initTheme() {
    const saved = localStorage.getItem('sg-theme') || 'light';
    if (saved === 'dark') {
      document.body.classList.add('dark');
    } else {
      document.body.classList.remove('dark');
    }
  }

  // 2. Search Modal Controller
  let currentSubjectFilter = 'all';

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

  window.handleSearch = function (query) {
    const resultsContainer = document.getElementById('searchResults');
    if (!resultsContainer) return;

    query = (query || '').trim().toLowerCase();
    if (!query) {
      resultsContainer.innerHTML = '<div class="search-empty-state"><span>Type keywords to search across 33+ comprehensive M.Tech topics...</span></div>';
      return;
    }

    const index = window.SEARCH_INDEX || [];
    const rootPrefix = getRelativeRootPrefix();

    const filtered = index.filter(item => {
      if (currentSubjectFilter !== 'all' && item.subject_slug !== currentSubjectFilter) {
        return false;
      }
      const fullText = (item.title + ' ' + item.subject + ' ' + item.module + ' ' + (item.overview || '') + ' ' + (item.keywords ? item.keywords.join(' ') : '')).toLowerCase();
      return query.split(' ').every(w => fullText.includes(w));
    }).slice(0, 10);

    if (filtered.length === 0) {
      resultsContainer.innerHTML = `<div class="search-empty-state"><span>No matching topics found for "${htmlEscape(query)}".</span></div>`;
    } else {
      resultsContainer.innerHTML = filtered.map(item => `
        <div class="search-result-item">
          <a class="search-result-title" href="${rootPrefix}topics/${item.subject_slug}/${item.slug}.html">${htmlEscape(item.title)}</a>
          <div class="search-result-meta">${htmlEscape(item.subject)} · ${htmlEscape(item.module)}</div>
          <div class="search-result-snippet">${htmlEscape((item.overview || '').slice(0, 150))}...</div>
        </div>
      `).join('');
    }
  };

  function getRelativeRootPrefix() {
    const path = window.location.pathname.replace(/\\\\/g, '/');
    if (path.includes('/topics/')) return '../../';
    if (path.includes('/subjects/') || path.includes('/semesters/') || path.includes('/sem-1/')) return '../';
    return './';
  }

  function htmlEscape(str) {
    return String(str || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

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
