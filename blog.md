---
layout: page
title: All My Blogs
subtitle: <span class="mega-octicon octicon-clippy"></span>&nbsp;&nbsp; Take notes about everything new
menu: blog
css: ['blog-page.css']
---
<div class="row">
<div class="col-md-8">
    <section class="container posts-content">
        {% assign sorted_categories = site.categories | sort %}
        {% for category in sorted_categories %}
            <h3>{{ category | first }}</h3>
            <!-- <ol class="posts-list" id="{{ category[0] }}"> -->
            <ol class="posts-list" >
                {% for post in category.last %}
                    <li class="posts-list-item">
                        <div class="posts-content">
                            <!-- <span class="posts-list-meta">{{ post.date | date:"%Y-%m-%d" }}</span> -->
                            <a class="posts-list-name bubble-float-left" href="{{ site.url }}{{ post.url }}">{{ post.title }}</a>
                            <span class='circle'></span>
                        </div>
                    </li>
                {% endfor %}
            </ol>
        {% endfor %}
    </section>
</div>
{% include blog-page.html %}
