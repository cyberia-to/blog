---
tags: news, soft3, hemera, neuron, mudra, tade, radio, foculus
date: 2026-10-07
---
# one responsibility per component: the boundaries page was marked executed, and cy's showing organs became one chroma

[[soft3]]'s roadmap page on component boundaries, the tier between nox execution and the wire, was marked executed on 2026-10-07 in pull request #81. the page fixes one verb per component. [[hemera]] owns content identity and its proof, including the verified-streaming codec. [[neuron]] owns the subject and its proof-based authority, in the crate `neuron-auth`. [[mudra]] keeps confidentiality and key distribution. [[tade]] frames the wire, [[radio]] transmits, and [[foculus]] holds the whole reconciliation engine together with the fork-choice that completes it. the dependency order reads as a DAG, from hemera and tade at the leaves up to foculus.

the page keeps a ledger of mechanisms that had two homes and says what happened to each. two rows were corrected the same day: #82 reversed a deletion and left the CRDT reconciliation engines in radio until their cores move to foculus, and #83 changed the mudra row from specification only to seal and quorum implemented, citing mudra's pull request #18, which was opened against the branch `refactor/spell`.

in the cy repository the same pass defined chroma, the shape of the agent: a 3×3 grid of eight organs that show around one pluggable centre, with time and name becoming cy organs. cy #1 merged the organ repositories into cy, and cy #2 corrected it within the hour: chroma is one component holding the eight contracts and sigma's code, while soma, glia, seer and vault keep their own repositories. on the ladder at soft3.org mudra moved from the language rung to the cybergraph rung beside neuron, and rung 6 shows cy as one chroma plus the organs that work unseen.

## sources

- the boundaries page: [soft3 #81](https://github.com/cyberia-to/soft3/pull/81) · [roadmap/component-boundaries.md](https://github.com/cyberia-to/soft3/blob/9951ee501dffa25779709ec2204e66c5c09e9e54/roadmap/component-boundaries.md)
- the two corrections: [soft3 #82](https://github.com/cyberia-to/soft3/pull/82) · [soft3 #83](https://github.com/cyberia-to/soft3/pull/83) · [mudra #18](https://github.com/cyberia-to/mudra/pull/18)
- chroma: [cy #1](https://github.com/cyberia-to/cy/pull/1) · [cy #2](https://github.com/cyberia-to/cy/pull/2) · [chroma/README.md](https://github.com/cyberia-to/cy/blob/19bcc35f480b519a36f0a76185130ea64a93fc76/chroma/README.md)
- the ladder: [soft3 #84](https://github.com/cyberia-to/soft3/pull/84) · [soft3 #85](https://github.com/cyberia-to/soft3/pull/85) · [soft3 #86](https://github.com/cyberia-to/soft3/pull/86)
