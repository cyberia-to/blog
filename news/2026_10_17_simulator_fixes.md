---
tags: news, soft3
date: 2026-10-17
---
# the first scenarios of the chain simulator changed the kernel: mempool and sync fixes in soft3 main

a network and economy simulator of the phase-1 chain was being built in the simulation repository: in-process nodes on the real [[soft3]] kernel, on a private test genesis, with a simulated network and a virtual clock. the kernel exposed two additive hooks for it: a `sim` feature that relaxes the proof-of-work limit inside a simulator process only, and `KernelChain::open_with`, which takes an explicit epoch clock, focus engine and settlement mode.

its scenarios then produced a run of pull requests into soft3 main. `flood` (5 nodes, 100 tx/s at the fee floor into one node) counted 792 signature verifications for 16 transactions; a bounded set of 65,536 verified keys brought that to at most 16. the same scenario showed integer fee-per-byte ranking a transfer that paid 1.45× the floor with the flood, so fee rates are now compared exactly, and it showed honest relays banned over nonces that a neighbour one block behind could not place; a stale nonce and a nonce outside the window are no longer charged. with a full pool of 8,192 transactions, re-validation after a tip move took 3,121 ms on the GitHub runner, and it now runs one pass per account. `reorg-140` showed a refused deep fork capturing body sync, which now targets the heaviest chain the node may still move to. `late-join` showed a node below a checkpoint that never downloaded through it. an announcer that cannot serve a body yet is no longer charged, and a new connection now fetches the peer's checkpoints.

the simulator's gate suite was wired into the release train as `simulation-gate`, and every push to soft3 main now dispatches a run to the simulation repository.

## sources

- the simulator: [simulation a4c1aa8](https://github.com/cyberia-to/simulation/commit/a4c1aa8ebc9fcb92b620b3a74ed77d3a755a63a5) · [simulation af2fd01](https://github.com/cyberia-to/simulation/commit/af2fd0167ce5dbe91ce47ab08ad05154086e1447) · [soft3 #228](https://github.com/cyberia-to/soft3/pull/228)
- the mempool: [soft3 #229](https://github.com/cyberia-to/soft3/pull/229) · [soft3 #231](https://github.com/cyberia-to/soft3/pull/231) · [soft3 #232](https://github.com/cyberia-to/soft3/pull/232) · [soft3 #236](https://github.com/cyberia-to/soft3/pull/236) · [soft3 #238](https://github.com/cyberia-to/soft3/pull/238)
- sync and gossip: [soft3 #230](https://github.com/cyberia-to/soft3/pull/230) · [soft3 #233](https://github.com/cyberia-to/soft3/pull/233) · [soft3 #237](https://github.com/cyberia-to/soft3/pull/237) · [soft3 #239](https://github.com/cyberia-to/soft3/pull/239)
- the gate: [soft3 #235](https://github.com/cyberia-to/soft3/pull/235) · [release/train_gates.py](https://github.com/cyberia-to/soft3/blob/12321a381cdb391f0a6690e1e3e450999c05e25b/release/train_gates.py)
