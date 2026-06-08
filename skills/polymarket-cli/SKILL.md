---
name: polymarket-cli
description: Use when an agent needs to interact with Polymarket through the official polymarket CLI for market and event research, tags, public profiles, sports metadata, CLOB prices and order books, JSON scripting, wallet setup, approvals, portfolio/on-chain data, bridge status, CTF operations, or authenticated trading and order management. Trigger for requests mentioning Polymarket CLI, polymarket markets/events/CLOB/order book/prices, Polymarket wallet setup, approvals, trading, CTF, bridge deposits, or scripting Polymarket data.
---

# Polymarket CLI

## Purpose

Use the official `polymarket` Rust CLI to browse Polymarket markets, query CLOB data, manage wallet/auth setup, inspect portfolio data, and perform authenticated trading or on-chain operations when explicitly requested.

This skill is based on `https://github.com/Polymarket/polymarket-cli` at default-branch commit `9b18b5faf5493b945c48ca22efaf9645f0c69ab8` with package version `0.1.4`. The upstream README warns that the CLI is experimental, so verify current help with `polymarket --help` and `polymarket <group> --help` before relying on a flag.

## Operating Rules

1. Prefer read-only commands for research and analysis unless the user explicitly asks for a wallet, approval, order, cancellation, CTF, bridge, or other fund-affecting action.
2. Use JSON output for programmatic work: `polymarket -o json ...`.
3. Use `scripts/polymarket-json.py` for routine read/query workflows when available; it forces JSON output and rejects `--private-key` on the command line.
4. Do not print, store, or repeat private keys. Prefer existing config or a scoped `POLYMARKET_PRIVATE_KEY` environment variable over `--private-key`, which can leak through shell history and process lists.
5. For commands that place/cancel orders, set approvals, split/merge/redeem CTF tokens, import/reset/create wallets, or otherwise affect funds, show the exact command and obtain explicit confirmation unless the user already gave that exact command and asked you to run it.
6. After any command with financial side effects, report the transaction hash, order ID, or error, and state whether output came from table mode or JSON mode.

## Setup

Check for the binary first:

```bash
polymarket --version
polymarket --help
```

Install options from the upstream project:

```bash
brew tap Polymarket/polymarket-cli https://github.com/Polymarket/polymarket-cli
brew install polymarket

curl -sSL https://raw.githubusercontent.com/Polymarket/polymarket-cli/main/install.sh | sh

git clone https://github.com/Polymarket/polymarket-cli
cd polymarket-cli
cargo install --path .
```

Wallet/auth resolution order:

1. `--private-key 0x...`
2. `POLYMARKET_PRIVATE_KEY=0x...`
3. `~/.config/polymarket/config.json`

Signature type resolution order is `--signature-type`, `POLYMARKET_SIGNATURE_TYPE`, config file, then default `proxy`. Valid signature types are `proxy`, `eoa`, and `gnosis-safe`.

Useful environment overrides:

```bash
POLYMARKET_PRIVATE_KEY=0x...
POLYMARKET_SIGNATURE_TYPE=proxy
POLYMARKET_CLOB_HOST=https://clob.polymarket.com
POLYMARKET_RPC_URL=https://polygon.drpc.org
```

## Common Workflows

Market research:

```bash
polymarket -o json markets search "bitcoin" --limit 5
polymarket -o json markets get <market-id-or-slug>
polymarket -o json events list --tag politics --active true
```

CLOB price and order-book research:

```bash
polymarket -o json clob midpoint <token-id>
polymarket -o json clob book <token-id>
polymarket -o json clob price-history <token-id> --interval 1d --fidelity 30
```

Wallet and approval checks:

```bash
polymarket wallet show
polymarket approve check
polymarket approve check <wallet-address>
```

Trading setup and trading commands require explicit user intent:

```bash
polymarket wallet create
polymarket wallet import <private-key>
polymarket approve set
polymarket clob create-order --token <token-id> --side buy --price 0.50 --size 10
polymarket clob cancel <order-id>
```

Portfolio and on-chain data:

```bash
polymarket -o json data positions <wallet-address>
polymarket -o json data value <wallet-address>
polymarket -o json clob orders
polymarket -o json clob trades
```

## Helper Script

Use the bundled helper for JSON-first CLI calls:

```bash
python3 scripts/polymarket-json.py markets search "bitcoin" --limit 5
python3 scripts/polymarket-json.py clob midpoint <token-id>
```

The helper:

- Locates `polymarket` with `PATH` or `POLYMARKET_BIN`.
- Prepends `-o json`.
- Rejects `--private-key` so secrets are not passed as command-line arguments.
- Returns CLI stdout unchanged when the CLI emits JSON.
- Emits a JSON error object when the binary is missing or the command emits only stderr.

## Detailed Reference

Read `references/commands.md` when you need the command map, authenticated/read-only split, install notes, or recipes for a specific command family.
