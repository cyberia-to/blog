---
tags: news, soft3, cybernode
date: 2026-11-01
---
# the node left soft3 on the release line: cybernode carries it, soft3 0.11 is the facade

the move of the node, executed on 2026-10-27, landed on `release/phase1` of [[soft3]]. the node code, its tests, `deploy/`, `audit/chain/` and the seven node specs live in [[cybernode]], carved out with 144 commits of history; the pull request records chain, genesis, node, wallet and network as byte-identical. soft3 0.11 is the facade: it re-exports those five modules from cybernode, and its binary forwards the node verbs for one release. cybernode is a sibling in `release/phase1.toml`.

the landing carried one fix. the owner's pull request failed its own drift gate: the ladder page named cybernode as rung 7 while the registry `release/components.toml` still gave that rung to soft3. in the registry cybernode is now the product of layer 7, role network; soft3 is the stack and holds no rung; foculus, radio, sync and solong are parts of cybernode; and the private operations repository is named apparatus. the checker then reported 81 components in the registry, 40 ladder chips, 50 chart nodes and 30 siblings, with no drift.

cybernode's own `release/phase1` took the node work soft3 had added since the carve, ported one for one: the named settlement halt, the overflow checks, the stand on two hosts, pussy's pins and the pussy-rc genesis.

## sources

- the move and its landing, into `release/phase1`: [soft3 #406](https://github.com/cyberia-to/soft3/pull/406) · [soft3 #407](https://github.com/cyberia-to/soft3/pull/407)
- the port, into cybernode's `release/phase1`: [cybernode #2](https://github.com/cyberia-to/cybernode/pull/2)
