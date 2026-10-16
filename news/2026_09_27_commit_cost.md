---
tags: news, cybergraph, bbg, soft3, launch
date: 2026-09-27
---
# the main-line node recommits every dimension per operation: deploy stopped, row 43 opened

an attempt to replace the 0.10.0 spacepussy-test node with the main-line composition (soft3 main plus the four version PR branches) stopped on a measurement. importing a strict prefix of the chaosnet signal log with `import_legacy` took 20 s for 250 events, 67 s for 500 and 194 s for 1,000 on an M4 Max: an exponent near 1.7 and rising toward 2. the stack, sampled with gdb on deimos, is always `prepare_native_batch → refresh_root → commit_fields → hemera`: every accepted operation rebuilds the commitment of every bbg dimension from its full record set. the full 39,060-signal log extrapolates to one and a half to two days; the bostrom genesis replay of 2,949,732 links cannot run on this path at all. the live `POST /v1/link` pays the same, so the main-line node is not deployable at chaosnet size.

the imports on three machines were killed, the 0.10.0 node stays live, and deimos and jupiter keep the log, the binaries and their units ready for the fixed node (deimos already routed at deimos.cybernode.ai/spacepussy-test/). the tracker gained row 43, owned by bbg and cybergraph: accepting a block must cost O(changes · log n), with incremental dimension commitments and a root refreshed once per block; row 14 (genesis replay) is blocked on it.

## sources

- https://github.com/cyberia-to/cybergraph/pull/13
- https://github.com/cyberia-to/cybergraph/blob/master/audit/import-commit-cost-2026-09-27.md
- https://github.com/cyberia-to/cyber/blob/master/launch.md (property registry, rows 14 and 43)
