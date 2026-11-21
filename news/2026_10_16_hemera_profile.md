---
tags: news, soft3, hemera, zheng, lens, nox, cybergraph, cyber
date: 2026-10-16
---
# hemera 0.4: x⁷ in every round, and the stack re-derived on it

the cryptanalysis campaign on [[hemera]] opened with `audit/campaign.md` and a public summary page in [[cyber]]. the campaign states the exact object, the claims with numbers, an attack map with margins computed for two profiles side by side, the bounty tiers, the review plan and the pass criterion, and it recommended freezing the permutation of profile #15. the decision of 2026-10-16 in the launch page took the recommendation: genesis freezes profile #15 as hemera 0.4.

hemera #21 merged the new version into `release/0.4`, with `main` staying on 0.3 and promotion left to the owner. 0.3 ran x⁷ in the full rounds and x⁻¹ in the partial rounds, 4+4 full and 16 partial, with 144 constants. 0.4 runs x⁷ in every round, 6+6 full and 48 partial, with 240 constants and the Poseidon2 reference matrices; width, rate, capacity and the 32-byte digest are unchanged. the permutation changed, so every output changed. on an M4 Max a single permutation went from 2.97 µs to 1.35 µs, and the batched path from 0.73 µs to 1.23 µs per permutation.

the sweep followed the same day. the specs of [[zheng]] and [[nox]] on their `release/0.4` branches, [[lens]] on `release/0.2`, [[soft3]], [[cybergraph]], cybics and the cyber whitepaper quote the profile and its cost: about 1,440 zheng constraints per permutation against about 736. soft3 #198 moved the chain to 0.4: every pinned digest was re-derived, the conformance header was re-mined at nonce 934,636, all 30 entries of `chain.snap` moved, and both genesis files were rebuilt, bostrom in 327 s with 5.9 GB.

## sources

- the campaign: [hemera #20](https://github.com/cyberia-to/hemera/pull/20) · [hemera/audit/campaign.md](https://github.com/cyberia-to/hemera/blob/main/audit/campaign.md) · [cyber #133](https://github.com/cyberia-to/cyber/pull/133) · [cyber/hemera cryptanalysis.md](https://github.com/cyberia-to/cyber/blob/master/hemera%20cryptanalysis.md)
- the decision: [cyber #134](https://github.com/cyberia-to/cyber/pull/134)
- the profile: [hemera #21](https://github.com/cyberia-to/hemera/pull/21) · the receipt [hemera/audit/profile-0.4-2026-10.md](https://github.com/cyberia-to/hemera/blob/release/0.4/audit/profile-0.4-2026-10.md)
- the sweep: [cyber #137](https://github.com/cyberia-to/cyber/pull/137) · [zheng #68](https://github.com/cyberia-to/zheng/pull/68) · [lens #30](https://github.com/cyberia-to/lens/pull/30) · [nox #32](https://github.com/cyberia-to/nox/pull/32) · [soft3 #197](https://github.com/cyberia-to/soft3/pull/197) · [cybergraph #18](https://github.com/cyberia-to/cybergraph/pull/18) · [cybics #3](https://github.com/cyberia-to/cybics/pull/3)
- the chain on 0.4: [soft3 #198](https://github.com/cyberia-to/soft3/pull/198) · [cyber #138](https://github.com/cyberia-to/cyber/pull/138)
