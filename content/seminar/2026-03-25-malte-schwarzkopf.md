+++
title = 'Practical End-to-End Privacy and Data Use Policy Enforcement'
date = 2026-03-23T15:00:00-04:00
eventTime = 2026-03-25T12:45:00-04:00
speaker = 'Malte Schwarzkopf (Brown University)'
location = "SEC 2.122 & 2.123"
summary = "While modern data is governed by strict privacy policies, developers often lack the practical abstractions needed to ensure their code complies, leading to frequent manual errors and costly violations. Malte Schwarzkopf will introduce Sesame, a framework that utilizes policy containers and static analysis to automate end-to-end privacy enforcement with minimal developer effort and low performance overhead."
draft = false
+++

## Abstract

Data today is often governed by privacy and data use policies, but developers lack practical abstractions to ensure that their code actually abides by these policies. This leads to frequent oversights, bugs, and costly privacy violations.

In this talk, I will present Sesame, a practical framework for end-to-end privacy policy enforcement. Sesame wraps data in policy containers that associate data with policies that govern its use. Policy containers force developers to use privacy regions when operating on the data, and Sesame combines sandboxing and a novel static analysis to prevent privacy regions from leaking data. Sesame enforces a policy check before externalizing
data, and it supports custom I/O via reviewed, signed code. 

Experience with four web applications shows that Sesame achieves this with reasonable application developer effort, requires no manual work for most code (>95%), and imposes acceptable performance overhead. Sesame's ideas give rise to new research questions on policy enforcement for distributed services and the utility and realism of system designs that rely on language-level guarantees.

## Bio

Malte Schwarzkopf is an Associate Professor of Computer Science at Brown University, where he leads the ETOS group. Malte's research is on new abstractions that deliver efficient, easy-to-use, and trustworthy computer systems. Malte is a recipient of the NSF CAREER award, a Google Research Award, a Google ML and Systems Junior Faculty Award, and an Amazon Research Award. He received Brown University's Philip J. Bray Award for Excellence in Teaching, the Henry Merritt Wriston Fellowship, and a class of 2023 Barrett Hazeltine Citation for Excellence in Teaching, Guidance, and Support. His past research received best paper awards at NSDI and EuroSys, as well as the EuroSys 2023 Test of Time Award. Prior to Brown, Malte was a postdoc with MIT's PDOS group and completed his PhD at the University of Cambridge. He is still getting used to living in a city not called Cambridge.
