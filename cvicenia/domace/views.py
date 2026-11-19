from django.shortcuts import render

# Create your views here.

def domace(request):
    return render(request, "domace/domace.html", {"domace_text": "Moje domace ulohy"})

def du2_vizitka(request):
    moje_info = {"meno": "Jozef","trieda": "3.AT", "vek": 18, "oblubene_predmety": ["IOT", "Programovanie", "ANJ"]}
    return render(request, "domace/du2_vizitka.html", moje_info)

def du3_teplota(request):
    vysledok = None
    if request.method == "POST":
        try:
            smer = str(request.POST["smer"])
            teplota = float(request.POST["teplota"])
            if smer == "F_to_C":
                vysledok = str(round((teplota - 32) * 5 / 9, 1)) + "°C"
            elif smer == "C_to_F":
                vysledok = str(round(teplota * 9 / 5 + 32, 1)) + "°F"
            else:
                vysledok = "Zly smer"
        except ValueError:
            vysledok = "Nemozem pracovat s pismenami"
        return render(request, "domace/du3_teplota.html", {"vysledok": vysledok})
    return render(request, "domace/du3_teplota.html", {"vysledok": vysledok})