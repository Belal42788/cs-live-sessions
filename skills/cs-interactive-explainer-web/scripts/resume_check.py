#!/usr/bin/env python3
"""
resume_check.py — progress tracking for cs-interactive-explainer's Q&A phase.

Progress is stored as a small JSON file next to where the skill is being run,
named `.cs-interactive-explainer-progress-<slug>.json`, where <slug> is a
short identifier derived from the lesson title (or content) — this keeps
progress files distinct per lesson so working on two lessons doesn't collide.

Usage (called by the assistant running the skill, not by the end user):

  # 1. At the start of a run, check whether a progress file already exists:
  python3 resume_check.py check "<slug>"
    -> prints JSON: {"exists": true/false, "sections_done": [...], "data": {...}}
       or {"exists": false}

  # 2. Immediately after finishing a section's Q&A, save it:
  python3 resume_check.py save "<slug>" "<section_id>" '<json_answers>'
    -> writes/updates the progress file right away (not held in memory)

  # 3. After the master prompt has been generated successfully:
  python3 resume_check.py clear "<slug>"
    -> deletes the progress file
"""
import json
import re
import sys
from pathlib import Path


def _progress_path(slug: str) -> Path:
    safe_slug = re.sub(r"[^a-zA-Z0-9_-]", "-", slug.strip().lower())[:80]
    return Path.cwd() / f".cs-interactive-explainer-progress-{safe_slug}.json"


def check(slug: str) -> None:
    path = _progress_path(slug)
    if not path.exists():
        print(json.dumps({"exists": False}, ensure_ascii=False))
        return
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        print(json.dumps({"exists": False}, ensure_ascii=False))
        return
    print(json.dumps(
        {"exists": True, "sections_done": list(data.get("sections", {}).keys()), "data": data},
        ensure_ascii=False,
    ))


def save(slug: str, section_id: str, answers_json: str) -> None:
    path = _progress_path(slug)
    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            data = {"sections": {}}
    else:
        data = {"sections": {}}

    try:
        answers = json.loads(answers_json)
    except json.JSONDecodeError:
        print(json.dumps({"ok": False, "error": "answers_json is not valid JSON"}, ensure_ascii=False))
        sys.exit(1)

    data.setdefault("sections", {})[section_id] = answers
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"ok": True, "saved_section": section_id, "path": str(path)}, ensure_ascii=False))


def clear(slug: str) -> None:
    path = _progress_path(slug)
    if path.exists():
        path.unlink()
        print(json.dumps({"ok": True, "cleared": True}, ensure_ascii=False))
    else:
        print(json.dumps({"ok": True, "cleared": False, "note": "no progress file existed"}, ensure_ascii=False))


def main() -> None:
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    command, slug = sys.argv[1], sys.argv[2]

    if command == "check":
        check(slug)
    elif command == "save":
        if len(sys.argv) < 4:
            print(json.dumps({"ok": False, "error": "save requires: save <slug> <section_id> <json_answers>"}, ensure_ascii=False))
            sys.exit(1)
        section_id = sys.argv[3]
        answers_json = sys.argv[4] if len(sys.argv) > 4 else "{}"
        save(slug, section_id, answers_json)
    elif command == "clear":
        clear(slug)
    else:
        print(json.dumps({"ok": False, "error": f"unknown command: {command}"}, ensure_ascii=False))
        sys.exit(1)


if __name__ == "__main__":
    main()
