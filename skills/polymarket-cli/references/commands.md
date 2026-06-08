# Polymarket CLI Command Reference

Source inspected: `https://github.com/Polymarket/polymarket-cli`, commit `9b18b5faf5493b945c48ca22efaf9645f0c69ab8`, package version `0.1.4`.

Always prefer `polymarket <command> --help` for the live command surface because the upstream project describes the CLI as experimental.

## Global

```bash
polymarket --help
polymarket --version
polymarket -o json <command>
polymarket --output table <command>
polymarket --signature-type proxy <command>
polymarket --private-key 0x... <command>
```

Global output formats are `table` and `json`. Use JSON for scripts and agent parsing.

Avoid passing private keys with `--private-key` unless explicitly required by the user; command-line arguments can leak through process listings and shell history.

## Install And Update

```bash
brew tap Polymarket/polymarket-cli https://github.com/Polymarket/polymarket-cli
brew install polymarket

curl -sSL https://raw.githubusercontent.com/Polymarket/polymarket-cli/main/install.sh | sh

git clone https://github.com/Polymarket/polymarket-cli
cd polymarket-cli
cargo install --path .

polymarket upgrade
```

`Cargo.toml` declares Rust `1.88.0` and binary name `polymarket`.

## Wallet And Auth

```bash
polymarket setup
polymarket wallet create
polymarket wallet create --force
polymarket wallet create --signature-type proxy
polymarket wallet import 0xKEY...
polymarket wallet import 0xKEY... --force --signature-type eoa
polymarket wallet address
polymarket wallet show
polymarket wallet reset
polymarket wallet reset --force
```

Private key resolution order:

1. `--private-key`
2. `POLYMARKET_PRIVATE_KEY`
3. `~/.config/polymarket/config.json`

Signature type resolution order:

1. `--signature-type`
2. `POLYMARKET_SIGNATURE_TYPE`
3. `~/.config/polymarket/config.json`
4. default `proxy`

Signature types: `proxy`, `eoa`, `gnosis-safe`.

## Read-Only Market Data

```bash
polymarket markets list --limit 10
polymarket markets list --active true --closed false --order volume_num --ascending
polymarket markets get <market-id-or-slug>
polymarket markets search "bitcoin" --limit 5
polymarket markets tags <market-id>

polymarket events list --limit 10
polymarket events list --tag politics --active true
polymarket events get <event-id-or-slug>
polymarket events tags <event-id>

polymarket tags list
polymarket tags get <tag-id-or-slug>
polymarket tags related <tag-id-or-slug>
polymarket tags related-tags <tag-id-or-slug>

polymarket series list --limit 10
polymarket series get <series-id>

polymarket comments list --entity-type event --entity-id <id> --limit 25
polymarket comments get <comment-id>
polymarket comments by-user <wallet-address>

polymarket profiles get <wallet-address>

polymarket sports list
polymarket sports market-types
polymarket sports teams --league NFL --limit 32
```

Useful list flags include `--limit`, `--offset`, `--order`, `--ascending`, `--active`, `--closed`, and group-specific filters such as `--tag`, `--league`, or `--entity-type`.

## CLOB Read-Only

```bash
polymarket clob ok
polymarket clob price <token-id> --side buy
polymarket clob batch-prices "TOKEN1,TOKEN2" --side sell
polymarket clob midpoint <token-id>
polymarket clob midpoints "TOKEN1,TOKEN2"
polymarket clob spread <token-id>
polymarket clob spread <token-id> --side buy
polymarket clob spreads "TOKEN1,TOKEN2"
polymarket clob book <token-id>
polymarket clob books "TOKEN1,TOKEN2"
polymarket clob last-trade <token-id>
polymarket clob last-trades "TOKEN1,TOKEN2"
polymarket clob market <condition-id>
polymarket clob markets
polymarket clob markets --cursor <cursor>
polymarket clob sampling-markets
polymarket clob simplified-markets
polymarket clob sampling-simp-markets
polymarket clob tick-size <token-id>
polymarket clob fee-rate <token-id>
polymarket clob neg-risk <token-id>
polymarket clob price-history <token-id> --interval 1d --fidelity 30
polymarket clob time
polymarket clob geoblock
```

Sides are `buy` or `sell`. `price-history --interval` accepts `1m`, `1h`, `6h`, `1d`, `1w`, or `max`.

## CLOB Authenticated

Requires a configured wallet or private key.

