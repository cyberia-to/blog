---
tags: news, neural, warriors, trident, joy, trisha
date: 2026-10-02
---
# trident's compiler compiled itself on nox through joy on six platforms: SH6 accepted

[[trident]] recorded SH6 as accepted on its `release/0.4` branch: the frozen S1 compiler reproducibly compiles itself on [[nox]] through [[joy]]. the evidence is one CI run that passed on macOS, Linux glibc and Windows MSVC, each on ARM64 and x64. on every target two independent bootstrap repetitions each executed C1(S1)→C2 and C2(S1)→C3. all 24 resulting C2 and C3 corpus jobs passed the same 547 observations and 1816 commands, and the aggregate confirmed that C2 and C3 are byte-identical. a fresh restore from three stores compared all 88,488 expanded files against the original archives and matched every receipt hash. earlier timeouts and failed attempts stay in the record unchanged.

the practical result is a portable kit. [[trisha]] #19, also on `release/0.4`, packages an accepted C2 compiler at `share/trident-selfhost` after rerunning the committed native acceptance validator and verifying all 94 compiler source modules. the trident guide links the exact 4,377,450-byte archive and gives direct commands for compiling programs and for rebuilding the complete 94-module compiler.

the pull request states the reach of the claim: acceptance covers the declared frozen compiler subset and resource profile, and master, release tags and publication were left unchanged. trisha #20 rehearsed the 0.4 distribution from the frozen sources on the same six targets, as evidence on the feature branch.

## sources

- the acceptance, into `release/0.4`: [trident #115](https://github.com/cyberia-to/trident/pull/115) (six platforms, 24 jobs, 547 observations, 1816 commands, 88,488 files, the 4,377,450-byte archive)
- the kit, into `release/0.4`: [trisha #19](https://github.com/cyberia-to/trisha/pull/19) (94 modules)
- the distribution rehearsal, into `release/0.4`: [trisha #20](https://github.com/cyberia-to/trisha/pull/20)
