---
tags: news, soft3, zheng, warriors, joy
date: 2026-10-10
---
# the proof repair merged into release/0.4: one envelope, a 6.5 KB public certificate, succinct and zk profiles

seven pull requests of [[zheng]] and six of [[joy]] merged into `release/0.4`, carrying phases 1 to 4 of the repair [[soft3]] proposed the day before.

the public profile became certificate v3: it carries only the witness values at non-pinned positions, and the verifier derives the relation from the program and evaluates every row, with no commitment, no challenge and no hash. linear forms, native constants and a degree-7 S-box row took the hash.tri certificate from 295 KB to 15.6 KB; v3 took it to 6,495 B, and add.tri from 2,214 B to 216 B. the folded trace API moved behind the feature `legacy`, whose module doc states the path is unsound, and joy removed the artifact that rode it. one wire format, `ZHENGPF1`, carries the profiles behind a profile byte.

the succinct profile commits the witness, runs Spartan over Fp3 and closes with one opening. the bake-off shipped WHIR at rate 1/64, k = 4, 24 grinding bits: 15,921 B for hash.tri, with the 1 ms verification goal missed. the zk profile, veil, proved the hash of a secret preimage in 63.9 KB, 143 ms to prove and 10.0 ms to verify, against 8.9 MB, 7.3 s and 3.1 s for MPC-in-the-head. phase 3 states the nox machine as one uniform step relation of 64-column rows, its segments accumulated and closed by one decider; 512 statements of hash.tri folded into one. the pull request records that without recursion the constant-size and 1 ms gates are missed.

`joy prove --succinct` writes profile 1 and falls back to the machine, profile 4, beyond one relation, and `joy prove --zk` uses veil where zheng admits the relation, MPC-in-the-head otherwise. the proposal also took a prover goal that day: any device through joy, the same proof bytes on Metal, WebGPU and CPU, in seconds.

## sources

- phase 1: [zheng #45](https://github.com/cyberia-to/zheng/pull/45) · [#46](https://github.com/cyberia-to/zheng/pull/46) · [#47](https://github.com/cyberia-to/zheng/pull/47)
- phase 2, succinct: [zheng #48](https://github.com/cyberia-to/zheng/pull/48) · [audit/succinct-profile-2026-10.md](https://github.com/cyberia-to/zheng/blob/master/audit/succinct-profile-2026-10.md)
- phase 4, zk and state binding: [zheng #49](https://github.com/cyberia-to/zheng/pull/49) · [audit/zk-profile-2026-10.md](https://github.com/cyberia-to/zheng/blob/master/audit/zk-profile-2026-10.md)
- phase 3, machine and accumulation: [zheng #51](https://github.com/cyberia-to/zheng/pull/51) · the documents: [zheng #50](https://github.com/cyberia-to/zheng/pull/50)
- joy: [#32](https://github.com/cyberia-to/joy/pull/32) · [#33](https://github.com/cyberia-to/joy/pull/33) · [#34](https://github.com/cyberia-to/joy/pull/34) · [#35](https://github.com/cyberia-to/joy/pull/35) · [#36](https://github.com/cyberia-to/joy/pull/36) · [#37](https://github.com/cyberia-to/joy/pull/37)
- the prover goal: [soft3 #173](https://github.com/cyberia-to/soft3/pull/173)
