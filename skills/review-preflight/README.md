# Review Preflight

**Know the PR before you read the diff.**

English | [中文](README.zh-CN.md)

Review Preflight is a Agent skill that turns a pull request into a concise, self-contained HTML briefing file for human reviewers. It helps reviewers understand the intent, see the shape of the change, navigate the most important files first, and focus attention on likely risk areas before opening the full diff.

It is not an AI code reviewer. It does not approve, reject, or claim that code is correct. Its job is to reduce reviewer cold start.

## Why This Exists

AI can now produce code faster than humans can review it. The short-term answer is not to skip human review, but to make human review start from better context.

Review Preflight reframes a PR from a raw diff into reviewer-ready decision material:

- What is this PR trying to do?
- What changed at the module or system level?
- What relationships, flows, dependencies, states, or data shapes changed?
- Which files should be reviewed first?
- Which areas deserve skepticism?
- What questions should the reviewer ask the author?
- What checklist should guide the human review?

The goal is to move reviewers from "reading code to understand context" toward "validating the key judgments."

## What It Generates

The skill saves an HTML Review Preflight report to a file. The layout is intentionally flexible rather than a fixed template, so the report can adapt to the PR.

Typical content includes:

- PR intent
- Review complexity
- Core changes
- Change map by area
- Flow-line inventory and before/after diagrams when useful
- Suggested review route
- Risk areas
- Missing or weak tests
- Questions for the author
- Human review checklist

The HTML can use richer presentation patterns such as metric strips, route timelines, risk matrices, annotated diff excerpts, flow-line inventories, before/after diagrams, module maps, cards, tables, callouts, tabs, collapsible sections, and checkbox lists when they help the reviewer scan faster.

## Flow-Line Visualizations

Review Preflight should first identify which workflows, sequences, states, data paths, dependency paths, or operational paths the PR changes. Treat each meaningful path as a review line, then choose the right visual form for that line.

It can include multiple diagrams directly in the HTML report when different lines changed:

| Changed line                                              | Diagram                                 |
| --------------------------------------------------------- | --------------------------------------- |
| Business rules, conditions, errors, retries               | Flowchart                               |
| API, service, queue, webhook, or third-party interactions | Sequence diagram                        |
| Modules, services, runtime boundaries, dependencies       | Architecture or dependency diagram      |
| Function calls or execution paths                         | Call graph                              |
| Classes, interfaces, fields, methods, inheritance         | Class diagram                           |
| Lifecycle or status transitions                           | State diagram                           |
| Tables, fields, migrations, transformations               | ER or data-flow diagram                 |
| Release, CI, feature flag, environment, or infra paths     | Deployment or operations flow diagram   |

Each diagram should show the line before and after when that can be inferred. Diagrams should stay small, use real code names, mark added/removed/modified nodes and edges, and focus on the paths a human should inspect first.

## What It Is Not

Review Preflight should not be positioned as:

- An automatic approver
- A replacement for security review
- A replacement for tests
- A final judgment about correctness
- A bot that comments on every line of code

It is closer to a review preparation assistant: a structured briefing before human judgment.

## Inputs

The skill works best with:

- PR title
- PR description
- Changed files
- Diff
- Commit messages
- Linked issue or ticket
- Test changes
- Relevant repository context

The minimum useful input is a PR title, changed files, and diff.

## Installation

Install the skill from this repository:

```bash
npx skills add Toormi/skills --skills review-preflight
```

## Usage

Invoke the skill with a PR URL, local branch, or pasted PR context:

```text
Use $review-preflight to analyze this PR and produce an HTML review briefing.
```

Or provide explicit input:

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

The output should be saved as HTML only. By default it should be a complete, self-contained `.html` file that opens directly in a browser, with inline CSS and no external build step. If you need a specific destination, include the output path in the request.

## Review Philosophy

Review Preflight is built around four layers:

1. Understanding: help the reviewer grasp what the PR is.
2. Visualization: help the reviewer see which workflow or timing lines changed, and how each line changed before versus after.
3. Navigation: help the reviewer decide where to start.
4. Skepticism: help the reviewer know what to verify.

The most valuable parts are the visualization, navigation, and skepticism layers. A generic PR summary is easy to ignore; a change graph, review route, and risk briefing can change how the reviewer spends attention.

## Future of Review

The future shape of review may not be:

> Humans read AI-written code line by line.

Instead:

> AI compresses code changes into structured judgment material, and humans review only the high-risk decision points.

So Review Preflight is not trying to be "a better code summarizer." It is trying to:

> Reorganize PRs from diff form into a form humans can decide with more easily.

## Future Product Direction

The first version is intentionally a skill: PR context in, HTML briefing out.

If the report proves useful on real historical PRs, the natural product path is:

1. GitHub/GitLab PR bot that posts or updates the briefing.
2. Review check status such as Low Risk, Medium Risk, High Risk, or Needs Author Clarification.
3. Team configuration for custom checklists and path-specific risk rules.
4. Dashboard for review intelligence, high-risk PRs, recurring test gaps, and reviewer feedback.

The product thesis is simple:

> Turn every PR into a human-readable review briefing before the diff.
