---
tags: news, zheng, joy, trident
date: 2026-09-27
---
# zheng proves private nox execution natively; joy and trident follow

zheng #35 adds a native private backend, `execution::zk::{prove, verify}`, over the verifier-derived CCS in Goldilocks with hemera hashing: three-party MPC-in-the-head with 219 fixed repetitions, so the interactive soundness bound is (2/3)^219 < 2^-128, with Fiat–Shamir on top. proofs are linear in the admitted circuit and capped at 256 MiB; program, public input and output, dimensions and reduction count stay visible. the release suite reports 219 tests passed, eight of them on the new backend (false-witness forgery, constant and public binding, spliced proofs, an exhaustive small-field comparison against a witness-free simulator).

joy #16 restores private proving inside soft3 on that backend: `divine()` inputs and hidden state queries are proved under `JOYZH001` and verified against public results, program identity, costs and bbg roots without the witness; 151 release tests. trident #106 isolates foreign target resources from soft3 consumers, trident #107 rewrites the references and the self-hosting plan around the profile (joy owns soft3 and cyber; trisha owns triton and neptune), with 1,171 tests green on the documented commit.

all four target the `release/0.4` line; default branches and tags are untouched. this is the self-hosting lane, not a launch core: the fold (row 2) still verifies zheng sampling tickets by folding, and the private backend is a separate, linear-size proof.

## sources

- https://github.com/cyberia-to/zheng/pull/35
- https://github.com/cyberia-to/joy/pull/16
- https://github.com/cyberia-to/trident/pull/106
- https://github.com/cyberia-to/trident/pull/107
- https://github.com/cyberia-to/zheng/blob/94312e72efd91772d69a98bd7a283c124229353c/audit/native-private/README.md
