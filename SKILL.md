---
name: human-readable-chinese-writing
description: Write clear, natural, human-readable Chinese prose ("说人话" / 去AI味), informed by 2026 arXiv research on why AI-generated text is harder to read (processing-cost features, per-word reading time, Uniform Information Density, Chinese eye-tracking surprisal, stylometric footprints, over-answering). Use whenever the user asks to write, draft, polish, rewrite, or review Chinese text for human readers, asks AI to "说人话", remove "AI味", improve readability (提升可读性), or create Agents.md writing guidelines.
---
# Human-Readable Chinese Writing

Write and revise Chinese text for human readers. LLM output tends to be compressed, rare-word-heavy and template-driven. These rules push the other way: explicit connections, short modifier chains, concrete subjects, everyday collocations, consistent terms, varied rhythm, and no padding. See `README.md` for before/after examples and a ready-to-copy `AGENTS.md` snippet.

## When to Use

- Drafting Chinese articles, posts, reports, tutorials, or reader-facing documentation
- Rewriting or polishing Chinese drafts to remove "AI味" and make them sound human ("说人话")
- Diagnosing why a passage feels dense, repetitive, or tiring to read
- Generating or applying `AGENTS.md` / system-prompt writing rules for Chinese content

## Non-Negotiable: Preserve Meaning

Rewriting for readability must not change facts, stance, certainty, scope, numbers, or causal direction. When adding a connector or explanation would require information the source does not contain (a cause, a reason, a number), do not invent it. Mark it as `[待确认: ...]` or ask the user.

## Evidence Base and How Strong It Is

The rules are informed by the papers below. Most of them study English; only Zhu et al. study Chinese. Applying the findings to Chinese is an inference, and the numeric thresholds in the steps (two layers, two sentences, 6–12 characters) are practical heuristics, not values from the papers.

