import dj_database_url
from .base import *


STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

DATABASES['default'] = dj_database_url.config(
    default = os.environ.get('DATABASE_URL'),
    conn_max_age=500,
    conn_health_checks=True,
)