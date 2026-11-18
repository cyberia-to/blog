---
tags: news, cyberia
date: 2026-11-17
---
# cyberia.blog publishes again, and every build proves itself on the site

from 2026-10-29 to 2026-11-17 every publish of this site failed at its deploy step. the workflow copied the build to a hard-coded address of a host that had been retired, while cyberia.blog already resolved to the new front, which kept serving the build of 29 October. the first fix pointed the deploy at the front. the second removed the address: the deploy target is whatever cyberia.blog resolves to, a repository variable overrides it, and the deploy refuses to guess when the zone returns more than one address.

each build now carries a stamp, `build.txt`, with the run, the commit and the time. after the copy the run reads the stamp from cyberia.blog and fails unless the site serves this run. a failed run on master opens an issue labelled `publish-failing`, the next verified publish closes it, and a second workflow compares the served stamp with the last successful publish every hour.

the same day the daily beat got its first half: a collector that reads the public repositories of cyberia-to into one digest per UTC day, and a workflow that commits each digest to the branch `digests`. the chronicle had stopped on 2026-09-28 because beats and news were written by hand. the project chronicle opened beside it: the whole history of the project from git, the blog, X, Telegram, YouTube and BOOT's price, told as one chronology.

## sources

- the deploy: [blog #6](https://github.com/cyberia-to/blog/pull/6) · [blog #7](https://github.com/cyberia-to/blog/pull/7)
- the daily beat: [blog #9](https://github.com/cyberia-to/blog/pull/9)
- the chronicle project: [c5c9b82](https://github.com/cyberia-to/blog/commit/c5c9b82) · [projects/chronicle.md](https://github.com/cyberia-to/blog/blob/master/projects/chronicle.md)
