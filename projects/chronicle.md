---
tags: cyberia, blog, project
alias: chronicle, initializing the blog, the history of cyber
kind: project
status: accepted
owner: master
serves: cyberia.blog
lane: contained
---

# the chronicle — initializing the blog

The whole history of the project, from every source, read and told as one chronology: interesting, understandable and connected, with the price of BOOT running alongside it. It becomes the opening of cyberia.blog (the owner, 2026-11-17).

## the sources

| # | source | what is there | how it is read | state |
|---|---|---|---|---|
| s1 | git: every repository of cyberia-to (118) and cybercongress (48) | commits, authors, repositories born, renamed and archived, tags and releases | metadata-only clones (`--filter=blob:none`) into `~/.cache/cyber/chronicle/git`; a script turns them into events | agent, no dependency |
| s2 | this repository: `blog/` (99 posts, 2019-12 → 2026-09) and `news/` (16) | the story already written | read in place; each post becomes an event with its link | agent, no dependency |
| s3 | X, @cyber_devs | the public voice, post by post | the account's archive (X → Settings → Your account → Download an archive): X has no free API, and pages without a login show almost nothing | **the owner's hand**: request the archive today, since X takes up to 24 h to prepare it |
| s4 | Telegram: Cyber Hall of Fame (t.me/fameofcyber, 156 members), Cyber & Bostrom Community (t.me/CyberGlobalHub, 536), Cyberdevs (t.me/cyber_devs, 15), and the others the owner names | the decisions and moods of the core and the community | these are groups, not channels, so their history is not on the public web. Telegram Desktop → the group → ⋯ → Export chat history → JSON, text only; the folders go to `~/.cache/cyber/chronicle/telegram/` | **the owner's hand**: one export per group, plus the list of other groups |
| s5 | YouTube: "Дима Стародубцев", "Дмитрий Стародубцев", the cybercongress channels | talks, interviews, streams with their dates | the YouTube Data API v3 (search, list, captions) with a Google API key, in Python. yt-dlp now needs a JavaScript runtime to read YouTube, which the house does not bring in | agent, needs a Google API key (the owner's, or one the apparatus already holds) |
| s6 | BOOT's price | the market's line under the story | CoinGecko (`bostrom`): the free API gives the last 365 days. The full series is the CSV the coin's page exports (one click in a browser), or a paid plan | agent for 365 days; **the owner's click** for the full CSV |
| s7 | the chains' own dates | launch, genesis, the airdrop, the burial of bostrom and space-pussy | the specs and the burial pages (`snapshot.bostrom.network`) | agent |

The raw material stays private in `~/.cache/cyber/chronicle/`: group chats hold other people's words. The published chronicle quotes only the public voices (posts, talks, commits) and the core's words with their consent.

## how it is made

1. **Events.** Every source gives the same shape: `events.jsonl` lines `{at, source, who, what, link, weight}`. One extractor per source, run in parallel.
2. **Eras.** The events cluster into chapters by time and by subject (names, repositories, chains). A chapter has a title, its years, what happened, the numbers (commits, people, repositories), the voices (quotes with their links), and BOOT across it.
3. **The story.** Each chapter is written as a page in `blog/` (the optica graph) with links to its sources, and one page holds the whole timeline: the chapters as cards over BOOT's price line, with the events as marks on it.
4. **Review and publish.** The owner reads the draft at a preview, and then it goes live on cyberia.blog.

## how it finishes fast

The slow part is waiting, not work, so the waits start first and everything else runs alongside them:

- **Today, the owner's hand** (each one starts a clock): request the X archive (s3); export the three groups and name the others (s4); click the BOOT CSV (s6); say which Google key to use (s5).
- **Today, the agents, in parallel**: s1 git, s2 the blog, s6 the last 365 days, s7 the chain dates. Each one is a script with a receipt, and none of them waits on anything.
- **Draft one** from s1 + s2 + s6 + s7: the skeleton of eras with numbers and price. **Draft two** adds the voices once the X archive and the Telegram exports arrive.

Estimate: agents, about 1 session for s1 + s2 + s6 + s7, 1 session for s5, 2 sessions for eras and story, 1 for the timeline page. The owner, about 15 minutes of clicks today. The critical path is the X archive, about 24 h.

## steps

| # | step | gate | state |
|---|---|---|---|
| 1 | s1 git events from 166 repositories | `events.jsonl` with one line per repository's birth, its monthly commits, its tags; the counts match `gh api` | done 2026-11-17: 2,959 events; own commits are separated from inherited ones (forks, imported histories); receipt `audit/chronicle-git-2026-11-17.md` |
| 2 | s2 the blog and news as events | every post a line with its link | open |
| 3 | s6 + s7 BOOT's series and the chain dates | a daily series; every chain date with its source | open |
| 4 | s3 + s4 the owner's exports read | events with the exports' message ids | waits for the owner |
| 5 | s5 YouTube | every video with its date, title, views; captions for the talks | waits for the key |
| 6 | the eras and the story, draft one | chapters as pages in `blog/` at a preview link | open |
| 7 | the timeline page over BOOT | renders on the desk and the phone at the preview | open |
| 8 | draft two with the voices; the owner's review; publish | live on cyberia.blog | open |
