from django.urls import path
from prova_pratica_1.views import index,diff,pari

app_name="prova_pratica_1"
urlpatterns=[
             path ('',index, name="index"),
             path('view_x',diff,name="differenza"),
             path('view_y',pari,name="pari_dispari")]