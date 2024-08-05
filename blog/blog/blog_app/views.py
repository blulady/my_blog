from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import PostForm

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
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'phone': phone,
            'subject': subject,
            'message': message
        }

        message = """
        Subject: {}
        New message: {}
        
        From: {} At Email {} At Phone {}
        """.format(data['subject'], data['message'], data['name'], data['email'], data['phone'])
        send_mail(data['subject'], message, 'mailtrap@demomailtrap.com', ["ssanger2020@gmail.com"], fail_silently=False )
        return HttpResponseRedirect("/success")
    return render(request, 'blog/contact.html', {})


def success(request):
    template = loader.get_template("blog/email_submission_success.html")
    return HttpResponse(template.render())


def post_create_view(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})

