"""Master Institutional HTML Generator for M.Tech Study Guide Website.
Theme and layout: Blueprint Aesthetic for Landing Page + Comprehensive Institutional Subject Hubs & Topic Notes.
"""
import sys
import json
import html
import re
import shutil
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = TOOLS_DIR.parent
STUDY_GUIDE_DIR = PROJECT_ROOT / "StudyGuide"

if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

import topic_data

def escape_text(text):
    if not text:
        return ""
    return html.escape(str(text))

def format_math_markdown(text):
    """Formats basic markdown bold/italic/math for display."""
    if not text:
        return ""
    t = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    t = re.sub(r'\*(.*?)\*', r'<em>\1</em>', t)
    t = t.replace('\n', '<br>')
    return t

# Clean Feather Vector SVG Icons
SVG_HOME = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>'
SVG_SEARCH = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>'
SVG_BOOK = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>'
SVG_ARROW_RIGHT = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>'
SVG_ARROW_LEFT = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>'
SVG_CHECK = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>'
SVG_PRINT = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>'
SVG_MOON = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>'

def render_navbar(relative_root=".."):
    return f"""
<header class="navbar">
    <div class="navbar-container">
        <a href="{relative_root}/index.html" class="nav-brand" title="Return to Master Home / Landing Page">
            <img src="{relative_root}/assets/img/bits_logo.png" alt="BITS Pilani Logo" class="nav-brand-logo" width="38" height="38" style="height:38px; width:auto; max-height:38px; object-fit:contain;">
            <div class="brand-details">
                <span class="brand-inst">Birla Institute of Technology & Science, Pilani</span>
                <span class="brand-dept">Work Integrated Learning Programmes • Automotive Engineering</span>
            </div>
        </a>
        <div class="nav-search-box" onclick="openSearchModal()">
            <span class="icon">{SVG_SEARCH}</span>
            <span class="search-placeholder">Search curriculum, formulas, registers, questions (Ctrl+K)...</span>
            <span class="search-shortcut">Ctrl+K</span>
        </div>
        <div class="nav-actions">
            <a href="{relative_root}/index.html" class="nav-link" title="Go to Master Home / Landing Page">
                <span class="icon">{SVG_HOME}</span>
                <span>Home</span>
            </a>
            <a href="{relative_root}/semesters/sem1.html" class="nav-link" title="Go to Semester 1 Curriculum Hub">
                <span class="icon">{SVG_BOOK}</span>
                <span>Semester 1</span>
            </a>
            <button class="theme-toggle-btn" id="themeToggle" onclick="toggleTheme()" title="Toggle Dark/Light Mode">
                <span class="icon">{SVG_MOON}</span>
                <span>Theme</span>
            </button>
        </div>
    </div>
</header>
"""

def render_footer(relative_root=".."):
    return f"""
<footer class="site-footer">
    <div class="footer-container">
        <div class="footer-col brand-col">
            <div class="footer-brand">
                <img src="{relative_root}/assets/img/bits_logo.png" alt="BITS Pilani Logo" class="footer-bits-logo" width="36" height="36" style="height:36px; width:auto; max-height:36px; object-fit:contain;">
                <div class="footer-brand-text">
                    <span class="footer-title">Birla Institute of Technology & Science, Pilani</span>
                    <span class="footer-sub">Work Integrated Learning Programmes (WILP)</span>
                </div>
            </div>
            <p class="footer-desc">Institutional knowledge base engineered from official lecture transcripts, handouts, and laboratory sessions for M.Tech Automotive Engineering.</p>
            <div class="footer-tags">
                <span class="badge badge-info">BITS WILP</span>
                <span class="badge badge-success">4 Core Courses</span>
                <span class="badge badge-warning">Exam & Viva Ready</span>
            </div>
        </div>
        <div class="footer-col">
            <h4>Semester 1 Courses</h4>
            <ul>
                <li><a href="{relative_root}/subjects/automotive-communication.html">Automotive Communication (AELZG513)</a></li>
                <li><a href="{relative_root}/subjects/automotive-vehicle.html">Automotive Vehicle (AELZC441)</a></li>
                <li><a href="{relative_root}/subjects/autotronics.html">Autotronics (AEZG533)</a></li>
                <li><a href="{relative_root}/subjects/embedded-system-design.html">Embedded System Design (AEZG512)</a></li>
            </ul>
        </div>
        <div class="footer-col">
            <h4>Navigation</h4>
            <ul>
                <li><a href="{relative_root}/index.html">Master Portal Home</a></li>
                <li><a href="{relative_root}/semesters/sem1.html">Semester 1 Overview & Credits</a></li>
                <li><a href="javascript:void(0)" onclick="openSearchModal()">Global Topic Search</a></li>
            </ul>
        </div>
    </div>
    <div class="footer-bottom">
        <div class="footer-bottom-content">
            <span>© 2026 M.Tech Automotive Engineering Knowledge Base. Built for High-Performance Academic Study.</span>
            <span>Birla Institute of Technology & Science, Pilani.</span>
        </div>
    </div>
</footer>
"""

