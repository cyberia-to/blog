---
tags: news, soft3, bbg, tru, cyber
date: 2026-10-17
---
# the focus economy went into consensus from genesis: staked cyberlinks with valence, 240-block epochs

an owner decision of 2026-10-17 moved the cores out of shadow mode and into consensus at genesis, and the spec, the state layer, the engine and the kernel landed the same day. [[soft3]] gained a normative page, `specs/chain-economy.md`: epochs of 240 blocks with the boundary block id as beacon, settlement applied at boundary + 120 and recomputed by every node. a cyberlink with amount > 0 locks native stake on a card with its valence; transaction kind 6 unlocks after MIN_LOCK (7 days) and kind 7 re-points the payout owner. the focus pool takes min(½, θ^½) of the subsidy.

[[bbg]] moved to dimension version 4: a card record carries owner, particle, author, valence and since, beside reserved stake and focus keys and an axon index. [[tru]] gained the epoch engine: integer-only φ*, syntropy J and the per-axon gradient, PHI_STEPS = 48 from a cold uniform start, the same bits for every thread count. on bostrom (2.85 M axons, 3.06 M particles) φ* took 6.2–6.9 s on one thread of an M4 Max. a second pull request gave every particle a ground weight of a quarter of its in-weight, which made φ* continuous, and replaced the midpoint with four Gauss–Legendre nodes; the median error against exact Shapley on a first or last out-axon fell from 34–45 % to between 0.65 % and 3.03 %.

the kernel implemented the page in `crate/src/chain`: 276 lib tests, a dev net of 4 nodes holding equal epoch records across a fork over a boundary, both genesis files byte-identical with only their roots moved. after the amendment a bostrom settlement took 75 s on one core and 17–19 s on 12. the launch page in [[cyber]] recorded the decision.

## sources

- the decision: [cyber #150](https://github.com/cyberia-to/cyber/pull/150)
- the spec: [soft3 #225](https://github.com/cyberia-to/soft3/pull/225) · [soft3 #227](https://github.com/cyberia-to/soft3/pull/227) · [specs/chain-economy.md](https://github.com/cyberia-to/soft3/blob/b5847850cbaed367fb60b2ab6042945cae9057a1/specs/chain-economy.md)
- the state: [bbg #51](https://github.com/cyberia-to/bbg/pull/51) · [audit/positions-v4-2026-10-17.md](https://github.com/cyberia-to/bbg/blob/a38d9ed86a19bd4cb2afb2c9c62d6a13dd176360/audit/positions-v4-2026-10-17.md)
- the engine: [tru #39](https://github.com/cyberia-to/tru/pull/39) · [tru #40](https://github.com/cyberia-to/tru/pull/40) · [tru #41](https://github.com/cyberia-to/tru/pull/41) · [audit/epoch-settlement-2026-10.md](https://github.com/cyberia-to/tru/blob/fdbe30bc64bbb8e70ae34d41d7ed259a7810893c/audit/epoch-settlement-2026-10.md)
- the kernel: [soft3 #226](https://github.com/cyberia-to/soft3/pull/226) · [audit/chain/economy-2026-10-17.md](https://github.com/cyberia-to/soft3/blob/1bcc0814dcfbc093d788d13259c6a271d25bbf29/audit/chain/economy-2026-10-17.md)
