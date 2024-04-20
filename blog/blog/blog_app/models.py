from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_author")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=options, default="draft")

    class Meta: 
        ordering = ["-created_at"]

    def __str__(self):
        return self.title