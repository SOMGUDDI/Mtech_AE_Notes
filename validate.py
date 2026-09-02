"""Offline validation for generated StudyGuide HTML links, assets, and JSON files."""
import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent / 'StudyGuide'
errors = []

pages = list(ROOT.rglob('*.html'))
print(f"Found {len(pages)} HTML pages to validate...")

for page in pages:
    text = page.read_text(encoding='utf-8')
    
    # 1. Check title
    if '<title>' not in text:
        errors.append(f'Missing <title> tag: {page.relative_to(ROOT)}')
        
    # 2. Check CSS link
    if 'rel="stylesheet"' in text and '<link' not in text:
        errors.append(f'Malformed CSS link: {page.relative_to(ROOT)}')
        
    # 3. Check internal href links
    for href in re.findall(r'href="([^"]+)"', text):
        if href.startswith(('#', 'http://', 'https://', 'javascript:')):
            continue
        target = (page.parent / href).resolve()
        if not target.exists():
            errors.append(f'Broken link in {page.relative_to(ROOT)} -> {href} (Resolved: {target})')

    # 4. Check internal script src
    for src in re.findall(r'src="([^"]+)"', text):
        if src.startswith(('http://', 'https://')):
            continue
        target = (page.parent / src).resolve()
        if not target.exists():
            errors.append(f'Missing script in {page.relative_to(ROOT)} -> {src}')

# 5. Check JSON validity
for p in (ROOT / 'data').glob('*.json'):
    try:
        json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:
        errors.append(f'Invalid JSON in {p.relative_to(ROOT)}: {e}')

print('========================================================')
print('STUDY GUIDE VALIDATION REPORT')
print('========================================================')
print(f'Total HTML pages checked  : {len(pages)}')
print(f'Total JSON datasets checked: {len(list((ROOT / "data").glob("*.json")))}')
print(f'Total Broken / Invalid Items: {len(errors)}')

if errors:
    for error in errors:
        print('[ERROR]', error)
    sys.exit(1)
else:
    print('[PASS] Status: ALL CHECKS PASSED (0 broken links, 0 missing assets)')
