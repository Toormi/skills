# Review Preflight

**Know the PR before you read the diff.**

English | [中文](README.zh-CN.md)

Review Preflight is a Agent skill that turns a pull request into a concise, self-contained HTML briefing file for human reviewers. It helps reviewers understand the intent, navigate the most important files first, and focus attention on likely risk areas before opening the full diff.

It is not an AI code reviewer. It does not approve, reject, or claim that code is correct. Its job is to reduce reviewer cold start.

## Why This Exists

AI can now produce code faster than humans can review it. The short-term answer is not to skip human review, but to make human review start from better context.

Review Preflight reframes a PR from a raw diff into reviewer-ready decision material:

- What is this PR trying to do?
- What changed at the module or system level?
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
- Suggested review route
- Risk areas
- Missing or weak tests
- Questions for the author
- Human review checklist

The HTML can use richer presentation patterns such as metric strips, route timelines, risk matrices, annotated diff excerpts, module maps, cards, tables, callouts, tabs, collapsible sections, and checkbox lists when they help the reviewer scan faster.

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
npx skills add https://github.com/Toormi/review-preflight
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

Review Preflight is built around three layers:

1. Understanding: help the reviewer grasp what the PR is.
2. Navigation: help the reviewer decide where to start.
3. Skepticism: help the reviewer know what to verify.

The most valuable parts are the second and third layers. A generic PR summary is easy to ignore; a review route and risk briefing can change how the reviewer spends attention.

## Future of Review

The future shape of review may not be:

> Humans read AI-written code line by line.

Instead:

> AI compresses code changes into structured judgment material, and humans review only the high-risk decision points.

So Review Preflight is not trying to be "a better code summarizer." It is trying to:

> Reorganize PRs from diff form into a form humans can decide with more easily.

## Repository Structure

```text
review-preflight/
├── SKILL.md
├── README.md
└── README.zh-CN.md
```

- `SKILL.md` contains the actual skill instructions.
- `README.md` is the default English README.
- `README.zh-CN.md` is the Chinese README.

## Future Product Direction

The first version is intentionally a skill: PR context in, HTML briefing out.

If the report proves useful on real historical PRs, the natural product path is:

1. GitHub/GitLab PR bot that posts or updates the briefing.
2. Review check status such as Low Risk, Medium Risk, High Risk, or Needs Author Clarification.
3. Team configuration for custom checklists and path-specific risk rules.
4. Dashboard for review intelligence, high-risk PRs, recurring test gaps, and reviewer feedback.

The product thesis is simple:

> Turn every PR into a human-readable review briefing before the diff.
