"""
WSGI config for portfoliofx project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

load_dotenv()

settings_module = os.environ.get("DJANGO_SETTINGS_MODULE")

if not settings_module:
    raise RuntimeError(
        "From wsgi: DJANGO_SETTINGS_MODULE environment variable is not set."
    )

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    settings_module
)

application = get_wsgi_application()
