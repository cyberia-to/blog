---
tags: news, soft3
date: 2026-10-08
---
# the chart on soft3.org draws 133 wires from the Cargo manifests, and the loop has seven verbs

two pages of [[soft3]]'s site changed in substance. the chart's wires became real: #122 derived 133 wires from every Cargo.toml across the component repositories, path dependencies and the project's published crates, with dashed wires for parts that are specified and have no crate. #126 then diffed every edge against every manifest. it removed nu→rune (nu-ansi-term is a different project from the nu repository), cyb→cyber (cyber has no cyb dependency) and three wires into cyber that were dev-dependencies only. it demoted radio→foculus to specified, because foculus uses upstream iroh 0.96, and it added five wires, among them soft3→cyber, which the pull request calls the only real dependency of cyber. the chart shows direct wires: joy reaches lens through zheng and nox, so joy→lens stays absent.

the loop grew from three verbs to seven in six merges (#133 to #138), one verb per product in rung order and in the seven colours of the flag: COMPUTE (nox), BUILD (trident), PROVE (joy), REMEMBER (cybergraph), LEARN (neural), LINK (cy), FOCUS (soft3). every caption follows one grammar, A becomes B with one property, and each arrow names the one thing it carries to the next verb. a written draft of the loop was merged as #131 and reverted as #132 at the owner's request, the loop being drawn on the site.

around these, #118 and #120 made the pages one continuous world: a seeded scene with a session clock, internal links that swap the main element under a cross-fade, and a fixed menu that marks the current page.

## sources

- the wires: [soft3 #122](https://github.com/cyberia-to/soft3/pull/122) (133 wires) · the audit [#126](https://github.com/cyberia-to/soft3/pull/126) · one font size [#128](https://github.com/cyberia-to/soft3/pull/128)
- the loop: [#133](https://github.com/cyberia-to/soft3/pull/133) · [#134](https://github.com/cyberia-to/soft3/pull/134) · [#135](https://github.com/cyberia-to/soft3/pull/135) · [#136](https://github.com/cyberia-to/soft3/pull/136) · [#137](https://github.com/cyberia-to/soft3/pull/137) · [#138](https://github.com/cyberia-to/soft3/pull/138)
- the draft and its revert: [#131](https://github.com/cyberia-to/soft3/pull/131) · [#132](https://github.com/cyberia-to/soft3/pull/132)
- one world across pages: [#118](https://github.com/cyberia-to/soft3/pull/118) · [#120](https://github.com/cyberia-to/soft3/pull/120) · [#121](https://github.com/cyberia-to/soft3/pull/121)
