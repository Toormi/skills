---
name: review-preflight
description: Prepare a human reviewer to open the most informative diff first. Use for a PR preflight, an HTML review brief, a guided review of a large or AI-generated change, a visualization of a changed workflow, or an author preparing to request review. Accept a PR URL, local changes, or a pasted diff.
---

# Review Preflight

Save a short, self-contained HTML briefing in the user's language. Help the reviewer choose what to read and what to verify. Leave approval, rejection, and findings to the actual code review.

## Prepare the first screen

1. **State the change.** In one or two sentences, name the condition, what happened before, and what happens now. For documentation or configuration, describe what readers see or what the setting controls. If a side of the comparison is unknown, say which detail is missing.
2. **Give the reviewer a place to start.** Immediately link to the first worthwhile diff hunk and name the file and symbol (or heading). Make that link the primary action. Choose the place that decides the behavior or contract. It may be one line in a small file. Explain why this spot is decisive and give one question the reader can answer there.
3. **Continue only for a distinct decision.** Add the next location when a caller, a test, a migration, or another path answers a question the first stop leaves open. Attach the supporting evidence, risk, or author question to that stop. Mention each concern once. End the report when the next step is clear. A small correction can take one linked sentence.

Keep the change, first location, reason, and question visible together before any statistics, diagrams, or background. No item quotas or required panels. Match the route to the requested reviewer role or, for an author, to the decisions to clarify before review.

## Establish the evidence

- For a hosted PR, collect the description, base and head revisions, changed files, and relevant hunks. For a local branch, compare with the merge base of the intended target. Include working-tree changes when requested. For a pasted or partial diff, work within the supplied evidence.
- Trace the behavior that determines the first stop. Read enough of the old and new implementation to establish the change. Follow a direct caller if it chooses the path, and inspect a related test's setup and assertions if they bear on the question. Treat the PR description as a statement of intent.
- Link the first stop to the changed lines in the diff when available. For supporting evidence, use commit-pinned source lines at the inspected head for additions and at the base or parent for removed behavior. Check the path, revision, side, and line numbers. If a hunk link is unavailable, use a verified source permalink and identify the changed symbol. For local or pasted changes, give the exact path and symbol or heading, plus a line or a short hunk excerpt when known. Avoid fabricated URLs or coordinates.
- State demonstrated behavior plainly. For an inference, name the missing caller, configuration, test assertion, or other evidence that would settle it. For example, write “The changed test asserts the first delivery. Does a second delivery produce a second record?” Scope a coverage claim to the tests inspected. If the patch is truncated, identify the affected path and explain how that limits the conclusion.

## Decide whether to draw

Write the review question first. If a sentence and a code link answer it, use **zero diagrams**. When a reviewer needs to compare ordering, branching, or relationships across locations, place a small diagram beside the route step it explains.

For example, “Does a retry occur before or after the transaction commits?” can justify a sequence diagram. Use a state diagram for a changed transition or a dependency or data-flow diagram for a changed boundary. Show the relevant before/after difference using real symbols and labeled edges. Mark any inferred step. Use text or symbols as well as color, and link the supporting code at that stop.

## Example openings

**A rule change across three files** (commit `4187514`)

> When preparing a PR brief, the agent previously chose a diagram based on the review question. The revised instructions first inventory changed flows, then select one to five to draw.
>
> **Start at the [diagram selection rule in `SKILL.md`](https://github.com/Toormi/skills/commit/41875142f8e84ddfcf3e26a03fcff0f977b45458#diff-f506559efe0492a8586f5a5ec09e303398d9edb5f08cb80ab907fbd91f2963a9R86).** This line introduces a minimum absent from the [previous rule](https://github.com/Toormi/skills/blob/bf941ab4befb6379cc6fd84fcab3b3496a14aafa/skills/review-preflight/SKILL.md#L77-L83), while [the opening of the same section](https://github.com/Toormi/skills/blob/41875142f8e84ddfcf3e26a03fcff0f977b45458/skills/review-preflight/SKILL.md#L78-L87) makes diagrams conditional. Can the agent skip a diagram for a one-line copy edit?
>
> Then compare the [English](https://github.com/Toormi/skills/commit/41875142f8e84ddfcf3e26a03fcff0f977b45458#diff-6e7004987fc3ddcdd74eb0fdf502303663630a26bfdf459a762d49701a971d9e) and [Chinese](https://github.com/Toormi/skills/commit/41875142f8e84ddfcf3e26a03fcff0f977b45458#diff-626d85f8e01c0c1e0b35f8eebba5241ad4f493953ce51b8973448a92879a85dc) READMEs. Do both describe the selection rule the reviewer expects the agent to follow?

**A directory link correction** (commit `0fb7c73`). Use one sentence for the whole brief.

> The [root README link](https://github.com/Toormi/skills/commit/0fb7c7395e02d5c7539a926274b25e881baa7bf1#diff-b335630551682c19a781afebcf4d07bf978fb1f8ac04c6bf87428ed5106870f5R11) now points to `skills/review-preflight/` instead of `review-preflight/` after the move — does it open the directory containing `SKILL.md`, and do the English and Chinese directory trees match that path?

## Save the HTML

Use the requested path or `review-preflight-<pr-or-branch>.html` in the working directory. Choose a fresh name if needed to avoid overwriting an earlier report. Produce a complete HTML document unless the user explicitly requests a fragment. Use a title, UTF-8 and viewport metadata, semantic headings and links, inline CSS, and inline SVG or CSS for diagrams. Escape supplied text and code. Keep the brief usable offline with no scripts, fonts, or assets to download. Evidence links may open the code host.

Before handing it over, read just the opening. Can a reviewer tell what changed, open the decisive location, and say what to check there without scrolling? Check the evidence links or local locators, remove repeated concerns, and return the saved file path with a short summary.