def render_search_modal():
    return f"""
<div class="search-modal-overlay" id="searchModal" onclick="closeSearchModal(event)">
    <div class="search-modal-container" onclick="event.stopPropagation()">
        <div class="search-modal-header">
            <span class="icon">{SVG_SEARCH}</span>
            <input type="text" id="searchInput" class="search-modal-input" placeholder="Type to search curriculum, formulas, registers, exam questions..." autocomplete="off" oninput="handleSearch(this.value)">
            <button class="search-modal-close" onclick="closeSearchModal()">&times;</button>
        </div>
        <div class="search-modal-filters">
            <button class="search-filter-btn active" data-subject="all" onclick="setSearchFilter('all')">All Courses</button>
            <button class="search-filter-btn" data-subject="automotive-communication" onclick="setSearchFilter('automotive-communication')">Communication</button>
            <button class="search-filter-btn" data-subject="automotive-vehicle" onclick="setSearchFilter('automotive-vehicle')">Vehicle</button>
            <button class="search-filter-btn" data-subject="autotronics" onclick="setSearchFilter('autotronics')">Autotronics</button>
            <button class="search-filter-btn" data-subject="embedded-system-design" onclick="setSearchFilter('embedded-system-design')">Embedded</button>
        </div>
        <div class="search-modal-results" id="searchResults">
            <div class="search-empty-state">
                <span>Start typing to search across 33+ comprehensive M.Tech topics...</span>
            </div>
        </div>
    </div>
</div>
"""

def render_home_page():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>M.Tech Notes — BITS Pilani • Automotive Engineering</title>
    <meta name="description" content="A focused home for M.Tech Automotive Engineering notes, lectures, labs, and reference material—arranged by semester and subject.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
    <script>
      (function(){{
        const savedTheme = localStorage.getItem('sg-theme') || localStorage.getItem('mtech_theme') || 'light';
        if (savedTheme === 'dark') {{ document.documentElement.setAttribute('data-theme', 'dark'); }}
      }})();
    </script>
</head>
<body>

{render_navbar(relative_root=".")}

<section class="home-hero">
    <div class="container">
        <div class="eyebrow">// M.TECH AUTOMOTIVE ENGINEERING · WILP 2026</div>
        <h1 class="hero-title">Study the systems that move <em style="color:var(--accent); font-style:normal;">machines.</em></h1>
        <p class="hero-subtitle">A focused home for M.Tech Automotive Engineering notes, lectures, labs, and reference material—arranged by semester and subject.</p>

        <div class="hero-actions">
            <a href="semesters/sem1.html" class="btn btn-primary">
                <span>OPEN INTERACTIVE STUDY GUIDE →</span>
            </a>
            <a href="semesters/sem1.html" class="btn btn-secondary">
                <span>SEMESTER 1 HUB</span>
            </a>
        </div>

        <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--muted); text-transform:uppercase; letter-spacing:0.08em; margin-top:2rem; line-height:1.8;">
            <div>SYSTEM STATUS</div>
            <div>AE</div>
            <div>SEMESTER 01 • <strong style="color:var(--accent);">ACTIVE</strong></div>
        </div>
    </div>
</section>

<main class="home-main-container">
    <div class="section-head" style="margin-bottom:1.5rem;">
        <div>
            <div class="kicker">// COURSE ROADMAP</div>
            <h2>Choose a semester</h2>
            <p>Each semester is a dedicated workspace for subject notes and study resources.</p>
        </div>
    </div>

    <div class="portal-grid">
        <div class="semester-card" style="border-top:4px solid var(--accent);">
            <div class="sem-number">01 • ACTIVE</div>
            <h3><a href="semesters/sem1.html">Semester One</a></h3>
            <p>Autotronics, automotive communication, vehicle systems, and embedded design.</p>
            <div class="card-meta">
                <span>04 SUBJECTS</span> • <span>33+ TOPIC PAGES</span>
            </div>
            <a href="semesters/sem1.html" class="card-action-link">
                <span>Enter semester 1 hub →</span>
            </a>
        </div>

        <div class="semester-card" style="opacity:0.75;">
            <div class="sem-number" style="color:var(--muted);">02 ~ LOCKED</div>
            <h3 style="color:var(--muted);">Semester Two</h3>
            <p>Subject workspace will be added as the semester begins.</p>
            <div class="card-meta" style="color:var(--muted);">
                <span>COMING SOON</span>
            </div>
        </div>

        <div class="semester-card" style="opacity:0.75;">
            <div class="sem-number" style="color:var(--muted);">03 ~ LOCKED</div>
            <h3 style="color:var(--muted);">Semester Three</h3>
            <p>Subject workspace will be added as the semester begins.</p>
            <div class="card-meta" style="color:var(--muted);">
                <span>COMING SOON</span>
            </div>
        </div>

        <div class="semester-card" style="opacity:0.75;">
            <div class="sem-number" style="color:var(--muted);">04 ~ LOCKED</div>
            <h3 style="color:var(--muted);">Semester Four</h3>
            <p>Subject workspace will be added as the semester begins.</p>
            <div class="card-meta" style="color:var(--muted);">
                <span>COMING SOON</span>
            </div>
        </div>
    </div>
