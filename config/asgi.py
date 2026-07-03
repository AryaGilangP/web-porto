# config/asgi.py
import os
from django.core.asgi import get_asgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Jalankan collectstatic otomatis saat Vercel melakukan inisialisasi aplikasi
try:
    call_command('collectstatic', '--noinput', '--clear')
except Exception as e:
    print(f"Collectstatic error: {e}")

application = get_asgi_application()

# Tetap kunci setting host agar aman dari DisallowedHost
from django.conf import settings
settings.ALLOWED_HOSTS = ['*']

app = application