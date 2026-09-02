"""Builds the comprehensive institutional Fraunces + Inter + JetBrains Mono design system."""
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = TOOLS_DIR.parent
CSS_FILE = PROJECT_ROOT / "StudyGuide" / "css" / "style.css"

INSTITUTIONAL_CSS = """/* =========================================================================
   BIRLA INSTITUTE OF TECHNOLOGY & SCIENCE, PILANI (BITS PILANI WILP)
   M.Tech Automotive Engineering — Master Portal & Study Guide Design System
   Institutional, Academic, Clean Aesthetic (Fraunces + Inter + JetBrains Mono)
   ========================================================================= */

@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

:root {
  /* Color Palette - Light Theme (Default Academic / Paper) */
  --bg: #f8fafc;
  --bg-subtle: #f1f5f9;
  --surface: #ffffff;
  --surface-hover: #f8fafc;
  --surface-elevated: rgba(255, 255, 255, 0.95);
  
  --border: #e2e8f0;
  --border-strong: #cbd5e1;
  
  --bits-navy: #0b1f3a;
  --bits-teal: #0d7a68;
  --bits-teal-soft: #e6f4f1;
  --bits-gold: #b45309;
  --bits-gold-soft: #fef3c7;
  --bits-blue: #1d4ed8;
  --bits-blue-soft: #eff6ff;
  --bits-red: #b91c1c;
  --bits-red-soft: #fef2f2;
  
  --ink: #0f172a;
  --ink-secondary: #334155;
  --text: #1e293b;
  --muted: #64748b;
  --muted-light: #94a3b8;
  
  --accent: #0d7a68;
  --accent-hover: #0a5f51;
  --accent-soft: #e6f4f1;
  --accent-border: #99d6cb;
  
  --code-bg: #0f172a;
  --code-text: #f8fafc;
  --code-inline-bg: #f1f5f9;
  --code-inline-text: #0d7a68;
  
  --shadow-xs: 0 1px 2px rgba(15, 23, 42, 0.04);
  --shadow-sm: 0 1px 3px rgba(15, 23, 42, 0.08), 0 1px 2px rgba(15, 23, 42, 0.04);
  --shadow-md: 0 4px 12px rgba(15, 23, 42, 0.07), 0 2px 4px rgba(15, 23, 42, 0.04);
  --shadow-lg: 0 10px 25px -3px rgba(15, 23, 42, 0.1), 0 4px 6px -4px rgba(15, 23, 42, 0.05);

  --radius-xs: 4px;
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-pill: 9999px;

  --font-serif: 'Fraunces', Georgia, serif;
  --font-sans: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'JetBrains Mono', Consolas, monospace;

  --transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

/* =========================================================================
   Dark Theme (High-Contrast Academic Dark)
   ========================================================================= */
body.dark, [data-theme="dark"] {
  --bg: #0b0f19;
  --bg-subtle: #111827;
  --surface: #161f30;
  --surface-hover: #1c273c;
  --surface-elevated: rgba(22, 31, 48, 0.95);
  
  --border: #233048;
  --border-strong: #334464;

  --bits-navy: #38bdf8;
  --bits-teal: #2dd4bf;
  --bits-teal-soft: rgba(45, 212, 191, 0.12);
  --bits-gold: #f59e0b;
  --bits-gold-soft: rgba(245, 158, 11, 0.15);
  --bits-blue: #60a5fa;
  --bits-blue-soft: rgba(96, 165, 250, 0.15);
  --bits-red: #f87171;
  --bits-red-soft: rgba(248, 113, 113, 0.15);

  --ink: #f8fafc;
  --ink-secondary: #cbd5e1;
  --text: #e2e8f0;
  --muted: #94a3b8;
  --muted-light: #64748b;

  --accent: #2dd4bf;
  --accent-hover: #5eead4;
  --accent-soft: rgba(45, 212, 191, 0.15);
  --accent-border: rgba(45, 212, 191, 0.35);

  --code-bg: #030712;
  --code-text: #f3f4f6;
  --code-inline-bg: #1e293b;
  --code-inline-text: #2dd4bf;

  --shadow-xs: 0 1px 2px rgba(0, 0, 0, 0.3);
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.4);
  --shadow-md: 0 4px 14px rgba(0, 0, 0, 0.45);
  --shadow-lg: 0 10px 30px rgba(0, 0, 0, 0.6);
}

/* =========================================================================
   Global Reset & Base Typography
   ========================================================================= */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
  color-scheme: light dark;
  font-size: 16px;
}

body {
  background-color: var(--bg);
  color: var(--text);
  font-family: var(--font-sans);
  line-height: 1.65;
  -webkit-font-smoothing: antialiased;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  transition: background-color 0.2s ease, color 0.2s ease;
}

h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-serif);
  color: var(--ink);
  letter-spacing: -0.015em;
  font-weight: 700;
  line-height: 1.25;
}

a {
  color: var(--accent);
  text-decoration: none;
  transition: var(--transition);
}

a:hover {
  color: var(--accent-hover);
  text-decoration: underline;
}

.mono {
  font-family: var(--font-mono);
}

.icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.icon svg {
  width: 100%;
  height: 100%;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
  fill: none;
}

img, svg {
  max-width: 100%;
  height: auto;
  vertical-align: middle;
}

code {
  font-family: var(--font-mono);
  font-size: 0.88em;
  background-color: var(--code-inline-bg);
  color: var(--code-inline-text);
  padding: 0.15em 0.45em;
  border-radius: var(--radius-xs);
  border: 1px solid var(--border);
}

pre {
  font-family: var(--font-mono);
  background-color: var(--code-bg);
  color: var(--code-text);
  padding: 1.25rem 1.5rem;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-strong);
  overflow-x: auto;
  line-height: 1.55;
  font-size: 0.88rem;
  margin: 1.25rem 0;
}

pre code {
  background: transparent;
  color: inherit;
  padding: 0;
  border: none;
}

/* =========================================================================
   Top Navigation Bar
   ========================================================================= */
.navbar, .portal-header, .top {
  position: sticky;
  top: 0;
  z-index: 1000;
  background-color: var(--surface-elevated);
  border-bottom: 1px solid var(--border);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  transition: var(--transition);
}

.navbar-container, .nav-container, .bar {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 1.5rem;
  height: 68px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
}

.nav-brand, .brand, .logo {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  color: inherit;
}

.nav-brand:hover, .logo:hover {
  text-decoration: none;
}

.nav-brand-logo, .bits-logo-img, .logo img {
  height: 44px;
  width: auto;
  object-fit: contain;
}

.brand-details, .nav-brand-text, .logo-text {
  display: flex;
  flex-direction: column;
}

.brand-inst, .nav-brand-title {
  font-family: var(--font-serif);
  font-weight: 700;
  font-size: 1.05rem;
  color: var(--ink);
  letter-spacing: -0.01em;
  line-height: 1.2;
}

.brand-dept, .nav-brand-sub, .logo-text small {
  font-family: var(--font-sans);
  font-size: 0.76rem;
  color: var(--muted);
  font-weight: 500;
}

/* Nav Search Box */
.nav-search-box {
  flex: 1;
  max-width: 480px;
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 6px 12px;
  color: var(--muted);
  font-size: 0.85rem;
  cursor: pointer;
  transition: var(--transition);
}

.nav-search-box:hover {
  border-color: var(--accent);
  color: var(--text);
  background: var(--surface);
}

.search-placeholder {
  flex: 1;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.search-shortcut {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  background: var(--surface);
  border: 1px solid var(--border);
  padding: 1px 6px;
  border-radius: var(--radius-xs);
  color: var(--muted);
}

.nav-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}

.nav-link, .header-link {
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--ink-secondary);
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.nav-link:hover, .header-link:hover {
  color: var(--accent);
  text-decoration: none;
}

.theme-toggle-btn, .theme {
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  color: var(--ink-secondary);
  padding: 6px 12px;
  border-radius: var(--radius-sm);
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: var(--transition);
}

.theme-toggle-btn:hover, .theme:hover {
  border-color: var(--accent);
  color: var(--accent);
}

/* =========================================================================
   Hero Banners (Institutional Fraunces Header)
   ========================================================================= */
.home-hero, .hero-section, .hub-hero, .subject-hero, .hero, .portal-hero {
  background: linear-gradient(180deg, var(--bg-subtle) 0%, var(--bg) 100%);
  border-bottom: 1px solid var(--border);
  padding: 3.5rem 1.5rem 3.5rem;
  position: relative;
}

.home-hero-container, .container, .wrap {
  max-width: 1140px;
  margin: 0 auto;
}

.hero-pill, .hero-bits-logo-badge, .hub-brand-badge {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: var(--surface);
  padding: 6px 16px;
  border-radius: var(--radius-pill);
  border: 1px solid var(--border);
  box-shadow: var(--shadow-xs);
  margin-bottom: 1.25rem;
  font-size: 0.84rem;
  font-weight: 600;
  color: var(--ink-secondary);
}

.hero-bits-logo, .hub-bits-logo {
  height: 32px;
  width: auto;
  object-fit: contain;
}

.status-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: #10b981;
  display: inline-block;
}

.kicker, .eyebrow {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--accent);
  display: block;
  margin-bottom: 0.5rem;
}

.hero-title, .hub-hero-title, .subject-hero-title, .hero h1, .portal-hero h1 {
  font-size: clamp(2.3rem, 4.2vw, 3.4rem);
  font-weight: 700;
  line-height: 1.15;
  color: var(--ink);
  letter-spacing: -0.025em;
  margin-bottom: 1rem;
}

.hero-subtitle, .hero-sub, .hub-hero-desc, .subject-hero-desc, .hero p, .hero-lead {
  font-size: 1.12rem;
  color: var(--muted);
  max-width: 780px;
  line-height: 1.65;
  margin-bottom: 1.75rem;
}

/* Hero Action Buttons */
.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 2.5rem;
}

.btn, .button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 10px 20px;
  border-radius: var(--radius-sm);
  font-weight: 600;
  font-size: 0.92rem;
  cursor: pointer;
  text-decoration: none;
  transition: var(--transition);
}

.btn-primary, .button-primary {
  background-color: var(--accent);
  color: #ffffff;
  border: 1px solid var(--accent);
  box-shadow: var(--shadow-sm);
}

.btn-primary:hover, .button-primary:hover {
  background-color: var(--accent-hover);
  color: #ffffff;
  box-shadow: var(--shadow-md);
  text-decoration: none;
  transform: translateY(-1px);
}

.btn-secondary, .button-quiet {
  background-color: var(--surface);
  color: var(--ink);
  border: 1px solid var(--border-strong);
  box-shadow: var(--shadow-xs);
}

.btn-secondary:hover, .button-quiet:hover {
  border-color: var(--accent);
  color: var(--accent);
  background-color: var(--surface-hover);
  text-decoration: none;
  transform: translateY(-1px);
}

/* Institutional Stat Grid */
.hero-stats-grid, .hero-metrics-strip, .subject-stats-bar, .meta {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 14px;
}

.stat-box, .metric-box, .stat-pill {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 16px 20px;
  display: flex;
  align-items: center;
  gap: 14px;
  box-shadow: var(--shadow-xs);
}

.stat-icon-wrapper {
  width: 44px;
  height: 44px;
  border-radius: var(--radius-sm);
  background: var(--accent-soft);
  color: var(--accent);
  display: flex;
  align-items: center;
  justify-content: center;
}

.stat-value, .metric-num {
  font-family: var(--font-serif);
  font-size: 1.45rem;
  font-weight: 700;
  color: var(--ink);
  line-height: 1.1;
}

.stat-label, .metric-label {
  font-size: 0.78rem;
  color: var(--muted);
  font-weight: 500;
  display: block;
  margin-top: 2px;
}

/* =========================================================================
   Grids & Course Cards (Master Portal & Semester Hub)
   ========================================================================= */
.home-main-container, .hub-main-container, .subject-main-container, main {
  max-width: 1140px;
  margin: 0 auto;
  padding: 3.5rem 1.5rem 5rem;
  width: 100%;
}

.section-head, .home-section-header, .section-heading, .semester-intro {
  margin-bottom: 2rem;
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
}

.section-head h2, .home-section-header h2, .section-heading h2 {
  font-size: 1.85rem;
  color: var(--ink);
}

.section-head .note, .home-section-header p, .section-heading p {
  font-size: 0.92rem;
  color: var(--muted);
}

/* Subject Grid */
.portal-grid, .hub-grid, .subject-grid, .subjects-grid, .semester-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 20px;
  margin-bottom: 4rem;
}

.subject-card, .portal-subject-card, .subject-hub-card, .semester-card {
  position: relative;
  display: flex;
  flex-direction: column;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 24px;
  box-shadow: var(--shadow-xs);
  transition: transform 0.15s ease, box-shadow 0.15s ease, border-color 0.15s ease;
  border-top: 4px solid var(--card-accent, #0d7a68);
  text-decoration: none;
  color: inherit;
}

.subject-card:hover, .portal-subject-card:hover, .subject-hub-card:hover, .semester-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-md);
  border-color: var(--border-strong);
  text-decoration: none;
}

.subject-card .badge, .portal-code-badge, .hub-card-code, .subject-code {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  padding: 3px 10px;
  border-radius: var(--radius-pill);
  font-weight: 600;
  margin-bottom: 12px;
  background: var(--accent-soft);
  color: var(--accent);
  width: fit-content;
}

.subject-card h3, .portal-card-title, .hub-card-title {
  font-size: 1.28rem;
  font-weight: 700;
  margin-bottom: 8px;
  color: var(--ink);
  line-height: 1.3;
}

.subject-card p, .portal-card-desc, .hub-card-desc {
  font-size: 0.88rem;
  color: var(--muted);
  line-height: 1.6;
  margin-bottom: 14px;
  flex-grow: 1;
}

.portal-sample-topics {
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 10px 14px;
  margin-bottom: 14px;
}

.portal-sample-topics h5 {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--muted);
  margin-bottom: 6px;
  font-weight: 700;
}

.portal-sample-topics ul {
  list-style: none;
}

.portal-sample-topics li {
  font-size: 0.82rem;
  margin-bottom: 4px;
}

.portal-sample-topics a {
  color: var(--ink-secondary);
}

.portal-sample-topics a:hover {
  color: var(--accent);
}

.card-action-link, .subject-card .go, .hub-card-link, .portal-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-family: var(--font-mono);
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--accent);
  margin-top: auto;
  padding-top: 10px;
  border-top: 1px solid var(--border);
}

.card-action-link:hover, .portal-btn:hover {
  color: var(--accent-hover);
  text-decoration: none;
}

/* =========================================================================
   Engineering Curriculum Framework Section (Replaces childish text)
   ========================================================================= */
.curriculum-framework-section {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 2.5rem;
  margin: 3.5rem 0;
  box-shadow: var(--shadow-sm);
}

.framework-header {
  margin-bottom: 2rem;
}

.framework-header h3 {
  font-size: 1.6rem;
  color: var(--ink);
  margin-bottom: 0.4rem;
}

.framework-header p {
  font-size: 0.95rem;
  color: var(--muted);
}

.framework-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.framework-card {
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 1.5rem;
}

.framework-tag {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--accent);
  letter-spacing: 0.06em;
  text-transform: uppercase;
  margin-bottom: 0.5rem;
}

.framework-card h4 {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--ink);
  margin-bottom: 0.65rem;
}

.framework-card p {
  font-size: 0.88rem;
  color: var(--text);
  line-height: 1.6;
}

/* =========================================================================
   Subject Dashboard Layout
   ========================================================================= */
.dashboard-module-block {
  margin-bottom: 3.5rem;
}

.module-block-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-bottom: 0.85rem;
  margin-bottom: 1.5rem;
  border-bottom: 2px solid var(--ink);
}

.module-block-header h2 {
  font-size: 1.45rem;
  color: var(--ink);
}

.module-count {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--muted);
  background: var(--surface);
  border: 1px solid var(--border);
  padding: 3px 10px;
  border-radius: var(--radius-pill);
}

.dashboard-topics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 1.5rem;
}

.dashboard-topic-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  box-shadow: var(--shadow-xs);
  transition: var(--transition);
}

.dashboard-topic-card:hover {
  transform: translateY(-2px);
  border-color: var(--accent);
  box-shadow: var(--shadow-sm);
}

.topic-card-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.85rem;
}

.topic-level-badge {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  padding: 2px 8px;
  border-radius: var(--radius-pill);
}

.level-beginner { background: var(--bits-teal-soft); color: var(--bits-teal); }
.level-intermediate { background: var(--bits-gold-soft); color: var(--bits-gold); }
.level-advanced { background: var(--bits-red-soft); color: var(--bits-red); }

.topic-stars {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--muted);
}

.topic-card-title {
  font-size: 1.18rem;
  font-weight: 700;
  line-height: 1.35;
  margin-bottom: 0.65rem;
}

.topic-card-title a {
  color: var(--ink);
}

.topic-card-title a:hover {
  color: var(--accent);
}

.topic-card-desc {
  font-size: 0.88rem;
  color: var(--muted);
  line-height: 1.6;
  margin-bottom: 1.25rem;
  flex-grow: 1;
}

.topic-card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 0.85rem;
  border-top: 1px solid var(--border);
}

.topic-status-tag {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--muted);
}

.topic-card-footer .study-btn {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--accent);
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

/* =========================================================================
   Topic Page Layout (Sidebar + Main Article)
   ========================================================================= */
.topic-page-layout, .topic-shell {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2.5rem 1.5rem 5rem;
  display: grid;
  grid-template-columns: 280px minmax(0, 1fr);
  gap: 3.5rem;
  align-items: start;
}

/* Sidebar */
.topic-sidebar, .side {
  position: sticky;
  top: 90px;
  max-height: calc(100vh - 110px);
  overflow-y: auto;
  padding-right: 1.5rem;
  border-right: 1px solid var(--border);
}

.sidebar-header {
  margin-bottom: 1.25rem;
  padding-bottom: 0.85rem;
  border-bottom: 1px solid var(--border);
}

.sidebar-back {
  font-family: var(--font-mono);
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--ink);
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 0.4rem;
}

.sidebar-subject-badge {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--accent);
}

.sidebar-toc h4 {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--muted);
  margin-bottom: 0.75rem;
}

.sidebar-toc ul {
  list-style: none;
}

.sidebar-toc li {
  margin-bottom: 0.35rem;
}

.sidebar-toc a {
  display: block;
  font-size: 0.84rem;
  color: var(--ink-secondary);
  padding: 0.3rem 0.6rem;
  border-radius: var(--radius-xs);
  transition: var(--transition);
}

.sidebar-toc a:hover {
  background-color: var(--bg-subtle);
  color: var(--accent);
  text-decoration: none;
}

.sidebar-progress-widget {
  margin-top: 2rem;
  padding-top: 1.25rem;
  border-top: 1px solid var(--border);
}

.sidebar-progress-widget h4 {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--muted);
  margin-bottom: 0.65rem;
}

.status-btn-group {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  margin-bottom: 0.85rem;
}

.status-btn {
  background-color: var(--bg-subtle);
  color: var(--ink-secondary);
  border: 1px solid var(--border);
  padding: 0.45rem 0.75rem;
  border-radius: var(--radius-xs);
  font-family: var(--font-mono);
  font-size: 0.76rem;
  font-weight: 600;
  cursor: pointer;
  text-align: left;
  transition: var(--transition);
}

.status-btn:hover {
  border-color: var(--accent);
}

.status-btn.active {
  background-color: var(--accent);
  color: #ffffff;
  border-color: var(--accent);
}

.bookmark-btn {
  width: 100%;
  background: var(--surface);
  border: 1px dashed var(--border-strong);
  color: var(--ink-secondary);
  font-family: var(--font-mono);
  padding: 0.5rem;
  border-radius: var(--radius-xs);
  font-size: 0.76rem;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition);
}

.bookmark-btn:hover, .bookmark-btn.active {
  border-color: var(--bits-gold);
  color: var(--bits-gold);
  background: var(--bits-gold-soft);
}

/* =========================================================================
   Topic Main Content Article
   ========================================================================= */
.topic-main-content, .topic {
  max-width: 880px;
}

.breadcrumbs, .crumb {
  font-family: var(--font-mono);
  font-size: 0.8rem;
  color: var(--muted);
  margin-bottom: 1rem;
}

.breadcrumbs a, .crumb a {
  color: var(--muted);
}

.breadcrumbs a:hover, .crumb a:hover {
  color: var(--accent);
}

.curr-crumb {
  color: var(--ink);
  font-weight: 600;
}

.topic-meta-row, .meta {
  display: flex;
  flex-wrap: wrap;
  gap: 0.65rem;
  margin-bottom: 1.25rem;
}

.meta-pill, .pill {
  font-family: var(--font-mono);
  font-size: 0.74rem;
  font-weight: 600;
  background: var(--bg-subtle);
  color: var(--ink-secondary);
  border: 1px solid var(--border);
  padding: 0.25rem 0.65rem;
  border-radius: var(--radius-pill);
  text-transform: uppercase;
}

.module-pill { background: var(--bits-blue-soft); color: var(--bits-blue); border-color: rgba(29, 78, 216, 0.2); }
.level-pill { background: var(--bits-teal-soft); color: var(--bits-teal); border-color: rgba(13, 122, 104, 0.2); }
.importance-pill { background: var(--bits-gold-soft); color: var(--bits-gold); border-color: rgba(180, 83, 9, 0.2); }

.topic-main-title, .topic-title {
  font-size: clamp(2.2rem, 3.8vw, 3rem);
  font-weight: 700;
  line-height: 1.2;
  color: var(--ink);
  margin-bottom: 1.25rem;
}

.action-bar-top, .topic-actions {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.75rem 1.25rem;
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  margin-bottom: 2.5rem;
}

.read-estimate {
  font-family: var(--font-mono);
  font-size: 0.8rem;
  color: var(--muted);
}

.print-btn {
  background: var(--surface);
  color: var(--ink);
  border: 1px solid var(--border);
  font-family: var(--font-mono);
  padding: 0.4rem 0.85rem;
  border-radius: var(--radius-xs);
  font-size: 0.75rem;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: var(--transition);
}

.print-btn:hover {
  border-color: var(--accent);
  color: var(--accent);
}

/* Topic Sections */
.topic-section, .topic section {
  margin-bottom: 3.5rem;
}

.section-header, .topic h2 {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.25rem;
  padding-bottom: 0.65rem;
  border-bottom: 1px solid var(--border-strong);
}

.section-header h2 {
  font-family: var(--font-serif);
  font-size: 1.55rem;
  font-weight: 700;
  color: var(--ink);
}

.sec-tag {
  font-family: var(--font-mono);
  font-size: 0.82rem;
  color: var(--accent);
  margin-right: 0.5rem;
}

.overview-lead {
  font-size: 1.12rem;
  line-height: 1.75;
  color: var(--text);
}

/* Objectives Card */
.objectives-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-left: 4px solid var(--bits-blue);
  border-radius: var(--radius-sm);
  padding: 1.5rem 1.75rem;
  box-shadow: var(--shadow-xs);
}

.objectives-card h5 {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--bits-blue);
  margin-bottom: 0.75rem;
}

.objectives-list {
  padding-left: 1.25rem;
  margin-bottom: 1rem;
}

.objectives-list li {
  margin-bottom: 0.4rem;
  color: var(--text);
  font-size: 0.95rem;
}

.prereq-note {
  font-family: var(--font-mono);
  font-size: 0.82rem;
  color: var(--muted);
  border-top: 1px solid var(--border);
  padding-top: 0.75rem;
}

/* Callout Boxes */
.callout, .box {
  border-radius: var(--radius-sm);
  padding: 1.5rem 1.75rem;
  margin: 1.5rem 0;
  box-shadow: var(--shadow-xs);
}

.callout-header {
  font-family: var(--font-mono);
  font-size: 0.82rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin-bottom: 0.85rem;
  display: flex;
  align-items: center;
  gap: 8px;
}

.callout-lecture {
  background: var(--bits-teal-soft);
  border-left: 4px solid var(--bits-teal);
  color: var(--text);
}

.callout-lecture .callout-header {
  color: var(--bits-teal);
}

.callout-deep {
  background: var(--bits-blue-soft);
  border-left: 4px solid var(--bits-blue);
  color: var(--text);
}

.callout-deep .callout-header {
  color: var(--bits-blue);
}

.callout-application {
  background: var(--bg-subtle);
  border-left: 4px solid var(--ink);
  color: var(--text);
}

.callout-warning {
  background: var(--bits-gold-soft);
  border-left: 4px solid var(--bits-gold);
  color: var(--text);
}

.callout-warning .callout-header {
  color: var(--bits-gold);
}

.callout-body p, .concept-body p, .principle-body p {
  margin-bottom: 0.85rem;
  line-height: 1.75;
  font-size: 0.96rem;
}

.callout-body p:last-child {
  margin-bottom: 0;
}

/* Workflow Steps */
.workflow-container, .workflow {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin: 1.5rem 0;
}

.workflow-step, .step {
  display: flex;
  align-items: flex-start;
  gap: 1.25rem;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 1.25rem 1.5rem;
  box-shadow: var(--shadow-xs);
}

.step-badge {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--accent);
  background: var(--accent-soft);
  border: 1px solid var(--accent-border);
  padding: 0.25rem 0.6rem;
  border-radius: var(--radius-xs);
  flex-shrink: 0;
}

.step-title {
  font-weight: 700;
  font-size: 1.05rem;
  color: var(--ink);
  margin-bottom: 0.25rem;
}

.step-desc {
  color: var(--text);
  font-size: 0.92rem;
  line-height: 1.6;
}

/* ASCII Diagrams */
.diagram-box {
  background: var(--code-bg);
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-strong);
  padding: 1.5rem;
  overflow-x: auto;
  margin: 1.5rem 0;
  box-shadow: var(--shadow-sm);
}

.ascii-diagram {
  color: #34d399;
  font-family: var(--font-mono);
  font-size: 0.85rem;
  line-height: 1.4;
  margin: 0;
  background: transparent;
  padding: 0;
  border: none;
}

/* Tables */
.table-responsive {
  overflow-x: auto;
  margin: 1.5rem 0;
}

.specs-table {
  width: 100%;
  border-collapse: collapse;
  background: var(--surface);
  border-radius: var(--radius-sm);
  border: 1px solid var(--border);
  box-shadow: var(--shadow-xs);
}

.specs-table th {
  background: var(--bg-subtle);
  color: var(--ink);
  font-family: var(--font-mono);
  font-weight: 700;
  font-size: 0.82rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 0.85rem 1.25rem;
  text-align: left;
  border-bottom: 2px solid var(--border);
}

.specs-table td {
  padding: 0.85rem 1.25rem;
  border-bottom: 1px solid var(--border);
  color: var(--text);
  font-size: 0.92rem;
}

.specs-table tr:last-child td {
  border-bottom: none;
}

.specs-table tr:hover {
  background: var(--bg-subtle);
}

/* Formulas Grid */
.formulas-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 1.5rem;
  margin: 1.5rem 0;
}

.formula-card, .formula {
  background: var(--surface);
  border: 1px solid var(--border);
  border-left: 4px solid var(--bits-blue);
  border-radius: var(--radius-sm);
  padding: 1.5rem;
  box-shadow: var(--shadow-xs);
}

.formula-name {
  font-family: var(--font-serif);
  font-weight: 700;
  font-size: 1.1rem;
  color: var(--ink);
  margin-bottom: 0.85rem;
}

.formula-math {
  background: var(--code-bg);
  color: #38bdf8;
  padding: 0.85rem 1rem;
  border-radius: var(--radius-xs);
  margin-bottom: 1rem;
  font-family: var(--font-mono);
  font-size: 0.92rem;
}

.formula-details h5 {
  font-family: var(--font-mono);
  font-size: 0.74rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--muted);
  margin-bottom: 0.5rem;
}

.formula-vars {
  padding-left: 1.25rem;
  margin-bottom: 0.85rem;
  font-size: 0.88rem;
  color: var(--text);
}

.formula-example {
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  padding: 0.75rem 1rem;
  border-radius: var(--radius-xs);
  font-size: 0.88rem;
  color: var(--text);
}

/* Code Container */
.code-container {
  position: relative;
  margin: 1.5rem 0;
}

.copy-btn {
  background: var(--surface);
  color: var(--ink-secondary);
  border: 1px solid var(--border);
  font-family: var(--font-mono);
  padding: 0.35rem 0.75rem;
  border-radius: var(--radius-xs);
  font-size: 0.74rem;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: var(--transition);
}

.copy-btn:hover {
  border-color: var(--accent);
  color: var(--accent);
}

/* Exam Questions */
.exam-qa-block {
  margin-bottom: 2rem;
}

.exam-qa-block h3 {
  font-size: 1.25rem;
  color: var(--ink);
  margin-bottom: 1rem;
}

.qa-list {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.qa-item {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 1.5rem;
  box-shadow: var(--shadow-xs);
}

.qa-question {
  font-weight: 700;
  font-size: 1.05rem;
  color: var(--ink);
  margin-bottom: 0.75rem;
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
}

.q-badge {
  font-family: var(--font-mono);
  background: var(--bits-blue-soft);
  color: var(--bits-blue);
  border: 1px solid rgba(29, 78, 216, 0.25);
  font-size: 0.72rem;
  font-weight: 700;
  padding: 0.2rem 0.55rem;
  border-radius: var(--radius-xs);
  flex-shrink: 0;
}

.qa-answer {
  color: var(--text);
  font-size: 0.95rem;
  line-height: 1.7;
}

/* Must Remember & Flashcard */
.must-remember-card {
  background: var(--bits-gold-soft);
  border: 1px solid rgba(180, 83, 9, 0.2);
  border-left: 4px solid var(--bits-gold);
  border-radius: var(--radius-sm);
  padding: 1.5rem 1.75rem;
}

.must-remember-card ul, .flashcard-points {
  list-style: none;
}

.must-remember-card li {
  margin-bottom: 0.65rem;
  font-weight: 600;
  color: var(--bits-gold);
  font-size: 0.95rem;
}

.flashcard, .revision {
  background: var(--surface);
  border: 1px solid var(--border);
  border-left: 4px solid var(--bits-teal);
  border-radius: var(--radius-sm);
  padding: 1.75rem;
  box-shadow: var(--shadow-xs);
}

.flashcard-badge {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--bits-teal);
  margin-bottom: 1rem;
}

.flashcard-points li {
  margin-bottom: 0.65rem;
  line-height: 1.6;
  font-size: 0.95rem;
  color: var(--text);
}

/* Personal Notes */
.personal-notes-widget {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 1.5rem;
}

.notes-hint {
  font-size: 0.85rem;
  color: var(--muted);
  margin-bottom: 0.75rem;
}

.personal-notes-textarea, .personal-note {
  width: 100%;
  min-height: 120px;
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  border-radius: var(--radius-xs);
  padding: 0.85rem;
  font-family: var(--font-sans);
  font-size: 0.92rem;
  color: var(--text);
  resize: vertical;
}

.notes-save-indicator {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--accent);
  font-weight: 600;
  margin-top: 0.45rem;
}

/* Sources & Pagination */
.sources-box, .source {
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 1.25rem 1.5rem;
  font-size: 0.88rem;
  color: var(--muted);
}

.topic-pagination, .nav-pages {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  margin-top: 3.5rem;
  padding-top: 2rem;
  border-top: 1px solid var(--border);
}

.nav-prev-btn, .nav-next-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-family: var(--font-mono);
  font-weight: 600;
  font-size: 0.84rem;
  color: var(--accent);
  background: var(--surface);
  border: 1px solid var(--border);
  padding: 0.65rem 1.25rem;
  border-radius: var(--radius-xs);
}

.nav-prev-btn:hover, .nav-next-btn:hover {
  border-color: var(--accent);
  text-decoration: none;
}

.nav-disabled {
  font-family: var(--font-mono);
  color: var(--muted);
  font-size: 0.8rem;
}

/* =========================================================================
   Search Modal
   ========================================================================= */
.search-modal-overlay {
  display: none;
  position: fixed;
  inset: 0;
  z-index: 2000;
  background: rgba(15, 23, 42, 0.6);
  backdrop-filter: blur(6px);
  padding: 4rem 1.5rem;
  align-items: flex-start;
  justify-content: center;
}

.search-modal-overlay.open {
  display: flex;
}

.search-modal-container {
  background: var(--surface);
  border: 1px solid var(--border-strong);
  border-radius: var(--radius-md);
  width: 100%;
  max-width: 720px;
  box-shadow: var(--shadow-lg);
  overflow: hidden;
}

.search-modal-header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 1.25rem 1.5rem;
  border-bottom: 1px solid var(--border);
}

.search-modal-input, .search {
  flex: 1;
  background: transparent;
  border: none;
  font-size: 1.1rem;
  font-family: var(--font-sans);
  color: var(--ink);
  outline: none;
}

.search-modal-close {
  background: transparent;
  border: none;
  font-size: 1.5rem;
  color: var(--muted);
  cursor: pointer;
}

.search-modal-filters {
  display: flex;
  gap: 6px;
  padding: 0.75rem 1.5rem;
  background: var(--bg-subtle);
  border-bottom: 1px solid var(--border);
  overflow-x: auto;
}

.search-filter-btn {
  background: transparent;
  border: 1px solid var(--border);
  color: var(--ink-secondary);
  font-family: var(--font-mono);
  padding: 4px 10px;
  border-radius: var(--radius-pill);
  font-size: 0.75rem;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
}

.search-filter-btn.active {
  background: var(--accent);
  color: #ffffff;
  border-color: var(--accent);
}

.search-modal-results, .results {
  max-height: 480px;
  overflow-y: auto;
  padding: 1rem 1.5rem;
}

.search-result-item, .result {
  padding: 1rem 0;
  border-bottom: 1px solid var(--border);
}

.search-result-item:last-child, .result:last-child {
  border-bottom: none;
}

.search-result-title, .result a {
  font-family: var(--font-serif);
  font-weight: 700;
  font-size: 1.05rem;
  color: var(--ink);
  margin-bottom: 4px;
  display: block;
}

.search-result-title:hover {
  color: var(--accent);
}

.search-result-meta, .result div {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--muted);
  margin-bottom: 4px;
}

.search-result-snippet, .result small {
  font-size: 0.88rem;
  color: var(--text);
  line-height: 1.5;
}

/* =========================================================================
   Footer
   ========================================================================= */
.site-footer, .footer, .portal-footer {
  background: var(--bg-subtle);
  border-top: 1px solid var(--border);
  color: var(--muted);
  padding: 3.5rem 1.5rem 2rem;
  margin-top: auto;
}

.footer-container {
  max-width: 1140px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 2fr 1.2fr 1fr;
  gap: 3rem;
  margin-bottom: 2.5rem;
}

.footer-brand {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 1rem;
}

.footer-bits-logo {
  height: 40px;
  width: auto;
  object-fit: contain;
}

.footer-title {
  font-family: var(--font-serif);
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--ink);
}

.footer-sub {
  font-size: 0.78rem;
  color: var(--muted);
}

.footer-desc {
  font-size: 0.88rem;
  color: var(--muted);
  line-height: 1.6;
  margin-bottom: 1.25rem;
}

.footer-tags {
  display: flex;
  gap: 6px;
}

.badge {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: var(--radius-pill);
}

.badge-info { background: var(--bits-blue-soft); color: var(--bits-blue); }
.badge-success { background: var(--bits-teal-soft); color: var(--bits-teal); }
.badge-warning { background: var(--bits-gold-soft); color: var(--bits-gold); }

.footer-col h4 {
  font-family: var(--font-mono);
  font-size: 0.82rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--ink);
  margin-bottom: 1rem;
}

.footer-col ul {
  list-style: none;
}

.footer-col li {
  margin-bottom: 0.5rem;
}

.footer-col a {
  color: var(--muted);
  font-size: 0.88rem;
}

.footer-col a:hover {
  color: var(--accent);
}

.footer-bottom {
  max-width: 1140px;
  margin: 0 auto;
  padding-top: 1.75rem;
  border-top: 1px solid var(--border);
  font-family: var(--font-mono);
  font-size: 0.76rem;
  color: var(--muted);
}

.footer-bottom-content {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
}

/* =========================================================================
   Responsive Breakpoints
   ========================================================================= */
@media (max-width: 1024px) {
  .topic-page-layout, .topic-shell {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  
  .topic-sidebar, .side {
    position: static;
    max-height: none;
    border-right: none;
    border-bottom: 1px solid var(--border);
    padding-bottom: 1.5rem;
  }
  
  .footer-container {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
}

@media (max-width: 768px) {
  .nav-search-box {
    display: none;
  }
  
  .portal-grid, .hub-grid, .subject-grid, .semester-grid {
    grid-template-columns: 1fr;
  }
}
"""

CSS_FILE.write_text(INSTITUTIONAL_CSS, encoding='utf-8')
print(f"Generated institutional Fraunces + Inter CSS at {CSS_FILE}")