</main>

{render_footer(relative_root=".")}
{render_search_modal()}

<script src="js/search-index.js"></script>
<script src="js/app.js"></script>
</body>
</html>
"""

def render_semester_hub(relative_root=".."):
    all_subjects_cards = ""
    for sub_slug, data in topic_data.SUBJECT_DATA.items():
        meta = data["metadata"]
        topics = data["topics"]
        all_subjects_cards += f"""
        <div class="subject-card">
            <span class="badge">{escape_text(meta["code"])}</span>
            <h3><a href="{relative_root}/subjects/{sub_slug}.html">{escape_text(meta["title"])}</a></h3>
            <p>{escape_text(meta["description"][:130])}...</p>
            <div class="card-meta">
                <span>{len(topics)} TOPICS</span> • <span>{escape_text(meta.get("credits", "3 Units"))}</span>
            </div>
            <a href="{relative_root}/subjects/{sub_slug}.html" class="card-action-link">
                <span>Open Subject Guide</span>
                <span class="icon">{SVG_ARROW_RIGHT}</span>
            </a>
        </div>
        """
        
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Semester 1 Hub | M.Tech Automotive Engineering, BITS Pilani</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{relative_root}/css/style.css">
    <script>
      (function(){{
        const savedTheme = localStorage.getItem('sg-theme') || localStorage.getItem('mtech_theme') || 'light';
        if (savedTheme === 'dark') {{ document.documentElement.setAttribute('data-theme', 'dark'); }}
      }})();
    </script>
</head>
<body>

{render_navbar(relative_root=relative_root)}

<header class="hub-hero">
    <div class="container">
        <div class="hero-pill">
            <span class="status-dot"></span>
            <span>Birla Institute of Technology & Science, Pilani (BITS WILP) • Semester 1</span>
        </div>
        <div class="breadcrumbs">
            <a href="{relative_root}/index.html">Home</a> / 
            <span class="curr-crumb">Semester 1 Curriculum Hub</span>
        </div>
        <h1 class="hero-title">Semester 1 Core Knowledge Base</h1>
        <p class="hero-subtitle">Foundational pillars of Automotive Engineering: Communication Networks, Vehicle Dynamics & Chassis, Autotronics Mechatronics, and Real-Time Embedded Systems.</p>
    </div>
</header>

<main class="hub-main-container">
    <div class="section-head">
        <h2>Registered Core Courses</h2>
        <span class="note">Semester 1 Curriculum • 4 Core Subjects • 33 In-Depth Topic Modules</span>
    </div>
    <div class="hub-grid">
        {all_subjects_cards}
    </div>
</main>

{render_footer(relative_root=relative_root)}
{render_search_modal()}

<script src="{relative_root}/js/search-index.js"></script>
<script src="{relative_root}/js/app.js"></script>
</body>
</html>
"""

