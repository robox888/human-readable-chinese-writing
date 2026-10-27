"""Build or verify the WorkBuddy expert ZIP from the canonical root skill."""
import argparse
import io
import json
import re
import struct
import zipfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
NAME = "human-readable-chinese-writing"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def frontmatter(data):
    match = re.match(r"---\n(.*?)\n---\n", data.decode("utf-8"), re.S)
    require(match is not None, "Missing YAML frontmatter")
    return yaml.safe_load(match.group(1))


def build(check=False):
    config_path = ".codebuddy-plugin/plugin.json"
    config = json.loads((ROOT / config_path).read_text(encoding="utf-8"))
    agent_path = f"agents/{NAME}.md"
    avatar_path = "avatars/expert.png"
    require(config["name"] == config["plugin"] == config["agentName"] == NAME, "Expert names differ")
    require(config["expertType"] == "agent", "expertType must be agent")
    version = config["version"]
    require(re.fullmatch(r"\d+\.\d+\.\d+", version), "Invalid expert version")
    require(config["agents"] == [f"./{agent_path}"], "Invalid agents array")
    require(config["skills"] == [f"./skills/{NAME}"], "Invalid skills array")
    require(config["avatar"] == avatar_path, "Invalid avatar path")
    require(config["categoryId"] == "06-ContentCreative", "Unexpected category")
    require(config["description"].strip(), "Missing English description")
    require(config["author"]["name"].strip(), "Missing author")
    require(re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", config["author"]["email"]), "Missing or invalid author email")
    for key in ["displayName", "profession", "displayDescription", "defaultInitPrompt"]:
        require(all(config[key].get(lang, "").strip() for lang in ["zh", "en"]), f"Missing bilingual {key}")
    require(40 <= len(config["displayDescription"]["zh"]) <= 50, "Chinese description must be 40–50 characters")
    for key in ["tags", "quickPrompts"]:
        require(len(config[key]) == 3, f"{key} must contain 3 entries")
        require(all(item.get("zh") and item.get("en") for item in config[key]), f"Missing bilingual {key}")
    require(config["defaultInitPrompt"] == config["quickPrompts"][0], "Default prompt differs")
    agent = frontmatter((ROOT / agent_path).read_bytes())
    require(agent["name"] == NAME and agent["skills"] == [NAME], "Agent/skill mismatch")
    require(agent["description"].strip(), "Missing agent description")
    for key in ["displayName", "profession"]:
        require(agent[key] == config[key], f"Agent {key} differs")
    require("tools" not in agent, "WorkBuddy assigns tools")
    avatar = (ROOT / avatar_path).read_bytes()
    require(avatar[:8] == b"\x89PNG\r\n\x1a\n", "Avatar must be PNG")
    require(struct.unpack(">II", avatar[16:24]) == (512, 512), "Avatar must be 512×512")
    require(len(avatar) <= 500 * 1024, "Avatar exceeds 500 KiB")

    files = {p: (ROOT / p).read_bytes() for p in [config_path, agent_path, avatar_path, "LICENSE"]}
    files["README.md"] = (ROOT / "WORKBUDDY.md").read_bytes()
    sources = ["SKILL.md", "LICENSE", "README.md", "README.en.md", "CHANGELOG.md", "CITATION.cff"]
    sources += [str(p.relative_to(ROOT)) for folder in ["docs", "rules"] for p in sorted((ROOT / folder).glob("*.md"))]
    sources += [str(p.relative_to(ROOT)) for p in sorted((ROOT / "assets").glob("*.svg"))]
    skill = frontmatter((ROOT / "SKILL.md").read_bytes())
    require(skill["name"] == NAME, "Unexpected skill name")
    for source in sources:
        target = f"skills/{NAME}/{source}"
        files[target] = (ROOT / source).read_bytes()
        if check:
            require((ROOT / target).read_bytes() == files[target], f"Stale generated skill: {target}")
        else:
            (ROOT / target).parent.mkdir(parents=True, exist_ok=True)
            (ROOT / target).write_bytes(files[target])

    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path, data in sorted(files.items()):
            info = zipfile.ZipInfo(path, date_time=(2026, 10, 27, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    output = ROOT / "dist" / f"{NAME}-workbuddy-{version}.zip"
    if check:
        with zipfile.ZipFile(output) as archive:
            require(archive.testzip() is None, "Corrupt ZIP")
            require(set(archive.namelist()) == set(files), "Unexpected/missing ZIP entries")
            for path, data in files.items():
                require(archive.read(path) == data, f"Stale ZIP entry: {path}")
    else:
        output.parent.mkdir(exist_ok=True)
        output.write_bytes(buffer.getvalue())
    print(f"{'Verified' if check else 'Built'} {output.name}: {len(files)} files; skill {skill['metadata']['version']}; expert {version}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify generated skill and ZIP without writing")
    build(parser.parse_args().check)
