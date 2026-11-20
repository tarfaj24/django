from django.shortcuts import render

# Create your views here.

def cv1_index(request):
    return render(request, "cv1/cv1_index.html", {"meno": "Jozef Tarfa"})

def cv1_obchod(request):
    max_cena = request.GET.get("max_cena")

    obchodne_data = [{"nazov": "Pero", "cena": 2.5445},
                     {"nazov": "Zošit", "cena": 4.99},
                     {"nazov": "Guma", "cena": 1},
                     {"nazov": "Taška", "cena": 10.2898},
                    ]
    if max_cena:
        try:
            max_cena = float(max_cena)
            return render(request, "cv1/cv1_obchod.html", {"obchodne_data": obchodne_data, "max_cena": max_cena, "error": None})
        except ValueError:
            return render(request, "cv1/cv1_obchod.html", {"obchodne_data": obchodne_data, "max_cena": None, "error": "Max cena musi byť v tvare čísla!"})

    return render(request, "cv1/cv1_obchod.html", {"obchodne_data": obchodne_data, "max_cena": None, "error": None})

def cv1_body(request):
    vysledok = None
    error= None
    if request.method == "POST":
        try:
            body = float(request.POST["body"])
            maximum = float(request.POST["maximum"])
            vysledok = round((body / maximum) * 100, 2)
            return render(request, "cv1/cv1_body.html", {"vysledok": vysledok, "body": body,"maximum": maximum, "error": error})
        except ValueError:
            return render(request, "cv1/cv1_body.html", {"vysledok": "Musi byť v tvare čísla!", "error": True})
    return render(request, "cv1/cv1_body.html", {"vysledok": vysledok, "error": error})