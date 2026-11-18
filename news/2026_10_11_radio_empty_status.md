---
tags: news, soft3, radio
date: 2026-10-11
---
# radio reports the empty file as complete and builds against one pinned hemera revision

two changes merged into [[radio]].

the Fs store already synthesized the canonical empty file on read, while `status` and `has` returned missing until a database row existed. both now return `Complete { size: 0 }` for that root before the lookup, including after a forced deletion. identity, listing, the storage schema and the lookup of nonempty content are preserved. the suite written to fail first had 15 passing tests and 2 Fs failures on the parent, and the candidate passes all 17 in debug and release.

the eight workspace crates that consume [[hemera]] required an adjacent local checkout. they now inherit one exact git revision with their existing `std` and `serde` features, `Cargo.lock` changes only that package's source, and radio resolves without a sibling directory. on the parent with that hemera revision the BAO suite passed 88 cases in debug and in release, and the native nextest run passed 547 tests with 9 skipped in both the default and the no-default variant.

both commits carry the `wip:` prefix because required broad gates stayed red. the first all-feature build error reproduces on the exact parent, and two further commits retain the logs of the hosted runs.

## sources

- the empty file: [radio #36](https://github.com/cyberia-to/radio/pull/36) · [4da5651](https://github.com/cyberia-to/radio/commit/4da5651316382b3d5a58766074a42fa132f60330)
- the pin: [radio #37](https://github.com/cyberia-to/radio/pull/37) · [d90a784](https://github.com/cyberia-to/radio/commit/d90a784fa6a7f410492cc6c6d5242527e221c399) · [audit/2026-10-11-hemera-source-pin](https://github.com/cyberia-to/radio/blob/d90a784fa6a7f410492cc6c6d5242527e221c399/audit/2026-10-11-hemera-source-pin/README.md)
- the retained logs: [80077a7](https://github.com/cyberia-to/radio/commit/80077a76eea1e9fdeff01cfcdf2f858b5825ef93) · [1375da9](https://github.com/cyberia-to/radio/commit/1375da962eb91be6e8791e2c2e5250370a0e0a15)
