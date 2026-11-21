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

# LABORATORUL 2 - TASK 1, CERINTA 1: Lista pentru memorarea accesarilor
accesari = []


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

    # LABORATORUL 2 - TASK 1, CERINTA 1: Salvarea accesarii in lista
    accesari.append(accesare)

    # LABORATORUL 1 - CERINTA 9: Afisarea accesarii in consola
    print(accesare)

    return render(request, "website_magazin/index.html")


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

    # LABORATORUL 2 - TASK 1, CERINTA 1: Salvarea accesarii paginii info in lista
    accesari.append(accesare)

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

    # return HttpResponse(f"""
    #     <html>
    #         <head>
    #             <title>Informatii despre server</title>
    #         </head>
    #         <body>
    #             <h1>Informatii despre server</h1>
    #             <h2>Data si ora</h2>
    #             <!-- LABORATORUL 1 - CERINTA 10: Varianta noua -->
    #             {data_afisata}
    #         </body>
    #     </html>
    # """)

    # LABORATORUL 2 - TASK 2, CERINTA 6: Afisarea paginii info cu footer comun
    return render(request, "website_magazin/info.html", {
        "data_afisata": data_afisata
    })


# LABORATORUL 2 - TASK 1, CERINTA 1: Jurnalul accesarilor si filtrarea dupa ultimele
def log(request):

    url = request.build_absolute_uri()

    parametri = request.GET.dict()
    ip_client = request.ip_client
    accesare = Accesare(url, ip_client, parametri)
    accesari.append(accesare)

    continut = ""
    ultimele = request.GET.get("ultimele", "")

    try:
        if "ultimele" in request.GET:
            ultimele = int(ultimele)
    except ValueError:
        # return HttpResponse("Parametrul ultimele trebuie sa fie un numar intreg")
        # LABORATORUL 2 - TASK 2, CERINTA 6: Afisarea erorii pentru ultimele nenumeric cu footer comun
        return render(request, "website_magazin/log.html", {
            "continut": "Parametrul ultimele trebuie sa fie un numar intreg"
        })

    if ultimele != "" and ultimele < 0:
        # return HttpResponse("Numarul de accesari nu poate fi negativ")
        # LABORATORUL 2 - TASK 2, CERINTA 6: Afisarea erorii pentru ultimele negativ cu footer comun
        return render(request, "website_magazin/log.html", {
            "continut": "Numarul de accesari nu poate fi negativ"
        })

    accesari_de_afisat = accesari

    # LABORATORUL 2 - TASK 1, CERINTA 2: Numarul accesarilor si filtrarea dupa ID-uri
    iduri = request.GET.getlist("iduri")
    dubluri = request.GET.get("dubluri", "false")

    if "iduri" in request.GET:
        lista_iduri = []

        for grup in iduri:
            for id_accesare in grup.split(","):
                try:
                    id_accesare = int(id_accesare)
                except ValueError:
                    # return HttpResponse("Parametrul iduri trebuie sa contina doar numere intregi")
                    # LABORATORUL 2 - TASK 2, CERINTA 6: Afisarea erorii pentru iduri nenumeric cu footer comun
                    return render(request, "website_magazin/log.html", {
                        "continut": "Parametrul iduri trebuie sa contina doar numere intregi"
                    })

                if id_accesare not in lista_iduri or dubluri == "true":
                    lista_iduri.append(id_accesare)

        accesari_selectate = []

        for id_cautat in lista_iduri:
            for accesare in accesari:
                if id_cautat == accesare.id:
                    accesari_selectate.append(accesare)
                    break

        accesari_de_afisat = accesari_selectate

    numar_disponibile = len(accesari_de_afisat)

    if ultimele != "":
        if ultimele == 0:
            accesari_de_afisat = []
        else:
            accesari_de_afisat = accesari_de_afisat[-ultimele:]

    if "tabel" not in request.GET:
        for accesare in accesari_de_afisat:
            continut += str(accesare).replace("\n", "<br>") + "<hr>"

    if request.GET.get("accesari") == "nr":
        continut += f"<section><h2>Numar total de accesari</h2><p>{len(accesari)}</p></section>"

    # LABORATORUL 2 - TASK 1, CERINTA 3: Detaliile accesarilor si parametrii cererii
    if request.GET.get("accesari") == "detalii":
        continut += "<ul>"

        for accesare in accesari:
            continut += f"<li>{accesare.calculeaza_data()}</li>"

        continut += "</ul>"

    continut += "<h2>Parametri</h2>"
    continut += f"<p>Numar parametri: {len(request.GET)}</p>"
    continut += f"<p>Nume parametri: {', '.join(request.GET.keys())}</p>"

    # LABORATORUL 2 - TASK 1, CERINTA 4: Afisarea accesarilor intr-un tabel HTML
    tabel = request.GET.get("tabel")

    if "tabel" in request.GET:
        if tabel == "tot":
            coloane = ["id", "url", "ip_client", "parametri", "data"]
        else:
            coloane = tabel.split(",")

        continut += "<table>"
        continut += "<tr>"

        for coloana in coloane:
            continut += f"<th>{coloana}</th>"

        continut += "</tr>"

        for accesare in accesari_de_afisat:
            continut += "<tr>"

            for coloana in coloane:
                continut += f"<td>{getattr(accesare, coloana)}</td>"

            continut += "</tr>"

        continut += "</table>"

    # LABORATORUL 2 - TASK 1, CERINTA 5: Pagina cea mai accesata si cea mai putin
    numar_accesari = {
    "/": 0,
    "/info": 0,
    "/log": 0,
    "/istoric": 0,
    "/despre": 0
    }

    for accesare in accesari:
        pagina = accesare.pagina()

        if pagina in numar_accesari:
            numar_accesari[pagina] += 1
        else:
            numar_accesari[pagina] = 1

    if numar_accesari:
        pagina_maxima = max(numar_accesari, key=numar_accesari.get)
        pagina_minima = min(numar_accesari, key=numar_accesari.get)

        continut += f"<p>Pagina cea mai accesata: {pagina_maxima}</p>"
        continut += f"<p>Pagina cea mai putin accesata: {pagina_minima}</p>"

    if ultimele != "" and ultimele > numar_disponibile:
        continut += f"Exista doar {numar_disponibile} accesari fata de {ultimele} accesari cerute"

    # LABORATORUL 2 - TASK 2, CERINTA 6: Afisarea jurnalului cu footer comun
    return render(request, "website_magazin/log.html", {
        "continut": continut
})

