from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import ContactForm



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


# def contact(request):
#     template = loader.get_template("blog/contact.html")
#     return HttpResponse(template.render())


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.Post)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        form.name = name
        form.email = email
        form.phone = phone
        form.message = message
        if form.is_valid():
            pass
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})


def success(request):
    template = loader.get_template("blog/email_submission_success.html")
    return HttpResponse(template.render())