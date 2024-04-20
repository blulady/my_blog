from pytest_factoryboy import register

from .factories import PostFactory

from django.conf import settings
from blog.settings import settings

register(PostFactory)