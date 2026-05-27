# Review Preflight

**在读 diff 之前，先了解这个 PR。**

[English](README.md) | 中文

Review Preflight 是一个 Agent skill，用来把 Pull Request 转换成面向人工 reviewer 的自包含 HTML 预检报告文件。它帮助 reviewer 在打开完整 diff 之前，先理解 PR 的意图、核心变更、推荐 review 路线和需要重点怀疑的风险区域。

它不是 AI code reviewer，不负责 approve、reject，也不宣称代码正确。它的目标是减少 reviewer 的冷启动时间。

## 为什么需要它

AI 写代码的速度已经很快，但上线前的人类 review 仍然不能跳过。短期内更现实的方向不是取消人工 review，而是让人工 review 从“先读代码理解上下文”升级成“验证关键判断”。

Review Preflight 会把原始 diff 重组成 reviewer 更容易决策的信息：

- 这个 PR 想做什么？
- 它在模块或系统层面改了哪些地方？
- reviewer 应该先看哪些文件？
- 哪些地方最值得怀疑？
- 应该问作者哪些具体问题？
- 人工 review 应该按什么 checklist 检查？

## 它会生成什么

这个 skill 会把 HTML 格式的 Review Preflight 报告保存到文件。报告不是固定模板，而是根据 PR 内容选择更合适的展示方式。

常见内容包括：

- PR 意图
- Review 复杂度
- 核心变更
- 按区域分组的变更地图
- 建议 review 路线
- 风险区域
- 可能缺失或薄弱的测试
- 建议问作者的问题
- 人工 review checklist

HTML 可以使用更丰富的表达方式，例如指标条、review 路线时间线、风险矩阵、带注释的 diff 片段、模块关系图、卡片、表格、提示区、tabs、折叠区和 checkbox 列表。原则是帮助 reviewer 更快扫描和判断，而不是做装饰。

## 它不是什么

Review Preflight 不应该被定位成：

- 自动 approve 工具
- 安全审计替代品
- 测试替代品
- 代码正确性的最终判断
- 对每一行代码发表评论的机器人

它更像一个 review 前置助理：在人做判断之前，先把上下文、路线和风险整理好。

## 输入

最理想的输入包括：

- PR title
- PR description
- Changed files
- Diff
- Commit messages
- 关联 issue 或 ticket
- 测试变更
- 相关仓库上下文

最低可用输入是 PR title、changed files 和 diff。

## 安装

从这个仓库安装 skill：

```bash
npx skills add Toormi/skills --skills review-preflight
```

## 使用方式

可以直接传入 PR URL、本地分支或粘贴 PR 上下文：

```text
Use $review-preflight to analyze this PR and produce an HTML review briefing.
```

也可以提供结构化输入：

```text
Use $review-preflight.

PR Title:
...

PR Description:
...

Changed Files:
...

Diff:
...
```

输出应保存为 HTML 文件。默认生成可直接在浏览器打开的完整自包含 `.html` 文件，使用内联 CSS，不依赖外部构建步骤。如果需要保存到指定位置，请在请求中说明输出路径。

## Review 理念

Review Preflight 有三层价值：

1. 理解层：帮助 reviewer 知道这个 PR 是什么。
2. 导航层：帮助 reviewer 决定先看哪里。
3. 怀疑层：帮助 reviewer 知道哪里需要验证。

真正的价值在第二层和第三层。普通 PR summary 很容易变成“看起来有用但没人读”的内容；review 路线和风险预检可以直接改变 reviewer 的注意力分配。

## 未来 Review 的形式

未来 review 的形式可能不是：

> 人逐行读 AI 写的代码。

而是：

> AI 先把代码变更压缩成结构化判断材料，人只 review 高风险判断点。

所以Review Preflight现在要做的不是“更好的代码总结器”，而是：

> 把 PR 从 diff 形式，重组成人类更容易决策的形式。

## 仓库结构

```text
skills/
└── review-preflight/
    ├── SKILL.md
    ├── README.md
    └── README.zh-CN.md
```

- `SKILL.md` 包含实际的 skill 指令。
- `README.md` 是默认英文 README。
- `README.zh-CN.md` 是中文 README。

## 未来产品方向

第一版刻意保持为一个 skill：输入 PR 上下文，输出 HTML briefing。

如果它在真实历史 PR 上证明有用，后续自然的产品路径是：

1. GitHub/GitLab PR bot，自动发布或更新 briefing。
2. Review check 状态，例如 Low Risk、Medium Risk、High Risk 或 Needs Author Clarification。
3. 团队配置，包括自定义 checklist 和按路径配置风险规则。
4. Dashboard，用于 review intelligence、高风险 PR、反复出现的测试缺口和 reviewer 反馈。

这个产品命题很简单：

> 在读 diff 之前，把每个 PR 转换成人类可读的 review briefing。
