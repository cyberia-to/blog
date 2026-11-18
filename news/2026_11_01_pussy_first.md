---
tags: news, cyberia, soft3, bootloader, space-pussy
date: 2026-11-01
---
# pussy first: the top-priority project, with its identity pinned in the binary

on the owner's word of 2026-11-01 pussy became the top-priority project. [[cyberia]] gave it a passport, projects/pussy, with the target set against the measured distance, the critical path and every open task placed; a row in the projects table; and the first goal narrowed to pussy. the director's plan on `release/phase1` of [[soft3]] took the same word as decision D16: the P rows come before every other row. the new rows are P4, pussy's identity pinned in the binary; P5, transactions without signatures, measured first; P6, foculus off the legacy fold; P7, the φ* relation, measured first; and P8, the block relation.

P4 merged the same day. until then the chain parameters carried a zero chain id and a zero block-0 id for pussy, so the node booted any genesis file whose parameters named the chain pussy. the binary now pins the values blessed on 2026-10-17 in `conformance/chain-genesis.toml`. the node checks the hash of the file against the pin before anything is written, and checks block 0 after the kernel opens, so a build whose state rules drifted from the blessed root refuses to start instead of forking. `soft3 conformance check chain --genesis` compares a file to the binary's pins, and the release gate `stack-chain-genesis` runs exactly that on the file it builds. bostrom stays unpinned for now.

## sources

- the project: [cyberia #10](https://github.com/cyberia-to/cyberia/pull/10)
- the plan, into `release/phase1`: [soft3 #560](https://github.com/cyberia-to/soft3/pull/560)
- the pin, into `release/phase1`: [soft3 #562](https://github.com/cyberia-to/soft3/pull/562)
