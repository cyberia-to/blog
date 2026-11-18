---
tags: news, soft3, neural, rs, trident, nox
date: 2026-10-04
---
# the bootstrap order was written down: a reviewed nox seed, then trident, then rs through an interpreter written in trident

one day after the verified bootstrap plan, two documents fixed its order across components. [[soft3]] gained `docs/verified-bootstrap.md`, the page that owns the cross-component order and the trust boundary. the accepted design starts from a reviewed native [[nox]] executor, establishes [[trident]] on it, then establishes a native [[rs]] toolchain through an interpreter of restricted Rs written in trident. those routes build the Rust and the trident implementations of the complete declared stack.

the page names the artifacts of the ceremony: `N_seed`, the reviewed nox executor; `I_rs`, the interpreter, a trident program compiled to `.nox`; `R_first`, the first native Rs compiler obtained by interpreting its own source; and `R_rebuilt`, the same compiler rebuilt by `R_first` from the same frozen recipe. the initial root platform is Linux AArch64, as a design baseline.

rs gained `roadmap/verified-bootstrap.md` with the gates RS0–RS9. it separates two languages. B is the restricted Rs in which the compiler and its whole bootstrap build closure are written; L is the language that compiler accepts, which must grow to the declared full Rust compatibility. the bootstrap interpreter needs to execute B alone, and RS0 freezes the exact B profile.

both pages carry the status accepted for the design and open for the milestone. the soft3 page says the ceremony describes future work, and it lists every VB and RS gate as open.

## sources

- the ceremony: [soft3 commit 647a700](https://github.com/cyberia-to/soft3/commit/647a7004b6727a4ac641ca99aa8f4bbd829db543) · [docs/verified-bootstrap.md](https://github.com/cyberia-to/soft3/blob/647a7004b6727a4ac641ca99aa8f4bbd829db543/docs/verified-bootstrap.md)
- the rs plan: [rs commit 4648872](https://github.com/cyberia-to/rs/commit/464887261a2c90546223d1b7a3a4f3366b19281a) · [roadmap/verified-bootstrap.md](https://github.com/cyberia-to/rs/blob/464887261a2c90546223d1b7a3a4f3366b19281a/roadmap/verified-bootstrap.md)
- the plan it follows, into `release/0.4`: [trident #122](https://github.com/cyberia-to/trident/pull/122)
