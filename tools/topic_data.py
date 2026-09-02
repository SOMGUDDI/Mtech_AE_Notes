"""Master Topic Data Aggregator for all 4 Semester 1 Courses.
Imports and validates datasets from data_ac, data_av, data_at, and data_esd.
"""
from pathlib import Path
import sys

# Add tools directory to path
TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

import data_ac
import data_av
import data_at
import data_esd

SUBJECT_DATA = {
    "automotive-communication": {
        "metadata": data_ac.SUBJECT_METADATA,
        "topics": data_ac.TOPICS
    },
    "automotive-vehicle": {
        "metadata": data_av.SUBJECT_METADATA,
        "topics": data_av.TOPICS
    },
    "autotronics": {
        "metadata": data_at.SUBJECT_METADATA,
        "topics": data_at.TOPICS
    },
    "embedded-system-design": {
        "metadata": data_esd.SUBJECT_METADATA,
        "topics": data_esd.TOPICS
    }
}

def get_all_topics():
    all_t = []
    for sub_slug, data in SUBJECT_DATA.items():
        for t in data["topics"]:
            all_t.append((sub_slug, t))
    return all_t

if __name__ == '__main__':
    total = 0
    for sub_slug, data in SUBJECT_DATA.items():
        count = len(data["topics"])
        total += count
        print(f"[{sub_slug}] {data['metadata']['title']} -> {count} topics")
    print(f"Total Topics Loaded: {total}")
