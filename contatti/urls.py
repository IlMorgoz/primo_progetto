from django.urls import path
from .views import contatti,index,lista_contatti

app_name="contatti"

urlpatterns = [
    path('contattaci/', contatti, name='contatti'),
    path('', index, name='index'),
    path('lista_contatti/', lista_contatti, name='lista_contatti'),
]