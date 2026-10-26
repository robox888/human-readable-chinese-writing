# Research Basis and Evidence Strength

[← Back](../README.en.md) | [中文](evidence.md)

The rules draw on 9 arXiv papers published between June and October 2026. The numbers below were checked against each paper's full text.

| Paper | Key finding | Rules |
|---|---|---|
| Clark, Martin & Mahowald, *Why is AI-generated language so hard to understand?* [arXiv:2610.29162](https://arxiv.org/abs/2610.29162) | Text was collected from 14 models. Compared with human writing, all nine frontier / near-frontier models use more inanimate subjects with animate verbs and more low-frequency n-grams; most also use longer dependencies, more stacked nouns, and more reduced object relatives. The authors hypothesize that post-training for math, code, and reasoning creates pressure for information density, and test it with a length-penalty fine-tuning experiment. | 1, 2, 3, 4 |
| Cekini et al., *The Cognitive Cost of LLM Writing* [arXiv:2610.23715](https://arxiv.org/abs/2610.23715) | On 496 human / LLM-rewrite pairs, a reading-time model trained on English eye-tracking data predicts LLM rewrites to be 2.66% shorter but 1.57% slower per word, with longer words (+6.06% characters), less frequent words (−7.61%), and higher lexical diversity (MTLD +31.83%). | 5 |
| Li & Xu, *UIDPO* [arXiv:2610.14578](https://arxiv.org/abs/2610.14578) | A preference-optimization method based on Uniform Information Density. It allows a wide density range globally but keeps local transitions uniform ("piecewise linearity"). In an English complement-clause analysis, it correctly favored a necessary *that* in 36.57% more cases than the SFT baseline. | 1, 6 |
| Zhu et al., *LM Surprisal in Reading Chinese* [arXiv:2610.04898](https://arxiv.org/abs/2610.04898) | On three Mandarin eye-tracking corpora, LM surprisal predicts reading times, but whether bigger models predict better depends on the corpus. On the HKP news corpus, checkpoints whose surprisal stays closer to local bigram / trigram statistics predict reading times better. | 4 |
| Shan, Lee & Hao, *AI Writers Have a Consistent Stylometric Footprint* [arXiv:2608.27855](https://arxiv.org/abs/2608.27855) | Across 8 LLMs and 5 domains, AI-generated text has entropy about 1 SD and lexical diversity about 2 SD above human text; these are the most stable signals. | 5 |
| El Attar et al., *Linguistic Features in AI-Generated Text Detection* [arXiv:2606.04177](https://arxiv.org/abs/2606.04177) | Across 27 LLMs, 10 domains, and 284 features, lexical richness is the most robust signal of AI-generated text. | 5 |
| Massaro, *Literary Non-Style in LLM-Generated Text* [arXiv:2607.17228](https://arxiv.org/abs/2607.17228) | LLM text relies on stock 3- and 4-grams and carries less semantic content for the same length. | 7 |
| Hu et al., *When LLMs Over-Answer* [arXiv:2607.17063](https://arxiv.org/abs/2607.17063) | In hardware-description-language Q&A, engineers flagged 65.7% of LLM answers as redundant (vs 4.4% of accepted human answers) and 69.1% as verbose (vs 5.8%). Participants still rated the LLM answer more readable in 58.3% of cases. | 7 |
| Zhu et al., *LLMs Do Not Always Need Readable Language* [arXiv:2606.19857](https://arxiv.org/abs/2606.19857) | When prompted to drop human readability as a constraint, LLMs produce opaque compressed text that keeps 99.5% semantic fidelity at 27.9% of the original length. What a model can decode and what a person can read can partly come apart. | Background |

## How strong the evidence is

- **Directly supported**: AI text uses more abstract subjects, stacked nouns, and rare word combinations (rules 2, 3, 4); longer, rarer words and inflated lexical diversity (rule 5); stock phrases and over-answering (rule 7).
- **Inferred from research**: making sentence relations explicit and keeping local transitions smooth (rules 1, 6), based on Uniform Information Density theory and the English connector analysis.
- **Rules of thumb**: all numeric thresholds (two layers, two sentences, 6–12 characters) and the word-boundary check come from writing practice, not from the papers.
