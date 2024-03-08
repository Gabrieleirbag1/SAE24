from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import MqForm
from .forms import DoForm
from .forms import F5Form
from . import models
from mqtt.models import Mq
from mqtt.models import Do
from . import models
from django.shortcuts import render
from . import insertion
import csv
from django.http import HttpResponse
from django.db.models import Q
from datetime import datetime

#------------------------------------------------------------------#


                                #TABLEAUX


#------------------------------------------------------------------#

def home(request):
    Mqtt = models.Mq.objects.order_by('-id')[:1]
    Donnees = models.Do.objects.order_by('-id')[:1]

    data = zip(Mqtt, Donnees)

    return render(request, 'MAIN/home.html', {'data': data})

def mainpage(request):
    Mqtt = models.Mq.objects.order_by('-id')[:20]
    Donnees = models.Do.objects.order_by('-id')[:20]

    data = zip(Mqtt, Donnees)

    return render(request, 'MAIN/mainpage.html', {'data': data})

def mainpager(request):
    Mqtt = models.Mq.objects.order_by('id')[:20]
    Donnees = models.Do.objects.order_by('id')[:20]

    data = zip(Mqtt, Donnees)

    return render(request, 'MAIN/mainpage-r.html', {'data': data})


#ordre alphabétique A-Z
def mainpageaz(request):
    Mqtt = models.Mq.objects.order_by('nom')[:20]
    Donnees = models.Do.objects.order_by('mqnom')[:20]

    data = zip(Mqtt, Donnees)

    return render(request, 'MAIN/mainpage-az.html', {'data': data})

#ordre alphabétique Z-A
def mainpageza(request):
    Mqtt = models.Mq.objects.order_by('-nom')[:20]
    Donnees = models.Do.objects.order_by('-mqnom')[:20]

    data = zip(Mqtt, Donnees)

    return render(request, 'MAIN/mainpage-za.html', {'data': data})

#filtre date
def mainpagedate(request):
    if request.method == 'POST':
        date_debut_filtre = request.POST.get('date_debut_filtre')
        date_fin_filtre = request.POST.get('date_fin_filtre')
        mqdate_debut_filtre = request.POST.get('mqdate_debut_filtre')
        mqdate_fin_filtre = request.POST.get('mqdate_fin_filtre')
        conditions_filtre = Q()
        conditions_filtre2 = Q()

        if date_debut_filtre:
            date_debut = datetime.strptime(date_debut_filtre, '%Y-%m-%d').date()
            conditions_filtre &= Q(date__gte=date_debut)
        if date_fin_filtre:
            date_fin = datetime.strptime(date_fin_filtre, '%Y-%m-%d').date()
            conditions_filtre &= Q(date__lte=date_fin)
        
        if mqdate_debut_filtre:
            mqdate_debut = datetime.strptime(mqdate_debut_filtre, '%Y-%m-%d').date()
            conditions_filtre2 &= Q(mqdate__gte=mqdate_debut)
        if mqdate_fin_filtre:
            mqdate_fin = datetime.strptime(mqdate_fin_filtre, '%Y-%m-%d').date()
            conditions_filtre2 &= Q(mqdate__lte=mqdate_fin)

        Donnees = Do.objects.filter(conditions_filtre)
        Mqtt = Mq.objects.filter(conditions_filtre2)
        data = zip(Mqtt, Donnees)
    else:
        Mqtt = Mq.objects.order_by('-id')[:20]
        Donnees = Do.objects.order_by('-id')[:20]
        data = zip(Mqtt, Donnees)

    return render(request, 'MAIN/mainpagedate.html', {'data': data})

def listecompletedate(request):
    if request.method == 'POST':
        date_debut_filtre = request.POST.get('date_debut_filtre')
        date_fin_filtre = request.POST.get('date_fin_filtre')
        mqdate_debut_filtre = request.POST.get('mqdate_debut_filtre')
        mqdate_fin_filtre = request.POST.get('mqdate_fin_filtre')
        conditions_filtre = Q()
        conditions_filtre2 = Q()

        if date_debut_filtre:
            date_debut = datetime.strptime(date_debut_filtre, '%Y-%m-%d').date()
            conditions_filtre &= Q(date__gte=date_debut)
        if date_fin_filtre:
            date_fin = datetime.strptime(date_fin_filtre, '%Y-%m-%d').date()
            conditions_filtre &= Q(date__lte=date_fin)
        
        if mqdate_debut_filtre:
            mqdate_debut = datetime.strptime(mqdate_debut_filtre, '%Y-%m-%d').date()
            conditions_filtre2 &= Q(mqdate__gte=mqdate_debut)
        if mqdate_fin_filtre:
            mqdate_fin = datetime.strptime(mqdate_fin_filtre, '%Y-%m-%d').date()
            conditions_filtre2 &= Q(mqdate__lte=mqdate_fin)

        Donnees = Do.objects.filter(conditions_filtre)
        Mqtt = Mq.objects.filter(conditions_filtre2)
        data = zip(Mqtt, Donnees)
    else:
        Mqtt = Mq.objects.order_by('-id')[:20]
        Donnees = Do.objects.order_by('-id')[:20]
        data = zip(Mqtt, Donnees)

    return render(request, 'MAIN/listecompletedate.html', {'data': data})




#liste complète

def listecomplete(request):
    Mqtt = Mq.objects.all().order_by('-id')
    Donnees = Do.objects.all().order_by('-id')

    data = zip(Mqtt, Donnees)

    return render(request, 'MAIN/listecomplete.html', {'data': data})

