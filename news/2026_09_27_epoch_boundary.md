---
tags: news, foculus, launch
date: 2026-09-27
---
# the epoch boundary is nobody's: row 41 opens on foculus

a read of foculus, the soft3 node, bbg, cybergraph and the tru specs found that every downstream mechanism consumes an epoch index and an epoch boundary — the beacon, settlement depth, the settle and fold windows, the equivocation predicate, tok's per-epoch mint budget, the annuity, bbg's per-epoch archive — and no mechanism produces it. in code the propose window closes when a unit test calls `freeze()` (`src/epoch.rs:90-103`); the only two-node test copies Alice's beacon and claims root into Bob (`src/live.rs:529-540`); the beacon hashes every VDF the node ever ingested with no finality or depth filter (`src/beacon.rs:79-86`); block height is a per-process counter. the specs defer the clock to each other and disagree on its unit (100 blocks, 1000 blocks, 85 s).

the tracker gains property 41: the epoch boundary is a consensus object, two nodes agree on E, R_E and S_E from gossip alone with no state copy, and beacon, settlement, fold, tok and bbg read the boundary and never define it. the gate is a network test that replaces the state copy; the draft spec puts the boundary as a particle finalized by φ*, with the ticket-DAG blue score kept as the alternative. owner foculus, due 2026-10-16, inside the core-spec freeze of 10-09 only if the spec lands first.

## sources

- https://github.com/cyberia-to/cyber/blob/master/launch.md (property registry, row 41)
- foculus/audit/epoch-clock-gap-2026-09-27.md and foculus/specs/epoch.md (on the foculus branch, not yet pushed at the time of writing)
