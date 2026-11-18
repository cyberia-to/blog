---
tags: news, soft3, radio
date: 2026-10-08
---
# radio measured against the specs: a roadmap from 194K lines to about 14K of own code, and a page named cybernet

[[radio]] gained a roadmap page, soft3 radio, that measures the module against what the specs require of it. the count: 194,163 lines of Rust in 497 files, 334 dependency crates for `cyber-radio` alone and 646 for the workspace, forked wholesale from iroh 0.96, with a fork delta in the core transport of +72/−71 lines. the page sorts the tree into three vectors. cut: code with zero consumers and zero spec, about 78K lines and about 250 crates. replace with the stack's own components: about 12K lines. keep, and keep upstream.

the projection is a radio with one verb, transmit: eight modules (endpoint, paths, relay, observe, gossip, stream, fetch, custody) and cyber-bao, about 13,800 lines of own code, with about 80 crates in place of 334. the page calls that fourteen times smaller than the tree it measured. the work is laid out as nine steps, each a pull request against main with a gate that is a test or a measurement: trim, the tade binding, graph addressing, relay through a peer, observe, fetch by particle, the PQ handshake, PLACE frames and custody.

a second page, renamed cybernet the same day, describes the native wire in draft: an address is a neuron or a particle, the route is the locus, every chunk verifies against its particle, and a forwarder emits a signed receipt for every chunk it carries. the roadmap's last section says what the stack is missing to build it.

## sources

- the roadmap: [radio 4e772c9](https://github.com/cyberia-to/radio/commit/4e772c966e311d226d93e50982fa88ce5d1eff24) · [3139440](https://github.com/cyberia-to/radio/commit/31394405b8f9ee5b6310f36e5e80ad2736083316) · [e6ebafc](https://github.com/cyberia-to/radio/commit/e6ebafc316f85f95be1d090dcd9405c84aa70611) · [b5dd740](https://github.com/cyberia-to/radio/commit/b5dd740e5ebf240ea4ed43d6c28466f4bb785ab5)
- the page and its counts: [roadmap/soft3-radio.md](https://github.com/cyberia-to/radio/blob/aa897e7f1596a0f300198d40318131507578814d/roadmap/soft3-radio.md)
- cybernet: [radio ab5b219](https://github.com/cyberia-to/radio/commit/ab5b219c85a1d7e766257d2a5cc33a258c2d37aa) · [aa897e7](https://github.com/cyberia-to/radio/commit/aa897e7f1596a0f300198d40318131507578814d) · [docs/explanation/cybernet.md](https://github.com/cyberia-to/radio/blob/aa897e7f1596a0f300198d40318131507578814d/docs/explanation/cybernet.md)
