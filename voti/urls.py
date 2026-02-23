from django.contrib import admin
from django.urls import path,include
from .views import view_a,view_b,view_c,view_d,index
app_name = 'voti'
urlpatterns = [
    path('',index, name="index"),
    path("materie/",view_a,name="materie"),
   path("materie_e_assenze/",view_b,name="MaterieEAssenze"),
   path("medie_voti/",view_c,name="MediaVoti"),
   path("min_max/",view_d,name="min_max_voti"),]