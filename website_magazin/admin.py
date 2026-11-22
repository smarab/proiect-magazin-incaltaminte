from django.contrib import admin

# LABORATORUL 3 - TASK 2
from .models import (
    Brand,
    Categorie,
    Colectie,
    InstructiuneIntretinere,
    Material,
    Produs
)

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nume', 'ordine_afisare', 'culoare')

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('nume', 'tara_origine', 'an_infiintare')

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('nume', 'tip_material')

@admin.register(Colectie)
class ColectieAdmin(admin.ModelAdmin):
    list_display = ('nume', 'sezon', 'an_lansare')

@admin.register(Produs)
class ProdusAdmin(admin.ModelAdmin):
    list_display = (
        'nume',
        'brand',
        'categorie',
        'colectie',
        'pret',
        'marimi_disponibile',
        'tip_inchidere',
        'impermeabil',
        'stoc'
    )

@admin.register(InstructiuneIntretinere)
class InstructiuneIntretinereAdmin(admin.ModelAdmin):
    list_display = (
        'produs',
        'numar_instructiune',
        'tip_intretinere',
        'este_avertisment'
    )
