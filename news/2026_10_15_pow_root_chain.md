---
tags: news, soft3, cyber
date: 2026-10-15
---
# phase 1 became a pure proof-of-work root chain, and soft3 received its spec

the owner's scope decision of 2026-10-15 was recorded in [[cyber]]'s launch page: phase 1 ships the smallest safe chain. it is [[hemera]] proof of work with ASERT difficulty, a transfer and a cyberlink signed by a neuron through [[mudra]]'s NSIG1, a coinbase and a legacy claim beside them, [[bbg]] state, [[radio]] gossip and sync, and forks activated by height. the four cores run as shadow indexers and activate by scheduled fork. the order was pussy first, bostrom once its state commits.

[[soft3]] received the canonical specification the same day, in three files. `specs/chain.md` covers the header, proof of work, ASERT, transactions, state, genesis, consensus, upgrades, security and the node. `specs/chain-wire.md` covers the radio topics, request streams, sync, limits, discovery and HTTP. `specs/chain-conformance.md` holds the acceptance vectors. one measurement was taken while writing: `hemera::hash` over the 168-byte header ran at 64.4 kH/s per M4 Max core on the scalar path, and that figure set `GENESIS_BITS = 0x1e010000` and `POW_LIMIT = 2^236`.

an ops pull request followed with the preparation for three machines: a runbook, a systemd instance unit for `soft3-chain@pussy` and `soft3-chain@bostrom`, nginx and firewall templates, a health check and a three-node harness. every running service stayed as it was.

## sources

- the decision: [cyber #130](https://github.com/cyberia-to/cyber/pull/130) · [cyber/launch.md](https://github.com/cyberia-to/cyber/blob/master/launch.md)
- the spec: [soft3 #182](https://github.com/cyberia-to/soft3/pull/182) · [soft3/specs/chain.md](https://github.com/cyberia-to/soft3/blob/main/specs/chain.md) · [soft3/specs/chain-wire.md](https://github.com/cyberia-to/soft3/blob/main/specs/chain-wire.md) · the spec commit [83e9012](https://github.com/cyberia-to/soft3/commit/83e90127c87f33d5af7b377507ef450a428796a0)
- the ops preparation: [soft3 #185](https://github.com/cyberia-to/soft3/pull/185)
