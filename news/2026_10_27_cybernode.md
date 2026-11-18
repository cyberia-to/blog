---
tags: news, soft3, cybernode
date: 2026-10-27
---
# the node moved out of the soft3 crate into cybernode, with its history

the node got a repository of its own. it was carved out of the [[soft3]] crate into [[cybernode]], steps C2 and C3 of `soft3/proposals/cybernode.md`, the proposal that names rung 7 of the stack: soft3 is the stack and its contracts, cybernode is the node that runs. the carve kept history, 144 commits through `git filter-repo`, and was taken from soft3 `release/phase1` at 5ab03f6, the integration branch.

what moved: the chain, genesis, node and wallet modules, the tests, the deploy tree, the seven node specs and the chain audits. the receipt of the move compares the carved tree with its origin: the 61 files of `rs/src/chain/` and the genesis, node and wallet modules are byte-identical. the differences are the renames. the crate and the binary are `cybernode` 0.1.0, the CLI is the library module `cybernode::cli` so that the soft3 facade can forward its verbs, and the deploy units are `cybernode@<network>` and `cybernode-check`. wire identifiers, genesis files, home directories and env names stayed as they were, since a change to any of them is a consensus change.

the compile proof stayed outside the receipt: it states that on that day the sibling revisions on origin did not yet resolve the node's dependencies, for the new crate and for the soft3 crate it came from alike. later the same day soft3 #414, a plan update merged into `release/phase1`, recorded a diagnostic run that built the node at the head of cybernode #1, a pull request that commits the lock and tests the renamed binary: 314 tests passed, 0 failed. [[cyberia]], [[cyber]] and the blog census took the new name: rung 7 is cybernode, and the operations repository is apparatus.

## sources

- the move: [0594820](https://github.com/cyberia-to/cybernode/commit/059482084eada7a79200a2042e6762d4c40de692) · [cffc728](https://github.com/cyberia-to/cybernode/commit/cffc7282afbd85ddd215552b29e0d7b1681eab75) · [abb8bf1](https://github.com/cyberia-to/cybernode/commit/abb8bf1e9a10516e2c513b3581676e1f6d6e67c0) · [cd13f6c](https://github.com/cyberia-to/cybernode/commit/cd13f6cc8b3385ff43f702e27f42237e3559c0b5)
- the receipt: [52538a6](https://github.com/cyberia-to/cybernode/commit/52538a64ef92e92b421d3b30f62b0148b74019ca) · [audit/move-2026-10-27.md](https://github.com/cyberia-to/cybernode/blob/main/audit/move-2026-10-27.md)
- the proposal: [soft3/proposals/cybernode.md](https://github.com/cyberia-to/soft3/blob/main/proposals/cybernode.md)
- the diagnostic: [soft3 #414](https://github.com/cyberia-to/soft3/pull/414) · [cybernode #1](https://github.com/cyberia-to/cybernode/pull/1)
- the name across the graph: [cyberia 149a33d](https://github.com/cyberia-to/cyberia/commit/149a33dc7162bb0f7efa674f6aedcc8af696264c) · [cyberia 61f0db9](https://github.com/cyberia-to/cyberia/commit/61f0db964a0cee1ef154c51690f5712c62d6a7fd) · [cyber a779d1d](https://github.com/cyberia-to/cyber/commit/a779d1d7b87d1699465a05ba8662ce5a11ff98b6) · [blog 53ad99b](https://github.com/cyberia-to/blog/commit/53ad99b042ee79c60e019d10e0ee79a15baea0be)
