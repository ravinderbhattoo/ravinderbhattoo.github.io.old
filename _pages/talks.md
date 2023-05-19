---
layout: archive
title: "Conference Talks, Workshops and Posters"
permalink: /talks/
author_profile: true
---
{% include base_path %}

{% include group-by-array collection=site.talks field="presentation_type" %}
{% assign collection_tags = group_names | join: '~~~' | downcase | split: '~~~' %}

## Talks

{% for tag in collection_tags  %}
  {% if tag == "talk" %}
    {% assign posts = group_items[forloop.index0] %}
    {% for post in posts reversed %}
        {% include archive-single-talk-cv.html %}
    {% endfor %}
  {% endif %}
{% endfor %}

## Workshops

{% for tag in collection_tags  %}
  {% if tag == "workshop" %}
    {% assign posts = group_items[forloop.index0] %}
    {% for post in posts reversed %}
        {% include archive-single-talk-cv.html %}
    {% endfor %}
  {% endif %}
{% endfor %}

## Posters

{% for tag in collection_tags %}
  {% if tag == "poster" %}
    {% assign posts = group_items[forloop.index0] %}
    {% for post in posts reversed %}
        {% include archive-single-talk-cv.html %}
    {% endfor %}
  {% endif %}
{% endfor %}
