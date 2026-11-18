---
tags: news, soft3, zheng
date: 2026-10-17
---
# the proven present: every block is a proven transition whose proof verifies its parents' proofs

[[soft3]] gained a cross-cutting proposal, `proposals/proven-present.md`, for a base property the owner fixed on 2026-10-17. its first version stated that a soft3 state is checked by one constant-size proof in place of a replay of the history that produced it: a node holding the state, its proof and a short suffix is a full validator. it placed the missing work in the block relation and the chain proof, since the constant size is already in the design of [[zheng]] (profile 6 on `release/0.4`: 63,865 B regardless of length).

an owner correction rewrote the page within the hour. the property is per block: every block is a proven transition whose proof verifies its parents' proofs, written as proof-carrying data over the block DAG, with proving first and mining second. the rewrite removed the 120-block cadence and the shadow stage of the first version and listed eleven decisions, among them every block from genesis, proving spread over the DAG, a proof that carries chainwork, and hash-only authorization. it recorded the conflict with `specs/chain.md` §2.7, which authorizes every transaction with NSIG1, secp256k1 ECDSA.

a third pull request recorded the owner's plan for that conflict. PUSSY and BOOT keep ECDSA until their balances are claimed, and their block proofs prove those signatures. CYB has no ECDSA; it launches with claims only, each claim proving a lock or burn against the source chain's proven state. all three pull requests are documents: the page ends in phases S0–S6 with acceptance and a list of open questions.

## sources

- the first version: [soft3 #209](https://github.com/cyberia-to/soft3/pull/209) · [soft3 6b9765d](https://github.com/cyberia-to/soft3/commit/6b9765d857b630b19d4ab72a3ed7e25637411c53)
- the correction: [soft3 #216](https://github.com/cyberia-to/soft3/pull/216) · [soft3 64754e0](https://github.com/cyberia-to/soft3/commit/64754e001d237d56247cb2f12c89f62cbb25b302)
- where ECDSA lives: [soft3 #218](https://github.com/cyberia-to/soft3/pull/218)
- the page: [proposals/proven-present.md](https://github.com/cyberia-to/soft3/blob/ccbf7b78371e6116888e86bfebe34a646cb12fa7/proposals/proven-present.md)
