from django import template
from news.models import Giornalista

register = template.Library()

@register.filter
def get_nome_giornalista(value):
    try:
        giornalista = Giornalista.objects.get(id=value)
        return f"{giornalista.nome} {giornalista.cognome}"
    except Giornalista.DoesNotExist:
        return "N/A"