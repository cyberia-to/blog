---
tags: news, soft3, lytics, cyb
date: 2026-10-21
---
# the lytics tracker moved its proof of work into a worker

a new visitor to a site that carries the [[lytics]] tracker enrols with a proof of work, and that proof ran on the page's main thread. measured headless on cyb.money on a phone viewport, it was a 7.2 s long task at load and 0.8 s on the first navigation, which on a real phone is a frozen tab.

lytics #2 moved the wasm core (init, entropy for a new visitor, `build_event`) into `core-worker.js`, a module worker. the loader keeps the DOM, localStorage and the transport, and falls back to the inline core in browsers without module workers.

lytics #3 fixed the cross-origin case minutes later. a worker script must be same-origin with its page, and the loader is cross-origin on every site that uses it, so cross-origin loaders had fallen back to the inline core. the worker is now created from a same-origin blob module that imports `core-worker.js`.

measured after: zero long tasks, and a neuron enrols on the live endpoint. the cyb.money landing in [[cyb]] recorded its side of the same fix: 8 s on the first switch before, 1 ms after. both pull requests state that they were deployed on 2026-10-21.

## sources

- the worker: [lytics #2](https://github.com/cyberia-to/lytics/pull/2) · [2bc94c6](https://github.com/cyberia-to/lytics/commit/2bc94c6e241ddabd5e89855a453b7bb7784160ac)
- the blob: [lytics #3](https://github.com/cyberia-to/lytics/pull/3) · [03a34ca](https://github.com/cyberia-to/lytics/commit/03a34ca54490db445477a19c6b2403eca43db4fe)
- the landing's measurement: [cyb 185c41d](https://github.com/cyberia-to/cyb/commit/185c41df47f3fd1a718aa0cb7a5b3ba4dbdcfffb)
