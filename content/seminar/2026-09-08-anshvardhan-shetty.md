+++
title = 'KV Cache on Flash: What to Write When Writes Wear Out'
date = 2026-09-04T18:00:00-04:00
eventTime = 2026-09-08T12:45:00-04:00
speaker = 'Anshvardhan Shetty (Imperial College London)'
location = "SEC 4.307 & 4.308"
summary = "Long agentic sessions make the KV cache the dominant memory cost in LLM serving, and flash offers capacity HBM cannot, but every block written spends a fraction of the drive's lifetime, so a flash tier needs an admission policy and not only an eviction policy. Anshvardhan will present a study of that one-shot admission decision on a 222-day production trace of agentic coding traffic, including a learned prefill-time scorer and a two-tier implementation inside vLLM."
draft = false
+++

## Abstract

Long agentic sessions make the KV cache the dominant memory cost in LLM serving, and high-bandwidth flash offers capacity that HBM cannot. But flash wears out: every block written spends a fraction of the drive's lifetime, so a flash tier needs an admission policy and not only an eviction policy. The decision is one-shot and irrevocable as a request's blocks must be admitted at prefill, before anything is known about how long its session will run. Prior flash-caching work assumes reuse can be observed in DRAM before admission, or that the write budget is not the binding constraint. Neither holds here.

I'll present a study of that decision on a 222-day production trace of agentic coding traffic, graded causally on its final 21 days against a hindsight oracle under three endurance budgets. The work builds a learned scorer that predicts per-block reuse density at prefill and identifies what limits it, measures when admission control is worth running at all as the write budget varies against demand, and implements the policy inside vLLM with a two-tier block pool and in-engine scoring.

## Bio

Anshvardhan Shetty is a first-year undergraduate majoring in EECS at Imperial College London, currently a research intern working with Professor Juncheng Yang at Harvard SEAS. He works on ML systems, with a focus on caching and admission policies for LLM serving under hardware endurance constraints.
