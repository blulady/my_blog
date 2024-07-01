import dj_database_url
from .base import *


STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('NAME'),
#         'USER': os.environ.get('USER'),
#         'HOST': os.environ.get('HOST'),
#         'PORT': os.environ.get('PORT'),
#     }
# }

DATABASES['default'] = dj_database_url.config(
    default = os.environ.get('DATABASE_URL'),
    conn_max_age=500,
    conn_health_checks=True,
)

# ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'sarahsblog.up.railway.app']
# CSRF_TRUSTED_ORIGINS = ['https://sarahsblog.up.railway.app'] https://sarahsblog.up.railway.app/

