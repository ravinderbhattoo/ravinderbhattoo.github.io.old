---
conf: "2022 Glass and Optical Materials Division Annual Meeting"
date: "May 2022"
venue: "Hyatt Regency Baltimore"
location: "Baltimore, MD, United States"
title: "Talk: Learning Quantum-accuracy Interatomic Potential for Silica Using Lagrangian Graph Neural Networks"
abstract: "talk_gomd_2022_sio2.md"
files: "nan"
---

<!--  -->

## Abstract

Molecular dynamics (MD) simulations are used extensively to study the complex behavior of glasses. In MD simulations, we use the equations of motion along with time integration to generate atomic trajectories. Due to the small timestep used in simulations, a prohibitively large number of runs are required to perform the meltquench simulation of glasses, especially when using first principle simulations or density functional theory (DFT). Thus, the MD simulations of glasses rely on empirical interatomic potentials that are fitted from the experiment or DFT simulations data. Thus, the accuracy of any MD simulation is limited by the interatomic potential used in the simulation. Further, fitting the interatomic potential is a challenging process that restricts the applicability of MD simulations to a small family of glasses. To address this challenge, it is imperative to develop a scalable scheme that allows the seamless development of quantum accuracy interatomic potentials for glasses. Here, we propose a novel Lagrangian graph neural network (LGNN) to learn such interatomic potentials for complex glassy systems directly from the trajectory of DFT simulations. We demonstrate it in a silica glass system. We show that the LGNN model can learn silica interatomic potential for Si-O, O-O and Si-Si interactions.

