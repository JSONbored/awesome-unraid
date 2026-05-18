#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"


def main() -> int:
    readme = README.read_text()
    xml_names = published_template_names()
    listed_names = readme_available_template_names(readme)
    expected_count = len(xml_names)

    failures: list[str] = []
    for label, pattern in {
        "At A Glance available template count": r"Available templates: `(\d+)`",
        "Available Templates heading count": r"### Available Templates \((\d+)\)",
    }.items():
        match = re.search(pattern, readme)
        if not match:
            failures.append(f"{label} is missing")
            continue
        count = int(match.group(1))
        if count != expected_count:
            failures.append(f"{label} is {count}, expected {expected_count}")

    missing = sorted(set(xml_names) - set(listed_names))
    extra = sorted(set(listed_names) - set(xml_names))
    if missing:
        failures.append("README is missing published templates: " + ", ".join(missing))
    if extra:
        failures.append("README lists templates without root XML: " + ", ".join(extra))

    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    return 0


def published_template_names() -> list[str]:
    names: list[str] = []
    for path in sorted(ROOT.glob("*.xml")):
        if path.name == "ca_profile.xml":
            continue
        root = ElementTree.parse(path).getroot()
        name = (root.findtext("Name") or "").strip()
        if not name:
            raise ValueError(f"{path.name} is missing <Name>")
        names.append(name)
    return names


def readme_available_template_names(readme: str) -> list[str]:
    section_match = re.search(
        r"### Available Templates \(\d+\)\n(?P<section>.*?)(?:\n### |\Z)",
        readme,
        re.S,
    )
    if not section_match:
        return []
    return re.findall(r"^- \*\*\[([^]]+)\]\(", section_match.group("section"), re.M)


if __name__ == "__main__":
    raise SystemExit(main())
