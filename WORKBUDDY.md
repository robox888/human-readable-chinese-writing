# 让 AI 说人话 · WorkBuddy 专家

将中文初稿、工作记录或文章交给专家，获得更好读的正文或具体修改意见。保留事实、立场和不确定性；缺的信息标为待确认。

## 使用

上架后，在 WorkBuddy 的「专家·技能·连接器 → 专家」中找到「让 AI 说人话」，点击「召唤专家」。市场详情链接待上架后补充；仓库提供上传包不代表已经上架。

可以这样开口：

- 帮我把下面这段中文改得自然、好读，不要改原意：……
- 根据这些工作记录写一段周报，不夸大，缺的信息标待确认：……
- 先别改稿，指出这段话哪里难读、为什么：……

专家的输出仍需本人核对；不承诺规避 AI 检测。

## 维护者上传

1. 在 [WorkBuddy 开放平台](https://open.workbuddy.cn/)创建或更新专家，上传 `human-readable-chinese-writing-workbuddy-0.1.0.zip`。
2. 核对名称「让 AI 说人话」、分类「内容创作」、头像、作者信息和 3 条推荐提示词。
3. 完成平台要求的预览、试用和审核步骤，再提交上架。解析结果、实际调用和审核结果以平台为准。

ZIP 根目录直接包含 `.codebuddy-plugin/plugin.json`、`agents/`、`avatars/`、`skills/`、`README.md` 和 `LICENSE`，无外层文件夹。不要上传 GitHub 自动生成的整个源码 ZIP。

## 分支与更新

- `main`：通用技能、示例和研究说明。
- `codex/workbuddy-expert`：在通用技能之上维护专家配置、Agent、头像、构建脚本和 `dist/` 上传包。
- 更新时将 `main` 合并到专家分支；在专家分支运行 `python scripts/build_workbuddy.py`，同步嵌套技能并重新生成 ZIP，再提交所有改动。不要直接修改 `skills/human-readable-chinese-writing/` 的生成副本。
- 按需独立递增 `.codebuddy-plugin/plugin.json` 中的专家包版本；技能版本仍由根目录 `SKILL.md` 维护。重新发布前按新包文件名更新下载链接和本文。

以下命令在源码仓库的专家分支执行。构建脚本依赖 `PyYAML==6.0.2`，与仓库自动检查一致。运行 `python .github/scripts/check.py` 和 `python scripts/build_workbuddy.py --check` 可检查文档、配置、头像、引用路径、技能同步和 ZIP 一致性。自动检查不替代 WorkBuddy 导入和实际改稿验证。

打包规则依据：[WorkBuddy 专家规范](https://open.workbuddy.cn/docs/expert)。
