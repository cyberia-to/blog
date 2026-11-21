---
tags: news, soft3, lens, zheng, warriors, joy
date: 2026-10-13
---
# the prover runs on Metal and WebGPU and writes the bytes the CPU writes

[[lens]] gained prover backends behind one trait, merged into `release/0.2`. `Backend` carries three operations: `permute`, many hemera states at once; `grind`, the least nonce; and `coset_ntt`. the CPU is the default and a binary installs another. the new crate `cyber-lens-gpu` holds two: Metal, through aruminium of [[honeycrisp]], and WebGPU on wgpu, in WGSL over 32-bit limbs. it builds for wasm32-unknown-unknown and aarch64-linux-android. on a loaded M4 Max, 2^20 permutations took 27–39 ms on Metal against 89–143 ms on 16 CPU threads, and a 24-bit grind 1.4–1.9 s against 5.1–11.6 s.

[[zheng]] routed its recursion through the trait in `release/0.4`: permutation batches of 4096 states and more, grinding, leaf hashing and streamed commitments. [[joy]] exposes the choice as `joy prove --backend auto|cpu|metal|webgpu`, where `auto` takes Metal if it opens, then a WebGPU adapter, then the CPU. `joy prove --succinct hash.tri` took 17.7 s before the backends, 5.5 s on the CPU after, 2.8 s on WebGPU and 1.4 s on Metal, and all four artifacts, 16,308 B each, share one SHA-1.

byte identity served as a test. WebGPU proofs that verified differed from the CPU's in about half the runs; the cause was a missing bounds check in the WGSL `ntt_block` on a ragged grid, fixed in lens with a regression test. a review finding closed with it: the verifier's key derivation had used the installed prover backend, so the admitted key roots are pinned and the verifier's permutation paths run on the CPU whatever backend is installed. after the fixes the wrap chain measured 34.5 s on Metal and 70.5 s on WebGPU, with final proofs byte-identical. [[soft3]] recorded the prover figures in its proof-system-repair proposal.

## sources

- the trait and the devices: [lens #23](https://github.com/cyberia-to/lens/pull/23)
- zheng on the backends: [zheng #59](https://github.com/cyberia-to/zheng/pull/59)
- the command line: [joy #40](https://github.com/cyberia-to/joy/pull/40)
- the WebGPU fault and the verifier paths: [zheng #62](https://github.com/cyberia-to/zheng/pull/62) · [0b05059](https://github.com/cyberia-to/zheng/commit/0b050593da1a844e627cd89f59319561fd277567)
- the figures in the proposal: [soft3 #174](https://github.com/cyberia-to/soft3/pull/174)
