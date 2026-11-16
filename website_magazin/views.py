from django.shortcuts import render
# LABORATORUL 1 - CERINTA 2, 3: Raspunsuri HTTP
from django.http import HttpResponse
# LABORATORUL 1 - CERINTA 3, 4: Data si ora
from datetime import datetime
# LABORATORUL 1 - CERINTA 6: Parsare URL
from urllib.parse import urlparse

# LABORATORUL 1 - CERINTA 7: Liste mutate din cerinta 3
zile = ["Luni", "Marti", "Miercuri", "Joi", "Vineri", "Sambata", "Duminica"]
luni = ["Ianuarie", "Februarie", "Martie", "Aprilie", "Mai", "Iunie", "Iulie", "August", "Septembrie", "Octombrie", "Noiembrie", "Decembrie"]


# LABORATORUL 1 - CERINTA 4: Clasa Accesare
class Accesare:
    id_curent = 0

    def __init__(self, url, ip_client, parametri=None):

        Accesare.id_curent += 1
        self.id = Accesare.id_curent

        self.url = url
        self.ip_client = ip_client

        if parametri is None:
            parametri = {}

        self.parametri = parametri
        self.data = datetime.now()

    # LABORATORUL 1 - CERINTA 5: Lista parametrilor
    def lista_parametri(self):
        return list(self.parametri.items())

    #LABORATORUL 1 - CERINTA 6: URL complet
    def string_url(self):
        return self.url
    # LABORATORUL 1 - CERINTA 6: Pagina accesata
    def pagina(self):
        return urlparse(self.url).path

    # LABORATORUL 1 - CERINTA 7: Calculare data accesarii

    # LABORATORUL 1 - CERINTA 7: Varianta initiala
    # def calculeaza_data(self, format="%A, %d %B %Y"):
    #     nume_zi = zile[self.data.weekday()]
    #     zi = self.data.day
    #     nume_luna = luni[self.data.month-1]
    #
    #     format = format.replace("%A", nume_zi)
    #     format = format.replace("%B", nume_luna)
    #     format = format.replace("%d", str(zi))
    #
    #     return self.data.strftime(format)

    # LABORATORUL 1 - CERINTA 10: Varianta noua
    def calculeaza_data(self, format="%A, %d %B %Y", tip=""):
        nume_zi = zile[self.data.weekday()]
        zi = self.data.day
        nume_luna = luni[self.data.month-1]

        if tip == "zi":
            format_data = "%d %B %Y"
        else:
            format_data = format

        format_data = format_data.replace("%A", nume_zi)
        format_data = format_data.replace("%B", nume_luna)
        format_data = format_data.replace("%d", str(zi))

        data_formatata = self.data.strftime(format_data)
        ora_formatata = self.data.strftime("%H:%M:%S")

        if tip == "zi":
            return f"<p>{data_formatata}</p>"
        elif tip == "timp":
            return f"<p>{ora_formatata}</p>"
        else:
            return f"<p>{data_formatata} - Ora: {ora_formatata}</p>"

    # LABORATORUL 1 - CERINTA 9: Afisarea datelor unei accesari
    def __str__(self):
        return f"id: {self.id}\nip_client: {self.ip_client}\nstring_url: {self.string_url()}\npagina: {self.pagina()}\ncalculeaza_data: {self.calculeaza_data()}\nlista_parametri: {self.lista_parametri()}"

# LABORATORUL 1 - CERINTA 2: Pagina principala
def index(request):
    # LABORATORUL 1 - CERINTA 4: Crearea accesărilor
    url = request.build_absolute_uri() # LABORATORUL 1 - CERINTA 6: Obtinere URL absolut

    # LABORATORUL 1 - CERINTA 4: Varianta initiala
    # ip_client = request.META.get("REMOTE_ADDR")
    # LABORATORUL 1 - CERINTA 8: Obtinere IP prin middleware
    ip_client = request.ip_client

    parametri = request.GET.dict()
    accesare = Accesare(url, ip_client, parametri)

    # LABORATORUL 1 - CERINTA 9: Afisarea accesarii in consola
    print(accesare)

    return HttpResponse(
        "KomfortSchuhe - Magazin online de incaltaminte sport"
        " pentru femei, dezvoltat folosind Python si Django"
    )


# LABORATORUL 1 - CERINTA 3: Data si ora
def info(request):
    # LABORATORUL 1 - CERINTA 4: Crearea accesărilor
    url = request.build_absolute_uri() # LABORATORUL 1 - CERINTA 6: Obtinere URL absolut

    # LABORATORUL 1 - CERINTA 4: Varianta initiala
    # ip_client = request.META.get("REMOTE_ADDR")
    # LABORATORUL 1 - CERINTA 8: Obtinere IP prin middleware
    ip_client = request.ip_client

    parametri = request.GET.dict()

    # LABORATORUL 1 - CERINTA 10: Preluare parametru data
    data = request.GET.get("data", "")

    accesare = Accesare(url, ip_client, parametri)

    # LABORATORUL 1 - CERINTA 9: Afisarea accesarii in consola
    print(accesare)

    # LABORATORUL 1 - CERINTA 3: Varianta initiala
    # data_curenta = datetime.now()
    # numar_zi = data_curenta.weekday()
    # nume_zi = zile[numar_zi]
    # nume_luna = luni[data_curenta.month-1]

    # LABORATORUL 1 - CERINTA 7: Folosirea metodei calculeaza_data()
    # LABORATORUL 1 - CERINTA 7: Varianta initiala
    # data_afisata = accesare.calculeaza_data()

    # LABORATORUL 1 - CERINTA 10: Transmiterea parametrului data
    data_afisata = accesare.calculeaza_data(tip=data)

    # LABORATORUL 1 - CERINTA 3: Varianta initiala din HttpResponse
    # <p>{nume_zi}, {data_curenta.day} {nume_luna} {data_curenta.year} - Ora: {data_curenta.hour:02d}:{data_curenta.minute:02d}:{data_curenta.second:02d}</p>

    # LABORATORUL 1 - CERINTA 7: Varianta veche din HttpResponse
    # <p>{data_afisata} - Ora: {accesare.data.hour:02d}:{accesare.data.minute:02d}:{accesare.data.second:02d}</p>

    return HttpResponse(f"""
        <html>
            <head>
                <title>Informatii despre server</title>
            </head>
            <body>
                <h1>Informatii despre server</h1>
                <h2>Data si ora</h2>
                <!-- LABORATORUL 1 - CERINTA 10: Varianta noua -->
                {data_afisata}
            </body>
        </html>
    """)