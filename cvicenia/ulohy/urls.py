from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("ahoj_svet/", views.ahoj_svet, name="ahoj_svet"),
    path("o_mne/", views.o_mne, name="o_mne"),
    path("rozvrh/", views.rozvrh, name="rozvrh"),
	]