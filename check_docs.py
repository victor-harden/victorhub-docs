#!/usr/bin/env python3
"""Validate VictorHub documentation links, titles and navigation."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
DOCS = BASE / "docs"
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def check_links():
    problems = []
    for path in sorted(DOCS.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for target in LINK.findall(text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            clean = target.split("#", 1)[0]
            if clean and not (path.parent / clean).resolve().exists():
                problems.append(f"{path.name}: broken link {target}")
    return problems


def check_titles():
    problems = []
    for path in sorted(DOCS.rglob("*.md")):
        first = next((line for line in path.read_text(encoding="utf-8").splitlines()
                      if line.strip()), "")
        if not first.startswith("# "):
            problems.append(f"{path.name}: missing level-1 title")
    return problems


def check_nav():
    nav_path = BASE / "mkdocs.yml"
    if not nav_path.exists():
        return ["mkdocs.yml is missing"]
    problems = []
    for line in nav_path.read_text(encoding="utf-8").splitlines():
        if ":" in line and line.strip().endswith(".md"):
            target = line.split(":", 1)[1].strip()
            if not (DOCS / target).exists():
                problems.append(f"mkdocs.yml: missing page {target}")
    return problems


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Documentation checker")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    problems = check_links() + check_titles() + check_nav()
    if args.json:
        print(json.dumps({"problems": problems, "ok": not problems}, indent=2))
    else:
        print("\n".join(problems) if problems else "docs ok")
    return 0 if not problems else 1


if __name__ == "__main__":
    raise SystemExit(main())