def render_subject_dashboard(subject_slug, relative_root=".."):
    sub_data = topic_data.SUBJECT_DATA[subject_slug]
    meta = sub_data["metadata"]
    topics = sub_data["topics"]
    
    # Group topics by module
    modules = {}
    for t in topics:
        m = t.get("module", "Core Topics")
        if m not in modules:
            modules[m] = []
        modules[m].append(t)
        
    modules_html = ""
    for mod_name, mod_topics in modules.items():
        topic_cards = ""
        for t in mod_topics:
            topic_cards += f"""
            <div class="dashboard-topic-card" data-topic-id="{t['slug']}">
                <div class="topic-card-top">
                    <span class="topic-level-badge level-{t.get('level', 'Intermediate').lower()}">{escape_text(t.get('level', 'Intermediate'))}</span>
                    <span class="topic-stars">WEIGHT: {t.get('importance', 5)}/5</span>
                </div>
                <h3 class="topic-card-title"><a href="{relative_root}/topics/{subject_slug}/{t['slug']}.html">{escape_text(t['title'])}</a></h3>
                <p class="topic-card-desc">{escape_text(t.get('overview', '')[:140])}...</p>
                <div class="topic-card-footer">
                    <span class="topic-status-tag" id="tag_{t['slug']}">☐ Not Started</span>
                    <a href="{relative_root}/topics/{subject_slug}/{t['slug']}.html" class="study-btn">Study Topic →</a>
                </div>
            </div>
            """
        modules_html += f"""
        <div class="dashboard-module-block">
            <div class="module-block-header">
                <h2>{escape_text(mod_name)}</h2>
                <span class="module-count">{len(mod_topics)} Topics</span>
            </div>
            <div class="dashboard-topics-grid">
                {topic_cards}
            </div>
        </div>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{escape_text(meta["title"])} ({escape_text(meta["code"])}) | BITS Pilani M.Tech Study Guide</title>
    <meta name="description" content="{escape_text(meta["description"])}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{relative_root}/css/style.css">
    <script>
      (function(){{
        const savedTheme = localStorage.getItem('sg-theme') || localStorage.getItem('mtech_theme') || 'light';
        if (savedTheme === 'dark') {{ document.documentElement.setAttribute('data-theme', 'dark'); }}
      }})();
    </script>
</head>
<body data-subject-id="{subject_slug}">

{render_navbar(relative_root=relative_root)}

<header class="subject-hero">
    <div class="container">
        <div class="hero-pill">
            <span class="status-dot"></span>
            <span>BITS Pilani WILP • Course Code: {escape_text(meta["code"])} • {escape_text(meta.get("credits", "3 Units"))}</span>
        </div>
        <div class="breadcrumbs">
            <a href="{relative_root}/index.html">Home</a> / 
            <a href="{relative_root}/semesters/sem1.html">Semester 1</a> / 
            <span class="curr-crumb">{escape_text(meta["title"])}</span>
        </div>
        <h1 class="hero-title">{escape_text(meta["title"])}</h1>
        <p class="hero-subtitle">{escape_text(meta["description"])}</p>
        
        <div class="hero-stats-grid">
            <div class="stat-box">
                <div class="stat-icon-wrapper"><span class="icon">{SVG_BOOK}</span></div>
                <div class="stat-info">
                    <span class="stat-value">{len(topics)}</span>
                    <span class="stat-label">In-Depth Topics</span>
                </div>
            </div>
            <div class="stat-box">
                <div class="stat-icon-wrapper"><span class="icon">{SVG_CHECK}</span></div>
                <div class="stat-info">
                    <span class="stat-value">{len(modules)}</span>
                    <span class="stat-label">Learning Modules</span>
                </div>
            </div>
            <div class="stat-box">
                <div class="stat-icon-wrapper"><span class="icon">{SVG_CHECK}</span></div>
                <div class="stat-info">
                    <span class="stat-value">100%</span>
                    <span class="stat-label">Transcript Coverage</span>
                </div>
            </div>
        </div>
    </div>
</header>

<main class="subject-main-container">
    <div class="subject-content-wrapper">
        <div class="subject-modules-container">
            {modules_html}
        </div>
    </div>
</main>

{render_footer(relative_root=relative_root)}
{render_search_modal()}

<script src="{relative_root}/js/search-index.js"></script>
<script src="{relative_root}/js/app.js"></script>
</body>
</html>
"""

