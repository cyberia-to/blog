# chronicle, source s1 — git, 2026-11-17

`scripts/chronicle_git.py` over every repository of cyberia-to and cybercongress (projects/chronicle.md, step 1). The events are at `~/.cache/cyber/chronicle/git/events.jsonl`, which stays private because it includes private repositories.

- 166 repositories, 2959 events, 0 failed.
- The team's own commits on default branches, merges excluded: **22,015**. Inherited: **43,445**. Inherited covers 15 forks carrying their upstream (cosmos-sdk 12,523, cometbft 9,136, space-pussy 3,217, wasmd 947), plus histories imported with code, meaning commits older than the repository itself (nu 10,071, radio 2,220, wysm 1,363). Inherited months stay as events marked `inherited` and are never counted as the team's work.
- "repos born" is the year of a repository's first commit; for a fork, that is its upstream's.

| year | org | own commits | inherited | repos born |
|---|---|---|---|---|
| 2014 | cybercongress | 0 | 233 | 1 |
| 2015 | cybercongress | 0 | 768 | 0 |
| 2016 | cybercongress | 0 | 686 | 1 |
| 2017 | cybercongress | 459 | 3236 | 2 |
| 2018 | cybercongress | 1306 | 5069 | 7 |
| 2018 | cyberia-to | 544 | 441 | 5 |
| 2019 | cybercongress | 1355 | 2443 | 16 |
| 2019 | cyberia-to | 807 | 1970 | 2 |
| 2020 | cybercongress | 942 | 3269 | 8 |
| 2020 | cyberia-to | 797 | 1751 | 0 |
| 2021 | cybercongress | 280 | 1897 | 2 |
| 2021 | cyberia-to | 571 | 2031 | 2 |
| 2022 | cybercongress | 68 | 2261 | 4 |
| 2022 | cyberia-to | 284 | 2371 | 0 |
| 2023 | cybercongress | 21 | 2405 | 0 |
| 2023 | cyberia-to | 679 | 3589 | 2 |
| 2024 | cybercongress | 95 | 3476 | 7 |
| 2024 | cyberia-to | 987 | 2801 | 4 |
| 2025 | cybercongress | 1 | 0 | 0 |
| 2025 | cyberia-to | 1412 | 2203 | 4 |
| 2026 | cyberia-to | 11407 | 545 | 99 |

Open for the synthesis: a repository moved between organizations keeps its GitHub creation date, so its older commits may be the team's own yet counted as imported. Identifying the core authors (by name and email across the years) settles this.
