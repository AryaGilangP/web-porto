"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

# config/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

# PENTING: Suntikkan override host secara langsung ke setelan runtime Django
from django.conf import settings
settings.ALLOWED_HOSTS = ['*']

# Handler untuk Vercel
app = application