# LABORATORUL 2 - TASK 1, CERINTA 5: Paginile istoric si despre
def istoric(request):
    url = request.build_absolute_uri()
    ip_client = request.ip_client
    parametri = request.GET.dict()
    accesare = Accesare(url, ip_client, parametri)
    accesari.append(accesare)

    # LABORATORUL 2 - TASK 2, CERINTA 6: Afisarea paginii istoric cu footer comun
    return render(request, "website_magazin/pagina.html", {
        "titlu": "Istoric KomfortSchuhe",
        "descriere": "KomfortSchuhe este un magazin online de incaltaminte sport, creat pentru a oferi modele confortabile pentru femei. Aceasta pagina va prezenta evolutia si povestea magazinului."
    })


def despre(request):
    url = request.build_absolute_uri()
    ip_client = request.ip_client
    parametri = request.GET.dict()
    accesare = Accesare(url, ip_client, parametri)
    accesari.append(accesare)

    # return HttpResponse("""
    #     <h1>Despre KomfortSchuhe</h1>
    #     <p>KomfortSchuhe este un magazin online specializat in incaltaminte sport
    #     pentru femei. Ne propunem sa oferim produse care imbina
    #     confortul, functionalitatea si stilul.</p>
    # """)

    # LABORATORUL 2 - TASK 2, CERINTA 6: Afisarea paginii despre cu footer comun
    return render(request, "website_magazin/despre.html", {
        "titlu": "Despre KomfortSchuhe",
        "descriere": "KomfortSchuhe este un magazin online specializat in incaltaminte sport pentru femei. Ne propunem sa oferim produse care imbina confortul, functionalitatea si stilul."
    })

# LABORATORUL 2 - TASK 1, CERINTA 5: Afisarea detaliilor unei accesari dupa ID
def detalii_accesare(request, id):
    url = request.build_absolute_uri()
    ip_client = request.ip_client
    parametri = request.GET.dict()
    accesare = Accesare(url, ip_client, parametri)
    accesari.append(accesare)

    id = int(id)

    # LABORATORUL 2 - TASK 2, CERINTA 6: Afisarea detaliilor cu footer comun
    for accesare in accesari:
        if accesare.id == id:
            return render(request, "website_magazin/accesare.html", {
                "accesare": accesare
            })

    return render(request, "website_magazin/pagina.html", {
        "titlu": "Accesare inexistenta",
        "descriere": "Accesarea nu exista"
    })

# LABORATORUL 2 - TASK 2, CERINTA 4: Pagini care vor fi implementate ulterior
def pagina_in_constructie(request):
    url = request.build_absolute_uri()
    ip_client = request.ip_client
    parametri = request.GET.dict()
    accesare = Accesare(url, ip_client, parametri)
    accesari.append(accesare)

    # # LABORATORUL 2 - TASK 2, CERINTA 6: Footer comun pentru paginile temporare
    # return render(request, "website_magazin/pagina.html", {
    #     "titlu": "Pagina in constructie",
    #     "descriere": "Pagina va fi implementata ulterior."
    # })
    # LABORATORUL 2 - TASK 2, CERINTA 10: Afisarea template-ului in_lucru.html
    return render(request, "website_magazin/in_lucru.html")
