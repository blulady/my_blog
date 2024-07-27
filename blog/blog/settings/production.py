import dj_database_url
from .base import *
import cloudinary
import cloudinary.api



STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'live.smtp.mailtrap.io'
EMAIL_HOST_USER = 'api'
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = '587'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

DATABASES['default'] = dj_database_url.config(
    default=os.environ.get('DATABASE_URL'),
    conn_max_age=500,
    conn_health_checks=True,
)

cloudinary.config(
    cloudname=os.environ.get('CLOUDNAME'),
    api_key=os.environ.get('APIKEY'),
    api_secret=os.environ.get('APISECRET')
)
