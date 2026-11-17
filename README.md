---
title: cyberia.blog
tags: cyberia
crystal-type: entity
crystal-domain: socio
icon: "📡"
alias: chronicle, the graph, cyberia blog
---
# cyberia.blog

the chronicle of the project, and the place the whole knowledge graph lives.

the homepage is the [[blog]]. filter it by topic: [[cyber]] · [[cyb]] · [[soft3]] · [[cyberia]].

the protocol itself — small, readable, one subject — stays at [cyber.page](https://cyber.page). this site holds the history, the subgraphs, and the graph that binds them.

## local

```
git clone git@github.com:cyberia-to/cyberia-blog.git ~/cyber/cyberia-blog
cd ~/cyber/cyberia-blog
nu scripts/sync.nu        # clone every declared subgraph as a sibling
nu scripts/serve.nu       # full graph at localhost:8888
nu scripts/build.nu       # static build
nu scripts/deploy.nu      # rsync build/ → the front that serves cyberia.blog
```

`optica` is the publisher. the workspace root is this repo; `cyber` is a subgraph mounted at `/cyber`.

## domain

`cyberia.blog` — zone `apparatus/dns/zones/cyberia.blog.zone`: A `@` → the front, CNAME `www` → `cyberia.blog`. nginx: `apparatus/servers/front/nginx/cyberia.blog`. TLS via certbot after DNS answers. tracker: lytics.cyb.ai.

## publish

The Publish workflow builds every public subgraph, writes `build.txt` (run, commit, time) into the build and rsyncs it to the address `cyberia.blog` resolves to; the repo variable `FRONT_HOST` overrides that address once the zone carries more than one A record. It then reads https://cyberia.blog/build.txt, and a run whose stamp the domain does not serve fails. Watch compares the served stamp with the last successful publish every hour. A failure of either opens the issue labelled `publish-failing`; the next verified publish closes it.

## license

cyber license: don't trust. don't fear. don't beg.
