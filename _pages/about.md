---
permalink: /
title: "Home"
hidetitle: true
excerpt: "Hi! I'm Ravinder Bhattoo, assistant professor in the Department of [Civil Engineering](https://ce.iiti.ac.in/) at the [Indian Institute of Technology Indore](https://iiti.ac.in/). I focus on researching machine learning-aided structural design, multiscale material modeling, physics-informed machine learning, graph neural networks, dynamic fracture and crack propagation on ballistic impact, molecular dynamics, and peridynamics.

Previously, I have worked as a postdoctoral scholar in the Department of [Civil and Environmental Engineering](https://engineering.wisc.edu/departments/civil-environmental-engineering/) at the [University of Wisconsin-Madison](https://www.wisc.edu/) and as an early doc scholar in the Department of Civil Engineering at the [Indian Institute of Technology Delhi](https://home.iitd.ac.in). I earned my Ph.D. in Civil Engineering from the Indian Institute of Technology Delhi in January 2023, and my B. Tech. in Civil Engineering from the [Indian Institute of Technology Roorkee](https://www.iitr.ac.in) in June 2015. My Ph.D. research focused on data-driven modeling and physics-informed machine learning for glass discovery."
author_profile: true
---


{% include base_path %}

## About me

{{ page.excerpt}}

## Some recent work

{% for post in site.featuredpub %}
    {% include featuredpub.html %}
{% endfor %}

