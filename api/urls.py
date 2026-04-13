from django.urls import path
from .views import todos_view,index

app_name="api"
urlpatterns=[path ('todos/',todos_view, name="todos"),
             path ('/',index, name="index"),]