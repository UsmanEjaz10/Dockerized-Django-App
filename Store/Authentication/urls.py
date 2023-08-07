from django.contrib import admin
from django.urls import path
from .views import Authentication_views

urlpatterns = [
    path("", Authentication_views.Authentication.as_view(), "login"),
]

