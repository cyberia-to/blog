---
tags: news, soft3, tru, zheng
date: 2026-11-01
---
# measured first: a proof-authorized transfer weighs about 98 KB, and a φ solve needs its own relation

two rows of the plan asked for a measurement before any building, and both receipts merged into `release/phase1`.

the first is a transaction authorized by a proof in place of a signature. the measured object is a veil proof that the sender knows a 4-limb key whose hemera hash is the account key, bound to the transaction digest. it is about 98 KB with 128.2 proven bits. proving takes 208–673 ms and cached verification 12.7–23.1 ms, and on each leg 0 of 64 bit flips were accepted. against rule set 1 of the chain spec such a proof is 193× `MAX_TX_BYTES`, and 2 such transfers fit in a block, 0.067 tx/s. the receipt names three ways out; raising the limits is the one buildable without new measurements.

the second is the φ* relation of [[tru]]. one pussy φ solve, 32,682 particles and 48 steps, is 32.80 M sparse multiply-accumulates plus 17.26 M qmul. under the sound nox machine of [[zheng]] that comes to about 11–14 G machine rows per solve, which sets the general machine aside. the decision the receipt records is a direct CCS relation for the exact integer step, folded over the 48 steps by IVC. the forgery tests ran 696 + 1,160 forged witnesses, and 0 were accepted with a different output.

## sources

- proof-authorized transactions: [soft3 #570](https://github.com/cyberia-to/soft3/pull/570)
- the φ* relation: [tru #44](https://github.com/cyberia-to/tru/pull/44)
