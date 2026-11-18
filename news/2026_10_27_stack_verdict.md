---
tags: news, soft3
date: 2026-10-27
---
# the release train gave its first full stack verdict on soft3's release line

[[soft3]]'s release train judged the whole stack for the first time, in rehearsal 40446879208 on `release/phase1`. three fixes merged into that branch came first, and a fourth merge took its pins from the run.

the stack leg got its own job cap (#368): 210 minutes, with the four platform legs kept at 90. the rehearsal before it had been cancelled at the 90-minute cap inside simulation-gate, after 5401 s, and gave no verdict. under the new cap the stack leg ran 6501 s, 108.4 minutes, and reported 24 gates summing to 6478.0 s. simulation-gate was green with 16 scenarios and 0 failures in 961.7 s, and conformance-snapshot, chain-genesis, soft3-tests, soft3-release and node-status were green. the verdict itself was red, on five gates (#375).

the conformance snapshot was ported to [[zheng]] 0.4 (#362), against which it had stopped compiling with 8 errors. the zheng surface now fingerprints the production wire format `ZHENGPF1`: the same four programs proven under profile 0 and profile 1, with a verify verdict on the committed fixture plus nine one-bit tamperings. the re-bless on [[hemera]] 0.4 gave 169 changes.

the miner's backend probe was corrected (#358). the CPU search stops at its first hit, about 2^10 hashes, and had been credited with 2^14, which overstated the CPU rate about 16 times and pushed the automatic choice toward the CPU. the probe now rates the CPU on the hashes it did. the 11 phase-1 leaves in `release/phase1.toml` were then pinned to the default-branch heads the rehearsal had captured (#373).

## sources

- the cap and the verdict: [soft3 #368](https://github.com/cyberia-to/soft3/pull/368) · [soft3 #375](https://github.com/cyberia-to/soft3/pull/375)
- the conformance snapshot: [soft3 #362](https://github.com/cyberia-to/soft3/pull/362)
- the probe: [soft3 #358](https://github.com/cyberia-to/soft3/pull/358)
- the pins: [soft3 #373](https://github.com/cyberia-to/soft3/pull/373)
