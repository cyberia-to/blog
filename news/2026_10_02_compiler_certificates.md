---
tags: news, warriors, soft3, neural, joy, zheng, nox, trident, trisha
date: 2026-10-02
---
# joy certifies complete compiler executions and zheng checks them without running nox: SH7 accepted

a chain of merges on the `release/0.4` branches gave the self-hosted compiler a proof route. [[zheng]] gained four experimental components (#40 to #43): a verifier-owned table that authenticates disclosed noun memory, admission of noun values without repeated metadata, a check of successful pure nox evaluations as finite derivation DAGs, and verification of disclosed execution across complete noun-table resets, with a bounded activation stack and a fixed cache of locally verified summaries. [[nox]] #26 added an opt-in version-2 observer that reports an arena reset followed by the complete resident arena. [[joy]] #25 bounded the transport: ordered 64 KiB frames bound to their context, with strict bounded DEFLATE decoding.

on top of these, joy #26 added two commands. `prove-artifact` records a public native certificate of a complete ART1/JOB1/RES1 execution. `verify-artifact` checks the expected program and input, the full result, the charged reductions and the expanded logical work through zheng, without running nox or a compiler. joy #27 allowed an explicitly selected host deadline of up to four hours for whole compiler proofs, the default staying at 30 seconds.

[[trident]] #116 then recorded SH7 as accepted: the unchanged C2 compiled the SH3 fixtures and the exact 64 KiB SH4 source through joy and nox with fresh certificate verification, three rebuilt-chain controls passed, and 24 altered inputs and certificates were rejected. [[trisha]] #21 added a gate for the public proof profile on six native platforms. SH8, the certificates of the complete self-build, was kept open by the same pull request.

## sources

- zheng, into `release/0.4`: [#40](https://github.com/cyberia-to/zheng/pull/40) · [#41](https://github.com/cyberia-to/zheng/pull/41) · [#42](https://github.com/cyberia-to/zheng/pull/42) · [#43](https://github.com/cyberia-to/zheng/pull/43)
- nox, into `release/0.4`: [#26](https://github.com/cyberia-to/nox/pull/26)
- joy, into `release/0.4`: [#25](https://github.com/cyberia-to/joy/pull/25) (64 KiB frames) · [#26](https://github.com/cyberia-to/joy/pull/26) (`prove-artifact`, `verify-artifact`) · [#27](https://github.com/cyberia-to/joy/pull/27) (deadlines)
- the acceptance, into `release/0.4`: [trident #116](https://github.com/cyberia-to/trident/pull/116) (three controls, 24 rejections)
- the six-platform gate, into `release/0.4`: [trisha #21](https://github.com/cyberia-to/trisha/pull/21)
