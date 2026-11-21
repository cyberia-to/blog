---
tags: news, cyb
date: 2026-10-01
---
# cyb pays the referrer: the Dunbar-decay share landed in the money core

two days after the spec, [[cyb]] core gained `referral.rs`, 254 lines that implement `cyber/specs/referral.md`. the module keeps a referral registry for one cell: bind-once bindings from referee to referrer where the first binding wins, the epoch of each neuron's last settled reward, and the set of witnessed neurons, all in ordered maps so that iteration stays deterministic. a binding is rejected as a self-referral, as already bound, or as a cycle.

the constants are the spec's, in micros: a pool of 100,000 (10%), a floor of 10,000 (1%), a Dunbar scale of 150 and a default activity window of 30 epochs. `share_micros(n)` computes max(floor, pool·150 / (150 + 9n)) for n active referees; a witnessed referrer gets the full curve and everyone else earns the floor.

the split applies to a neuron's settled share in `MoneyWallet::apply_settle_receipt`: the referrer cut rounds down and the referee keeps the net. a new money event, `ReferralAccrued`, carries the result outward. the command line prints it as a `referral` line, sense turns it into a notification for the referrer, and the sigma world shows it as `ref` with the share applied.

## sources

- the commit: [cyb 31574c2](https://github.com/cyberia-to/cyb/commit/31574c24566d3a30b7497800025ca12d370da074)
- the module and its constants: [core/src/referral.rs](https://github.com/cyberia-to/cyb/blob/31574c24566d3a30b7497800025ca12d370da074/core/src/referral.rs)
- the spec it implements: [cyber/specs/referral.md](https://github.com/cyberia-to/cyber/blob/cbac3f53fa2169c2a03acac07de77cfba54b7f3d/specs/referral.md)
