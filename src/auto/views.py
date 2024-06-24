from django.shortcuts import render, redirect
from .models import Voiture, Categorie, Location, Vente
from django.core.paginator import Paginator
from django.contrib import messages 
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Utilisateur

# Fonction pour afficher la page d'accueil
def index(request):
    # Recuperation de la liste des voitures
    liste_voiture = Voiture.objects.all()
    # Rechercher une marque de voiture
    marque = request.GET.get("marque")
    if marque != "" and marque is not None:
        liste_voiture = Voiture.objects.filter(marque__icontains=marque)
    #Limiter le nombre de voitures à afficher
    pagination = Paginator(liste_voiture, 4)
    page = request.GET.get("page")
    liste_voiture = pagination.get_page(page)
    contexte = {"liste_voiture":  liste_voiture}
    return render(request, 'index.html', contexte)

#Fonction pour afficher les détails de la voiture
def detail(request,id):
    # Recuperer la voiture via son id
    voiture = Voiture.objects.get(id = id)
    contexte = {"voiture":  voiture}
    return render(request, "detail.html", contexte)

# Fonction pour louer une voiture
def location(request, id):
    # Recuperer la voiture via son id
    voiture = Voiture.objects.get(id=id)
    contexte = {"voiture":  voiture}
    if request.method == "POST" :
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        adresse = request.POST.get('adresse')
        ville= request.POST.get('ville')
        permis= request.FILES.get('permis')
        date_debut= request.POST.get('date-debut')
        total_jours= request.POST.get('total-jours')

        location = Location(nom=nom, prenom=prenom, adresse=adresse, telephone=phone, email=email, ville=ville,  permit_conduit=permis, voiture=voiture, date_debut=date_debut, total_jours=total_jours)
        location.save()
        return redirect('confirmation-location')
    
    return render(request, "formulaire-location.html", contexte)


# Fonction pour acheter une voiture
def achat(request, id):
    # Recuperer la voiture via son id
    voiture = Voiture.objects.get(id = id)
    contexte = {"voiture":  voiture}
    return render(request, "formulaire-achat.html", contexte)

# Fonction pour afficher la voiture par categorie
def categorie(request, nom_categorie):
    categorie = Categorie.objects.get(nom=nom_categorie)
    liste_voiture = Voiture.objects.filter(categorie=categorie)
    contexte = {
        'categorie' : categorie,
        'liste_voiture' : liste_voiture
    }
    return render(request, "categorie.html", contexte)

# Fonction pour afficher la page  apropos
def apropos(request):
    return render(request, 'apropos.html')

# Fonction pour afficher la page  contact
def contact(request):
    return render(request, 'contact.html')


# Fonction pour gerer la location de voiture
def confirmationLocation(request):
    info = Location.objects.all().order_by('-id')[:1]
    for item in info:
        nom = item.nom
        prenom = item.prenom
        date_debut = item.date_debut
        total_jours = item.total_jours
        voiture = item.voiture
    contexte = {
        'nom': nom, 
        'prenom': prenom,
        'date_debut': date_debut,
        'jours': total_jours,
        'voiture': voiture
    }
    
    return render(request, "confirme-location.html", contexte)

# Fonction pour acheter une voiture
def achat(request, id):
    # Recuperer la voiture via son id
    voiture = Voiture.objects.get(id=id)
    contexte = {"voiture":  voiture}
    if request.method == "POST" :
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        adresse = request.POST.get('adresse')
        ville= request.POST.get('ville')

        achat = Vente(nom=nom, prenom=prenom, adresse=adresse, telephone=phone, email=email, ville=ville, voiture=voiture)
        achat.save()
        return redirect('confirmation-achat')
    
    return render(request, "formulaire-achat.html", contexte)

# Fonction pour gerer la confirmation de l'achat d'une voiture
def confirmationVente(request):
    info = Vente.objects.all().order_by('-id')[:1]
    for item in info:
        nom = item.nom
        prenom = item.prenom
        telephone = item.telephone
        voiture = item.voiture
    contexte = {
        'nom': nom, 
        'prenom': prenom,
        'telephone': telephone,
        'voiture': voiture
    }
    
    return render(request, "confirme-achat.html", contexte)

def inscription(request):
    if request.method=='POST':
        nom = request.POST.get('name')
        adresse_mail = request.POST.get('email')
        mot_de_passe = request.POST.get('password')
        mot_de_passe_confirmation = request.POST.get('password1')

        if mot_de_passe != mot_de_passe_confirmation:
            messages.error(request, 'Les mot de passes ne correspondent pas')
        elif Utilisateur.objects.filter(nom=nom).exists():
            messages.error(request, "Ce nom d'utilisateur existe déjà.")
        elif Utilisateur.objects.filter(adresse_mail=adresse_mail).exists():
            messages.error(request, "Cet email existe déjà.")

        else:
            return redirect("connexion.html")

        context = {
           " nom": "nom",
            "adresse_mail": "adresse_mail",
            "mot_de_passe" : "mot_de_passe",
            "mot_de_passe_confirmation" : "mot_de_passe_confirmation"
        }

        messages.success(request, "Inscription reussi")

    return render(request, 'inscription.html', context)


def connexion(request):
    if request.method == 'POST':

        adresse_mail = request.POST.get('email')

        mot_de_passe = request.POST.get('password') 

        utilisateur= Utilisateur.objects.filter(adresse_mail=adresse_mail)

        if utilisateur.exists():

            utilisateur = authenticate(request, adresse_mail=adresse_mail, mot_de_passe=mot_de_passe)

            if utilisateur is not None:

                login(request,utilisateur)

                messages.success(request, 'Vous etes connectés')

    else:
        return render(request,' connexion.html')




    





