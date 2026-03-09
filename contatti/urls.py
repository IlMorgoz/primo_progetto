from django.urls import path
from .views import contatti,index,lista_contatti,modifica_contatto,elimina_contatto,grazie

app_name="contatti"

urlpatterns = [
    path('contattaci/', contatti, name='contatti'),
    path('', index, name='index'),
    path('lista_contatti/', lista_contatti, name='lista_contatti'),
    path('modifica_contatto/<int:pk>/', modifica_contatto, name='modifica_contatto'),
    path('elimina_contatto/<int:pk>/', elimina_contatto, name='elimina_contatto'),
    path('grazie/', grazie, name='grazie'),
]