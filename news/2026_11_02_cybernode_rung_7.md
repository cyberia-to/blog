---
tags: news, soft3, cybernode, cyberia
date: 2026-11-02
---
# the node says its own name: cybernode is rung 7 across the stack

the proposal `proposals/cybernode.md` in [[soft3]] was closed in full on the owner's word of 2026-11-02: a closed proposal means the whole codebase adapted, code, documentation and presentation. an inventory found 59 places across six repositories. two pull requests, both into `release/phase1`, carried the two halves.

in [[cybernode]], everything a reader sees now says cybernode: the deploy runbook and units, the user-visible strings and comments in `rs/`, the verbs and paths of the specs. four files moved in from soft3: `scripts/chain-fleet.nu`, the node operator guide `docs/launch.md`, and the chain audits `block-relation-2026-11.md` and `proof-auth-2026-11.md`. a kept-names note in the README lists what stays for the running hosts: wire identifiers, genesis files, home directories and every `SOFT3_*` environment variable.

in soft3, the home, chart and loop pages of the site put cybernode on rung 7, the proposals registry marks the proposal executed on 2026-10-27, and the release train builds and boots the `cybernode` binary from the sibling checkout. `release/components.toml` describes soft3 as the stack.

the pages of [[cyberia]] followed on main: the projects table says executed, and the operate process points at apparatus, the operations repository that used to carry the cybernode name.

## sources

- the cybernode half: [cybernode #14](https://github.com/cyberia-to/cybernode/pull/14)
- the soft3 half: [soft3 #661](https://github.com/cyberia-to/soft3/pull/661) · the two merges recorded on the same branch in [soft3 #665](https://github.com/cyberia-to/soft3/pull/665)
- the cyberia pages: [7513ff9](https://github.com/cyberia-to/cyberia/commit/7513ff96b26bce3daf8d2b2cd9f2aaa23f3ef2f7) · [a08ae96](https://github.com/cyberia-to/cyberia/commit/a08ae964e24517c591b3719f2d739c322d34cd86)
