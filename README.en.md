# Make AI Write Chinese Like a Human

[中文](README.md) | **English**

A writing skill for AI agents that write Chinese. Seven checkable rules for text where every word is familiar but the sentence still won't go in.

---

## You already know this problem

Read this sentence:

> *Your instinct is right; the convoluted sentence you are currently reading is quietly eating its own reader-patience budget — footnote it.*

It sounds like a modern LLM. That's the opening line of [Clark, Martin & Mahowald (2026)](https://arxiv.org/abs/2610.29162), written to pack four features that make text harder to process and that frontier models overuse:

- an object relative clause
- a noun turned into a verb ("footnote it")
- an inanimate subject doing something only living things do ("a sentence ... eating")
- stacked nouns forming a rare phrase ("reader-patience budget")

**Chinese AI text has the same habits, and Chinese has no spaces between words to help the reader parse them.** This skill makes those habits visible and gives the agent a rule for each one.

---

## The 7 rules

Each row shows a typical AI phrasing and a human rewrite, with a literal English gloss.

| # | Rule | AI tends to write | A human would write |
|---|---|---|---|
| 1 | Say how sentences connect | 转化率降了 3%。工单量没变。先不回滚。<br>*Conversion fell 3%. Tickets unchanged. Not rolling back.* | 转化率降了 3%，不过工单量没变，我们判断影响有限，所以先不回滚。<br>*Conversion fell 3%, but tickets didn't change, so we judge the impact limited and won't roll back yet.* |
| 2 | Max two layers of modifiers before a noun | 用户行为数据分析模型优化方案<br>*user-behavior-data-analysis-model optimization plan* | 我们有一个分析用户行为数据的模型，请针对它提交优化方案。<br>*We have a model that analyzes user behavior data. Please propose how to improve it.* |
| 3 | Don't let abstractions act like people | 这个框架吞噬了团队大量时间。<br>*This framework devoured the team's time.* | 团队在这个框架上花了大量时间。<br>*The team spent a lot of time on this framework.* |
| 4 | Use everyday word pairings; watch word boundaries | 对齐颗粒度、日历化<br>*align the granularity, calendarize it* | 核对细节、排进日程<br>*check the details, put it on the schedule* |
| 5 | Common words; one term per concept | 该方法……该范式……这一路径……<br>*this method ... this paradigm ... this pathway ...* | 这个方法……它……它……<br>*this method ... it ... it ...* |
| 6 | Smooth locally, vary rhythm overall | Three sentences of equal length, each "X, thereby Y" | Follow a long sentence with a short one or an example |
| 7 | Cut stock phrases and over-answering | 这是个好问题。在当今……综上所述……<br>*Great question. In today's ... In summary ...* | Answer first, then give the reason |

Rule 0 sits above all of them: **a rewrite must not change the meaning.** If the source doesn't state a cause or a number, the agent must not invent one. It marks the gap as `[待确认]` (to be confirmed).

More examples (in Chinese) are in [docs/examples.md](docs/examples.md).

---

## Get started

**Install as a skill** (Claude Code shown):

```bash
git clone https://github.com/robox888/human-readable-chinese-writing.git \
  ~/.claude/skills/human-readable-chinese-writing
```

When you ask the agent to write, polish, or "de-AI" Chinese text, it follows the 7 rules and checks each one before handing the text back. Other tools that read `SKILL.md` work the same way: put the folder in their skills directory.

**Rules only**: paste [rules/AGENTS-snippet.md](rules/AGENTS-snippet.md) into your project's `AGENTS.md`, `CLAUDE.md`, or system prompt. The rules are written in Chinese, which is what the model needs when it writes Chinese.

---

## Companion: think first, then write

Sometimes a report reads as "too AI" because it's hard to read; sometimes because it never decided what to say. This skill handles the first. For the second, use the companion skill **[think-before-slides](https://github.com/robox888/think-before-slides)** (Chinese): it helps you settle the goal, the evidence, and a page-by-page outline before writing.

---

## Why AI text got harder to read

A cluster of 2026 papers looked at this directly:

- One explanation is post-training. Models are increasingly trained on math, code, and reasoning, where a correct answer is rewarded and a clear one is not. Long outputs can also be penalized, which pushes models to pack more information into fewer words. Clark et al. offer a length-penalty fine-tuning experiment as a proof of concept.
- The result: more stacked nouns, rare word combinations, and abstract subjects. In one study, LLM rewrites had 2.66% fewer words but a 1.57% longer predicted reading time per word.
- Models also rotate synonyms, reuse stock phrases, and give several overlapping answers. In a hardware-description-language Q&A study, engineers flagged 65.7% of LLM answers as redundant, compared with 4.4% of accepted human answers.

Sources, key numbers, and how strong the evidence is for each rule: [docs/evidence.en.md](docs/evidence.en.md).

---

## What's in this repo

| File | For | Contents |
|---|---|---|
| `SKILL.md` | AI | Skill entry: when to trigger, the 7-step process, a self-check list |
| `rules/AGENTS-snippet.md` | AI | Rules to paste into `AGENTS.md` / `CLAUDE.md` |
| `README.md` / `README.en.md` | People | This page |
| `docs/examples.md` | People | All rewrite examples (Chinese) |
| `docs/evidence.md` / `docs/evidence.en.md` | People | Research basis and evidence strength |

---

## Limitations

- Only 1 of the 9 papers studies Chinese. Applying the rest to Chinese is an inference.
- Thresholds like "two layers" and "two sentences" are rules of thumb; the papers don't give them.
- The over-answering study also found that participants rated the LLM answer as more readable in 58.3% of cases. Readable is not always the same as concise or accurate.
- The rules address readability. Whether the content is correct needs a separate check.

## Contributing

Before/after rewrites and cases where a rule doesn't fit are welcome in [Issues](https://github.com/robox888/human-readable-chinese-writing/issues).

## License

[MIT](LICENSE)
