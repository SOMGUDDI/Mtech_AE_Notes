# M.Tech Automotive Electronics Study Guide

`StudyGuide/` is the generated, offline-first Semester 1 study website. The original `Automotive Communication`, `Automotive Vehicle`, `Autotronics`, and `Embedded System Design` folders are source material and are never modified by the builder.

## Use it

Run `python build.py`, then open `StudyGuide/index.html` directly. It works without a server. For a local HTTP server, run `python -m http.server 8000 --directory StudyGuide` and open `http://localhost:8000`.

Run `python validate.py` after a build to check generated HTML links, page titles, and JSON data.

## Structure

- `StudyGuide/sem-1/` — four subject dashboards and individual topic pages
- `StudyGuide/css/`, `StudyGuide/js/` — local styles and offline study features
- `StudyGuide/data/` — subject/topic metadata, searchable index, and source-file inventory
- `build.py` — the maintainable page generator and curated topic map
- `validate.py` — static site validation

Topic pages label lecture synthesis separately from additional explanation. Progress, bookmarks, theme choice, recently viewed topics, and personal notes use browser local storage; nothing is uploaded.

## Adding a lecture

Keep the new PPT, PDF, or Teams transcript in its original subject folder. Add a source-traceable entry to `TOPICS` in `build.py`, then run `python build.py` and `python validate.py`. Do not move or overwrite original lecture files.
