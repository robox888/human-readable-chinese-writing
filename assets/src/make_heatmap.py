"""根据 boss_quotes.csv 统计各类吐槽出现次数，生成中英文热力圆点图 SVG。"""
import csv, math, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE

rows = list(csv.DictReader(open(HERE / "boss_quotes.csv", encoding="utf-8")))
count = Counter(r["category"] for r in rows)
N = len(rows)

CATS = {
    "zh": {
        "A": ("一眼看出是 AI", "“这一看就是 AI 写的，重写。”"),
        "B": ("读不进去", "“太 AI 了，不想看，懒得读。”"),
        "C": ("不像你写的", "“没有你的思考。”"),
        "D": ("空洞、夸大", "“这周你做了这么多事？”"),
        "E": ("你自己看过没有", "“请合理使用 AI，不要偷懒。”"),
    },
    "en": {
        "A": ("Obviously AI", "“Clearly AI-written. Redo it.”"),
        "B": ("Can't get through it", "“Too AI. Don't want to read it.”"),
        "C": ("Doesn't sound like you", "“Where's your own thinking?”"),
        "D": ("Empty or inflated", "“You did all this?”"),
        "E": ("Did you even read it?", "“Don't be lazy.”"),
    },
}
TEXT = {
    "zh": {
        "title": "老板到底在嫌什么？",
        "sub": f"{N} 条上级评价，按嫌弃的点归类",
        "g1": "说人话：本仓库",
        "g2": "想清楚：think-before-slides",
        "g3": "交稿前自己读一遍",
        "foot": f"样本：{N} 条来自公开文章、帖子与作者亲历的上级评价（2026-10 收集，多为转述，未逐条核实）。圆点越大、颜色越深，出现次数越多；样本小，不代表总体比例。",
        "unit": "条",
    },
    "en": {
        "title": "What is the boss actually complaining about?",
        "sub": f"{N} comments from managers, grouped by complaint",
        "g1": "Make it readable: this repo",
        "g2": "Think it through: think-before-slides",
        "g3": "Reread before sending",
        "foot": f"Sample: {N} manager comments from public Chinese articles, posts, and the author's own experience (collected Oct 2026; mostly second-hand, not individually verified). Bigger, darker circles = more mentions. Small sample; not representative.",
        "unit": "",
    },
}
HEAT = {5: "#D7301F", 4: "#EF6548", 3: "#FC8D59", 2: "#FDBB84", 1: "#FDD49E"}
XS = {"A": 150, "B": 365, "C": 650, "D": 865, "E": 1070}
FONT = "PingFang SC, Hiragino Sans GB, Microsoft YaHei, Noto Sans CJK SC, Helvetica, Arial, sans-serif"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def wrap_foot(s, width, by_space):
    out, line = [], ""
    for tok in (s.split(" ") if by_space else list(s)):
        cand = f"{line} {tok}" if line and by_space else line + tok
        if len(cand) > width:
            out.append(line); line = tok
        else:
            line = cand
    return out + [line]


def svg(lang):
    t, cats = TEXT[lang], CATS[lang]
    H = 560
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1220 {H}" width="1220" height="{H}" font-family="{FONT}">',
         '<rect width="1220" height="100%" fill="#FFFDF8" rx="16"/>',
         f'<text x="40" y="58" font-size="30" font-weight="700" fill="#2B2B2B">{esc(t["title"])}</text>',
         f'<text x="40" y="92" font-size="17" fill="#6B6B6B">{esc(t["sub"])}</text>']
    cy = 215
    for k, x in XS.items():
        n = count.get(k, 0)
        r = 22 + 30 * math.sqrt(n)
        col = HEAT[min(max(n, 1), 5)]
        p.append(f'<circle cx="{x}" cy="{cy}" r="{r + 14:.0f}" fill="{col}" opacity="0.18"/>')
        p.append(f'<circle cx="{x}" cy="{cy}" r="{r:.0f}" fill="{col}"/>')
        txt = "#FFFFFF" if n >= 3 else "#5A2A00"
        p.append(f'<text x="{x}" y="{cy + 12}" font-size="38" font-weight="700" fill="{txt}" text-anchor="middle">{n}<tspan font-size="16" font-weight="400">{t["unit"]}</tspan></text>')
        name, q = cats[k]
        p.append(f'<text x="{x}" y="335" font-size="19" font-weight="700" fill="#2B2B2B" text-anchor="middle">{esc(name)}</text>')
        p.append(f'<text x="{x}" y="362" font-size="14" fill="#7A7A7A" text-anchor="middle">{esc(q)}</text>')

    def bracket(x1, x2, label, color):
        y = 398
        p.append(f'<path d="M{x1} {y} v10 H{x2} v-10" fill="none" stroke="{color}" stroke-width="2.5"/>')
        p.append(f'<text x="{(x1 + x2) / 2:.0f}" y="{y + 38}" font-size="17" font-weight="700" fill="{color}" text-anchor="middle">{esc(label)}</text>')

    bracket(70, 445, t["g1"], "#C2410C")
    bracket(570, 945, t["g2"], "#1D4ED8")
    bracket(990, 1150, t["g3"], "#4B5563")
    y = 488
    width = 67 if lang == "zh" else 150
    for line in wrap_foot(t["foot"], width, lang == "en"):
        p.append(f'<text x="40" y="{y}" font-size="13" fill="#8A8A8A">{esc(line)}</text>')
        y += 20
    p.append("</svg>")
    return "\n".join(p)


for lang in ("zh", "en"):
    (OUT / f"boss-complaints.{lang}.svg").write_text(svg(lang), encoding="utf-8")
print({k: count.get(k, 0) for k in XS}, "N =", N)
