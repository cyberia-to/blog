---
tags: news, soft3, radio, nox
date: 2026-10-13
---
# radio verifies a BAO buffer in bounded steps before it exposes the payload, and nox compiles for a thumb target

[[radio]] added a verifier on top of the group hasher and the range cursor merged the day before. it is a no_std verifier of a complete buffer: it exposes a sealed borrowed view of the payload only after the canonical hash checks, all selected groups and the exact end of input succeed. verification and output each advance by one bounded action, reusing the merged traversal and the group reducer. the result is conditional on a trusted complete root and length supplied by the caller, and particle authority and range publication remain separate work. the change is three production paths and four focused test files, and the focused tests pass 18 cases in each of four combinations. the API is additive, with no breaking findings against the parent.

a second pull request made radio consumable through git. seven archived harness manifests had let Cargo discover a duplicate `cyber-bao`. they were renamed from `Cargo.toml` to `.txt`, and three replay wrappers rebuild the historical layout in disposable directories. production Rust, source manifests, locks and versions are unchanged.

[[nox]] closed a matching edge for embedded builds. its default dependency features enabled hemera's `std` even when nox was built with its own default features off. hemera's defaults are now disabled and nox's `std` feature forwards to `hemera/std`, with a build gate for `thumbv7em-none-eabi`: the parent fails code generation there at hemera's `extern crate std`, and the candidate passes. workspace tests pass 161 cases in each of debug, release and std.

the three commits carry `wip:`, with required broad gates still red in both repositories.

## sources

- the verifier: [radio #40](https://github.com/cyberia-to/radio/pull/40) · [7b7d8b6](https://github.com/cyberia-to/radio/commit/7b7d8b6d9a14e9c552d9d1f193cc323de85e9f46)
- the manifests: [radio #41](https://github.com/cyberia-to/radio/pull/41) · [137cf86](https://github.com/cyberia-to/radio/commit/137cf86575b62675e7ab23e5a36288cb236eae88)
- nox: [nox #30](https://github.com/cyberia-to/nox/pull/30) · [75cb8eb](https://github.com/cyberia-to/nox/commit/75cb8ebe8fb1a493c8bcd46fd35801a37105c311)
