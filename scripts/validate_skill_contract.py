from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_FILES = [
    ROOT / "SKILL.md",
    ROOT / "plugin" / "skills" / "hookradar-creative-intelligence" / "SKILL.md",
]
VERSION_FILES = [
    ROOT / "plugin" / ".claude-plugin" / "plugin.json",
    ROOT / "plugin" / ".codex-plugin" / "plugin.json",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_text(path: Path) -> str:
    if not path.exists():
        fail(f"missing file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def require(text: str, pattern: str, label: str, path: Path) -> None:
    if not re.search(pattern, text, re.IGNORECASE | re.MULTILINE):
        fail(f"{path.relative_to(ROOT)} missing {label}")


def validate_skill(path: Path) -> None:
    text = read_text(path)
    require(text, r"## MCP-only request gate", "MCP-only request gate section", path)
    require(text, r"do not attempt to fulfill the full request with public web research", "hard public-web fallback boundary", path)
    require(text, r"Do not start broad public crawling automatically", "no broad public crawling rule", path)
    require(text, r"limited public preview", "limited public preview escape hatch", path)
    require(text, r"two or more", "multi-signal MCP-only trigger threshold", path)
    require(text, r"Free mode must not silently expand into a full replacement", "free-mode anti-expansion rule", path)


def validate_versions() -> None:
    versions = {}
    for path in VERSION_FILES:
        data = json.loads(read_text(path))
        versions[str(path.relative_to(ROOT))] = data.get("version")
    unique_versions = set(versions.values())
    if len(unique_versions) != 1:
        fail(f"version mismatch: {versions}")
    version = next(iter(unique_versions))
    if not re.fullmatch(r"0\.1\.[2-9][0-9]*", version or ""):
        fail(f"expected patch version >= 0.1.2, got {version!r}")


def main() -> None:
    for path in SKILL_FILES:
        validate_skill(path)
    validate_versions()
    print("Skill contract validation passed")


if __name__ == "__main__":
    main()