def render_topic_page(subject_slug, topic, all_topics):
    sub_meta = topic_data.SUBJECT_DATA[subject_slug]["metadata"]
    
    # Find prev and next topics in same subject
    subj_topic_list = topic_data.SUBJECT_DATA[subject_slug]["topics"]
    curr_idx = -1
    for i, t in enumerate(subj_topic_list):
        if t["slug"] == topic["slug"]:
            curr_idx = i
            break
            
    prev_topic = subj_topic_list[curr_idx - 1] if curr_idx > 0 else None
    next_topic = subj_topic_list[curr_idx + 1] if curr_idx < len(subj_topic_list) - 1 else None

    # Workflow HTML
    workflow_html = ""
    if "workflow" in topic and topic["workflow"]:
        wf_steps = ""
        for s in topic["workflow"]:
            wf_steps += f"""
            <div class="workflow-step">
                <span class="step-badge">[{s['step']:02d}]</span>
                <div class="step-content">
                    <div class="step-title">{escape_text(s['name'])}</div>
                    <div class="step-desc">{escape_text(s['desc'])}</div>
                </div>
            </div>
            """
        workflow_html = f"""
        <section class="topic-section workflow-section" id="workflow">
            <div class="section-header">
                <h2><span class="sec-tag">[SEC 06]</span> System Architecture & Workflow Pipeline</h2>
            </div>
            <div class="workflow-container">
                {wf_steps}
            </div>
        </section>
        """

    # ASCII Diagram HTML
    diagram_html = ""
    if topic.get("ascii_diagram"):
        diagram_html = f"""
        <section class="topic-section diagram-section" id="architecture">
            <div class="section-header">
                <h2><span class="sec-tag">[SEC 07]</span> System Schematic & Block Diagram</h2>
            </div>
            <div class="diagram-box">
                <pre class="ascii-diagram"><code>{escape_text(topic["ascii_diagram"].strip())}</code></pre>
            </div>
        </section>
        """

    # Formulas HTML
    formulas_html = ""
    if "formulas" in topic and topic["formulas"]:
        form_cards = ""
        for f in topic["formulas"]:
            vars_list = "".join([f"<li><code>{escape_text(v[0])}</code>: {escape_text(v[1])}</li>" for v in f.get("vars", [])])
            form_cards += f"""
            <div class="formula-card">
                <div class="formula-name">{escape_text(f.get("name", "Engineering Formulation"))}</div>
                <div class="formula-math"><code>{escape_text(f.get("math", ""))}</code></div>
                <div class="formula-details">
                    <h5>Parameter Definitions:</h5>
                    <ul class="formula-vars">{vars_list}</ul>
                    {f'<div class="formula-example"><strong>Worked Numerical Example:</strong><br>{escape_text(f.get("example"))}</div>' if f.get("example") else ''}
                </div>
            </div>
            """
        formulas_html = f"""
        <section class="topic-section formulas-section" id="formulas">
            <div class="section-header">
                <h2><span class="sec-tag">[SEC 11]</span> Mathematical Formulas & Numerical Breakdown</h2>
            </div>
            <div class="formulas-grid">
                {form_cards}
            </div>
        </section>
        """

    # Comparison Table HTML
    table_html = ""
    if "comparison_table" in topic and topic["comparison_table"]:
        tbl = topic["comparison_table"]
        th_html = "".join([f"<th>{escape_text(h)}</th>" for h in tbl.get("headers", [])])
        tr_html = ""
        for row in tbl.get("rows", []):
            td_html = "".join([f"<td>{escape_text(cell)}</td>" for cell in row])
            tr_html += f"<tr>{td_html}</tr>"
        table_html = f"""
        <section class="topic-section table-section" id="comparison">
            <div class="section-header">
                <h2><span class="sec-tag">[SEC 10]</span> Technical Specifications & Benchmarks</h2>
            </div>
            <div class="table-responsive">
                <table class="specs-table">
                    <thead><tr>{th_html}</tr></thead>
                    <tbody>{tr_html}</tbody>
                </table>
            </div>
        </section>
        """

    # Code / Register snippet HTML
    code_html = ""
    if topic.get("code_snippet"):
        code_html = f"""
        <section class="topic-section code-section" id="code">
            <div class="section-header">
                <h2><span class="sec-tag">[SEC 12]</span> Embedded C Driver & Register Interface</h2>
                <button class="copy-btn" onclick="copyCodeBlock('codeBlock')">
                    <span class="icon">{SVG_CHECK}</span>
                    <span>Copy Code</span>
                </button>
            </div>
            <div class="code-container">
                <pre><code id="codeBlock" class="language-c">{escape_text(topic["code_snippet"].strip())}</code></pre>
            </div>
        </section>
        """

    # Short Q&A HTML
    short_qa_html = ""
    if "short_qa" in topic and topic["short_qa"]:
        items = ""
        for q, a in topic["short_qa"]:
            items += f"""
            <div class="qa-item short-qa-item">
                <div class="qa-question"><span class="q-badge">2 MARKS</span> {escape_text(q)}</div>
                <div class="qa-answer">{format_math_markdown(a)}</div>
            </div>
            """
        short_qa_html = f"""
        <div class="exam-qa-block">
            <h3>Short Answer Questions (1–2 Marks)</h3>
            <div class="qa-list">{items}</div>
        </div>
        """

    # Long Q&A HTML
    long_qa_html = ""
    if "long_qa" in topic and topic["long_qa"]:
        items = ""
        for q, a in topic["long_qa"]:
            items += f"""
            <div class="qa-item long-qa-item">
                <div class="qa-question"><span class="q-badge">10 MARKS</span> {escape_text(q)}</div>
                <div class="qa-answer">{format_math_markdown(a)}</div>
            </div>
            """
        long_qa_html = f"""
        <div class="exam-qa-block">
            <h3>Comprehensive Long Answer Questions (5–10 Marks)</h3>
            <div class="qa-list">{items}</div>
        </div>
        """

    # Viva Q&A HTML
    viva_qa_html = ""
    if "viva_interview_qa" in topic and topic["viva_interview_qa"]:
        items = ""
        for q, a in topic["viva_interview_qa"]:
            items += f"""
            <div class="qa-item viva-qa-item">
                <div class="qa-question"><span class="q-badge">VIVA / INTERVIEW</span> {escape_text(q)}</div>
                <div class="qa-answer">{format_math_markdown(a)}</div>
            </div>
            """
        viva_qa_html = f"""
        <div class="exam-qa-block">
            <h3>Viva Voce & Technical Interview Questions</h3>
            <div class="qa-list">{items}</div>
        </div>
        """

    # Mistakes HTML
    mistakes_html = ""
    if "common_mistakes" in topic and topic["common_mistakes"]:
        mistakes_li = "".join([f"<li><strong>Trap:</strong> {escape_text(m)}</li>" for m in topic["common_mistakes"]])
        mistakes_html = f"""
        <div class="callout callout-warning">
            <div class="callout-header">// COMMON EXAM TRAPS & MISCONCEPTIONS</div>
            <div class="callout-body">
                <ul>{mistakes_li}</ul>
            </div>
        </div>
        """

    # Key points HTML
    must_rem_li = "".join([f"<li>[KEY] {escape_text(p)}</li>" for p in topic.get("must_remember", [])])
    
    # Revision list HTML
    rev_li = "".join([f"<li>[REV] {escape_text(p)}</li>" for p in topic.get("revision_points", [])])

    # Navigation buttons
    prev_btn_html = f'<a href="{prev_topic["slug"]}.html" class="nav-prev-btn"><span class="icon">{SVG_ARROW_LEFT}</span><span>Previous: {escape_text(prev_topic["title"])}</span></a>' if prev_topic else '<span class="nav-disabled">First Topic in Course</span>'
    next_btn_html = f'<a href="{next_topic["slug"]}.html" class="nav-next-btn"><span>Next: {escape_text(next_topic["title"])}</span><span class="icon">{SVG_ARROW_RIGHT}</span></a>' if next_topic else '<span class="nav-disabled">End of Subject Topics</span>'

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{escape_text(topic["title"])} | {escape_text(sub_meta["title"])}</title>
    <meta name="description" content="{escape_text(topic.get("overview", "")[:150])}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../../css/style.css">
    <script>
      (function(){{
        const savedTheme = localStorage.getItem('sg-theme') || localStorage.getItem('mtech_theme') || 'light';
        if (savedTheme === 'dark') {{ document.documentElement.setAttribute('data-theme', 'dark'); }}
      }})();
    </script>
