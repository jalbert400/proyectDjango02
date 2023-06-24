from django.contrib import admin
from django.urls import path,include
from proyectDjango02.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('home/', home),
    #path('miprimerapp/', include('miprimerapp.urls'))
    #path('', home),
    path('', include('miprimerapp.urls'))
]
