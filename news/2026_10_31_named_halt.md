---
tags: news, soft3, tru
date: 2026-10-31
---
# a settlement panic became a named halt, and release builds check integer overflow

two fixes for the settlement path of the chain merged into `release/phase1` of [[soft3]]. the first settled a decision: a panic during settlement stays a halt. a deterministic panic at `settle(E)` stops every node at once and writes nothing, and a compute hotfix then replays the settlement and pays the epoch. a fallback that marked the epoch unsettled and let the chain continue would lose that epoch's payouts permanently. the settlement worker now catches its own panic and raises it again with a name: the epoch, the height and the original message. the payout check was a debug assertion, compiled out of release builds; it is an error in every build now. the test drives a chain to `settle(1)` = 15 with a panicking focus engine and checks that the tip, the pool and the state root are untouched, that a retry gives the same message, and that a second node fed the same 14 blocks halts identically.

the second turned on `overflow-checks` for the release builds of soft3 and cyber-tru, the crate of [[tru]]. debug builds panicked on overflow and release builds wrapped, so a debug node and a release node could disagree on an overflowing value. the diagnostic ran `cargo test --release --locked` with and without the checks: 294 passed and 0 failed in the library tests on both legs, and no overflow anywhere. the cost measured there is the library tests going from 73.6 s to 86.2 s.

## sources

- the named halt: [soft3 #479](https://github.com/cyberia-to/soft3/pull/479)
- the overflow checks: [soft3 #484](https://github.com/cyberia-to/soft3/pull/484)
