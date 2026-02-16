from django.shortcuts import render

voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
       'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
       'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
# Create your views here.
def index(request):
    return  render(request,"voti/indexVoti.html")
def view_a(request):
    context = {"materie":["Matematica","Italiano","Inglese","Storia","Geografia"]}
    return render(request,"voti/materie.html",context)
def view_b(request):
    return render(request,"voti/MaterieEAssenze.html",context={"voti":voti})
def view_c(request):
    medie=[]
    for studente in voti:
        media=[]
        for data in voti[studente]:
            media.append(data[1])
        medie.append(tuple ([studente,sum(media)/len(media)]))
    return render(request,"voti/MediaVoti.html",context={"medie":medie})
def view_d(request):
    voto_min=999
    voto_max=0
    studenti_min=[]
    studenti_max = []
    materie_min = []
    materie_max = []
    for studente in voti:
        for data in voti[studente]:
            if data[1]<voto_min:
                studenti_min.clear()
                materie_min.clear()
                voto_min=data[1]
                studenti_min.append(studente)
                materie_min.append(data[0])
            elif data[1]==voto_min:
                if studente not in materie_min:
                    studenti_min.append(studente)
                materie_min.append(data[0])
            if data[1]>voto_max:
                studenti_max.clear()
                materie_max.clear()
                voto_max = data[1]
                studenti_max.append(studente)
                materie_max.append(data[0])
            elif data[1]==voto_max:
                if studente not in materie_max:
                    studenti_max.append(studente)
                materie_max.append(data[0])
    context={"risultati": [voto_max,materie_max,studenti_max,voto_min,materie_min,studenti_min]}
    return render(request,"voti/MinMaxVoti.html",context)