1. Clark, Martin & Mahowald (2026), *Why is AI-generated language so hard to understand?*, [arXiv:2610.29162](https://arxiv.org/abs/2610.29162). Collects text from 14 models; compared with human writing, all nine frontier / near-frontier models use more inanimate subjects with animate verbs and more low-frequency n-grams, and most also use longer dependencies, more stacked nouns, and more reduced object relatives. Also examines denominal verbs. Hypothesis: post-training for math / code / reasoning creates pressure for information density; a length-penalty fine-tuning experiment is offered as proof-of-concept.
2. Cekini et al. (2026), *The Cognitive Cost of LLM Writing*, [arXiv:2610.23715](https://arxiv.org/abs/2610.23715). On 496 human/LLM-rewrite pairs, a reading-time model trained on English eye-tracking data predicts LLM rewrites to be shorter (−2.66% words) but slower per word (+1.57%), with longer words (+6.06% characters), less frequent words (−7.61% mean frequency), and higher lexical diversity (MTLD +31.83%).
3. Li & Xu (2026), *Uniform Information Density-Based Preference Optimization (UIDPO)*, [arXiv:2610.14578](https://arxiv.org/abs/2610.14578). Rewards responses whose information density is locally linear ("piecewise linearity"): a large density range is allowed globally, while local transitions are kept uniform. In an English complement-clause analysis, UIDPO correctly favored "necessary *that*" in 36.57% more cases than the SFT baseline.
4. Zhu et al. (2026), *A Systematic Analysis of the Predictive Power of LM Surprisal in Reading Chinese*, [arXiv:2610.04898](https://arxiv.org/abs/2610.04898). LM surprisal predicts Mandarin reading times on three eye-tracking corpora (GECO-CN, HKP, MECO), but scaling is corpus-specific. On HKP (news), checkpoints whose surprisal stays closer to local bigram/trigram statistics predict reading times better.
5. Shan, Lee & Hao (2026), *AI Writers Have a Consistent Stylometric Footprint, but AI Editors Do Not*, [arXiv:2608.27855](https://arxiv.org/abs/2608.27855); El Attar et al. (2026), *A Systematic Analysis of Linguistic Features in AI-Generated Text Detection*, [arXiv:2606.04177](https://arxiv.org/abs/2606.04177). Across 8 LLMs / 5 domains (Shan) and 27 LLMs / 10 domains (El Attar), lexical diversity is the most robust signal of AI-generated text; Shan also finds entropy about +1 SD and lexical diversity about +2 SD above human text.
6. Massaro (2026), *Literary Non-Style in LLM-Generated Text*, [arXiv:2607.17228](https://arxiv.org/abs/2607.17228): LLM text leans on stock higher-order n-grams (e.g. "despite these challenges"). Hu et al. (2026), *When LLMs Over-Answer*, [arXiv:2607.17063](https://arxiv.org/abs/2607.17063): in hardware-description-language Q&A, engineers flagged 65.7% of LLM answers as redundant (vs 4.4% of accepted human answers) and 69.1% as verbose (vs 5.8%).
7. Zhu et al. (2026), *Large Language Models Do Not Always Need Readable Language (BabelTele)*, [arXiv:2606.19857](https://arxiv.org/abs/2606.19857): when prompted to drop human readability as a constraint, LLMs produce opaque compressed text that keeps 99.5% semantic fidelity at 27.9% of the original length. Model-side recoverability and human readability can be partially decoupled.

## Steps

### Step 1: Make Relationships Between Sentences Explicit (句间关系要写出来)

Basis: LLMs drop optional connective material ([Clark et al.](https://arxiv.org/abs/2610.29162)); smoothing local information transitions is preferred ([Li & Xu](https://arxiv.org/abs/2610.14578)).

- When two adjacent claims are not a direct continuation, state their relationship (contrast, cause, condition, elaboration) in a clause.
- Use a natural clause that carries the actual logic ("但放到实际场景里，情况就不同了"), not a stiff stock connector.
- If the relationship is not in the source, do not guess. Mark it `[待确认]`.
- Self-posed rhetorical questions in an article may get one bridging sentence before the answer. When answering the reader's own question, lead with the answer (see Step 7).
- *Avoid*: 转化率下降了 3%。客服工单量没变。我们决定先不回滚。
- *Prefer*: 转化率下降了 3%，不过客服工单量没变，我们判断影响有限，所以先不回滚。(Only if "影响有限" is really the author's reason.)

### Step 2: Keep Modifier Chains Short (修饰语不超过两层)

Basis: stacked nouns and long dependencies ([Clark et al.](https://arxiv.org/abs/2610.29162)). Two layers is a heuristic.

- A noun gets at most two nested layers of pre-nominal modifiers (定语).
- For longer chains, state the inner concept in its own clause first, then build outward with verbs.
- Keep subject and main verb close; do not wedge long "通过……在……的背景下对……" frames between them.
- *Avoid*: 请提交用户行为数据分析模型优化方案。
- *Prefer*: 我们有一个分析用户行为数据的模型，请针对它提交一份优化方案。

### Step 3: Prefer Concrete Agents Over Personified Abstractions (少让抽象概念当主语做动作)

Basis: inanimate subjects with animate verbs are overused by every frontier model tested ([Clark et al.](https://arxiv.org/abs/2610.29162)). "Two per paragraph" is a heuristic.

- In one paragraph, allow at most two sentences where an abstract noun performs an agentive verb ("这个框架吞噬了……", "这条规则抓住了……", "这个机制驱动了……").
- From the third such sentence on, switch to people (团队、读者、我们), tangible objects, or concrete scenes.
- *Avoid*: 这个框架吞噬了团队大量时间。
- *Prefer*: 团队在这个框架上花了大量时间。

### Step 4: Use Everyday Collocations; Watch Word Boundaries (搭配要日常，注意分词边界)

Basis: low-frequency n-grams and denominal verbs ([Clark et al.](https://arxiv.org/abs/2610.29162)); on one Chinese corpus, LM surprisal that stays closer to local n-gram statistics predicts reading times better ([Zhu et al.](https://arxiv.org/abs/2610.04898)). The word-boundary check is a practical heuristic, not a finding of these papers.

- Read each verb-object and modifier-noun pair aloud: would you say it in conversation? Replace jargon combinations ("对齐颗粒度", "赋能闭环", "将其日历化") with everyday ones ("把细节核对清楚", "帮业务把流程跑通", "排进日程").
- Avoid character sequences that invite a wrong first-pass segmentation, e.g. "这些人才刚到" (人才 vs 人 / 才刚). Rewrite as "刚到公司的这批人才" (talent) or "这些人刚刚到" (people who just arrived), depending on meaning.

### Step 5: Prefer Common Short Words and Consistent Terms (用常见短词，不刻意换同义词)

Basis: LLM rewrites use longer, rarer words and inflated lexical diversity, raising predicted per-word reading time ([Cekini et al.](https://arxiv.org/abs/2610.23715)); lexical diversity is the most robust AI-text signal ([Shan et al.](https://arxiv.org/abs/2608.27855); [El Attar et al.](https://arxiv.org/abs/2606.04177)).

- Keep one term for one concept within a passage. Do not rotate "方法 / 范式 / 路径 / 抓手" or "使用 / 援引 / 仰赖 / 借力" for variety.
- Prefer common words over rare formal ones ("提高" over "擢升", "好处" over "裨益").
- Let natural function words (的、了、就、其实) stay. Do not pack every slot with heavy two-character nouns and verbs.

### Step 6: Smooth Locally, Vary Rhythm Across the Text (局部平滑，整体有长有短)

Basis: UIDPO's piecewise linearity: keep local transitions smooth while allowing larger variation globally ([Li & Xu](https://arxiv.org/abs/2610.14578)). The sentence-length advice is a writing heuristic built on that idea.

- Keep adjacent clauses smooth (no sudden pile-up of new terms in one clause).
- Do not force every sentence into the same length and "主谓宾，从而主谓宾" cadence. After a long analytical sentence, a short sentence (roughly 6–12 characters) or a concrete example often helps.

### Step 7: Cut Stock Phrases and Over-Answering (砍掉套话和过度作答)

Basis: stock higher-order n-grams ([Massaro](https://arxiv.org/abs/2607.17228)); redundant alternatives and padding ([Hu et al.](https://arxiv.org/abs/2607.17063)).

- Delete stock frames such as "值得注意的是", "综上所述", "不可否认的是", "在当今……的背景下". Use "不是……而是……" only to correct a real, stated misunderstanding or for data contrasts, not as a rhetorical device.
- Lead with the answer. Do not restate the question or add a generic background paragraph.
- Give one well-explained answer instead of several overlapping options; drop closing summaries that repeat the body.

## Verification Checklist

Before finalizing, check:

0. **Meaning preserved**: no new facts, reasons, numbers, or stronger certainty than the source; gaps are marked `[待确认]`.
1. **Relationships explicit**: every non-obvious transition between adjacent claims is stated in words.
2. **Short modifier chains**: no noun phrase with three or more stacked modifier layers.
3. **Concrete agents**: at most two "abstract noun + agentive verb" sentences per paragraph.
4. **Everyday collocations**: each verb-object pair passes the say-it-aloud test; no misleading character sequences.
5. **Consistent, common words**: one term per concept; no rare words where a common one works.
6. **Rhythm**: smooth local transitions; sentence lengths vary.
7. **No templates or padding**: no stock openers, no restated question, no overlapping bullets, no repeated summary.

## Gotchas

- **Connectors vs. clichés**: Step 1 does not mean starting sentences with "因此 / 此外 / 综上所述" (Step 7). Write a clause that states the actual link.
- **Concise vs. compressed**: cutting words by packing rare, dense vocabulary raises per-word reading cost ([Cekini et al.](https://arxiv.org/abs/2610.23715)). Cut padding, but give core ideas enough words.
- **Do not invent to smooth**: a connector that asserts a cause the source never stated is a factual change, not a style fix.
- **Heuristics, not laws**: the thresholds are starting points. Legal text, poetry, and fixed terminology may need exceptions.
