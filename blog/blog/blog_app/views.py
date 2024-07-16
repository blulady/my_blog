from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView
from .models import Post



class HomeView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.newmanager.all()


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    slug_url_kwarg = 'slug'


def about_me(request):
    template = loader.get_template("blog/about_me.html")
    return HttpResponse(template.render())
    
