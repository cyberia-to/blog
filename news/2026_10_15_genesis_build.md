---
tags: news, soft3, bootloader, bostrom, cyber
date: 2026-10-15
---
# soft3 genesis build turned the burial snapshots into genesis files, and the pussy state committed

[[soft3]] #183 added `soft3 genesis build` and `soft3 genesis verify`. the builder reads the burial snapshot of [[space-pussy]] or [[bostrom]]: it fetches every file the manifest pins and verifies CID, sha256 and size, derives the owners (`neuron_of(pubkey)` for secp256k1 accounts, `legacy_owner` for the rest), carries every denom as its own token with delegations and unbonding made liquid, and turns passports into height-0 links. the output is one [[tade]] stream, `urn:cyberia:chain-genesis:1`, and the hemera particle of that file is the chain id. loading the file into one bbg state and committing once gives the state root and block 0.

the pussy file was built in 4 s, byte-identical across builds: 1,385 balance frames and 29,113 link frames over 23 tokens, chain id `2a83e54f…`. the audit in the bostrom repository compared source counts with genesis counts: 29,112 links, 616 accounts, 16,271 particles, 1 passport and a supply of 1,099,389,810,279,114,036 all matched.

the bostrom file matched its counts as well: 2,949,732 links, 3,143,650 particles, 61,675 accounts and 47,837 passports, built in 122 s with 3.3 GB. its state root waited on a limit in lens, where Brakedown's `MAX_VARIABLES = 20` caps a dimension commitment at 2^20 field elements. [[cyber]]'s launch page recorded both results.

## sources

- the builder: [soft3 #183](https://github.com/cyberia-to/soft3/pull/183) · [soft3/specs/genesis.md](https://github.com/cyberia-to/soft3/blob/main/specs/genesis.md) · the run report [soft3/audit/genesis-2026-10-15.md](https://github.com/cyberia-to/soft3/blob/main/audit/genesis-2026-10-15.md)
- the counts: [bostrom #22](https://github.com/cyberia-to/bostrom/pull/22)
- the record: [cyber #131](https://github.com/cyberia-to/cyber/pull/131)
