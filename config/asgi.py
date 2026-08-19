"""
ASGI config for portfoliofx project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from dotenv import load_dotenv


load_dotenv()

settings_module = os.environ.get("DJANGO_SETTINGS_MODULE")

if not settings_module:
    raise RuntimeError(
        "From asgi: DJANGO_SETTINGS_MODULE environment variable is not set."
    )

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    settings_module
)

application = get_asgi_application()
