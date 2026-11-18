---
tags: news, soft3, radio
date: 2026-10-12
---
# radio's BAO gained a bounded group hasher and a range cursor in a no_std core

two pull requests gave `cyber-bao`, the BAO crate of [[radio]], a core that works in fixed memory.

`GroupHasher` is a resumable hash of one BAO group with fixed storage and exactly one hash kernel per pending step, so a caller can admit each step against its own work budget. the default-feature APIs keep their behavior. the new no_std surface omits the old I/O, range and traversal APIs, which sets a major compatibility floor for builds without default features, and the unchanged eager traversals moved into a std-gated module. the crate's tests pass 92, 95 and 21 cases in the default, all-feature and no-default configurations, and an isolated consumer for `thumbv7em-none-eabi` is among the checks.

the second pull request adds a checked no_std cursor that walks one byte range in preorder. it is built on a fixed 53-frame stack, and each `next()` returns one intersecting parent or whole-group leaf with no allocation, recursion, eager traversal or hashing. the geometry handles `u64::MAX`, rejects invalid block widths and ranges, and clips the final group by subtraction before a multiplication can overflow. the cursor keeps the complete tree's ROOT position and left-balanced shape. its tests pass 101, 104 and 28 cases in the same three configurations.

the pull requests name what stays separate work: proof parsing and the binding to an authenticated particle or root. both commits carry `wip:` because required broad gates stayed red, the first Clippy error being present on the parent as well.

## sources

- the group hasher: [radio #38](https://github.com/cyberia-to/radio/pull/38) · [82a0a29](https://github.com/cyberia-to/radio/commit/82a0a2931be86e211ba96e5e2188c8b68cf3252d)
- the range cursor: [radio #39](https://github.com/cyberia-to/radio/pull/39) · [24b189e](https://github.com/cyberia-to/radio/commit/24b189ea809d214994a32b78aa65d338c0c2b2b3)
