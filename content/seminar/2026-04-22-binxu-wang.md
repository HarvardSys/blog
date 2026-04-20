+++
title = 'High-Dimensional Gradient-Free Optimization for Neuroscience, Interpretability and LLMs: Why It Works and How to Make It Better'
date = 2026-04-20T10:00:00-04:00
eventTime = 2026-04-22T12:45:00-04:00
speaker = 'Binxu Wang (Harvard University)'
location = "SEC 2.122 & 2.123"
summary = "Evolution strategies (ES) provide a vital gradient-free alternative for solving complex, high-dimensional optimization problems in fields like neuroscience and LLM fine-tuning where traditional backpropagation is often unavailable or inefficient. Binxu Wang will explore the geometric properties that enable these methods to succeed and demonstrate how identifying task-irrelevant parameter directions can be leveraged to further accelerate optimization in modern large-scale models."
draft = false
+++

## Abstract

In a world dominated by backpropagation, gradient-free methods like evolution strategies (ES) can seem like a curiosity. Yet ES solves hard, high-dimensional problems where gradients are unavailable or expensive — from driving noisy neurons in the primate visual cortex to fine-tuning large language models. The surprising fact that it works at all reveals properties of these problems we often neglect. In this talk, I argue that understanding why ES works leads directly to better algorithms.

I begin with an interpretability challenge from neuroscience: finding images that maximally activate neurons deep in the primate visual hierarchy. Using CMA-ES in the latent space of deep generative models, we reliably optimize in thousand-dimensional spaces where gradient-free search should be hopeless. The search trajectories exhibit signatures of high-dimensional random walks that change systematically along the visual hierarchy, revealing structure in the optimization landscapes of visual neurons. Analyzing the geometry of GAN latent spaces, we further find a large null space in the generator Jacobian; projecting it out dramatically improves search efficiency.

I then turn to LLM fine-tuning, where ES has recently been found surprisingly competitive with policy gradient methods like GRPO — capable of tuning 4B parameters with a population of just 30. We validate this effect and investigate its geometric origin: the optimization trajectory again exhibits high-dimensional random walk signatures, suggesting that the vast majority of parameters are flat and task-irrelevant, which is precisely what makes ES effective. I present a theoretical framework analyzing ES dynamics across landscape geometries that formalizes this intuition.

I close with an open question: can we identify and remove these irrelevant directions to further accelerate gradient-free optimization in modern language models?

## Bio
Binxu Wang is a Research Fellow at the Kempner Institute for the Study of Natural and Artificial Intelligence at Harvard University. She received her Ph.D. in Neuroscience from Washington University in St. Louis and her B.S. in Physics from Peking University. Her research bridges computational neuroscience and deep learning theory, using each field's tools to illuminate the other. On the neuroscience side, she has developed closed-loop optimization methods to probe neural representations in the primate visual system. On the machine learning side, she studies the internal mechanisms and learning dynamics of generative models, particularly diffusion models, through analytical and mechanistic interpretability approaches. Her recent work spans spectral analysis of diffusion model training dynamics, circuit-level dissection of diffusion transformers, and comparisons of optimization strategies for LLM fine-tuning.