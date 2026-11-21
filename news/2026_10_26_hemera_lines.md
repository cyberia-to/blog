---
tags: news, soft3, hemera, nox, lens, bbg, tru, tok, zheng
date: 2026-10-26
---
# hemera 0.4 reached the release lines of nox, lens, bbg, tru, tok, file and rune

the dependents of [[hemera]] moved onto its 0.4 profile on their release lines, under the plan of the [[soft3]] release director. in [[nox]], #31 merged into `release/0.4`: the profile has 6 + 6 full and 48 partial rounds, the hash pattern emits one row per round plus the squeeze row, and its cost moved from 25 to 61. every dependent budget followed: the merkle_verify jet budget became depth × 61, and the spec figure for zheng constraints per permutation went from ~736 to ~1,440. a test pins `HASH_COST` against `hemera::ROUNDS_TOTAL`. #42 then synced master (30 commits, 19 conflicts resolved) into `release/0.4` and gave nox its first pull-request CI.

in [[lens]], #37 merged into `release/0.2` with master synced in, #31's `cyber-hemera` 0.3 → 0.4 and GPU kernels on the new profile, and a CI that lays out lens beside strata and hemera. three stacked pull requests had merged into its branch `sync/master-into-release-0.2` first: #38 fixed a WHIR cheating-prover test that tripped the honest prover's debug self-check before the verifier ran, #39 ran fmt and clippy over the line, and #40 built tests at opt-level 3 so the train's `stack-lens` gate fits its 900 s.

[[bbg]] #52, [[tru]] #43, plumb #23 (tok), file #39 and rune #8 merged into `release/phase1` of their repositories, each on cyber-hemera 0.4 with a CI on the train's stand that runs the train's gate command, `cargo test --locked`. the [[zheng]] sweep stayed on the branch of its open pull request #73, `ci/hemera-0.4-sweep`, where #74 (fmt and clippy) and #76 (the tape → tade rename in the cli) merged. of the 27 tests that failed there under hemera 0.4, 26 passed after the sweep; the one left was the 64 KiB gate on the wrapped proof.

## sources

- nox: [#31](https://github.com/cyberia-to/nox/pull/31) · [#42](https://github.com/cyberia-to/nox/pull/42)
- lens: [#37](https://github.com/cyberia-to/lens/pull/37) · [#31](https://github.com/cyberia-to/lens/pull/31) · [#38](https://github.com/cyberia-to/lens/pull/38) · [#39](https://github.com/cyberia-to/lens/pull/39) · [#40](https://github.com/cyberia-to/lens/pull/40)
- `release/phase1` lines: [bbg #52](https://github.com/cyberia-to/bbg/pull/52) · [tru #43](https://github.com/cyberia-to/tru/pull/43) · [plumb #23](https://github.com/cyberia-to/plumb/pull/23) · [file #39](https://github.com/cyberia-to/file/pull/39) · [rune #8](https://github.com/cyberia-to/rune/pull/8)
- zheng: [#73](https://github.com/cyberia-to/zheng/pull/73) · [#74](https://github.com/cyberia-to/zheng/pull/74) · [#76](https://github.com/cyberia-to/zheng/pull/76) · the 27 and the 26 of 27: [soft3 #270](https://github.com/cyberia-to/soft3/pull/270), [soft3 #271](https://github.com/cyberia-to/soft3/pull/271)
