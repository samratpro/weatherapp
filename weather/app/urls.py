from app import views
from django.urls import path
from unicodedata import name


urlpatterns = [
    path('', views.home, name='home'),
]
