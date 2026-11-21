---
tags: news, soft3, bbg
date: 2026-10-15
---
# bbg commits a block in O(changes · log n): a keyed trie under every dimension

[[bbg]] #40 changed what a state root costs. the measurement of 2026-09-27 had shown that every root recompute re-encoded and re-hashed every dimension, so the cost of a chain was quadratic in its length. after the merge every committed dimension of `BbgState` is a keyed map: reads go to the `BTreeMap` as before, and every mutation keeps a canonical keyed trie current.

two root versions came out of it. `RootVersion::V1` stayed the default: the flat Brakedown polynomial per dimension, bit-exact with the previous root, recommitted only after a dimension mutates. `RootVersion::V2` is the trie root per dimension, where a block costs O(changes · log n) and a `TrieProof` proves inclusion and non-inclusion against a dimension leaf. a node opts in with `Bbg::with_root_version(RootVersion::V2)`. the pull request names the condition for making v2 the default: [[zheng]] opening trie paths.

the figures are from an M4 Max, one thread, release build, 100 links per block. 10,000 links took 39.6 s before and 5.7 s on v2. 100,000 links took more than an hour before and 69.6 s on v2. 1,000,000 links took 847.8 s on v2 with a peak of 1.94 GB. the pussy snapshot, 29,112 links in 17,696 blocks, ran in 21.0 s and 63 MB on v2.

## sources

- [bbg #40](https://github.com/cyberia-to/bbg/pull/40)
- the table and method: [bbg/audit/commit-cost-2026-10-15.md](https://github.com/cyberia-to/bbg/blob/master/audit/commit-cost-2026-10-15.md)
- the merged commit: [b6b1be1](https://github.com/cyberia-to/bbg/commit/b6b1be13a8961a4b26c3d9338c2fd6284a93a7d3)
