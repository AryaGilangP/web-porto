# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/<str:project_slug>/', views.project_detail, name='project_detail'),
    path('about/', views.about, name='about'),
]