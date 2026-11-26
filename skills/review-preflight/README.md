# Review Preflight

**Know the PR before you read the diff.**

English | [中文](README.zh-CN.md)

Review Preflight turns a pull request into a self-contained HTML brief for a human reviewer. The opening tells you what changes under which condition, links to the first diff worth reading, and gives you a question to answer there. The reviewer makes the final judgment.

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

Open the saved HTML brief and start with the linked hunk. The opening describes the old and new behavior, explains why that hunk matters, and asks one question you can answer by reading it. For local changes, the brief points to the file and symbol or heading.

Follow another link when a caller, test, or migration answers a different question. Each concern appears at the place where you can check it. Claims about behavior point to the revisions inspected. An inference identifies the evidence still needed. A directory link correction can take a single sentence.

## Flow-Line Visualizations

The brief can contain zero diagrams. When a diagram helps answer a specific review question, it appears beside the relevant step. For example, if the order of a transaction commit and a retry is spread across two components, a sequence diagram can make the order visible.

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

Diagrams use real code names and mark changed nodes and edges. They show the before/after difference where the evidence supports it and label inferred relationships.

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

A pasted diff is enough to start. A partial patch limits which behavior the brief can establish.

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

Start where the behavior changes. A caller can explain how execution reaches that point, and a test can show exactly which outcome is asserted. The report ends once the reader has enough evidence to continue the review.

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
