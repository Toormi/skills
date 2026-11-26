# Review Preflight

**在读 diff 之前，先了解这个 PR。**

[English](README.md) | 中文

Review Preflight 把 PR 整理成一份可独立打开的 HTML 简报。首屏说明在什么条件下，行为从什么变成了什么，并给出第一处值得读的 diff 和一个能在代码里核实的问题。最终判断由 reviewer 做出。

## 为什么需要它

AI 写代码的速度已经很快，但上线前的人类 review 仍然不能跳过。短期内更现实的方向不是取消人工 review，而是让人工 review 从“先读代码理解上下文”升级成“验证关键判断”。

Review Preflight 会把原始 diff 重组成 reviewer 更容易决策的信息：

- 这个 PR 想做什么？
- 它在模块或系统层面改了哪些地方？
- 哪些关系、流程、依赖、状态或数据结构发生了变化？
- reviewer 应该先看哪些文件？
- 哪些地方最值得怀疑？
- 应该问作者哪些具体问题？
- 人工 review 应该按什么 checklist 检查？

## 它会生成什么

打开 HTML，第一个链接就会带你到决定行为的那几行。首屏给出一个具体情形，请你核实程序会怎样处理，以及这个答案会影响哪项兼容性判断、测试预期或实现选择。本地改动会标明文件和符号或小节名。

如果调用方、测试或迁移脚本能回答另一个问题，简报才会给出下一站。每个疑点只在能核实它的位置提一次。审整个 GitHub PR 时，用共同祖先（merge base）和本次审阅的 head 核对改动前后的行为；审单个提交时，从该 diff 展示的父版本开始比较。推断会写明还缺哪条证据。修正一个目录链接可以只用一句话。

## 流程线可视化

一份简报可以没有图。只有当图能帮助回答具体的审阅问题时，才把它放在对应的阅读位置。例如，事务提交和重试分布在两个组件里，时序图可以帮 reviewer 判断两者的先后。

| 变更的流程线                               | 图形               |
| ------------------------------------------ | ------------------ |
| 业务规则、条件判断、错误处理、重试降级变化 | 流程图             |
| API、服务、队列、webhook 或第三方交互变化  | 时序图             |
| 模块、服务、运行边界或依赖关系变化         | 架构图或依赖图     |
| 函数调用或执行路径变化                     | 调用图             |
| 类、接口、字段、方法、继承关系变化         | 类图               |
| 生命周期或状态流转变化                     | 状态图             |
| 表、字段、migration 或数据转换变化         | ER 图或数据流图    |
| 发布、CI、feature flag、环境或基础设施路径 | 部署或运维流程图   |

图里使用真实代码名称，标出发生变化的节点和连线。证据充分时展示改动前后的差异，推断出的关系则单独标明。

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

粘贴一段 diff 就可以开始。如果只提供了部分 diff，简报会说明哪些行为仍缺证据。

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

从决定行为的那几行开始。调用方可以解释程序如何走到这里，测试可以说明具体断言了哪种结果。证据足够让 reviewer 继续读代码时，简报就可以结束。

做 A/B 试读时，主持人先选定目标改动段，每位读者对同一个 PR 只读一个版本。记录读者第一次点击实际落在哪里、是否命中目标，从打开简报到指出目标改动段花了多久，以及能否准确复述前后行为。全程没有点击的情况单独记录。

## 未来 Review 的形式

未来 review 的形式可能不是：

> 人逐行读 AI 写的代码。

而是：

> AI 先把代码变更压缩成结构化判断材料，人只 review 高风险判断点。

所以Review Preflight现在要做的不是“更好的代码总结器”，而是：

> 把 PR 从 diff 形式，重组成人类更容易决策的形式。

## 未来产品方向

第一版刻意保持为一个 skill：输入 PR 上下文，输出 HTML briefing。

如果它在真实历史 PR 上证明有用，后续自然的产品路径是：

1. GitHub/GitLab PR bot，自动发布或更新 briefing。
2. Review check 状态，例如 Low Risk、Medium Risk、High Risk 或 Needs Author Clarification。
3. 团队配置，包括自定义 checklist 和按路径配置风险规则。
4. Dashboard，用于 review intelligence、高风险 PR、反复出现的测试缺口和 reviewer 反馈。

这个产品命题很简单：

> 在读 diff 之前，把每个 PR 转换成人类可读的 review briefing。
