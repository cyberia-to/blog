---
tags: news, soft3, cyber
date: 2026-10-16
---
# privacy, frozen: one pool, one proof, one material, and the pool's formats fixed at genesis

[[soft3]] gained `proposals/privacy-frozen.md` in answer to an owner question of 2026-10-16: a privacy scheme efficient on the present harness, quantum-safe, programmable over outputs, serving consensus and frozen at launch. the page takes twelve decisions, among them one material (hemera), ML-KEM for note delivery only, one shielded pool of records, predicates as programs and one proof per block. it states the SPEND relation, what freezes at genesis and what switches on as rule set 2, and three gates: G1 a hash-only zero-knowledge proof of at most 64 KB, G2 in-block aggregation of transaction proofs, G3 the cryptanalysis of hemera.

a second draft written the same day was reconciled into the page by two further pull requests. the resolution: genesis freezes the material, the supply and the pool's formats; the SPEND relation and its verifying keys are pinned at the activation height of rule set 2 and stay fixed from then on. decision 13 was added, and gates G4 to G7 (leakage model, lifetime security, secret inputs held by many neurons, network anonymity) joined the list.

soft3 #193 wrote the frozen formats into `specs/chain.md` §11: 64-byte wide digests, a 296-byte record, a depth-40 tree, an anchor window of 1,000 blocks, a lifetime nullifier set, transaction kinds 4 (deposit, 384 B) and 5 (spend, at most 9,985 B) and a 74-byte pool record at the end of the genesis params frame. rule set 1 rejects kinds 4 and 5. `conformance/chain.snap` grew from 9 to 30 entries. [[cyber]]'s launch page recorded the consequence: the chain is public until rule set 2 activates, and privacy holds from that height on.

## sources

- the proposal: [soft3 #188](https://github.com/cyberia-to/soft3/pull/188) · [soft3 #191](https://github.com/cyberia-to/soft3/pull/191) · [soft3 #192](https://github.com/cyberia-to/soft3/pull/192) · [soft3/proposals/privacy-frozen.md](https://github.com/cyberia-to/soft3/blob/main/proposals/privacy-frozen.md)
- the formats: [soft3 #193](https://github.com/cyberia-to/soft3/pull/193) · [soft3/specs/chain.md](https://github.com/cyberia-to/soft3/blob/main/specs/chain.md)
- the record: [cyber #135](https://github.com/cyberia-to/cyber/pull/135)