</head>
<body data-topic-id="{topic['slug']}" data-subject-id="{subject_slug}">

{render_navbar(relative_root="../..")}

<div class="topic-page-layout">
    <aside class="topic-sidebar">
        <div class="sidebar-header">
            <a href="../../subjects/{subject_slug}.html" class="sidebar-back">
                <span class="icon">{SVG_ARROW_LEFT}</span>
                <span>{escape_text(sub_meta["title"])}</span>
            </a>
            <div class="sidebar-subject-badge">{escape_text(sub_meta["code"])}</div>
        </div>
        <div class="sidebar-toc">
            <h4>Table of Contents</h4>
            <ul>
                <li><a href="#overview">Quick Overview</a></li>
                <li><a href="#objectives">Learning Objectives</a></li>
                <li><a href="#core-concept">Core Concept & Intuition</a></li>
                <li><a href="#lecture-notes">In-Class Lecture Notes</a></li>
                <li><a href="#extra-explanation">Comprehensive Theory</a></li>
                { '<li><a href="#workflow">Architecture & Workflow</a></li>' if workflow_html else '' }
                { '<li><a href="#architecture">System Schematic</a></li>' if diagram_html else '' }
                <li><a href="#working-principle">Working Principle</a></li>
                <li><a href="#application">Automotive Application</a></li>
                { '<li><a href="#comparison">Specifications Table</a></li>' if table_html else '' }
                { '<li><a href="#formulas">Math Formulas & Numericals</a></li>' if formulas_html else '' }
                { '<li><a href="#code">Embedded Driver / Registers</a></li>' if code_html else '' }
                <li><a href="#exam-questions">Exam & Viva Q&A</a></li>
                <li><a href="#revision-card">60-Second Flash Card</a></li>
                <li><a href="#personal-notes">My Personal Notes</a></li>
            </ul>
        </div>
        <div class="sidebar-progress-widget">
            <h4>Topic Status</h4>
            <div class="status-btn-group">
                <button class="status-btn" id="statusNotStarted" onclick="setTopicStatus('{topic['slug']}', 'not_started')">☐ Not Started</button>
                <button class="status-btn" id="statusInProgress" onclick="setTopicStatus('{topic['slug']}', 'in_progress')">◐ In Progress</button>
                <button class="status-btn" id="statusCompleted" onclick="setTopicStatus('{topic['slug']}', 'completed')">☑ Mastered</button>
            </div>
            <button class="bookmark-btn" id="bookmarkBtn" onclick="toggleBookmark('{topic['slug']}')">★ Bookmark for Revision</button>
        </div>
    </aside>

    <main class="topic-main-content">
        <header class="topic-header">
            <div class="breadcrumbs">
                <a href="../../index.html">Home</a> / 
                <a href="../../semesters/sem1.html">Semester 1</a> / 
                <a href="../../subjects/{subject_slug}.html">{escape_text(sub_meta["title"])}</a> / 
                <span class="curr-crumb">{escape_text(topic["title"])}</span>
            </div>
            
            <div class="topic-meta-row">
                <span class="meta-pill module-pill">MODULE: {escape_text(topic.get("module", "Core Module"))}</span>
                <span class="meta-pill level-pill">LEVEL: {escape_text(topic.get("level", "Intermediate"))}</span>
                <span class="meta-pill importance-pill">WEIGHT: {topic.get('importance', 5)}/5</span>
                <span class="meta-pill code-pill">{escape_text(sub_meta["code"])}</span>
            </div>

            <h1 class="topic-main-title">{escape_text(topic["title"])}</h1>

            <div class="action-bar-top">
                <div class="read-estimate">Estimated Read Time: <strong>12–15 mins</strong></div>
                <div class="action-buttons-group">
                    <button class="print-btn" onclick="window.print()" title="Print this complete note page or save as PDF">
                        <span class="icon">{SVG_PRINT}</span>
                        <span>Print / Save PDF</span>
                    </button>
                </div>
            </div>
        </header>

        <section class="topic-section" id="overview">
            <div class="section-header">
                <h2><span class="sec-tag">[SEC 01]</span> Quick Overview</h2>
            </div>
            <p class="overview-lead">{escape_text(topic.get("overview", ""))}</p>
        </section>

        <section class="topic-section" id="objectives">
            <div class="section-header">
                <h2><span class="sec-tag">[SEC 02]</span> Learning Objectives & Prerequisites</h2>
            </div>
            <div class="objectives-card">
                <h5>What You Will Master:</h5>
                <ul class="objectives-list">
                    {"".join([f"<li>{escape_text(obj)}</li>" for obj in topic.get("learning_objectives", [])])}
                </ul>
                <div class="prereq-note">
                    <strong>Prerequisites:</strong> {escape_text(topic.get("prerequisites", "None"))}
                </div>
            </div>
        </section>

        <section class="topic-section" id="core-concept">
            <div class="section-header">
                <h2><span class="sec-tag">[SEC 03]</span> Core Concept & Physical Intuition</h2>
            </div>
            <div class="concept-body">
                <p>{escape_text(topic.get("core_concept", ""))}</p>
            </div>
        </section>

        <section class="topic-section" id="lecture-notes">
            <div class="section-header">
                <h2><span class="sec-tag">[SEC 04]</span> In-Class Lecture Transcript Breakdown</h2>
            </div>
            <div class="callout callout-lecture">
                <div class="callout-header">// LECTURE TRANSCRIPT SYNTHESIS</div>
                <div class="callout-body">
                    <p>{escape_text(topic.get("lecture_notes", ""))}</p>
                </div>
            </div>
        </section>

        <section class="topic-section" id="extra-explanation">
            <div class="section-header">
                <h2><span class="sec-tag">[SEC 05]</span> Rigorous Engineering Theory & Derivations</h2>
            </div>
            <div class="callout callout-deep">
                <div class="callout-header">// RIGOROUS ENGINEERING THEORY</div>
                <div class="callout-body">
                    <p>{escape_text(topic.get("extra_explanation", ""))}</p>
                </div>
            </div>
        </section>

        {workflow_html}
        {diagram_html}

        <section class="topic-section" id="working-principle">
            <div class="section-header">
                <h2><span class="sec-tag">[SEC 08]</span> Step-by-Step Operational Principle</h2>
            </div>
            <div class="principle-body">
                <p>{escape_text(topic.get("working_principle", ""))}</p>
            </div>
        </section>

        <section class="topic-section" id="application">
            <div class="section-header">
                <h2><span class="sec-tag">[SEC 09]</span> Real Automotive Application</h2>
            </div>
            <div class="callout callout-application">
                <div class="callout-header">// AUTOMOTIVE OEM CASE STUDY</div>
                <div class="callout-body">
                    <p>{escape_text(topic.get("application", ""))}</p>
                </div>
            </div>
        </section>

        {table_html}
        {formulas_html}
        {code_html}

        <section class="topic-section" id="must-remember">
            <div class="section-header">
                <h2><span class="sec-tag">[SEC 13]</span> Must-Remember Key Points for Exams</h2>
            </div>
            <div class="must-remember-card">
                <ul>{must_rem_li}</ul>
            </div>
        </section>

        {mistakes_html}

        <section class="topic-section" id="exam-questions">
            <div class="section-header">
                <h2><span class="sec-tag">[SEC 15]</span> Exam Preparation & Model Questions</h2>
            </div>
            <div class="exam-qa-container">
                {short_qa_html}
                {long_qa_html}
                {viva_qa_html}
            </div>
        </section>

        <section class="topic-section" id="revision-card">
            <div class="section-header">
                <h2><span class="sec-tag">[SEC 18]</span> 60-Second Flash / Revision Card</h2>
            </div>
            <div class="flashcard">
                <div class="flashcard-badge">// 60-SECOND REVISION SUMMARY</div>
                <ul class="flashcard-points">{rev_li}</ul>
            </div>
        </section>

        <section class="topic-section" id="personal-notes">
            <div class="section-header">
                <h2><span class="sec-tag">[SEC 19]</span> Personal Study Notes (Auto-Saved)</h2>
            </div>
            <div class="personal-notes-widget">
                <p class="notes-hint">Type personal notes or lab observations below. Content auto-saves to your local browser storage.</p>
                <textarea id="personalNotePad" class="personal-notes-textarea" placeholder="Type personal study notes here..." oninput="savePersonalNote('{topic['slug']}', this.value)"></textarea>
                <div class="notes-save-indicator" id="notesSavedTag">✓ Saved locally</div>
            </div>
        </section>

        <section class="topic-section" id="sources">
            <div class="section-header">
                <h2><span class="sec-tag">[SEC 20]</span> Source Traceability & Curriculum References</h2>
            </div>
            <div class="sources-box">
                <p><strong>Primary Source Reference:</strong> {escape_text(topic.get("sources", "BITS Pilani M.Tech Course Handouts and Lecture Transcripts."))}</p>
            </div>
        </section>

        <nav class="topic-pagination">
            <div class="pagination-prev">{prev_btn_html}</div>
            <div class="pagination-next">{next_btn_html}</div>
        </nav>
    </main>
