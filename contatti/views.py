from django.shortcuts import render
from django.shortcuts import render
from .form import FormContatto
# Create your views here.
def contatti(request):
    form = FormContatto()
    context = {"form": form}
    return render(request, "contatto.html", context)