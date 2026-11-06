from django.shortcuts import render

# Create your views here.

def domace(request):
    return render(request, "domace/domace.html", {"domace_text": "Moje domace ulohy"})