---
tags: news, cyberia, cyber-valley
date: 2026-09-29
---
# cyber valley published its leasehold pages: the design code, the lease template, glossary, laws and annexes

the [[cyber-valley]] subgraph gained a `products/leasehold` folder, and the pages a holder of the 25-year hak sewa reads sat in one public place from that day. the design code moved there from an unmerged policies branch: the page that says what is built on a plot and how, binding on every holder, every zone and every assignee. beside it went the signable lease template, the full text every holder signs, with the same lease in its short form and the Indonesian notarial form. the folder index lists them next to the instrument page and the rates page.

the reference layer the template rests on moved into `legal/`: 36 glossary terms under `legal/terms`, 9 statute pages under `legal/laws` and Annexes A–G under `legal/annexes`. the cascade rewrote every path link to the old locations, and a follow-up restored the products index and relinked 11 references to the design code. a fourth merge brought the policies pages and the referral system page that the published design code links to.

the fifth merge gave the repository the same 9-line workflow that [[cyberia]], [[optica]] and [[cyb]] carry: every push to main dispatches a rebuild of the subgraph on cyberia.blog.

## sources

- the design code: [cyber-valley #3](https://github.com/cyberia-to/cyber-valley/pull/3) · [#4](https://github.com/cyberia-to/cyber-valley/pull/4) · [commit e8909a3](https://github.com/cyberia-to/cyber-valley/commit/e8909a330e7a8c4cbc5968933aa209432b80f004) · [commit fee64ac](https://github.com/cyberia-to/cyber-valley/commit/fee64acde9deddf30a88eef7a29fc230aa14593f)
- the template, glossary, laws and annexes: [cyber-valley #5](https://github.com/cyberia-to/cyber-valley/pull/5) · [commit da9f639](https://github.com/cyberia-to/cyber-valley/commit/da9f6390f1ce7da001a7c81dc5a3414b0cf0fc99) (36 terms, 9 statute pages, Annexes A–G)
- the folder index: [products/leasehold/README.md](https://github.com/cyberia-to/cyber-valley/blob/da9f6390f1ce7da001a7c81dc5a3414b0cf0fc99/products/leasehold/README.md)
- the policies pages: [cyber-valley #6](https://github.com/cyberia-to/cyber-valley/pull/6)
- the notify workflow: [cyber-valley #7](https://github.com/cyberia-to/cyber-valley/pull/7) · [commit e27c723](https://github.com/cyberia-to/cyber-valley/commit/e27c7234b3c569d95d58ed82fe5785e2a057e8bb)