def listecompleter(request):
    Mqtt = models.Mq.objects.order_by('id')[:20]
    Donnees = models.Do.objects.order_by('id')[:20]

    data = zip(Mqtt, Donnees)

    return render(request, 'MAIN/listecomplete-r.html', {'data': data})


#ordre alphabétique A-Z
def listecompleteaz(request):
    Mqtt = models.Mq.objects.order_by('nom')[:20]
    Donnees = models.Do.objects.order_by('mqnom')[:20]

    data = zip(Mqtt, Donnees)

    return render(request, 'MAIN/listecomplete-az.html', {'data': data})

#ordre alphabétique Z-A
def listecompleteza(request):
    Mqtt = models.Mq.objects.order_by('-nom')[:20]
    Donnees = models.Do.objects.order_by('-mqnom')[:20]

    data = zip(Mqtt, Donnees)

    return render(request, 'MAIN/listecomplete-za.html', {'data': data})








#------------------------------------------------------------------#


                                #GRAPHIQUES


#------------------------------------------------------------------#

def graphique(request):
    donnees = Do.objects.order_by('-id')[:20].values('heure', 'temp')
    stepcount = []
    for donnee in reversed(donnees):
        stepcount.append({
            'y': donnee['temp'],
            'label': donnee['heure']
        })

    return render(request, 'MAIN/graphique.html', {'stepcount': stepcount})

def graphiquecomplet(request):
    donnees = Do.objects.values('heure', 'temp')
    stepcount = []
    for donnee in reversed(donnees):
        stepcount.append({
            'y': donnee['temp'],
            'label': donnee['heure']
        })

    return render(request, 'MAIN/graphiquecomplet.html', {'stepcount': stepcount})

#------------------------------------------------------------------#


                                #CSV


#------------------------------------------------------------------#


def export_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="MQTT_DATA.csv"'
    writer = csv.writer(response)
    writer.writerow(['Topic', 'Payload'])
    for info in reversed(insertion.reception):
        writer.writerow(info)

    return response





#------------------------------------------------------------------#


                            #Fonctions de base


#------------------------------------------------------------------#

def ajout(request):
    if request.method == "POST":
        form = MqForm(request)
        if form.is_valid(): 
            mq = form.save() 
            return render(request,"MAIN/affiche.html",{"mq" : mq}) 
        else:
            return render(request,"MAIN/ajout.html",{"form": form})
    else :
        form = MqForm() 
        return render(request,"MAIN/ajout.html",{"form" : form})
    
    

def traitement(request):
    lform = MqForm(request.POST)
    if lform.is_valid():
        mq = lform.save()
        return HttpResponseRedirect("/mainpage")
    else:
        return render(request,"MAIN/ajout.html",{"form": lform})
    
def update(request, id):
    mq = models.Mq.objects.get(pk=id)
    lform = MqForm(request.POST)
    if lform.is_valid():
        mq = lform.save(commit=False)
        mq.id = id
        mq.save()
        do = models.Do.objects.get(pk=id)
        tform = DoForm(request.POST)
        if tform.is_valid():
            new_mqnom = mq.nom

            mqid = do.mqid
            date = do.date
            heure = do.heure
            temp = do.temp

            do.mqnom = new_mqnom
            do.save()

            do.mqid = mqid
            do.date = date
            do.heure = heure
            do.temp = temp
            do.save()
        else:
            do = models.Do.objects.get(pk=id)
            tform = DoForm(instance=do)
            return render(request, "MAIN2/updatedo.html", {"cform": tform, "id": id})

        return HttpResponseRedirect('/mainpage/')
    else:
        mq = models.Mq.objects.get(pk=id)
        lform = MqForm(instance=mq)
        return render(request, "MAIN/update.html", {"form": lform, "id": id})


    

def delete(request, mq_id=None, do_id=None):
    if mq_id:
        mq = models.Mq.objects.get(id=mq_id)
        mq.delete()
    if do_id:
        do = models.Do.objects.get(id=do_id)
        do.delete()
    return HttpResponseRedirect("/mainpage")



def affiche(request, id):
    mq = models.Mq.objects.get(pk=id) 
    return render(request,"MAIN/affiche.html",{"mq": mq})




#--------------------------------------------------------------------------#



def ajoutdo(request):
    if request.method == "POST": 
        cform = DoForm(request)
        if cform.is_valid(): 
            do = cform.save() 
            return render(request,"MAIN2/affichedo.html",{"do" : do}) 
        else:
            return render(request,"MAIN2/ajoutdo.html",{"cform": cform})
    else :
        cform = DoForm() 
        return render(request,"MAIN2/ajoutdo.html",{"cform" : cform})
    
    

def traitementdo(request):
    tform = DoForm(request.POST)
    if tform.is_valid():
        do = tform.save()
        return HttpResponseRedirect("/mainpage/")
    else:
        return render(request,"MAIN2/ajoutdo.html",{"cform": tform})
    
def updatedo(request, id):
    do = models.Do.objects.get(pk = id)
    tform = DoForm(request.POST)
    if tform.is_valid():
        do = tform.save(commit=False) 
        do.id = id; 
        do.save() 
        return HttpResponseRedirect('/mainpage')
    else:
        do = models.Do.objects.get(pk = id)
        tform = DoForm(do.__dict__)
        return render(request, "MAIN2/updatedo.html", {"cform": tform, "id": id})
    

def deletedo(request, id):
    do = models.Do.objects.get(id=id)
    do.delete()
    return HttpResponseRedirect("/mainpage/")


def affichedo(request, id):
    do = models.Do.objects.get(pk=id) 
    return render(request,"MAIN2/affichedo.html",{"do": do})



