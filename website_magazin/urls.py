from django.urls import path, re_path # re_path la LABORATORUL 2 - TASK 1, CERINTA 5
from . import views


# LABORATORUL 1 - CERINTA 2: Rutele paginilor
urlpatterns = [
    path("", views.index, name="index"),
    path("info", views.info, name="info"),
    # LABORATORUL 2 - TASK 1, CERINTA 1: Ruta pentru pagina jurnalului de accesari
    path("log", views.log, name="log"),
    # LABORATORUL 2 - TASK 1, CERINTA 5: Ruta pentru paginile istoric si despre
    path("istoric", views.istoric, name="istoric"),
    path("despre", views.despre, name="despre"),
    # LABORATORUL 2 - TASK 1, CERINTA 5: Ruta pentru accesari individuale
    re_path(r"^accesare(?P<id>\d+)$", views.detalii_accesare, name="detalii_accesare"),
    # LABORATORUL 2 - TASK 2, CERINTA 4: Rutele paginilor din documentatie
    path("produse", views.pagina_in_constructie, name="produse"),
    path("contact", views.pagina_in_constructie, name="contact"),
    path("cos_virtual", views.pagina_in_constructie, name="cos_virtual"),
    path("ghid_marimi", views.pagina_in_constructie, name="ghid_marimi"),
    path("livrare_retururi", views.pagina_in_constructie, name="livrare_retururi"),
]