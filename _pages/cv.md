---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

[Download CV]({{site.author.baseurl}}/files/ravinder_cv.pdf) in pdf form.

Education
======
- <p>PhD, Civil Engineering <p>2017-Present <br> Indian Institute of Technology Delhi, Delhi</p></p>
- <p>B. Tech., Civil Engineering <p>2011-2015 <br> Indian Institute of Technology Roorkee, Roorkee</p></p>

<br>


Research Achievements and Awards
======

PyGGi (Python for Glass Genomics)
It is an indigenous industry relevant software package that uses trained Machine Learning
algorithms to predict/optimise composition-property relationships in inorganic glasses. It will
make the tedious process of designing tailored glasses economical in terms of time, effort and
money.
The software package is launched through FITT IITD and is available at www.pyggi.iitd.ac.in

- ICG-GOMD 2019 registration grant (2019)
- Prime Ministers Research Fellowship (PMRF)
- SITARE/SRISTI Gandhian Young Technological Innovation (GYTI) Awards/Appreciations (2020) for PyGGi
- SERB International Travel Support (2022)


Software and Programing Languages
======

- Packages Developed:
  - Peridynamics: PeriDyn.jl, PDMesh.jl and PDBenchmark.jl
  - Molecular Dynamics: MDSimulator.jl and MDBase.jl
  - Others: GlassConversionPy

  All packages can be accessed at the [github repository](https://github.com/{{site.author.github}}).
- Operating Systems: Linux, MacOS and Windows
- Softwares: LAMMPS, NAMD, Peridigm, R.I.N.G.S, Ovito, VMD, Abaqus and STAADPRO
- Languages: Julia, Python, C++ and Matlab


<br>

Publications
======
  <ol>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ol>

<br>

Talks
======
  <ol>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ol>

