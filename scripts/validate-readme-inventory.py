#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
EXPECTED_PUBLISHED_IMAGES = (
    "jsonbored/dify-aio",
    "jsonbored/infisical-aio",
    "jsonbored/khoj-aio",
    "jsonbored/mem0-aio",
    "jsonbored/nanoclaw-agent",
    "jsonbored/nanoclaw-aio",
    "jsonbored/penpot-aio",
    "jsonbored/signoz-agent",
    "jsonbored/signoz-aio",
    "jsonbored/simplelogin-aio",
    "jsonbored/sure-aio",
    "jsonbored/sure-aio-alpha",
)


def main() -> int:
    readme = README.read_text()
    xml_names = published_template_names()
    listed_names = readme_available_template_names(readme)
    image_names = readme_published_image_names(readme)
    expected_count = len(xml_names)
    expected_image_count = len(EXPECTED_PUBLISHED_IMAGES)

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

    image_count_match = re.search(r"Published image packages: `(\d+)`", readme)
    if not image_count_match:
        failures.append("At A Glance published image package count is missing")
    else:
        image_count = int(image_count_match.group(1))
        if image_count != expected_image_count:
            failures.append(
                f"At A Glance published image package count is {image_count}, "
                f"expected {expected_image_count}"
            )

    missing = sorted(set(xml_names) - set(listed_names))
    extra = sorted(set(listed_names) - set(xml_names))
    if missing:
        failures.append("README is missing published templates: " + ", ".join(missing))
    if extra:
        failures.append("README lists templates without root XML: " + ", ".join(extra))

    missing_images = sorted(set(EXPECTED_PUBLISHED_IMAGES) - set(image_names))
    extra_images = sorted(set(image_names) - set(EXPECTED_PUBLISHED_IMAGES))
    if missing_images:
        failures.append(
            "README is missing published images: " + ", ".join(missing_images)
        )
    if extra_images:
        failures.append(
            "README lists unexpected published images: " + ", ".join(extra_images)
        )

    duplicated_images = sorted(
        {image for image in image_names if image_names.count(image) > 1}
    )
    if duplicated_images:
        failures.append(
            "README lists duplicate published images: " + ", ".join(duplicated_images)
        )

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


def readme_published_image_names(readme: str) -> list[str]:
    section_match = re.search(
        r"## Published Image Packages\n(?P<section>.*?)(?:\n## |\Z)",
        readme,
        re.S,
    )
    if not section_match:
        return []
    return re.findall(r"^\| \[`([^`]+)`\]\(", section_match.group("section"), re.M)


if __name__ == "__main__":
    raise SystemExit(main())
