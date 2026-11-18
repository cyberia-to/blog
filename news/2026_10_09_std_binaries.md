---
tags: news, neural, rs
date: 2026-10-09
---
# rs built a std binary with zero LLVM codegen

the pure-Rust toolchain of [[rs]] reached std programs. the codegen backend emits rlibs through rustc's own archive builder, with no LLVM, no ranlib and no system linker on that path, so a real crate compiles as an rlib and is consumed downstream; the crate verified was itoa 1.0.11. the backend then hands the rlibs of the dependency closure to the project's Mach-O linker, which pulls archive members on demand, and a std binary builds with zero LLVM codegen. every emitted symbol carries the Darwin underscore prefix, so the objects link against LLVM-built rlibs, and an allocator shim forwards to the libSystem malloc family.

the other commits of the day are the faults that binary met at run time, each fixed at its cause. pointers to backing statics are rematerialized per basic block, after which the std and itoa test binary ran main to completion. the thread-local link path was completed (the TLV relocations, the section type bits, 8-byte alignment of `__thread_vars`, the descriptor rewrite), so std binaries load with working thread-local storage. the no-alloc-shim guard is emitted as a function. local GOT slots are synthesized, after which panics print, and call arguments are set up in two phases. the commit that added the GOT slots records 173 workspace tests green, 11 of 11 codegen integration tests and 2 of 2 linker integration tests, and names the next fault: a pointer corruption in btree code.

## sources

- rlib emission: [rs 30ae482](https://github.com/cyberia-to/rs/commit/30ae482329dcdfef7db73cbc0248fcb1612c09b4)
- the sysroot rlib closure: [rs 0c356e2](https://github.com/cyberia-to/rs/commit/0c356e26e31f761e29a323550fee3b96d468fc41) · [dbced36](https://github.com/cyberia-to/rs/commit/dbced3626d91f9ac1597ae99dad275531702b7b5)
- the run-time faults: [68a42f8](https://github.com/cyberia-to/rs/commit/68a42f8eaa36c355bb61d64bee390de6cd961797) · [492f55b](https://github.com/cyberia-to/rs/commit/492f55be825b8a9c09c6c6a87ad6beea9159d960) · [870dbfd](https://github.com/cyberia-to/rs/commit/870dbfda979320758cde983dc1e03428305e3817) · [218419b](https://github.com/cyberia-to/rs/commit/218419bda254bb4b36ad197e3dae793871229bf0) · [8abf96c](https://github.com/cyberia-to/rs/commit/8abf96cf405c21c734d452ead308fa7e82cbec3e)
