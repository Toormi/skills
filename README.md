# Toormi Skills

A collection of reusable Agent skills maintained by Toormi.

Each skill lives in its own directory and includes a `SKILL.md` file with the instructions an Agent should follow. Some skills also include human-facing documentation, examples, or supporting assets.

## Skills

| Skill | Description |
| --- | --- |
| [`review-preflight`](review-preflight/) | Generates a concise HTML briefing to help humans prepare for PR review. |

## Repository Structure

```text
toormi-skills/
├── README.md
└── review-preflight/
    ├── SKILL.md
    ├── README.md
    └── README.zh-CN.md
```

## Using a Skill

Use a skill by referencing it in an Agent session:

```text
Use $review-preflight to prepare a review briefing for this PR.
```

See each skill directory for usage details and examples.

## Adding a Skill

Keep each skill self-contained:

- `SKILL.md` for Agent instructions.
- `README.md` for user-facing documentation.
- Optional examples, scripts, or templates in the same directory.

Skill instructions should be clear, actionable, and explicit about scope, expected inputs, outputs, and limitations.
