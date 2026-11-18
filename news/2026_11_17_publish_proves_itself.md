---
tags: news, cyberia
date: 2026-11-17
---
# cyberia.blog publishes again, and every publish proves itself

from 2026-10-29 to 2026-11-17 every publish of this site failed at the deploy step and nobody saw it. the workflow rsynced to a hard-coded address of a host that had since been retired, and cyberia.blog kept serving the 29 October build from front-primary. blog #6 pointed the deploy at front-primary on port 22, where the existing key is authorised for the user that owns the docroot; front-secondary pulls from front-primary every 2 minutes, so both edges receive the build.

blog #7 made the failure visible. the deploy now follows the domain: the target is the address cyberia.blog resolves to, the repository variable `FRONT_HOST` overrides it, and the deploy refuses to guess when the zone returns more than one A record. each build carries a stamp, `build.txt`, holding the run id, the commit and the build time; after the rsync the run reads https://cyberia.blog/build.txt and fails unless it serves this run, which also catches an rsync that lands on a host the domain no longer serves.

the same day blog #9 added the first half of the daily loop that writes this chronicle: a collector of the public record and a workflow that commits each day's digest to the branch `digests`, with the method written into AGENTS.md. the chronicle had stopped on 2026-09-28.

## sources

- https://github.com/cyberia-to/blog/pull/6
- https://github.com/cyberia-to/blog/pull/7
- https://github.com/cyberia-to/blog/pull/9
