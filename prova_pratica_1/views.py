from django.shortcuts import render
import random
# Create your views here.
def index(request):
    return render(request,"prova_pratica_1/index.html")

def diff(request):
    num1=random.randint(1,20)
    num2= random.randint(1,20)
    context={
            "num1": num1,
             "num2": num2,
             }
    return render(request,"prova_pratica_1/diff.html",context)

def pari(request):
    array=[]
    for i in range(0,14):
        array.append(random.randint(1,20))
    return render(request,"prova_pratica_1/pari.html",context={"array": array,})