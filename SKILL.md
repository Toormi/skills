---
name: review-preflight
description: Generate a concise HTML human review briefing before code review by turning PR titles, descriptions, changed files, commits, diffs, issue context, or local git changes into a Review Preflight report with PR intent, change map, suggested review route, risk areas, missing or weak tests, author questions, and a human checklist. Use when asked to prepare reviewers for a pull request, summarize a PR for review, triage a large or AI-generated PR, reduce reviewer cold start, create a PR preflight report, create an HTML review brief, or help an author improve a PR before requesting review.
---

# Review Preflight

## Purpose

Prepare a human reviewer before they inspect a PR diff. Do not replace code review, approve changes, reject changes, or claim the code is correct. Convert PR evidence into a short briefing that helps the reviewer understand context, choose where to look first, and focus skepticism on the highest-value areas.

## Workflow

1. Gather the best available PR context.
   - Prefer PR title, description, changed files, diff, commit messages, linked issue or ticket, test changes, and relevant repository context.
   - If the user provides a PR URL or current branch, use available GitHub/GitLab/local git tools to collect metadata and diff context.
   - If only local changes are available, compare against the likely base branch and use changed files, diff, and recent commits.
   - If key inputs are missing, proceed with what is available and state the limitation in the report.

2. Build the reviewer's mental model.
   - Infer what the PR appears to be trying to accomplish.
   - Group changes by system area or responsibility instead of listing files mechanically.
   - Identify the core files or modules where behavior, contracts, data, security, or tests actually change.

3. Plan the review route.
   - Recommend an order that minimizes cold start and maximizes risk discovery.
   - Usually prioritize central business logic, public interfaces, schema or migration changes, security-sensitive paths, integration boundaries, then tests.
   - Explain why each stop belongs in the route.

4. Surface concrete risks and uncertainty.
   - Frame risks as things the reviewer should verify, not as final findings.
   - Prefer specific paths, functions, data flows, and behaviors over generic warnings.
   - Distinguish "not observed in the provided diff" from "definitely missing."

5. Design the HTML presentation.
   - Output HTML only for the report.
   - Use an HTML fragment by default, rooted in a clear container such as `<article class="review-preflight">`.
   - Use a complete HTML document with inline CSS only when the user asks for a standalone page, file, preview, or polished visual artifact.
   - Adapt the layout to the PR instead of forcing every report into the same rigid section order.

6. Produce a concise Review Preflight report.
   - Match the user's language unless they request otherwise.
   - Keep the main report readable in one pass.
   - Default to 3-5 core changes, 3-7 risk points, 3-5 author questions, and 5-10 checklist items.

## Evidence Rules

- Use cautious language: "appears", "suggests", "likely", "needs confirmation", "not visible in the provided diff".
- Do not say "safe to merge", "approved", "correct", "no issues", or "this is secure".
- Do not invent issue context, production behavior, ownership, test coverage, or runtime facts.
- If the diff is too large or incomplete, say what was inspected and where confidence is limited.
- If the PR description is weak or missing, call that out as review friction.
- If the user wants an actual code review after the briefing, switch to normal review behavior after the preflight report.

## Risk Heuristics

Pay extra attention when a PR touches:

- Authentication, authorization, roles, sessions, tokens, policies, or permissions.
- Money, billing, payments, refunds, invoices, tax, currency, or decimal precision.
- Data migrations, schema changes, default values, nullable columns, backfills, or data retention.
- Concurrency, locks, transactions, idempotency, retries, queues, or race-prone state transitions.
- External integrations, webhooks, third-party APIs, payment gateways, email, SMS, or async workers.
- Error handling, partial failure, rollback, timeout, retry, cleanup, or observability.
- Backward compatibility, public APIs, event schemas, old clients, feature flags, or existing data.
- User-controlled input, file upload, SQL, command execution, serialization, redirects, or secrets.
- Configuration, infrastructure, deployment, CI, permissions, or environment-specific behavior.
- Tests that are absent, only happy-path, lack regression cases, or do not cover the risky behavior changed.

## HTML Output

Return the report as HTML only. Do not provide alternate report formats unless the user is asking to edit the skill itself or debug the generated HTML.

Use semantic, readable HTML and choose a presentation that fits the PR. Do not copy a fixed template. Compose from these patterns as useful:

- Summary header with PR title, review complexity, confidence, changed-file count, and the most important caveat.
- Metric strip for changed files, core files, risky paths, tests touched, migration changes, or external integrations.
- Review route timeline showing the recommended order of files or modules to inspect.
- Change map grouped by area, displayed as cards, columns, a table, or nested lists depending on density.
- Risk matrix grouped by high, medium, and low risk, with each item stating what to verify.
- Author question panel for concrete follow-up questions.
- Missing-test panel highlighting absent, weak, or uncertain coverage.
- Checklist with actual checkbox inputs when the output is intended for a browser; use plain list items when checkbox controls would be awkward in the target surface.
- Callouts for limited context, weak PR description, incomplete diff, or assumptions.

Keep the information architecture stable even when the layout varies:

1. PR intent.
2. Review complexity.
3. Core changes.
4. Change map.
5. Suggested review route.
6. Risk areas.
7. Missing or weak tests.
8. Questions for the author.
9. Human review checklist.

HTML rules:

- Escape user-provided text, file paths, branch names, and code snippets correctly.
- Use `<code>` for file paths, commands, symbols, and short literals.
- Use headings, sections, lists, tables, cards, badges, or callouts to improve scanability.
- Keep CSS inline in a `<style>` block only for standalone pages or polished previews.
- Keep fragments free of `<html>`, `<head>`, and `<body>` unless a complete page is requested.
- Make the report compact enough to read before opening the diff.
- Avoid decorative visuals that do not help reviewer decisions.

## Role-Specific Use

If the user names a reviewer role, tune the briefing:

- Backend reviewer: emphasize contracts, transactions, data consistency, integrations, state machines, and tests.
- Security reviewer: emphasize authorization, input boundaries, secrets, data exposure, abuse cases, and negative tests.
- Tech lead: emphasize design direction, coupling, migration strategy, operational risk, future extensibility, and rollout.
- Author preparing a PR: phrase findings as changes to make before requesting review, including description gaps, missing tests, and unclear decisions.

## Quality Bar

A good Review Preflight report makes the reviewer say: "I know what this PR is trying to do, where to start, what to distrust, and what to ask." If the output is merely a file summary, revise it toward review navigation and risk-focused human judgment.
