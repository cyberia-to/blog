---
tags: news, soft3, cybernode
date: 2026-10-18
---
# the chain simulator merged with three suites: gate, nightly and launch

the chain simulator merged into the repository cyberia-to/simulation: N in-process nodes on the real [[soft3]] kernel, with the real mempool, the real chain-wire frames and the gossip, sync and serve protocol as event handlers. around the nodes sits a simulated network (latency, jitter, loss, bandwidth, partitions, eclipses, crashes with replay from disk, late joiners, clock skew), a deterministic virtual clock, and a mining oracle that grinds valid headers at simulated hashrate shares. adversaries and economy strategies run against continuous invariants, and the output is JSONL metrics with a markdown verdict table.

three suites came with it: `gate` (about 7 minutes on an M4 Max), `nightly`, and `launch`, which runs the pussy and bostrom genesis files at the 2^232 target. the gate suite runs on Linux on every push and pull request of the simulation repository, on every soft3 merge and every six hours. the emergence simulator that the repository already held stays as `simulation emergence`.

the pull request names five kernel bugs found and fixed on soft3 main while the simulator was built, soft3 #229 to #233, [[2026-10-17-simulator-fixes|reported the day before]]. the receipt of the first runs is `audit/network-2026-10.md`, written against soft3 main at 0c6cbb5.

## sources

- the simulator: [simulation #1](https://github.com/cyberia-to/simulation/pull/1)
- the commits of the day: [44f7d57](https://github.com/cyberia-to/simulation/commit/44f7d57282e5c9ccc3fc3bcf03b5cd518873c03d) · [b2e8bf2](https://github.com/cyberia-to/simulation/commit/b2e8bf25959ccb72d20fc6fd3a60c0f1c31570a6)
- the receipt: [228a4d9, audit network-2026-10](https://github.com/cyberia-to/simulation/commit/228a4d99911d99d6c02f095c61abdd21df9ad2c6)
