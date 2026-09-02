"""Scans and extracts text inventory from all raw DOCX and PDF lecture transcripts."""
import sys
import json
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
STUDY_GUIDE_DATA = ROOT / "StudyGuide" / "data"

SUBJECT_DIRS = {
    "Automotive Communication": "AELZG513",
    "Automotive Vehicle": "AELZC441",
    "Autotronics": "AEZG533 / AELZG533",
    "Embedded System Design": "AEZG512 / AELZC512"
}

def extract_docx_text(docx_path):
    try:
        with zipfile.ZipFile(docx_path) as z:
            xml_content = z.read('word/document.xml')
            tree = ET.fromstring(xml_content)
            paragraphs = []
            for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
                texts = [node.text for node in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text]
                if texts:
                    paragraphs.append(''.join(texts))
            return '\n'.join(paragraphs)
    except Exception as e:
        return f"[Error extracting DOCX: {e}]"

def scan_sources():
    STUDY_GUIDE_DATA.mkdir(parents=True, exist_ok=True)
    inventory = []
    total_words = 0
    total_files = 0

    for subj_name, course_code in SUBJECT_DIRS.items():
        subj_dir = ROOT / subj_name
        if not subj_dir.exists():
            continue
        
        for file_path in subj_dir.rglob('*'):
            if file_path.is_file() and file_path.suffix.lower() in ['.docx', '.pdf', '.pptx', '.ppt', '.txt', '.vtt']:
                total_files += 1
                rel_path = file_path.relative_to(ROOT).as_posix()
                size_kb = round(file_path.stat().st_size / 1024, 1)
                
                word_count = 0
                if file_path.suffix.lower() == '.docx':
                    text = extract_docx_text(file_path)
                    word_count = len(text.split())
                    total_words += word_count
                
                inventory.append({
                    "subject": subj_name,
                    "course_code": course_code,
                    "filename": file_path.name,
                    "path": rel_path,
                    "size_kb": size_kb,
                    "extension": file_path.suffix.lower(),
                    "word_count": word_count
                })

    out_file = STUDY_GUIDE_DATA / "source-inventory.json"
    out_file.write_text(json.dumps(inventory, indent=2), encoding='utf-8')
    print(f"Scanned {total_files} lecture files across 4 subjects. Extracted {total_words:,} words from transcripts.")
    print(f"Saved source inventory to {out_file}")

if __name__ == '__main__':
    scan_sources()
