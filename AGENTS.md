# AGENTS.md — cyberia-blog

> the doctrine of the home is `~/cyber/AGENTS.md`; it applies here first. Claude Code receives both files at session start through `~/.config/cyber/agents-md.nu`; other agents read them in order.

this repo is the project chronicle and the graph assembler.
[cyber.page](https://cyber.page) is the protocol. this site is the history, the subgraphs, and the graph.

## Git Workflow

- **Commit by default.** After completing a change, commit it.
- **Atomic commits.** One logical change per commit.
- **Conventional commits.** Prefixes: `feat:`, `fix:`, `refactor:`, `docs:`, `test:`, `chore:`.

## What lives here

- `news/` — product news, several a day (`YYYY_MM_DD_<slug>.md`, tags `news, <topic>`). one change, one page, the day it changed. every news item ends with a `## sources` list: the release page, pull request or commit it reports, and the file or receipt every number in the prose comes from; a number without a source does not go in. optica publishes them as `/news/YYYY-MM-DD-<slug>`.
- `blog/` — the daily beat (`YYYY_MM_DD.md`, tags `blog, beat, <topics>`): one entry a day, a line per news item with a wiki-link to it. optica publishes them as `/YYYY-MM-DD`.
- `blog.md` — homepage: the beats. `news.md` — every news item.
- `cyber.md` `cyb.md` `soft3.md` `cyberia.md` — topic hubs. each is also the declaring page for that subgraph, so optica prepends the topic chronicle onto the subgraph README.
- `subgraphs.toml` — the census of the published graph: the top of each tree. a subgraph names its own children in a `subgraphs.toml` at its root (cyberia/subgraphs.toml is the first); optica, `scripts/sync.nu` and the publish clone step read those in turn.
- `scripts/` — sync, build, serve, lock, deploy.

## The daily beat

the chronicle is written once a day, for the UTC day that just ended, from the public record alone.

1. collect. the Beat workflow runs `python3 scripts/beat_collect.py` at 00:07 UTC and commits the digest of the day that ended to the branch `digests` as `YYYY-MM-DD.md`: releases published, pull requests merged and commits on default branches across the public repositories of cyberia-to, every line with its link. by hand the same command, with `--day` or `--since` and `--until`, writes into `~/.cache/cyber/beats/digest/`. the digest is the input; a line that needs its detail is opened at its link.
2. choose. a news item is one change a reader of the project can use or build on: a release, a capability that landed, a spec decision, a measurement, a product or a site going live. a chain of pull requests on one subject is one item. upkeep (formatting, CI, version pins, instruction files synced across the fleet) is a clause in the beat at most. zero to four items a day.
3. write the news. `news/YYYY_MM_DD_<slug>.md`: frontmatter `tags: news, <topics>` and `date: YYYY-MM-DD`; a title that states the change; one to three paragraphs in the past tense; `## sources`. every number, branch name and claim of state is copied from a source in that list. a pull request merged into a branch other than the default one is reported with its branch.
4. write the beat. `blog/YYYY_MM_DD.md`: frontmatter `tags: blog, beat, <topics>` and `date: YYYY-MM-DD`; `# the beat · YYYY-MM-DD`; one sentence for the day; a line per news item, `[[YYYY-MM-DD-slug|the change in a clause]]: one or two sentences`; a closing line for the upkeep when there was any. a beat exists for a day that has at least one news item.
5. deliver. one branch, one commit `docs: the beat · YYYY-MM-DD`, one pull request into master. the owner merges, and the merge publishes.

topics are the hub and the repository: `cyber` · `cyb` (honeycrisp, wysm, prysm, evy, optica, seer) · `soft3` (bbg, lens, mudra, radio, hemera, strata, zheng, cybernode, tru, glia, mir, tok, nox, cybergraph, tade, foculus, soma, neuron, lytics) · `neural` (trident, eidos, inf, nu, rs, rune) · `warriors` (erga, joy, trisha) · `bootloader` (bostrom, space-pussy) · `cyberia` (cyberia, cyber-valley, cyberia-my, cyberstates, blog).

the bounds: public repositories only. personal documents, addresses and payments stay out. a change that exposes an open weakness waits for its fix. plans, moods and deadlines enter only as a source states them.

## Local workflow

```
cd ~/cyber/cyberia-blog
nu scripts/sync.nu
nu scripts/build.nu --public-only
nu scripts/serve.nu
nu scripts/deploy.nu
```

## Writing

state what something is. never define by negation. never use bold. wiki-links for concepts. root terms from the cybergraph: file, particle, cyberlink, neuron, cybergraph.

## Do not touch without discussion

`subgraphs.toml` structure, `publish.toml` site identity, `LICENSE.md`.
