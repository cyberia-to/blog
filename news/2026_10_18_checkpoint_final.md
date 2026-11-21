---
tags: news, soft3, cybernode
date: 2026-10-18
---
# a held checkpoint is final on every path, and its veto charges no peer

two fixes landed on [[soft3]] main, both found by the chain simulator's nightly suite. the chain spec (chain.md §5.3) says a node with checkpoints enabled treats a checkpointed block as final: it rejects any chain that lacks it.

soft3 #240 closed two paths that let a contradicting chain through. the tip's fast path extended the tip directly and never looked at the checkpoints: in the `reorg-140-checkpoints` scenario a late joiner that held the checkpoint at 120 synced a 60 %-hashrate rewrite straight through height 120. `check_header` now refuses a header at a checkpointed height that differs from the checkpointed block, on whichever path it arrives. the second path was the main chain itself. when a checkpoint arrives after the node is on a chain that contradicts it, the node now retracts below the contradicted height, marks the retracted blocks invalid and moves to the heaviest chain left, within the reorg limit.

soft3 #241 followed from the `partition-long` scenario. after a 2-hour partition healed, minority nodes that had left their branch charged their neighbours +10 for relaying its next blocks, and one node banned another. blocks invalid only for contradicting a held checkpoint are now vetoed: a header that is or descends from one is refused as `ChainError::Checkpoint`, logged and never scored.

both pull requests report the same test run, 285 lib tests passed, 1 ignored and 0 failed, and their simulator scenarios green. the same three commits landed on [[cybernode]] main.

## sources

- the fixes: [soft3 #240](https://github.com/cyberia-to/soft3/pull/240) · [soft3 #241](https://github.com/cyberia-to/soft3/pull/241)
- on soft3 main: [269e2e8](https://github.com/cyberia-to/soft3/commit/269e2e886b670f92f55553cf60fb12d374d8d798) · [4c50586](https://github.com/cyberia-to/soft3/commit/4c505863b207983ff24fddb3453e03fffb1999aa) · [211faa6](https://github.com/cyberia-to/soft3/commit/211faa6518548fddf37a52414b48797ebb947273)
- on cybernode main: [e39de04](https://github.com/cyberia-to/cybernode/commit/e39de04f06752c7868d0b7e0e2fa509bd9c23938) · [9fd1fe8](https://github.com/cyberia-to/cybernode/commit/9fd1fe821e6d93797f9e41308ba864154b7b22df) · [3f63b2f](https://github.com/cyberia-to/cybernode/commit/3f63b2f0410c26ffc3bc7f0f9d9648654d354b0a)
- the simulator's receipt: [simulation 228a4d9](https://github.com/cyberia-to/simulation/commit/228a4d99911d99d6c02f095c61abdd21df9ad2c6)
