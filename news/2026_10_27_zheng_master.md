---
tags: news, soft3, zheng
date: 2026-10-27
---
# zheng's 0.4 line landed on master with the proof-system repair

[[zheng]] merged its `release/0.4` line into `master` in pull request #80, by the owner's order of the same day. the line carries crate 0.4.0 and the proof-system repair: profiles 0 to 6, Fp3 challenges, statement binding, a soundness ledger, WHIR, veil, the machine with accumulation, IVC and the wrap. the consistency receipt counts `release/0.4` at 246 commits ahead of `master`. master's own 14 commits were kept, among them AGENTS.md as the single instruction file, the zippel docs with `specs/proto`, and the tade dependency.

the merge came with a sweep of every file of the repository against two [[soft3]] proposals, `proposals/proof-system-repair.md` and `proposals/privacy-frozen.md` §1. on top of the merge sat `cargo fmt`, clippy clean with `-D warnings` on every target and feature, a dev profile at opt-level 3, the CLI moved to `tade`, and rewritten docs, specs, roadmap, changelog and README. the pull request records `cargo test --locked --workspace` at 394 passed, 0 failed and 19 ignored in 518 s, and a link check of 663 links with 0 unresolved.

the pull request also lists what stayed open: the crate pins [[hemera]] 0.3.1 while the move to hemera 0.4 waits in pull requests of its own, and every profile verifies in more than 1 ms. the changelog opens with 0.4.0 as unreleased: carried by `master` since 2026-10-27 and unpublished on crates.io.

## sources

- the promotion: [zheng #80](https://github.com/cyberia-to/zheng/pull/80) · the receipt [audit/consistency-2026-10-27.md](https://github.com/cyberia-to/zheng/blob/master/audit/consistency-2026-10-27.md)
- the commits on the merge: [2633f34](https://github.com/cyberia-to/zheng/commit/2633f348af6069df328b158019d654039dbccf44) · [5a14ae1](https://github.com/cyberia-to/zheng/commit/5a14ae1205fc6e5ac564e06f5badd86cda27ecc4) · [e3b21b4](https://github.com/cyberia-to/zheng/commit/e3b21b484e85eb43665959a713c3a25266f75bbf) · [78f6d94](https://github.com/cyberia-to/zheng/commit/78f6d949e58f93a82604fe04279059e5cc6033b5) · [58e417a](https://github.com/cyberia-to/zheng/commit/58e417a827403bb38083292c24b5188ca907b7b7) · [a076137](https://github.com/cyberia-to/zheng/commit/a0761379378e65b5b8adbfd74c732b131d178de4)
- the documentation sweep: [ab8b0d1](https://github.com/cyberia-to/zheng/commit/ab8b0d1e692082ba1b790c71b64eb1873574d0ca) · [61726aa](https://github.com/cyberia-to/zheng/commit/61726aa92d5f32076b61009680a11f74503dbb25) · [a4b33e9](https://github.com/cyberia-to/zheng/commit/a4b33e9b0fe93f9018e823dacbcf6c6bde5d38ce) · [0e03188](https://github.com/cyberia-to/zheng/commit/0e03188d44364ad60c9a0613f27c9c4c3ada7bd7)
- the changelog: [bddd898](https://github.com/cyberia-to/zheng/commit/bddd898bba285ead0538ea57bf5568d3df67b407) · [CHANGELOG.md](https://github.com/cyberia-to/zheng/blob/master/CHANGELOG.md)
