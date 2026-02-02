from django.urls import path
from .views import home, articoloDetailView, listaArticoli, queryBase,giornalista_detail,index_news

app_name = 'news'
urlpatterns = [
    path("/homepage", home, name="home"),
    path("/articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("/lista_articoli", listaArticoli, name="lista_articoli"),
    path("/lista_articoli/<int:pk>", listaArticoli, name="lista_articoli"),
    path("/query_base",queryBase, name="query_base"),
    path("/giornalista/<int:pk>",giornalista_detail, name="giornalista_detail"),
    path("", index_news, name="index_news"),
]
