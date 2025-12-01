from django.shortcuts import render
import random
# Create your views here.
def index(request):
    return render(request,"prova_pratica_1/index.html")

def diff(request):
    num1=random.randint(1,20)
    num2= random.randint(1,20)
    if num1>num2: diff=num1-num2 
    else: diff=num2-num1
    context={
                "num1": num1,
                "num2": num2,
                "diff": diff
            }
    return render(request,"prova_pratica_1/diff.html",context)

def pari(request):
    array=[]
    pari=0
    dispari=0
    for i in range(0,15):
        array.append(random.randint(1,20))
        if array[-1]%2==0:
            pari+=1
        else:
            dispari+=1

    return render(request,"prova_pratica_1/pari.html",context={"array": array,"pari": pari,"dispari":dispari})