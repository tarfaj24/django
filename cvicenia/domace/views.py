from django.shortcuts import render

# Create your views here.

def domace(request):
    return render(request, "domace/domace.html", {"domace_text": "Moje domace ulohy"})

def du2_vizitka(request):
    moje_info = {"meno": "Jozef","trieda": "3.AT", "vek": 18, "oblubene_predmety": ["IOT", "Programovanie", "ANJ"]}
    return render(request, "domace/du2_vizitka.html", moje_info)