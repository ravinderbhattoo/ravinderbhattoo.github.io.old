---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

- Our paper on 21 challenges in AI and ML in glass technology featured in American Ceramic Society's  CTT. Read the article [here](https://ceramics.org/ceramic-tech-today/glass-1/glass-discovery-and-design-21-challenges-in-artificial-intelligence-and-machine-learning-for-glass-science). A reprint of the article can be found in Glass machinery plants and accessories magazine [here](https://www.glassonline.com/pdf/magazine/GM/2021/GM_2021_3.pdf#page=74).

- Our paper on glassy h-BN selected as the cover page in Advanced Theory and Simulations. Read the paper here: [link](https://onlinelibrary.wiley.com/doi/full/10.1002/adts.201900174) !!!


{% include base_path %}

{% if page.author and site.data.authors[page.author] %}
  {% assign author = site.data.authors[page.author] %}{% else %}{% assign author = site.author %}
{% endif %}

{% if author.googlescholar %}
You can also find my articles on my <a href="{{author.googlescholar}}">Google Scholar</a> profile.
{% endif %}


{% include group-by-array collection=site.publications field="item_type" %}
{% assign collection_tags = group_names | join: '~~~' | downcase | split: '~~~' %}

# Journal Articles

{% for tag in collection_tags  %}
  {% if tag == "journalarticle" %}
    {% assign posts = group_items[forloop.index0] %}
    {% for post in posts reversed %}
        {% include archive-single-pub.html %}
    {% endfor %}
  {% endif %}
{% endfor %}

# Preprints

{% for tag in collection_tags  %}
  {% if tag == "preprint" %}
    {% assign posts = group_items[forloop.index0] %}
    {% for post in posts reversed %}
        {% include archive-single-pub.html %}
    {% endfor %}
  {% endif %}
{% endfor %}

# Conference Papers

{% for tag in collection_tags %}
  {% if tag == "conferencepaper" %}
    {% assign posts = group_items[forloop.index0] %}
    {% for post in posts reversed %}
        {% include archive-single-pub.html %}
    {% endfor %}
  {% endif %}
{% endfor %}

