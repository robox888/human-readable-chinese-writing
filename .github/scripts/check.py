"""检查 SKILL.md 的 frontmatter、版本号是否一致、文档里的相对链接是否有效。"""
import re
import sys
from pathlib import Path

import yaml

root = Path(__file__).resolve().parents[2]
errors = []

# 1. SKILL.md frontmatter
skill = (root / "SKILL.md").read_text(encoding="utf-8")
m = re.match(r"---\n(.*?)\n---\n", skill, re.S)
if not m:
    sys.exit("SKILL.md 缺少 frontmatter")
fm = yaml.safe_load(m.group(1))

if fm.get("name") != "human-readable-chinese-writing":
    errors.append(f"name 不对：{fm.get('name')}")
desc = fm.get("description", "")
if not desc:
    errors.append("description 为空")
if len(desc) > 1024:
    errors.append(f"description 过长：{len(desc)} 字符（上限 1024）")

# 2. 版本号一致：SKILL.md / CITATION.cff / CHANGELOG.md
skill_ver = str((fm.get("metadata") or {}).get("version", ""))
if not re.fullmatch(r"\d+\.\d+\.\d+", skill_ver):
    errors.append("metadata.version 必须是非空的三段版本号")
cff = yaml.safe_load((root / "CITATION.cff").read_text(encoding="utf-8"))
cl = re.search(r"^## \[(\d+\.\d+\.\d+)\]", (root / "CHANGELOG.md").read_text(encoding="utf-8"), re.M)
versions = {
    "SKILL.md": skill_ver,
    "CITATION.cff": str(cff.get("version", "")),
    "CHANGELOG.md": cl.group(1) if cl else "",
}
if len(set(versions.values())) != 1:
    errors.append(f"版本号不一致：{versions}")

# 3. 相对链接
required = ["README.md", "README.en.md", "SKILL.md", "LICENSE", "docs/examples.md", "docs/evidence.md", "rules/AGENTS-snippet.md"]
for name in required:
    if not (root / name).is_file():
        errors.append(f"缺少必需文件：{name}")
files = sorted(root.rglob("*.md"))
pattern = re.compile(r'\]\(([^)\s]+)\)|(?:src|href)="([^"]+)"')
for f in files:
    if not f.exists():
        continue
    for a, b in pattern.findall(f.read_text(encoding="utf-8")):
        link = (a or b).split("#")[0].split("?")[0]
        if not link or re.match(r"^(https?:|mailto:)", link):
            continue
        if not (f.parent / link).exists():
            errors.append(f"{f.relative_to(root)}：链接不存在 → {link}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("ok")
