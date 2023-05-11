---
layout: archive
title: "CV"
hidetitle: true
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

[Download CV]({{site.author.baseurl}}/files/ravinder_cv.pdf) in pdf form.

Research Interest
======
Machine learning aided structural design, material modeling, physics-informed machine learning, graph neural networks, dynamic fracture and crack propagation on ballistic impact, molecular dynamics, and peridynamics

Research Experience
======
- **Research Associate**, Civil and Environmental Engineering <br> _April 2023 -- Present <br> University of Wisconsin, Madison_
- **Postdoctoral Scholar**, Civil Engineering <br> _January 2023 -- March 2023 <br> Indian Institute of Technology Delhi, Delhi_

Education
======
- **Ph.D.**, Civil Engineering <br> _July 2017 -- January 2023 <br> Indian Institute of Technology Delhi, Delhi_
- **B.Tech.**, Civil Engineering <br>_July 2011 -- June 2015 <br> Indian Institute of Technology Roorkee, Roorkee_

Ph.D. Thesis
======
__Title: Data-driven Modeling and Physics-informed Machine Learning for Glass Discovery__

The research work explores the use of machine learning methods in modeling inorganic glass properties, revealing composition--property relationships through explainable ML, understanding mechanisms at atomic scale and up-scaling of material properties using MD and DFT simulation trajectory. The research work uses the graph neural network based interatomic potential for reproducing features at atomic scale for complex systems and use ML material models (peridynamics nonlocal operators) for reproducing material behavior at meso-scale with MD and DFT simulation trajectories


Research Achievements and Awards
======

PyGGi (Python for Glass Genomics)
It is an indigenous industry-relevant software package that uses trained Machine Learning
algorithms to predict/optimize composition-property relationships in inorganic glasses. It will
make the tedious process of designing tailored glasses economical in terms of time, effort, and
money.
The software package is launched through FITT IITD and is available at www.pyggi.iitd.ac.in

- ICG-GOMD 2019 registration grant (2019)
- Prime Ministers Research Fellowship (PMRF)
- SITARE/SRISTI Gandhian Young Technological Innovation (GYTI) Awards/Appreciations (2020) for PyGGi
- SERB International Travel Support (2022)

Book(s) and Contributed Chapters
======
- Machine Learning for Materials Discovery: Numerical Recipes and Practical Applications (__Draft__)

  *N. M. Anoop Krishnan, Hariprasad Kodamana and Ravinder Bhattoo*

Software and Programming Languages
======

- Packages Developed:
  - Peridynamics: __PeriDyn.jl, PDMesh.jl and PDBenchmark.jl__
  - Molecular Dynamics: __MDSimulator.jl and MDBase.jl__
  - Others: __GlassConversionPy, MLPipeline, MixModelsPytorch__
  - Contribution to other packages: __jax-md__

  All packages can be accessed at the [github repository](https://github.com/{{site.author.github}}).
- Operating Systems: Linux, MacOS, and Windows
- Softwares: LAMMPS, NAMD, Peridigm, R.I.N.G.S, Ovito, VMD, Abaqus and STAADPRO
- Languages: Julia, Python, C++, and Matlab

<br>

Publications
======
  <ol>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ol>

<br>

Conferences Talks and Workshops
======
  <ol>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ol>


