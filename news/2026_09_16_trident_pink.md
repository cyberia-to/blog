---
tags: news, soft3
date: 2026-09-16
---
# trident.pink, rebuilt for 0.3

the landing at [trident.pink](https://trident.pink) was still selling 0.2: a `cargo install` that now pulls an incompatible pair, a 4 ms / 1.3 KB proof from a format joy no longer accepts, an audit transcript the release would not print.

rebuilt tonight against the released binaries. every number on the page was measured with them: public certificate 3 ms and 2.2 KB, private Triton ZK proof 1.6 s and 818 KB, 29 ms on `--target triton`, audit `SAFE` with z3, `UNKNOWN` without it, `UNSAFE` on a false postcondition. install is the native cyber-tools archive with the machine's build picked automatically and a full grid for everyone else. new sections: the three proof modes, what changed in 0.3, the four binaries, the validation receipts. the targets tiers now match the release reference — nox, triton and neptune installed, the other nineteen engines declared — and a scope paragraph carries the release's own limits.

## sources

- the page: [trident.pink](https://trident.pink) — [trident #49](https://github.com/cyberia-to/trident/pull/49), `landing/index.html`
- the binaries the numbers were measured with: [cyber-tools 0.3.0, macOS ARM64](https://github.com/cyberia-to/trident/releases/download/v0.3.0/cyber-tools-aarch64-apple-darwin.tar.gz) (`trident 0.3.0 · trisha 0.3.0 · joy 0.5.0`), on an Apple M4 Max, 2026-09-16; the transcripts on the page are the commands as run
- validation figures on the page: [release-validation.json](https://github.com/cyberia-to/trident/releases/download/v0.3.0/release-validation.json)
- targets tiers: [trident/reference/targets.md](https://github.com/cyberia-to/trident/blob/master/reference/targets.md)
