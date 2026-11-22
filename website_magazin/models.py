from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone


# LAB 3 - TASK 1
# MODEL 1: CATEGORIE

class Categorie(models.Model):

    id_categorie = models.AutoField(primary_key=True)

    # Cerintele 2, 9
    nume = models.CharField(
        max_length=60,
        unique=True,
        error_messages={
            "unique": "Exista deja o categorie cu acest nume.",
            "max_length": "Numarul maxim de caractere este 60."
        }
    )

    # Cerinta 1
    descriere = models.TextField(
        blank=True,
        null=True
    )

    # Cerintele 6, 7
    culoare = models.CharField(
        max_length=7,
        default="#1E40AF",
        help_text="Introduceti culoarea in format HEX, de exemplu #FF5733."
    )

    # Cerintele 1, 3, 7
    sigla = models.SlugField(
        max_length=80,
        blank=True,
        null=True,
        help_text="Numele iconitei, de exemplu fa-shoe-prints."
    )

    # Cerintele 6, 7, 9, 11
    ordine_afisare = models.PositiveIntegerField(
        default=1,
        db_index=True,
        help_text="Pozitia categoriei in meniu, incepand de la 1.",
        error_messages={
            "invalid": "Introduceti un numar intreg valid."
        }
    )

    class Meta:
        verbose_name = 'categorie'
        verbose_name_plural = 'categorii'
        # Cerinta 4
        ordering = ["ordine_afisare", "nume"]

        # Cerinta 10
        constraints = [
            models.CheckConstraint(
                condition=models.Q(ordine_afisare__gte=1),
                name="categorie_ordine_minim_1"
            )
        ]

    def __str__(self):
        return self.nume


# LAB 3 - TASK 1 - PROGRES DUPA CATEGORIE (1/6 modele)
# 1. 2/5 campuri cu NULL
# 2. 1/1 camp unic
# 3. 1/1 SlugField
# 4. 1/2 modele cu ordering
# 5. 0/1 campuri cu choices
# 6. 2/4 campuri cu default
# 6. 0/1 campuri cu default + blank=True
# 7. 3/5 campuri cu help_text
# 8. 0/1 campuri DateTimeField cu default
# 9. 2/5 campuri cu error_messages
# 10. 1/5 constrangeri models.Q
# 11. 1/4 campuri indexate
# 12. 0/1 ImageField sau FileField


# MODEL 2: BRAND
class Brand(models.Model):

    id_brand = models.AutoField(primary_key=True)

    # Cerintele 2, 9
    nume = models.CharField(
        max_length=80,
        unique=True,
        error_messages={
            "unique": "Acest brand exista deja."
        }
    )

    # Cerintele 1, 7, 9, 11
    tara_origine = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        db_index=True,
        help_text="Tara in care a fost fondat brandul.",
        error_messages={
            "max_length": "Tara nu poate depasi 60 de caractere."
        }
    )

    # Cerintele 1, 7, 9
    an_infiintare = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="Anul in care a fost fondat brandul.",
        error_messages={
            "invalid": "Introduceti un an valid."
        }
    )

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'branduri'
        # Cerinta 4
        ordering = ["nume"]

        # Cerinta 10
        constraints = [
            models.CheckConstraint(
                condition=(
                    models.Q(an_infiintare__gte=1800) |
                    models.Q(an_infiintare__isnull=True)
                ),
                name="brand_an_minim_1800"
            )
        ]

    def __str__(self):
        return self.nume


# LAB 3 - TASK 1 - PROGRES DUPA BRAND (2/6 modele)
# 1. 4/5 campuri cu NULL
# 2. 1/1 camp unic
# 3. 1/1 SlugField
# 4. 2/2 modele cu ordering
# 5. 0/1 campuri cu choices
# 6. 2/4 campuri cu default
# 6. 0/1 campuri cu default + blank=True
# 7. 5/5 campuri cu help_text
# 8. 0/1 campuri DateTimeField cu default
# 9. 5/5 campuri cu error_messages
# 10. 2/5 constrangeri models.Q
# 11. 2/4 campuri indexate
# 12. 0/1 ImageField sau FileField


