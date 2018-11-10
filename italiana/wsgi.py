"""
WSGI config for italiana project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "italiana.settings")
# os.environ["DJANGO_SETTINGS_MODULE"] = "italiana.settings"  # para usar en un solo demon de Apache

application = get_wsgi_application()
