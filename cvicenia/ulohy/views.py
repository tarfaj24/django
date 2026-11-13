from django.shortcuts import render, HttpResponse
import datetime

def ahoj_svet(request):
    return HttpResponse("Ahoj svet")

def o_mne(request):
    kontext = {
        "meno": "Jozef",
        "vek": 18,
        "zaluby": ["programovanie", "lezenie", "anime"]
    }
    return render(request, "ulohy/o_mne.html", kontext)

def rozvrh(request):
    hodiny = [
        {"cislo":1, "predmet": "Programovanie"},
        {"cislo":2, "predmet": "Programovanie"},
        {"cislo":3, "predmet": "Matematika"},
        {"cislo":4, "predmet": "Prax"},
        {"cislo":5, "predmet": "Prax"},
        {"cislo":6, "predmet": "Anglický jazyk"}
    ]
    return render(request, "ulohy/rozvrh.html", {"den": "Pondelok", "hodiny": hodiny})

def pozdrav(request):
    meno = request.GET.get("meno","") # .get() najde a vrati hodnotu prvu s indexom(klucom) meno, ak ho nenajde vlozi prazdny string
    return render(request, "ulohy/pozdrav.html", {"meno": meno} )

def sucet(request):
    vysledok = None
    if request.method == "POST":
        cislo1 = float(request.POST["a"])
        cislo2 = float(request.POST["b"])
        vysledok = cislo1 + cislo2
    return render(request, "ulohy/sucet.html", {"vysledok": vysledok})

def kalkulacka(request):
    vysledok = None
    if request.method == "POST":
        cislo1 = float(request.POST["a"])
        cislo2 = float(request.POST["b"])
        operator = request.POST["vyber_operatora"]
        if operator == "+":
            vysledok = cislo1 + cislo2
        elif operator == "-":
            vysledok = cislo1 - cislo2
        elif operator == "*":
            vysledok = cislo1 * cislo2
    return render(request, "ulohy/kalkulacka.html", {"vysledok": vysledok})


def obdlznik(request):
    vysledok = None
    if request.method == "POST":
        try:
            cislo1 = float(request.POST["a"])
            cislo2 = float(request.POST["b"])
            operator = request.POST["operator"]
            if operator == "obvod":
                        vysledok = round(2 *(cislo1 + cislo2), 2)
            elif operator == "obsah":
                vysledok = round(cislo1 * cislo2, 2)
        except ValueError:
            vysledok = "Nemozem pracovat s pismenami"
        
        
    return render(request, "ulohy/obdlznik.html", {"vysledok": vysledok})

def vek(request):
    vek = None
    if request.method == "POST":
        x = datetime.datetime.now()
        akt_rok = x.year
        rok_narodenia = int(request.POST["rok"])
        vek = akt_rok - rok_narodenia
    return render(request, "ulohy/vek.html", {"vek": vek})