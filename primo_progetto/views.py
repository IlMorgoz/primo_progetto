from django.shortcuts import render
def index_root(request):
    return render(request,"index_root.html")
def base(request):
    return render(request,"base.html")