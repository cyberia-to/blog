---
tags: news, cyber, soft3
date: 2026-09-21
---
# thirty pull requests in three days

the launch has a tracker, [[cyber/launch]], and the tracker has workers. since 2026-09-18 a launchd job on the dev machine ticks every twenty minutes and starts three sonnet workers, one per lane: core, body, content. each reads the property registry, claims an open row, cuts a slice under four hundred lines, verifies it with `cargo test`, and opens one pull request with the commands and their output pasted in. thirty are open across foculus, zheng, tru, plumb, mudra, bbg, radio, cybergraph, file and cyb.

what they found matters more than what they wrote. a fold-mining ticket verifies in 9–19 ms where the spec estimated 10–50 µs, flat in size as promised, three orders of magnitude off in the constant. the settlement ticket publishes every contributor's Shapley marginal in the clear. the signal frame carries the link's content in the clear. valence, the privacy leg of the truth market, leaks on the wire. each of those is now an audit in the owning repository with the file and line, and each points at the same dependency: zheng private execution, which is incomplete.

what they built: the ICBS cost function and its price derivatives, the PoW/PoS allocation split and security floor, per-epoch accrual of the annuity, a home-book token per neuron, the referral birth split with self-referral rejected and a zero payout for Sybil books, transfer under conservation, fold in either order, four attacks on the beacon rejected, MinHash fork choice agreeing across n-way conflicts, gossip relaying across nodes with no direct link, PDF and video and audio sniffed by kind, and a re-addressing of bostrom CIDs to hemera particles with a black hole for the 2.37% without bytes.

none of it is merged. a worker cannot move a registry row; only a merge can.

## sources

- the tracker: [cyber/launch](https://cyber.page/launch), work log at the bottom
- the workers: [scripts/launch-hour.sh](https://github.com/cyberia-to/cyber/blob/master/scripts/launch-hour.sh) and [the prompt](https://github.com/cyberia-to/cyber/blob/master/scripts/launch-hour.prompt.md)
- the open pull requests: [label launch across the org](https://github.com/search?q=org%3Acyberia-to+label%3Alaunch+is%3Apr+is%3Aopen&type=pullrequests)
- the ticket measurement: [foculus #6](https://github.com/cyberia-to/foculus/pull/6); the privacy audits: [zheng #21](https://github.com/cyberia-to/zheng/pull/21), [foculus #12](https://github.com/cyberia-to/foculus/pull/12), [mudra #5](https://github.com/cyberia-to/mudra/pull/5)
