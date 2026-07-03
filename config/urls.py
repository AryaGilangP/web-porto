# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Change 'admin.site.url_matches' to 'admin.site.urls'
    path('admin/', admin.site.urls), 
    path('', include('core.urls')), 
]