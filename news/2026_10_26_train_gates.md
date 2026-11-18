---
tags: news, soft3, radio
date: 2026-10-26
---
# the release train builds the pussy genesis file, runs the chain simulator and gives each stack gate its own budget

five pull requests merged into [[soft3]] `release/phase1` changed what the release train checks. #288 made the `stack-chain-genesis` gate run on the build service, where it had always been blocked because no pussy genesis file existed on the runner. `release/phase1.toml` pins space-pussy `main` at `bdcfdaf`; the gate compares the sha256 of the pinned `snapshot/manifest.json` with `source_manifest_sha256` in `conformance/chain-genesis.toml`, then runs `soft3 genesis build --chain pussy` and `soft3 conformance check chain` on the file it built, each with 900 s. a mismatch is red and nothing is built. #242 pinned `cyberia-to/simulation` at `f5a14a1`, which let `simulation-gate` run: the stack target runs the gate suite of the phase-1 chain simulator, 16 gate scenarios.

#298 and #307 replaced the single 900 s budget of the stack gates with a per-gate one: 1800 s for stack-zheng, 1200 s for stack-lens and stack-radio, 900 s for the rest. the command stays `cargo test --locked` and no test leaves a gate; the zheng figure follows a measurement in which one soundness review test took about 985 s alone. #311 put the evidence on the gate that caused it: when a stack test changes its own source tree, that gate turns red, the diff is logged, and the train restores the checkout to its recorded revision.

two fixes for the same gates merged into [[radio]] `release/phase1`. #47 serialized the five `run_in_isolation` mDNS tests behind one mutex, after cross-talk between parallel tests under plain `cargo test`. #49 moved tokio from 1.49.0 to 1.51.5 after an mpsc `len()` underflow failed a proptest; a repeat job failed 1 of 50 at 1.49.0 and 0 of 50 at 1.51.5.

## sources

- the gates: [soft3 #288](https://github.com/cyberia-to/soft3/pull/288) · [soft3 #242](https://github.com/cyberia-to/soft3/pull/242)
- the budgets: [soft3 #298](https://github.com/cyberia-to/soft3/pull/298) · [soft3 #307](https://github.com/cyberia-to/soft3/pull/307)
- the restored tree: [soft3 #311](https://github.com/cyberia-to/soft3/pull/311)
- radio: [#47](https://github.com/cyberia-to/radio/pull/47) · [#49](https://github.com/cyberia-to/radio/pull/49) · the cross-talk reading: [soft3 #258](https://github.com/cyberia-to/soft3/pull/258) · the 50 repeats: [soft3 #310](https://github.com/cyberia-to/soft3/pull/310)