```bash
polymarket clob orders
polymarket clob orders --market <condition-id>
polymarket clob orders --asset <token-id>
polymarket clob order <order-id>

polymarket clob create-order --token <token-id> --side buy --price 0.50 --size 10
polymarket clob create-order --token <token-id> --side sell --price 0.75 --size 10 --order-type GTC --post-only
polymarket clob post-orders --tokens "TOKEN1,TOKEN2" --side buy --prices "0.40,0.60" --sizes "10,10"
polymarket clob market-order --token <token-id> --side buy --amount 5

polymarket clob cancel <order-id>
polymarket clob cancel-orders "ORDER1,ORDER2"
polymarket clob cancel-market --market <condition-id>
polymarket clob cancel-market --asset <token-id>
polymarket clob cancel-all

polymarket clob trades
polymarket clob trades --market <condition-id>
polymarket clob balance --asset-type collateral
polymarket clob balance --asset-type conditional --token <token-id>
polymarket clob update-balance --asset-type collateral
polymarket clob update-balance --asset-type conditional --token <token-id>
```

Order types: `GTC`, `FOK`, `GTD`, `FAK`. Market orders default to `FOK`.

Reward and account commands:

```bash
polymarket clob notifications
polymarket clob delete-notifications "NOTIF1,NOTIF2"
polymarket clob rewards --date YYYY-MM-DD
polymarket clob earnings --date YYYY-MM-DD
polymarket clob earnings-markets --date YYYY-MM-DD
polymarket clob reward-percentages
polymarket clob current-rewards
polymarket clob market-reward <condition-id>
polymarket clob order-scoring <order-id>
polymarket clob orders-scoring "ORDER1,ORDER2"
polymarket clob api-keys
polymarket clob create-api-key
polymarket clob delete-api-key
polymarket clob account-status
```

## On-Chain Data

Public data, no wallet required:

```bash
polymarket data positions <wallet-address> --limit 25
polymarket data closed-positions <wallet-address>
polymarket data value <wallet-address>
polymarket data traded <wallet-address>
polymarket data trades <wallet-address> --limit 50
polymarket data activity <wallet-address>
polymarket data holders <condition-id> --limit 10
polymarket data open-interest <condition-id>
polymarket data volume <event-id>
polymarket data leaderboard --period month --order-by pnl --limit 10
polymarket data builder-leaderboard --period week
polymarket data builder-volume --period month
```

Leaderboard periods: `day`, `week`, `month`, `all`. `--order-by` accepts `pnl` or `vol`.

## Approvals And CTF

Approvals:

```bash
polymarket approve check
polymarket approve check <wallet-address>
polymarket approve set
```

`approve set` sends on-chain transactions and needs gas on Polygon.

CTF operations:

```bash
polymarket ctf split --condition <condition-id> --amount 10
polymarket ctf merge --condition <condition-id> --amount 10
polymarket ctf redeem --condition <condition-id>
polymarket ctf redeem-neg-risk --condition <condition-id> --amounts "10,5"

polymarket ctf condition-id --oracle <oracle-address> --question <question-id> --outcomes 2
polymarket ctf collection-id --condition <condition-id> --index-set 1
polymarket ctf position-id --collection <collection-id>
```

`split`, `merge`, `redeem`, and `redeem-neg-risk` send on-chain transactions. Calculation commands are read-only.

## Bridge

```bash
polymarket bridge deposit <polymarket-wallet-address>
polymarket bridge supported-assets
polymarket bridge status <deposit-address>
```

## Interactive Shell

```bash
polymarket shell
```

Inside the shell, omit the `polymarket` prefix:

```text
polymarket> markets list --limit 3
polymarket> clob book <token-id>
polymarket> exit
```

The shell blocks running `setup` from inside the shell.

## Recipes

Find a market, then inspect token-level pricing:

```bash
polymarket -o json markets search "ethereum" --limit 5
polymarket -o json markets get <market-slug-or-id>
polymarket -o json clob midpoint <token-id>
polymarket -o json clob book <token-id>
```

Research an event by tag:

```bash
polymarket -o json events list --tag politics --active true --limit 10
polymarket -o json events get <event-id-or-slug>
```

Check a wallet without authenticating:

```bash
polymarket -o json data positions <wallet-address>
polymarket -o json data value <wallet-address>
polymarket -o json data trades <wallet-address> --limit 25
```

Prepare for trading without placing an order:

```bash
polymarket wallet show
polymarket approve check
polymarket -o json clob balance --asset-type collateral
polymarket -o json clob orders
```
