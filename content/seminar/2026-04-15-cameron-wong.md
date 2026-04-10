+++
title = 'Collapsing Towers of Interpreters for Security'
date = 2026-04-09T22:00:00-04:00
eventTime = 2026-04-15T12:45:00-04:00
speaker = 'Cameron Wong (Harvard University)'
location = "SEC 2.122 & 2.123"
summary = "Staged metaprogramming offers an alternative to traditional macros by using annotations to control execution timing, allowing programs to be specialized for known inputs by delaying specific computations. Cameron Wong will demonstrate how this technique can derive compilers from interpreters and reify low-level hardware behaviors to detect side-channel vulnerabilities, while also discussing future applications in address sanitization and decompilation."
draft = false
+++

## Abstract

Metaprogramming is the practice of writing programs that manipulate other programs as data, most commonly seen in preprocessor macros that expand syntactic shorthands into code. In this talk, I will focus on a different approach: staged metaprogramming, in which an ordinary program is annotated to control when different parts of the computation run. Rather than executing everything immediately, some computations are delayed, producing code for a later stage and enabling specialization with respect to known inputs.

In this talk, I will first show how staging can derive a compiler from an interpreter via the Futamura projection. I will then demonstrate how the same technique can reify low-level hardware behavior, such as cache effects and speculative execution, into explicit program values. We have used this approach to detect side-channel vulnerabilities in small assembly programs with off-the-shelf semantic analysis tools.

Finally, time permitting, I will discuss ongoing and future directions, including applications to address sanitization and decompilation.

## Bio

Cameron is a PhD candidate in the Programming Languages group at Harvard University, advised by Professor Nada Amin. His research focuses on the theory, implementation and applications of type-directed metaprogramming. More broadly, he has worked on functional programming, compiler development, and theorem proving. Prior to joining Harvard, he worked as a developer tooling engineer at Jane Street and received his Bachelor's degree from Carnegie Mellon University.
