from django.urls import path
from . import views

urlpatterns = [
    path("browse", views.Browse.as_view(), name="browse")
]
