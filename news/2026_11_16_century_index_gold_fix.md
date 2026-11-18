---
tags: news, cyberia, cx
date: 2026-11-16
---
# the century index fixes again: the gold leg reads PAXG closes

cx is the daily fix of the century index, ticker CX, the unit of account for century-scale obligations: each leg is pulled from its public source, carried onto a dense daily calendar and averaged over the trailing 365 days, and the quantities held from the base date are summed at the day's averages. the fix had failed for seven weeks. LBMA, the source of the gold leg, answered 403 to every machine since 2026-09-29.

on 2026-11-16 the gold leg changed its source: PAXG-USD daily closes from Yahoo Finance are the gold fix, and LBMA PM is the fallback. Coinbase's PAXG candles were set aside because they start too late for the base window. the fix of 2026-11-16 was committed to cyberia.my the same day: 1.4146.

## sources

- the source of gold: [cx d05fafe](https://github.com/cyberia-to/cx/commit/d05fafef0d6b23798c0b59aecab63070a16ae126)
- the fix of the day: [cyberia.my 42cd98d](https://github.com/cyberia-to/cyberia.my/commit/42cd98dce4008fc59ea50bbc25f693dd533122b8)
- the pipeline: [cx/README.md](https://github.com/cyberia-to/cx/blob/main/README.md)
