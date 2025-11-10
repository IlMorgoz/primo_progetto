from django.urls import path
from seconda_app.views import es_if,es_if_else_elif,index

app_name="seconda_app"
urlpatterns=[
            path('',index,name="index"),
            path("es_if",es_if,name="es_if"),
            path("es_if_else_elif",es_if_else_elif,name="es_if_else_elif"),
             ]