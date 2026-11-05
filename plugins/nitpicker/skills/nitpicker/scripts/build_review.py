#!/usr/bin/env python3
"""Fill the review template with review data and write a standalone HTML page.

Usage: python3 build_review.py <review.json> <out.html>

review.json shape:
{
  "title": "Doc or article title",
  "slug": "short-file-name",
  "source": "Where the text came from",
  "generated": "2026-11-04",
  "verdict": "Not ready: 3 blocking questions",
  "original": "<the full original text, verbatim>",
  "items": [
    {"id": 1, "severity": "blocking" | "non-blocking", "kind": "rewrite" | "question",
     "snippet": "exact substring of original", "issue": "what a reader would have to decide",
     "suggestion": "replacement text", "evidence": "optional locators"}
  ]
}
"""
import json
import sys
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parent.parent / "assets" / "review-template.html"


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    original = data.get("original", "")
    problems = []
    seen = set()
    for it in data.get("items", []):
        if it.get("id") in seen:
            problems.append(f"duplicate id {it.get('id')}")
        seen.add(it.get("id"))
        if it.get("severity") not in ("blocking", "non-blocking"):
            problems.append(f"#{it.get('id')}: severity must be blocking or non-blocking")
        snip = it.get("snippet", "")
        if not snip or snip not in original:
            problems.append(f"#{it.get('id')}: snippet is not an exact substring of original")
        elif original.count(snip) > 1:
            problems.append(f"#{it.get('id')}: snippet occurs {original.count(snip)} times; lengthen it so it is unique")
    # Escape so embedded text can never close the <script> block.
    payload = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c")
    html = TEMPLATE.read_text(encoding="utf-8").replace("__REVIEW_DATA__", payload)
    Path(sys.argv[2]).write_text(html, encoding="utf-8")
    print(f"wrote {sys.argv[2]} ({len(data.get('items', []))} items)")
    for p in problems:
        print(f"WARNING: {p}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
