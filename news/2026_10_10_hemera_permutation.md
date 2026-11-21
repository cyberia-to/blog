---
tags: news, soft3, hemera, mudra, strata
date: 2026-10-10
---
# hemera's permutation ran 1.4 times faster single and about 5 times batched, every output bit unchanged

[[hemera]] merged a rewrite of its permutation kernel. the Goldilocks multiply is written by hand in aarch64 assembly in two forms, a latency form for the serial inverse chain and a 9-instruction throughput form for the S-boxes and the internal layer; one kernel is generic over a profile and a lane count, with Montgomery batch inversion across lanes; a portable path serves every other target. `permute_batch`, `hash_node_batch` and `hash_leaf_batch` carry the batch up to Merkle trees.

the numbers, on an M4 Max in ns per operation: a single permutation 4,146 before and 2,932 after, 3,803 on the portable path; the row `1024 × permute_batch` 4,084 before and 832 after, 914 portable. the differential tests ran 10⁶ permutations and 10⁶ hashes, with non-canonical limbs among the inputs, and found 0 mismatches on both paths.

the same pull request added a constant-time kernel behind every entry point that takes a secret: `keyed_hash`, `derive_key` and the new `hash_secret`, which returns the digest of `hash`. the measured cost is 1.28× on a single permutation and 1.18× on a 64-byte digest. [[mudra]] moved the hashing of wallet entropy to `hash_secret`, so no derived key changed. the work also found that `Goldilocks::dot` in the nebu crate of [[strata]] overflowed at the second product; the fix reduces each product with the field multiply, and the pull request records no production caller in the stack.

## sources

- the kernel and the constant-time mode: [hemera #17](https://github.com/cyberia-to/hemera/pull/17) · [audit/permutation-performance-2026-10.md](https://github.com/cyberia-to/hemera/blob/main/audit/permutation-performance-2026-10.md)
- the consumer: [mudra #19](https://github.com/cyberia-to/mudra/pull/19)
- the dot fix: [strata #14](https://github.com/cyberia-to/strata/pull/14)
