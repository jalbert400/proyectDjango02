from django.urls import path
from miprimerapp.views import webscraping, about

urlpatterns = [
    path('',webscraping),
    path('about/',about)
]