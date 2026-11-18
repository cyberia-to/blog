---
tags: news, neural, eidos
date: 2026-10-27
---
# eidos took lean's place in the plan: a roadmap of six milestones, E0 to E5

[[eidos]] gained a roadmap page, `roadmap/replace-lean.md`, merged as pull request #3. it records the owner's call of 2026-10-27: lean is foreign, eidos is native, and whatever eidos lacks to replace lean gets built. the page is eidos's side of a [[soft3]] proposal, the assumptions registry, which was open that day as soft3 #398, a pull request into `main`. the status of the page is proposed.

the ladder has six milestones, each proving something the stack uses. E0 is the axiom file: `eidos axioms <file>` prints every axiom a theorem depends on, and `soft3/proofs/Axioms.ei` holds one axiom per registry entry of classes B, C, E, F, G and H. E1 is the integers of the economy: `Int` with the kernel's bounded `u64` and `u128` semantics, floor division, isqrt and saturation lemmas. E2 is the field and the sum-check: Goldilocks, polynomials, multilinear extensions, and Schwartz–Zippel as a counting bound over the challenge space; its acceptance is that each row of [[zheng]]'s soundness ledger becomes a theorem id. E3 is the zheng bridge: the type check runs on [[nox]], zheng certifies it, and the certificate is a cyberlink in [[bbg]]. E4 adds the random oracle and QROM as axiomatized interfaces with explicit query budgets. E5 is the port: a reader that renders a lean theorem's statement in eidos surface syntax.

the page dates E0 and the E1 entries A-03 and A-05 before 2026-11-02 and places E2 at the first fork window. from the v0.1.0 plan it keeps the TCB split, spans, vectors and docs, and it moves `Int` and the field library ahead of the tutorials, since the first real corpus is the stack's registry.

## sources

- the roadmap: [eidos #3](https://github.com/cyberia-to/eidos/pull/3) · [1a7a057](https://github.com/cyberia-to/eidos/commit/1a7a057b0d404c16c60f86309ad635109d21bd2e) · [roadmap/replace-lean.md](https://github.com/cyberia-to/eidos/blob/main/roadmap/replace-lean.md)
- the proposal: [soft3 #398](https://github.com/cyberia-to/soft3/pull/398) · its triage in [soft3 #399](https://github.com/cyberia-to/soft3/pull/399), merged into `release/phase1`
