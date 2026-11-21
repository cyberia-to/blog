---
tags: news, soft3, lens, radio
date: 2026-10-16
---
# the root chain ran as a node: kernel, miner and wire merged into soft3

three pull requests gave [[soft3]] the pieces of `soft3 node --chain`. #189 is the consensus kernel in `crate/src/chain/`: the 168-byte header, proof of work, integer ASERT, the transaction codec shared with the wallet, the state transition over [[bbg]] with an undo journal, a fjall store, the heaviest chain with `MAX_REORG` 119 and veto-only checkpoints, and `soft3 conformance bless|check chain`. its 19 engine scenarios include a 200-block random simulation with conservation checked at every height through a reorg.

#186 is the reference miner, `soft3 mine`, with CPU, Metal and WebGPU backends. the GPU kernels are `hemera_mine` in [[lens]], merged into `release/0.2` the day before. the bench on an M4 Max recorded 3.00 MH/s on 16 CPU threads, 275 kH/s on one, 16.13 MH/s on Metal and 7.02 MH/s on WebGPU. in the integer ASERT simulation a 100× step was absorbed in 192 blocks, 31 minutes.

#187 is the wire of `specs/chain-wire.md`: QUIC through cyber-radio, gossip of headers, transactions and checkpoints, header-first sync, a mempool, discovery and the HTTP routes. a follow-up commit put the wire on the kernel. the three-node harness ran green, with a transaction submitted to node 1, mined by node 2 and visible on node 3.

a rehearsal the same day found two defects, and both were fixed that day. after the first fix the node accepted the raw transaction bytes the wallet sends, and a transfer from `cyber` was admitted and mined at height 16. in [[radio]], `CidQueue::next` was made to wrap its ring index, which ended a panic on re-dial.

## sources

- the kernel: [soft3 #189](https://github.com/cyberia-to/soft3/pull/189)
- the miner: [soft3 #186](https://github.com/cyberia-to/soft3/pull/186) · [lens #28](https://github.com/cyberia-to/lens/pull/28) · the bench receipt [soft3/audit/chain/mine-2026-10-15.md](https://github.com/cyberia-to/soft3/blob/main/audit/chain/mine-2026-10-15.md)
- the wire: [soft3 #187](https://github.com/cyberia-to/soft3/pull/187) · the wire on the kernel [5efc3c3](https://github.com/cyberia-to/soft3/commit/5efc3c38ae817693774be4ff3ace7afe718ee571)
- the rehearsal fixes: soft3 [6043853](https://github.com/cyberia-to/soft3/commit/604385312b9993c5a79927013daeacbead0eb6fa) · radio [4dbfb89](https://github.com/cyberia-to/radio/commit/4dbfb89a152e4c75bdc551aaf9021c5a93fc735c)
