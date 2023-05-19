---
conf: "2022 Glass and Optical Materials Division Annual Meeting"
date: "May 2022"
venue: "Hyatt Regency Baltimore"
location: "Baltimore, MD, United States"
presentation_type: "Talk"
authors: "<b><u>Ravinder Bhattoo</u></b>*, N. M. Anoop Krishnan"
title: "Learning interaction laws in atomistic system using Lagrangian Graph Neural Networks"
abstract: "talk_gomd_2022_laws.txt"
files: "nan"
collection: talks
---

<!--  -->

## Abstract

Molecular dynamics simulations are used to realistically simulate the material properties. The interatomic potential energy function (PEF) is critical in determining the validity of the results. Such interatomic PEFs are parameterized using density functional theory (DFT). Usually, interatomic PEF is a multi-body function whose functional form is non-trivial to determine. Therefore, estimating the functional form is critical in determining the interatomic PEF and hence the material properties. Herein, we use Lagrangian Graph Neural Network (LGNN) to learn such interatomic PEF in silica glass system. We show that the LGNN model can learn silica interatomic potential for Si-O, O-O and Si-Si interactions. The inductive bias present in the LGNN makes training easier where it can learn from a significantly small dataset as compared to other ML methods. Thanks to the graph architecture, the size of LGNN model is agnostic to the size of system used and hence, learned LGNN model is scalable. We show the zero-shot generalizability of the LGNN model by simulating systems one orders of magnitude larger than the trained one. Further, LGNN architecture is also capable of incorporating the dissipative force due to connected thermostat. Finally, we show the interpretability of LGNN, which directly provides physical insights on the learned model.