# MODEL 3: MATERIAL
class Material(models.Model):

    id_material = models.AutoField(primary_key=True)

    # Cerinta 5
    TIPURI_MATERIAL = [
        ("textil", "Textil"),
        ("piele", "Piele"),
        ("cauciuc", "Cauciuc"),
        ("spuma", "Spuma"),
        ("sintetic", "Sintetic")
    ]

    # Cerinta 2
    nume = models.CharField(
        max_length=80,
        unique=True
    )

    # Cerintele 1, 6
    descriere = models.TextField(
        blank=True,
        null=True,
        default="Fara descriere"
    )

    # Cerintele 5, 6, 11
    tip_material = models.CharField(
        max_length=20,
        choices=TIPURI_MATERIAL,
        default="textil",
        db_index=True
    )

    class Meta:
        verbose_name = 'material'
        verbose_name_plural = 'materiale'
        # Cerinta 10
        constraints = [
            models.CheckConstraint(
                condition=models.Q(
                    tip_material__in=[
                        "textil",
                        "piele",
                        "cauciuc",
                        "spuma",
                        "sintetic"
                    ]
                ),
                name="material_tip_permis"
            )
        ]

    def __str__(self):
        return self.nume


# LAB 3 - TASK 1 - PROGRES DUPA MATERIAL (3/6 modele)
# 1. 5/5 campuri cu NULL
# 2. 1/1 camp unic
# 3. 1/1 SlugField
# 4. 2/2 modele cu ordering
# 5. 1/1 campuri cu choices
# 6. 4/4 campuri cu default
# 6. 1/1 campuri cu default + blank=True
# 7. 5/5 campuri cu help_text
# 8. 0/1 campuri DateTimeField cu default
# 9. 5/5 campuri cu error_messages
# 10. 3/5 constrangeri models.Q
# 11. 3/4 campuri indexate
# 12. 0/1 ImageField sau FileField


# MODEL 4: COLECTIE
class Colectie(models.Model):

    id_colectie = models.AutoField(primary_key=True)

    # Cerinta 5
    SEZOANE = [
        ("primavara", "Primavara"),
        ("vara", "Vara"),
        ("toamna", "Toamna"),
        ("iarna", "Iarna")
    ]

    nume = models.CharField(
        max_length=100
    )

    # Cerintele 5, 11
    sezon = models.CharField(
        max_length=20,
        choices=SEZOANE,
        db_index=True
    )

    # Cerinta 7
    an_lansare = models.PositiveIntegerField(
        help_text="Anul lansarii colectiei, de exemplu 2026."
    )

    class Meta:
        verbose_name = 'colectie'
        verbose_name_plural = 'colectii'
        # Cerinta 10
        constraints = [
            models.CheckConstraint(
                condition=models.Q(an_lansare__gte=1900),
                name="colectie_an_minim_1900"
            )
        ]

    def __str__(self):
        return self.nume


# LAB 3 - TASK 1 - PROGRES DUPA COLECTIE (4/6 modele)
# 1. 5/5 campuri cu NULL
# 2. 1/1 camp unic
# 3. 1/1 SlugField
# 4. 2/2 modele cu ordering
# 5. 1/1 campuri cu choices
# 6. 4/4 campuri cu default
# 6. 1/1 campuri cu default + blank=True
# 7. 5/5 campuri cu help_text
# 8. 0/1 campuri DateTimeField cu default
# 9. 5/5 campuri cu error_messages
# 10. 4/5 constrangeri models.Q
# 11. 4/4 campuri indexate
# 12. 0/1 ImageField sau FileField


