"""Master Build Pipeline for M.Tech Study Guide Website.

Runs:
1. tools/scan_notes.py (Inventories raw docx/pdf lecture materials)
2. tools/build_search_index.py (Builds search index and JSON data)
3. tools/generate_html.py (Renders master homepage, semester hubs, subject dashboards, and detailed topic pages)
4. Validates output integrity

Run: python build.py
"""
import sys
import subprocess
from pathlib import Path

# Ensure UTF-8 output on Windows PowerShell
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent
TOOLS = ROOT / "tools"

def run_step(description, script_path):
    print(f"\n========================================================")
    print(f"[STEP] {description}")
    print(f"========================================================")
    result = subprocess.run([sys.executable, str(script_path)], cwd=str(ROOT))
    if result.returncode != 0:
        print(f"[ERROR] Step failed: {description}")
        sys.exit(result.returncode)

def main():
    print("=== Starting Master Build for M.Tech Automotive Engineering Study Guide ===")
    
    # 1. Scan source notes
    run_step("Scanning Raw Lecture Transcripts & Notes", TOOLS / "scan_notes.py")
    
    # 2. Build search index and JSON data
    run_step("Building Offline Search Indices & Metadata", TOOLS / "build_search_index.py")
    
    # 3. Generate HTML pages
    run_step("Rendering Comprehensive HTML Topic Pages & Dashboards", TOOLS / "generate_html.py")
    
    # 4. Run validation
    run_step("Running Integrity & Link Verification", ROOT / "validate.py")
    
    print("\n========================================================")
    print("[SUCCESS] BUILD COMPLETE & FULLY VALIDATED!")
    print("========================================================")
    print("To preview the website locally, run:")
    print("  python -m http.server 8000 --directory StudyGuide")
    print("Then open: http://localhost:8000 in your browser.")

if __name__ == '__main__':
    main()
