"""Builds search indices and structured JSON data files for offline search and interactive features."""
import sys
import json
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

TOOLS_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = TOOLS_DIR.parent
STUDY_GUIDE_DIR = PROJECT_ROOT / "StudyGuide"
DATA_DIR = STUDY_GUIDE_DIR / "data"
JS_DIR = STUDY_GUIDE_DIR / "js"

if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

import topic_data

def build_indices():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    JS_DIR.mkdir(parents=True, exist_ok=True)

    search_items = []
    topics_list = []
    subjects_list = []

    for sub_slug, data in topic_data.SUBJECT_DATA.items():
        sub_meta = data["metadata"]
        subjects_list.append({
            "slug": sub_slug,
            "title": sub_meta["title"],
            "code": sub_meta["code"],
            "credits": sub_meta.get("credits", "3-0-0"),
            "topic_count": len(data["topics"])
        })

        for t in data["topics"]:
            keywords = [
                t["title"],
                t.get("module", ""),
                t.get("level", ""),
                sub_meta["title"],
                sub_meta["code"]
            ]
            
            if "formulas" in t:
                for f in t["formulas"]:
                    keywords.append(f.get("name", ""))

            if "short_qa" in t:
                for q, _ in t["short_qa"]:
                    keywords.append(q)

            if "long_qa" in t:
                for q, _ in t["long_qa"]:
                    keywords.append(q)

            search_entry = {
                "id": t["slug"],
                "subject": sub_slug,
                "subject_code": sub_meta["code"],
                "subject_title": sub_meta["title"],
                "title": t["title"],
                "module": t.get("module", ""),
                "level": t.get("level", "Intermediate"),
                "importance": t.get("importance", 5),
                "url": f"topics/{sub_slug}/{t['slug']}.html",
                "summary": t.get("overview", "")[:180],
                "keywords": " ".join(keywords)
            }
            search_items.append(search_entry)

            topic_item = {
                "slug": t["slug"],
                "subject": sub_slug,
                "title": t["title"],
                "module": t.get("module", ""),
                "importance": t.get("importance", 5),
                "url": f"topics/{sub_slug}/{t['slug']}.html"
            }
            topics_list.append(topic_item)

    (DATA_DIR / "search-index.json").write_text(json.dumps(search_items, indent=2), encoding='utf-8')
    print(f"Generated {DATA_DIR / 'search-index.json'} ({len(search_items)} searchable topics)")

    (DATA_DIR / "topics.json").write_text(json.dumps(topics_list, indent=2), encoding='utf-8')
    print(f"Generated {DATA_DIR / 'topics.json'}")

    (DATA_DIR / "subjects.json").write_text(json.dumps(subjects_list, indent=2), encoding='utf-8')
    print(f"Generated {DATA_DIR / 'subjects.json'}")

    js_content = f"window.SEARCH_INDEX = {json.dumps(search_items, indent=2)};\n"
    (JS_DIR / "search-index.js").write_text(js_content, encoding='utf-8')
    print(f"Generated {JS_DIR / 'search-index.js'}")

if __name__ == '__main__':
    build_indices()
