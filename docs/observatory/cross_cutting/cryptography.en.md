---
title: "Cryptography — across fields"
description: How cryptography draws on number theory and is realized in computer science.
tags:
  - type:explanation
  - status:budding
  - concept:cryptography
entry_type: TechArticle
aliases:
  - crypto
---

# Cryptography — across fields

> The practice and study of techniques for securing communication and data against
> adversaries.

Cryptography is a textbook cross-cutting concept: its **guarantees are mathematical** (they
rest on number-theoretic problems believed to be hard), while its **use is computational**
(protocols, key exchange, and primitives implemented in software). This map connects the two
treatments without redefining the term — the full definitions live in each field.

## Across fields

- **[Mathematics](../formal_sciences/mathematics/keywords.en.md#number-theory)** — the
  *foundation*. Public-key cryptography rests on number theory: **RSA** on the hardness of
  factoring, and the **Chinese Remainder Theorem**, **Euler's totient function**, and
  **Miller–Rabin** primality testing on the machinery that makes it work.
- **[Computer Science](../formal_sciences/computer_science/keywords.en.md#cryptography)** —
  the *realization*. Ciphers and protocols — **RSA**, **AES**, **MD5**, **TLS/SSL**,
  zero-knowledge proofs, block-cipher modes (ECB/CBC) — plus the attacks that keep them
  honest (padding oracles, Wiener's attack).

## Why they connect

The same object, **RSA**, appears in both fields — as a *theorem about integers* in
mathematics and as a *deployed cryptosystem* in computer science. The security of the
software artifact is exactly the difficulty of the mathematical problem underneath it: break
integer factorization and you break RSA. That dependency is what makes cryptography impossible
to file under a single discipline — and a natural home on this cross-cutting map.
