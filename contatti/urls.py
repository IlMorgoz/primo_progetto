from django.urls import path
from .views import contatti

app_name="contatti"

urlpatterns = [
    path('/contattaci', contatti, name='contatti'),
]