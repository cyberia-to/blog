---
tags: news, soft3, zheng, lens, warriors, joy
date: 2026-10-13
---
# zheng proved nox runs recursively: one proof of at most 64,213 B, constant in the number of steps

the recursion stack of [[zheng]] merged into `release/0.4` in six pull requests, with its commitment layer in [[lens]] `release/0.2` and its command line in [[joy]] `release/0.4`.

the machine relation now covers every nox opcode, 0 to 17, and every canonical axis address. over it runs IVC: the step relation of a segment proves the segment and that the verifier of the previous step accepted, so the final proof is constant in the number of steps. measured, it stayed at 282–285 KB from 33 cycles to 1.57M cycles. wrap levels then prove the final verifier and brought the proof to 62.5–62.9 KB. a second pass cut the wrap chain from 985 s to 83 s and peak memory from 32–38 GB to 19.5 GB.

the size became a bound. with the final level at 26 grinding bits the outermost proof is at most 64,213 B over every transcript, and a profile-6 envelope stays within 64 KiB whenever its encoded statement takes at most 1,272 B. base-field key columns moved the second level to rate 1/128, the shipped chain `4i:16,7i:22,9f:26`. at merge time `joy prove loop.tri --succinct --wrap` took 45.9 s on Metal and 96.6 s on CPU, its envelope was 63,131 B, and verification took 2.50 ms warm on 16 threads. every ledger row is at least 128 bits, the composition rows of the IVC and the wrap are conjectured, and the 1 ms verification goal is missed.

lens supplied `cyber-lens-rspcs`: WHIR and TensorRs behind one `MultilinearPcs` trait, WHIR over Fp3 tables, and the soundness rows of the batched openings the wrap uses. `joy prove --succinct` writes profile 5, the recursive proof, beyond one relation, and profile 6, the wrapped one, when 14 GiB of memory is available.

## sources

- the machine, the IVC and the wrap: [zheng #52](https://github.com/cyberia-to/zheng/pull/52) · [#53](https://github.com/cyberia-to/zheng/pull/53) · [#56](https://github.com/cyberia-to/zheng/pull/56)
- the speed, the bound and the split key: [zheng #58](https://github.com/cyberia-to/zheng/pull/58) · [#60](https://github.com/cyberia-to/zheng/pull/60) · [#61](https://github.com/cyberia-to/zheng/pull/61)
- lens: [#17](https://github.com/cyberia-to/lens/pull/17) · [#18](https://github.com/cyberia-to/lens/pull/18) · [#19](https://github.com/cyberia-to/lens/pull/19) · [#21](https://github.com/cyberia-to/lens/pull/21)
- joy: [#38](https://github.com/cyberia-to/joy/pull/38) · [#39](https://github.com/cyberia-to/joy/pull/39) · [#41](https://github.com/cyberia-to/joy/pull/41)
- the merge record: [cyber bc1882c](https://github.com/cyberia-to/cyber/commit/bc1882c67313568e602ff2dd13ddcc3bc8eab884)
