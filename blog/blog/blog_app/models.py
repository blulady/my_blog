from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_author")
    img = models.ImageField(upload_to='images/', default='images/coming_soon.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=options, default="draft")
    objects = models.Manager()
    newmanager = NewManager()

    class Meta: 
        ordering = ["-created_at"]

    def __str__(self):
        return self.title