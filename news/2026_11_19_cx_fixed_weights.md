---
tags: news, cyberia, cx
date: 2026-11-19
---
# the century index moves to fixed weights with a death rule, and the rent machine is retired

cx #1 rewrote the century index from fixed quantities to fixed weights rebalanced daily. the index is I(t) = I(t−1) · Σ wᵢ · P̄ᵢ(t)/P̄ᵢ(t−1) with I(2022-01-07) = $1: each day CX earns the weighted return of its legs at trailing-average prices. a mechanical death rule removes a leg from the basket the day its 365-day average closes below 10% of its peak average since the base date. the remaining weights scale pro rata, and a dead leg never returns. the level is carried at 1e-18 between days, and the daily factor divides by the living weight itself, never by rounded pro-rata weights. the same pull request retires the rent machine that sat over the index, as a second owner decision resting on the same path.

the follow-up commits closed the review of that pull request. the two longest source files split into modules, each with its own tests, so every file in the crate is under the 500-line limit. the level in the doc comment now reads $1.31, which is what the rebalanced index produces and what history.md publishes. the generated record, the committed one and the specification point at cx.cyberia.my, and the published page links its data as /cx.json, the path that host serves. tests for the publication were added.

## sources

- https://github.com/cyberia-to/cx/pull/1
- https://github.com/cyberia-to/cx/commit/b5cbdc98cab362199a6f29002e8c2cad287f4676
- https://github.com/cyberia-to/cx/commit/ef8380de834051f0afb3c72f58f410cba098a44b
