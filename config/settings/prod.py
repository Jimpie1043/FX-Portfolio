from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")
]

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True