# MODEL 5: PRODUS
class Produs(models.Model):

    id_produs = models.AutoField(primary_key=True)

    TIPURI_INCHIDERE = [
        ("sireturi", "Sireturi"),
        ("slip_on", "Slip-on"),
        ("velcro", "Velcro")
    ]

    # Cerinta 9
    nume = models.CharField(
        max_length=150,
        error_messages={
            "max_length": "Numele produsului este prea lung."
        }
    )

    # Cerinta 1
    descriere = models.TextField(
        blank=True,
        null=True
    )

    # Cerintele 10, 11
    pret = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        db_index=True
    )

    marimi_disponibile = ArrayField(
        models.PositiveIntegerField(),
        default=list,
        blank=True
    )

    culoare = models.CharField(
        max_length=50
    )

    # Cerinta 5
    tip_inchidere = models.CharField(
        max_length=20,
        choices=TIPURI_INCHIDERE,
        default="sireturi"
    )

    impermeabil = models.BooleanField(
        default=False
    )

    # Cerinta 1
    data_lansare = models.DateField(
        blank=True,
        null=True
    )

    stoc = models.PositiveIntegerField(
        default=0
    )

    # Cerintele 1, 12
    imagine = models.ImageField(
        upload_to="produse/",
        blank=True,
        null=True
    )

    # Cerinta 8
    data_adaugare = models.DateTimeField(
        default=timezone.now
    )

    # Relatii One-to-Many
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.PROTECT,
        related_name="produse",
        db_column="id_categorie"
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        related_name="produse",
        db_column="id_brand"
    )

    colectie = models.ForeignKey(
        Colectie,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="produse",
        db_column="id_colectie"
    )

    # Relatie Many-to-Many
    materiale = models.ManyToManyField(
        Material,
        blank=True,
        related_name="produse"
    )

    class Meta:
        verbose_name = 'produs'
        verbose_name_plural = 'produse'
        # Cerinta 10
        constraints = [
            models.CheckConstraint(
                condition=models.Q(pret__gt=0),
                name="produs_pret_pozitiv"
            )
        ]

    def __str__(self):
        return self.nume


# LAB 3 - TASK 1 - PROGRES DUPA PRODUS (5/6 modele)
# 1. 5/5 campuri cu NULL
# 2. 1/1 camp unic
# 3. 1/1 SlugField
# 4. 2/2 modele cu ordering
# 5. 1/1 campuri cu choices
# 6. 4/4 campuri cu default
# 6. 1/1 campuri cu default + blank=True
# 7. 5/5 campuri cu help_text
# 8. 1/1 campuri DateTimeField cu default
# 9. 5/5 campuri cu error_messages
# 10. 5/5 constrangeri models.Q
# 11. 4/4 campuri indexate
# 12. 1/1 ImageField sau FileField


# MODEL 6: INSTRUCTIUNE INTRETINERE
class InstructiuneIntretinere(models.Model):

    # Cerinta 5
    TIPURI_INTRETINERE = [
        ("curatare", "Curatare"),
        ("uscare", "Uscare"),
        ("depozitare", "Depozitare")
    ]

    id_instructiune = models.AutoField(
        primary_key=True
    )

    # Relatie One-to-Many
    produs = models.ForeignKey(
        Produs,
        on_delete=models.CASCADE,
        related_name="instructiuni_intretinere",
        db_column="id_produs"
    )

    numar_instructiune = models.PositiveIntegerField()

    descriere = models.TextField()

    # Cerinta 5
    tip_intretinere = models.CharField(
        max_length=20,
        choices=TIPURI_INTRETINERE
    )

    este_avertisment = models.BooleanField(
        default=False
    )

    class Meta:
        verbose_name = 'instructiune de intretinere'
        verbose_name_plural = 'instructiuni de intretinere'
        # Cerinta 4
        ordering = ["produs_id", "numar_instructiune"]

        constraints = [
            models.UniqueConstraint(
                fields=["produs", "numar_instructiune"],
                name="instructiune_unica_per_produs"
            ),

            # Cerinta 10
            models.CheckConstraint(
                condition=models.Q(numar_instructiune__gte=1),
                name="instructiune_numar_minim_1"
            )
        ]

    def __str__(self):
        return f"{self.produs.nume} - Instructiunea {self.numar_instructiune}"


# LAB 3 - TASK 1 - PROGRES FINAL (6/6 modele)
# 1. 5/5 campuri cu NULL
# 2. 1/1 camp unic
# 3. 1/1 SlugField
# 4. 2/2 modele cu ordering
# 5. 1/1 campuri cu choices
# 6. 4/4 campuri cu default
# 6. 1/1 campuri cu default + blank=True
# 7. 5/5 campuri cu help_text
# 8. 1/1 campuri DateTimeField cu default
# 9. 5/5 campuri cu error_messages
# 10. 5/5 constrangeri models.Q
# 11. 4/4 campuri indexate
# 12. 1/1 ImageField sau FileField
