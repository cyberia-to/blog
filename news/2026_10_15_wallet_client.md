---
tags: news, soft3, cyber
date: 2026-10-15
---
# cyber 0.8 became the command line of the root chain, on soft3::wallet

[[soft3]] #184 added `soft3::wallet`, the client half of `specs/chain.md`, shared by [[cyb]] and true-cyber so that one encoding and one signing path serve both. `wallet::tx` carries the rule-set-1 encodings (coinbase 82 B, transfer 224 B, cyberlink 257 B, claim 140 B) and a fee floor of 1 unit per byte. `wallet::Signer` holds a secp256k1 key as the chain sees it and derives it from a spell through [[mudra]]'s bridge at `m/44'/118'/0'/0/0`, so a holder in a bostrom or pussy snapshot signs with the key they already have. `wallet::verify` mirrors the kernel's signature check on the client, and `wallet::Client` speaks the HTTP routes of chain-wire §7.

true-cyber #5 put the command line on top of it as version 0.8. `cyber tx transfer`, `link`, `claim` and `show` sign with NSIG1, post to `/tx` and poll `/tx/{txid}` until inclusion. `cyber status`, `balance`, `balances`, `nonce`, `tip`, `block`, `history`, `neuron` and `fees` read the chain. the key comes from `--spell`, `$CYBER_SPELL`, `$CYBER_HOME/spell` or cyb's `~/cyb/spell`: one backup, one identity on every body. three end-to-end tests run the binary against a mock node that validates each transaction with `soft3::wallet::verify`.

at merge both pull requests named the consensus kernel as the piece they waited on: a real `soft3 node --chain` to point at. in [[cyber]], the launcher package dropped its `auth enable` subcommand and built again.

## sources

- the wallet: [soft3 #184](https://github.com/cyberia-to/soft3/pull/184)
- the command line: [true-cyber #5](https://github.com/cyberia-to/true-cyber/pull/5) · the mock-node tests [d5811c0](https://github.com/cyberia-to/true-cyber/commit/d5811c0be35e24bfc467c5199de3d54a9a99ec5f)
- the launcher: [cyber #132](https://github.com/cyberia-to/cyber/pull/132)
