+++
title = 'Learning-Directed Operating Systems'
date = 2026-02-12T10:00:00-05:00
eventTime = 2026-02-13T14:00:00-05:00
speaker = 'Aditya Akella (the University of Texas at Austin)'
location = "SEC 2.122 & 2.123"
summary = "Modern applications often face performance bottlenecks due to rigid OS policies, even when resources are plentiful. Aditya Akella will present LDOS (Learning-Directed Operating System), which replaces manual policy design with data-driven, system-wide optimization."
draft = false
+++

## Abstract

Modern applications run on increasingly heterogeneous and dynamic platforms, yet today's operating systems (OSes) still rely on rigid, locally optimized policies that are manually designed, weakly coordinated, and slow to adapt. As a result, even when resources are plentiful, performance and tail latency are often dominated by poor policy choices rather than fundamental hardware limits.

To address this, we are building LDOS, a Learning-Directed Operating System that treats policy design as a data-driven, system-wide optimization problem. In contrast to Linux, where mechanisms and policies are tightly entangled and global system state is difficult to observe or act upon, LDOS is designed from the ground up to expose rich observability, support fast feedback loops, and enable coordinated and trustworthy machine-learned control. 

This talk describes the main pillars of the LDOS approach. I will first describe UNUM, which constructs system-wide state embeddings to enable higher-quality and coordinated policy decisions. I will then introduce Darwin, a family of techniques that make ML-driven policies practical by balancing instance-optimal decisions with generalization and runtime overhead. Next, I will present C3, a framework that enforces system-wide and tail-latency guarantees despite learned, adaptive control. The talk will conclude with the core design principles behind LDOS’s clean-slate prototype and an overview of its current status.

## Bio

Aditya Akella is a Professor and Regents Chair in Computer Sciences at UT Austin and a Research Scientist at Meta. His research focuses on computer systems and their intersection with machine learning and formal methods. He leads the NSF CISE Expedition on Learning-Directed Operating Systems and serves as Founding Director of the InfraAI @ UT Center. Aditya’s work has influenced the infrastructure of large-scale online services and has been recognized with honors including ACM Fellow, SIGCOMM and IMC Test of Time Awards, the SIGCOMM Rising Star Award, the IRTF Applied Networking Research Prize, the NSF CAREER Award, and multiple best paper awards.


