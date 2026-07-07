from django.contrib import admin
from django.urls import path
from shortner import views 

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<str:short_code>/", views.redirect_url, name="redirect_url"),
]