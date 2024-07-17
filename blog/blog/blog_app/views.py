from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
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


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }

        message = """
        New message: {}
        
        From: {}
        """.format(data['message'], data['email'])
        send_mail(data['subject'], message,'', ["ssanger2020@gmail.com"], fail_silently=False )
        return HttpResponseRedirect("/success")
    return render(request, 'blog/contact.html', {})

# def contact(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             print(form)
#             return HttpResponseRedirect("/success")
#     else:
#         form = ContactForm()
#     return render(request, 'blog/contact.html', {"form": form})


def success(request):
    template = loader.get_template("blog/email_submission_success.html")
    return HttpResponse(template.render())
