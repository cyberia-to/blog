---
tags: news, bootloader, space-pussy
date: 2026-11-02
---
# the bytes of pussy's genesis particles: 83.20 % are in the archive

an audit in [[space-pussy]] answered the owner's question of 2026-11-02: is the content of pussy's 16,273 genesis particles available, or lost with the old infrastructure. the count is 16,271 particles with a legacy CID plus 2 passport particles without one.

13,538 of them (83.20 %) are in the Filecoin particle archive, and 600 of 600 sampled were served by the project's gateway. 679 (4.17 %) are on public IPFS only, 2.24 GB measured. 782 (4.81 %) are announced but not served. 1,272 (7.82 %) are lost.

weighted by focus on the alpha node at pussy-rc epoch 13, the archive carries 76.56 % of all φ* and the lost particles 12.61 %. of the top 50 particles, 42 are retrievable and 8 are lost. the receipt names the rescue for the 679 public-only particles: fetch them and add them to the archive as one more pack, a few hours of work.

the audit ships `audit/particles-cids.tsv`, which maps every particle to its legacy CID and class. the explorer uses that map, split into 256 shards, to preview a particle's bytes on its page.

## sources

- the audit: [space-pussy #18](https://github.com/cyberia-to/space-pussy/pull/18) · [18ab5be](https://github.com/cyberia-to/space-pussy/commit/18ab5be0b6746deba3a7f44c577cc08f022628f3)
- the shards for the explorer: [6237d48](https://github.com/cyberia-to/space-pussy/commit/6237d48f14f515d043dea23c42d6481d063afa01)
