---
tags: news, soft3
date: 2026-10-25
---
# the release train rehearses a sibling branch, and its schedule became daily

a director began work on the release line of [[soft3]], and every pull request it merged that day went into the branch `release/phase1`. its first session wrote `release/director/plan.md` and did nothing else. the plan states why the train needs a new tool: soft3 main requires hemera ^0.4, lens ^0.2 with `gpu/`, nox ^0.3, zheng ^0.4 and bbg ^0.3, those crates live on `release/*` lines, and the train reads default branches only.

soft3 #250 gave the train a sibling rehearsal. `train.py snapshot --override NAME=REF` takes a branch, `pull/N/head` or a 40-hex commit for a sibling. the overridden row keeps its default-branch data beside the override's revision, `sources.json` records `overrides` and `rehearsal`, and the release notes are titled `REHEARSAL <verdict> (not a candidate)`. a cut with any override is refused before any network call, and a draft refuses a candidate that carries overrides. the release engine's tests number 27, 9 of them new. the first rehearsal, run 40246391619 with `override=lens=release/0.2`, wrote a snapshot with `rehearsal: true` and the lens row at the head of `release/0.2`.

two smaller steps went into the same branch. the lane labels `contained`, `wide` and `irreversible` were created across the stack, and every open soft3 pull request carries one. the train's cron became `0 12 * * *`, a candidate every day at 12:00 UTC, on the owner's word of 2026-10-24 that the train runs every day. a red gate still makes a red candidate, and the owner still promotes.

## sources

- the plan: [soft3 #248](https://github.com/cyberia-to/soft3/pull/248)
- the rehearsal: [soft3 #250](https://github.com/cyberia-to/soft3/pull/250) · [soft3 #251](https://github.com/cyberia-to/soft3/pull/251)
- the lane labels: [soft3 #249](https://github.com/cyberia-to/soft3/pull/249)
- the daily schedule: [soft3 #246](https://github.com/cyberia-to/soft3/pull/246) · [soft3 #252](https://github.com/cyberia-to/soft3/pull/252)