</div>

{render_footer(relative_root="../..")}
{render_search_modal()}

<script src="../../js/search-index.js"></script>
<script src="../../js/app.js"></script>
</body>
</html>
"""
    return html_content

def generate_all_html():
    print("Beginning institutional HTML generation...", flush=True)
    
    # Ensure assets directory is copied
    src_assets = PROJECT_ROOT / "assets"
    dst_assets = STUDY_GUIDE_DIR / "assets"
    if src_assets.exists():
        shutil.copytree(src_assets, dst_assets, dirs_exist_ok=True)
        print("Copied assets to StudyGuide/assets")

    # 1. Generate Master Homepage
    home_html = render_home_page()
    (STUDY_GUIDE_DIR / "index.html").write_text(home_html, encoding='utf-8')
    print("Generated StudyGuide/index.html")

    # 2. Generate Semester 1 Hub
    sem_dir = STUDY_GUIDE_DIR / "semesters"
    sem_dir.mkdir(parents=True, exist_ok=True)
    sem1_html = render_semester_hub()
    (sem_dir / "sem1.html").write_text(sem1_html, encoding='utf-8')
    print("Generated StudyGuide/semesters/sem1.html")

    # Also generate StudyGuide/sem-1/index.html for legacy compatibility
    sem1_alias_dir = STUDY_GUIDE_DIR / "sem-1"
    sem1_alias_dir.mkdir(parents=True, exist_ok=True)
    (sem1_alias_dir / "index.html").write_text(sem1_html, encoding='utf-8')
    print("Generated StudyGuide/sem-1/index.html")

    # 3. Generate Subject Dashboards & Topics
    subj_dir = STUDY_GUIDE_DIR / "subjects"
    subj_dir.mkdir(parents=True, exist_ok=True)
    
    topic_base_dir = STUDY_GUIDE_DIR / "topics"
    topic_base_dir.mkdir(parents=True, exist_ok=True)

    all_topics = topic_data.get_all_topics()
    total_generated = 0

    for sub_slug, data in topic_data.SUBJECT_DATA.items():
        # Render Subject Dashboard
        subj_html = render_subject_dashboard(sub_slug)
        (subj_dir / f"{sub_slug}.html").write_text(subj_html, encoding='utf-8')
        print(f"Generated Subject Dashboard: StudyGuide/subjects/{sub_slug}.html")

        # Also create sem-1/{sub_slug}/index.html alias with correct relative root
        alias_sub_dir = sem1_alias_dir / sub_slug
        alias_sub_dir.mkdir(parents=True, exist_ok=True)
        alias_subj_html = render_subject_dashboard(sub_slug, relative_root="../..")
        (alias_sub_dir / "index.html").write_text(alias_subj_html, encoding='utf-8')

        # Create topic subdirectory
        sub_topic_dir = topic_base_dir / sub_slug
        sub_topic_dir.mkdir(parents=True, exist_ok=True)

        # Render Individual Topics
        for t in data["topics"]:
            topic_html = render_topic_page(sub_slug, t, all_topics)
            (sub_topic_dir / f"{t['slug']}.html").write_text(topic_html, encoding='utf-8')
            total_generated += 1

    print(f"\nSUCCESS: Generated {total_generated} institutional topic pages across 4 subjects!")

if __name__ == '__main__':
    generate_all_html()
