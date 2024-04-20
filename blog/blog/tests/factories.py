import factory
from django.contrib.auth.models import User
from blog.blog_app.models import Post

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "testuser"
    password = "testpassword"
    is_superuser = True
    is_staff = True

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = "Test Title"
    subtitle = "Test Subtitle"
    slug = "test-title"
    content = "Test Content"
    author = factory.SubFactory(UserFactory)
    status = "published"