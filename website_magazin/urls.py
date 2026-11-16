from django.urls import path
from . import views


# LABORATORUL 1 - CERINTA 2: Rutele paginilor
urlpatterns = [
    path("", views.index, name="index"),
    path("info", views.info, name="info"),
]