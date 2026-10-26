# 研究依据与证据强度

[← 返回首页](../README.md) | [English](evidence.en.md)

规则参考了 2026 年 6 月至 10 月发表在 arXiv 上的 9 篇论文。下表列出每篇的核心结论，数字已对照论文全文核对。

| 论文 | 核心结论 | 支撑规则 |
|---|---|---|
| Clark, Martin & Mahowald, *Why is AI-generated language so hard to understand?* [arXiv:2610.29162](https://arxiv.org/abs/2610.29162) | 采集了 14 个模型的文本。和人类写作相比，9 个前沿模型都更多使用"无生命主语 + 有生命动词"和低频词组，多数还更常用长依存、名词堆叠和省略关系词的从句。作者提出的解释是：数学、代码、推理类后训练带来"信息密度压力"，并用长度惩罚微调实验做了概念验证。 | 1、2、3、4 |
| Cekini et al., *The Cognitive Cost of LLM Writing* [arXiv:2610.23715](https://arxiv.org/abs/2610.23715) | 496 组"人类原文 / AI 改写"对比，用英文眼动数据训练的模型预测阅读时间：AI 改写词数少 2.66%，但每词预测阅读时间多 1.57%；词更长（+6.06%）、更少见（词频 −7.61%）、词汇多样性更高（MTLD +31.83%）。 | 5 |
| Li & Xu, *UIDPO* [arXiv:2610.14578](https://arxiv.org/abs/2610.14578) | 基于"均匀信息密度"理论设计偏好优化：允许整体信息密度有较大起伏，但要求局部过渡均匀（"分段线性"）。在英文补语从句分析里，该方法正确保留必要连接词 *that* 的次数比基线多 36.57%。 | 1、6 |
| Zhu et al., *LM Surprisal in Reading Chinese* [arXiv:2610.04898](https://arxiv.org/abs/2610.04898) | 在三个中文眼动语料库上，语言模型的"意外度"能预测中文阅读时间，但模型越大是否越准因语料而异。在新闻语料 HKP 上，越接近局部二元 / 三元词组统计的模型，预测越准。 | 4 |
| Shan, Lee & Hao, *AI Writers Have a Consistent Stylometric Footprint* [arXiv:2608.27855](https://arxiv.org/abs/2608.27855) | 8 个模型、5 个领域：AI 生成文本的信息熵比人类高约 1 个标准差，词汇多样性高约 2 个标准差，这是最稳定的特征。 | 5 |
| El Attar et al., *Linguistic Features in AI-Generated Text Detection* [arXiv:2606.04177](https://arxiv.org/abs/2606.04177) | 27 个模型、10 个领域、284 个语言特征：词汇丰富度是跨模型、跨领域最稳定的 AI 文本信号。 | 5 |
| Massaro, *Literary Non-Style in LLM-Generated Text* [arXiv:2607.17228](https://arxiv.org/abs/2607.17228) | AI 文本在三元、四元词组层面反复使用固定套话，同样篇幅里承载的语义内容更少。 | 7 |
| Hu et al., *When LLMs Over-Answer* [arXiv:2607.17063](https://arxiv.org/abs/2607.17063) | 在硬件描述语言（芯片设计用的编程语言）问答中，工程师认为 65.7% 的 AI 回答堆了重复备选（人类采纳答案 4.4%），69.1% 有多余铺垫和总结（人类 5.8%）。不过 58.3% 的情况下，参与者觉得 AI 回答更好读。 | 7 |
| Zhu et al., *LLMs Do Not Always Need Readable Language* [arXiv:2606.19857](https://arxiv.org/abs/2606.19857) | 提示模型放弃"人类可读"约束后，模型会写出人看不懂的压缩文本：长度只剩原文 27.9%，模型仍能恢复 99.5% 的语义。说明"模型能读懂"和"人能读懂"可以部分分开。 | 背景 |

**证据强度说明**：

- **有直接研究支撑的**：AI 文本更多使用抽象主语、名词堆叠、低频搭配（规则 2、3、4）；用词更长更少见、词汇多样性虚高（规则 5）；套话和过度作答（规则 7）。
- **由研究推断的**：句间关系写清楚、局部平滑（规则 1、6），来自均匀信息密度理论和英文连接词分析。
- **经验做法**：所有数字阈值（两层、两句、6–12 字）和分词边界检查，都是写作经验，论文里没有这些数值。

