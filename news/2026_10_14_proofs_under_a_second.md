---
tags: news, soft3, zheng, lens, warriors, joy
date: 2026-10-14
---
# device proofs measured under one second: hash.tri in 41 ms, a depth-32 membership in 0.15 s

[[soft3]] added a gate row to its proof-system-repair proposal: every proof a user device produces on the product path takes at most 1 s end to end through `joy prove`, with Metal on Apple Silicon as the gate and the constant-size wrap chain kept off that path. the audit beside it holds the day's measurements.

the one-relation profile of [[zheng]], merged into `release/0.4`, got threaded Spartan sumchecks, a faster relation compiler, a proving key held across proofs, and parameters that take the least grinding that keeps a proof within 64 KB, with at least 128 proven bits at every size. the relation cap rose from 32,768 to 2^20, so Merkle paths of depth 8 to 32 fit one relation. `joy prove` of hash.tri on Metal went from 1.47 s of wall time to 0.07 s, 41 ms of it proving. every product-shaped statement up to Merkle depth 16 came under 1 s, and depth 32 took 1.13 s cold.

a second round closed that gap. the hemera node jet, a nox formula of `hash_node` that the compiler turns into one permutation gadget per Merkle level, brought the depth-32 membership to 0.15 s cold on Metal with a proof of 46,719 B, and [[joy]] runs the same jet in its native check. veil got counter-mode coins and held keys; its membership proofs remain above 64 KB. [[lens]], in `release/0.2`, built commitment trees on the device and cached compiled Metal shaders, taking `Metal::new` from 4.0–4.2 s to 0.15 s with the archive present.

the recursive path moved in the same lines: the IVC step went from 3.45 s to 1.12 s and the wrap chain from 41.3 s to 18.9 s on Metal, with proof bytes identical on CPU, Metal and WebGPU and the 64,213 B bound unchanged.

## sources

- the gate and the audit: [soft3 #175](https://github.com/cyberia-to/soft3/pull/175) · [#178](https://github.com/cyberia-to/soft3/pull/178) · [audit/proof-latency-2026-10.md](https://github.com/cyberia-to/soft3/blob/587b697e41edb454d562d02e4608de5b52106af3/audit/proof-latency-2026-10.md)
- the one-relation profile: [zheng #64](https://github.com/cyberia-to/zheng/pull/64) · [lens #25](https://github.com/cyberia-to/lens/pull/25)
- the node jet, veil and the shader cache: [zheng #66](https://github.com/cyberia-to/zheng/pull/66) · [lens #27](https://github.com/cyberia-to/lens/pull/27) · [joy #42](https://github.com/cyberia-to/joy/pull/42)
- the recursive path: [zheng #63](https://github.com/cyberia-to/zheng/pull/63) · [#65](https://github.com/cyberia-to/zheng/pull/65) · [lens #24](https://github.com/cyberia-to/lens/pull/24) · [#26](https://github.com/cyberia-to/lens/pull/26)
