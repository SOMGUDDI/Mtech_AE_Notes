"""Generates rich datasets for Automotive Communication, Automotive Vehicle, Autotronics, and Embedded System Design."""
import json
from pathlib import Path

TOOLS_DIR = Path(__file__).parent

def write_file(filename, content):
    p = TOOLS_DIR / filename
    p.write_text(content, encoding='utf-8')
    print(f"Generated {filename} ({len(content.splitlines())} lines)")

print("Data builder ready.")
