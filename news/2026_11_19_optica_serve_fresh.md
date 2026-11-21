---
tags: news, cyb, optica
date: 2026-11-19
---
# optica serve keeps edited pages fresh through the initial build

optica #6 closed a race in `optica serve`. the server opens its port at once and runs the initial full build in a thread, while the file watcher starts at the same moment. a file edited during the build, which took about 13 minutes, was rendered incrementally and then overwritten by the final write of the build, parsed from the old bytes. the warm-up had already hashed the new bytes, so the page stayed stale until its next edit. the case was seen on cyberia/dev on 2026-10-22: the served page lacked a paragraph the file had, and `touch` answered "Rebuilt 0 pages".

the fix hands the server a `build_done` flag, set when `build_site` returns. the watcher keeps buffering events from the start, waits for the flag before its warm-up, and then forgets the parse and hash entries of the files edited in the meantime, so the next pass rebuilds them from the new bytes.

a site served while it builds now shows the latest bytes of every file once the build is done.

## sources

- https://github.com/cyberia-to/optica/pull/6
