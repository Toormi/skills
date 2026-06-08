#!/usr/bin/env python3
"""Run the polymarket CLI with JSON output.

This helper is intended for read/query workflows. It forces `-o json` and
rejects command-line private keys so secrets are not exposed through shell
history or process listings.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from typing import Iterable


USAGE = """Usage:
  python3 scripts/polymarket-json.py <polymarket-args...>

Examples:
  python3 scripts/polymarket-json.py markets search "bitcoin" --limit 5
  python3 scripts/polymarket-json.py clob midpoint <token-id>

Set POLYMARKET_BIN to use a non-PATH binary.
"""


def redact_args(args: Iterable[str]) -> list[str]:
    redacted: list[str] = []
    skip_next = False
    for arg in args:
        if skip_next:
            redacted.append("<redacted>")
            skip_next = False
            continue
        if arg == "--private-key":
            redacted.append(arg)
            skip_next = True
            continue
        if arg.startswith("--private-key="):
            redacted.append("--private-key=<redacted>")
            continue
        redacted.append(arg)
    return redacted


def emit_error(message: str, **extra: object) -> None:
    payload = {"error": message}
    payload.update(extra)
    print(json.dumps(payload, indent=2, sort_keys=True))


def main(argv: list[str]) -> int:
    if not argv or argv[0] in {"-h", "--help"}:
        print(USAGE)
        return 0

    if "-o" in argv or "--output" in argv or any(a.startswith("--output=") for a in argv):
        emit_error("Do not pass output flags to this helper; it always uses JSON output.")
        return 2

    if "--private-key" in argv or any(a.startswith("--private-key=") for a in argv):
        emit_error(
            "Refusing to pass --private-key on the command line. Use existing config or a scoped POLYMARKET_PRIVATE_KEY environment variable."
        )
        return 2

    binary_name = os.environ.get("POLYMARKET_BIN", "polymarket")
    binary = shutil.which(binary_name)
    if binary is None:
        emit_error(
            "polymarket binary not found",
            install=[
                "brew tap Polymarket/polymarket-cli https://github.com/Polymarket/polymarket-cli && brew install polymarket",
                "curl -sSL https://raw.githubusercontent.com/Polymarket/polymarket-cli/main/install.sh | sh",
                "cargo install --git https://github.com/Polymarket/polymarket-cli",
            ],
        )
        return 127

    cmd = [binary, "-o", "json", *argv]
    result = subprocess.run(cmd, check=False, capture_output=True, text=True)

    if result.stdout.strip():
        sys.stdout.write(result.stdout)
        if not result.stdout.endswith("\n"):
            sys.stdout.write("\n")
    else:
        emit_error(
            "polymarket command produced no stdout",
            exit_code=result.returncode,
            stderr=result.stderr.strip(),
            command=redact_args(cmd),
        )

    if result.stderr.strip():
        sys.stderr.write(result.stderr)
        if not result.stderr.endswith("\n"):
            sys.stderr.write("\n")

    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
