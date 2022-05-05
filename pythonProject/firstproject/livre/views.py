from django.shortcuts import render, HttpResponseRedirect
from .forms import LivreForm, BibliothequeForm
from .import models


def formulaire(request):
        if request.method == "POST":
                form = LivreForm(request)
                return render(request, 'livre/formulaire.html', {'form': form})
        else:
                form = LivreForm()
                return render(request, 'livre/formulaire.html', {'form': form})

def traitement(request):
    pForm = LivreForm(request.POST)
    if pForm.is_valid():
        livre = pForm.save()
        return HttpResponseRedirect("/livre/")
    else:
        return render(request, 'livre/name.html', {'form': pForm})

def index(request):
    liste = list(models.Livre.objects.all())
    return render(request,"livre/index.html",{"liste" : liste})

def affiche(request, id):
    livre = models.Livre.objects.get(pk=id)
    return render(request,"livre/affiche.html",{"livre": livre})

def update(request, id):
    livre = models.Livre.objects.get(pk=id)
    form = LivreForm(livre.dico())
    return render(request,"livre/formulaire.html",{"form":form, "id": id})

def updatetraitement(request, id):
    pform = LivreForm(request.POST)
    if pform.is_valid():
        livre = pform.save(commit = False)
        livre.id = id
        livre.save()
        return HttpResponseRedirect ("/livre/")
    else:
        return render(request, "livre/formulaire.html", {"form":pform, "id": id})

def delete(request, id):
    livre = models.Livre.objects.get(pk=id)
    livre.delete()
    return HttpResponseRedirect("/livre/")

def accueil(request):
    liste = list(models.Livre.objects.all())
    return render(request,"Bibliothèque/accueil.html",{"liste" : liste})

def formulairebibliothèque(request):
    if request.method == "POST":
        form = BibliothequeForm(request)
        return render(request, 'Bibliothèque/formulairebibliothèque.html', {'form': form})
    else:
        form = BibliothequeForm()
        return render(request, 'Bibliothèque/formulairebibliothèque.html', {'form': form})

def affichebibliotheque(request, id):
    bibli = models.Bibliotheque.objects.get(pk=id)
    return render(request, "Bibliothèque/affichebibliotheque.html", {"Bibliothèque": bibli})




