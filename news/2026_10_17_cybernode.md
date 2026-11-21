---
tags: news, soft3, cybernode
date: 2026-10-17
---
# rung 7 got its own name: the cybernode proposal, and a network defined as a repository

two proposals merged into [[soft3]] on an owner request of 2026-10-17 separated the stack from the thing that runs it. `proposals/cybernode.md` starts from one word that named too much: soft3 was the stack, rung 7, the repository, the crate, the binary and the site, and the crate held the chain kernel, genesis, node, wallet and deploy units against the repository's own charter. in the proposal soft3 is the stack and its contracts and never runs; [[cybernode]] is rung 7, one binary that runs network instances as data and owns everything networked; cybernode.ai is the reference instance. the page carries ten decisions, a capability table for [[cyberia]] to run its execution infrastructure on cybernode, and phases C0–C6 with acceptance. the pull request moved no code.

`proposals/network-repos.md` defines a network as one repository holding its contracts, genesis distribution, starting parameters and starting graph, plus a genesis lock, the chain id. it names three: `true-cyber` (CYB), `bostrom` (BOOT) and `space-pussy` (PUSSY). cybernode reads a repository at a pinned revision, builds the genesis deterministically, checks the lock and runs it; the binary knows no network by name.

follow-ups the same day added a fourth type, the home: a neuron's local network, one per unique name, raised from a template kept as a subfolder of cy. its genesis mints the native coin once, in full, to the name's owner: 18,446,744,069,414,584,320 base units, the largest Goldilocks element. an open item records the conflict with a draft that folds true-cyber into cyber and archives the other two repositories.

## sources

- cybernode: [soft3 #219](https://github.com/cyberia-to/soft3/pull/219) · [proposals/cybernode.md](https://github.com/cyberia-to/soft3/blob/3a3972417829830a48f27b3cb3a531e0b8fb9d78/proposals/cybernode.md)
- network repositories: [soft3 #221](https://github.com/cyberia-to/soft3/pull/221) · [soft3 #222](https://github.com/cyberia-to/soft3/pull/222) · [proposals/network-repos.md](https://github.com/cyberia-to/soft3/blob/3a3972417829830a48f27b3cb3a531e0b8fb9d78/proposals/network-repos.md)
- the home: [soft3 #223](https://github.com/cyberia-to/soft3/pull/223) · [soft3 #224](https://github.com/cyberia-to/soft3/pull/224)
