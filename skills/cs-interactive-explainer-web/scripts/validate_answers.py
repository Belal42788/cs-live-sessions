#!/usr/bin/env python3
"""
validate_answers.py — checks that Q&A answers are complete before the
master prompt is generated for cs-interactive-explainer.

Usage:
  python3 validate_answers.py <progress_file.json> [expected_section_ids_comma_separated]

If expected_section_ids is given, the script also checks that every expected
section actually has an entry (catches a section that was skipped entirely,
not just one with incomplete fields).

Required fields per section:
  - learning_objective   (non-empty string)
  - examples              (non-empty string or list)
  - common_mistakes      (non-empty string)
  - interaction_type     (non-empty string)
  - quiz                 (dict with "wanted": true/false; if wanted is true,
                           must also have "count": an integer >= 1)

Exits 0 and prints {"ok": true} if everything required is present.
Exits 1 and prints a JSON report of what's missing otherwise.
"""
import json
import sys
from pathlib import Path

REQUIRED_FIELDS = ["learning_objective", "examples", "common_mistakes", "interaction_type", "quiz"]


def _is_filled(value) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return value.strip() != ""
    if isinstance(value, (list, dict)):
        return len(value) > 0
    return True


def validate_section(answers: dict) -> list:
    missing = []
    for field in REQUIRED_FIELDS:
        if field not in answers or not _is_filled(answers.get(field)):
            missing.append(field)

    quiz = answers.get("quiz")
    if isinstance(quiz, dict):
        if "wanted" not in quiz:
            missing.append("quiz.wanted")
        elif quiz.get("wanted") is True and not quiz.get("count"):
            missing.append("quiz.count")

    return missing


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    progress_path = Path(sys.argv[1])
    if not progress_path.exists():
        print(json.dumps({"ok": False, "error": f"file not found: {progress_path}"}, ensure_ascii=False))
        sys.exit(1)

    try:
        data = json.loads(progress_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(json.dumps({"ok": False, "error": f"invalid JSON: {e}"}, ensure_ascii=False))
        sys.exit(1)

    sections = data.get("sections", {})
    expected_ids = []
    if len(sys.argv) > 2 and sys.argv[2].strip():
        expected_ids = [s.strip() for s in sys.argv[2].split(",") if s.strip()]

    missing_sections = [sid for sid in expected_ids if sid not in sections]

    incomplete = {}
    for section_id, answers in sections.items():
        missing_fields = validate_section(answers if isinstance(answers, dict) else {})
        if missing_fields:
            incomplete[section_id] = missing_fields

    ok = not missing_sections and not incomplete

    report = {"ok": ok}
    if missing_sections:
        report["missing_sections"] = missing_sections
    if incomplete:
        report["incomplete_sections"] = incomplete

    print(json.dumps(report, ensure_ascii=False, indent=2))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
