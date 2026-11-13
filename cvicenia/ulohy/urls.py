from django.contrib import admin
from django.urls import path
from ulohy.views import o_mne, ahoj_svet, rozvrh, pozdrav, sucet, kalkulacka, obdlznik, vek

urlpatterns = [
    path("ahoj_svet/", ahoj_svet, name="ahoj_svet"),
    path("o_mne/", o_mne, name="o_mne"),
    path("rozvrh/", rozvrh, name="rozvrh"),
    path("pozdrav/", pozdrav, name="pozdrav"),
    path("sucet/", sucet, name="sucet"),
    path("kalkulacka/", kalkulacka, name="kalkulacka"),
    path("obdlznik/", obdlznik, name="obdlznik"),
    path("vek/", vek, name="vek"),
	]