---
tags: news, soft3, bbg, cyber
date: 2026-10-16
---
# bbg dimension version 3: the nonce under the root, deferred hashing, and both burials commit

[[bbg]] #43 made dimension version 3 the genesis version of the root chain and put the 0.3 line on master. `NeuronRecord.nonce` is a `u64`, the fourth neuron value under the root, and `DIMENSION_VERSION = 3` enters every trie leaf. the keyed trie is the dimension leaf, free of the 2^20 cap of the flat commitment. a conviction-free link writes topology only, and a zero balance is an absent row. hashing became deferred: mutations mark keys and trie paths, and the next root read hashes each touched leaf once and each dirty branch once.

the pull request measured it at 100 links per block with a root every block. at 10,000 links the flat root cost 3.96 ms per link, the eager trie of #40 594 µs and the deferred trie 294 µs. at 1,000,000 links the deferred trie cost 687 µs per link with 1.48 GB. chunked Brakedown was measured as an alternative and set aside: about 70 s per block on bostrom's adjacency dimensions against a 30 s target.

[[soft3]] #194 took the nonce under `state_root` and removed the `bbg-nonce` feature with its side map. both burials then committed. bbg #43 records the pussy state root in 2.5 s and 75 MB, and the bostrom root, blocked the day before, in 204 s with a peak of 7.5 GB; `verify --root` reproduced it in 157 s. these roots were computed against hemera 0.3 and moved again with 0.4 the same day.

## sources

- [bbg #43](https://github.com/cyberia-to/bbg/pull/43) · [bbg/audit/dimension-version-3-2026-10-16.md](https://github.com/cyberia-to/bbg/blob/master/audit/dimension-version-3-2026-10-16.md)
- the chain side: [soft3 #194](https://github.com/cyberia-to/soft3/pull/194)
- the record: [cyber #136](https://github.com/cyberia-to/cyber/pull/136)
