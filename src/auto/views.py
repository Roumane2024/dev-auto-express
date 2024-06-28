from django.shortcuts import render, redirect
from .models import Voiture, Categorie, Location, Vente
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import User
from .forms import UserResgisterFrom, UserLoginForm


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

# La fonction qui permet de s'inscrire
def inscription(request):
    if request.method=='POST':
        form= UserResgisterFrom(request.POST or None)
        if form.is_valid():
            new_user= form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Bienvenue {username}, votre compte a ete crée avec succes !!!")
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('connexion')
        
    else:
        form = UserResgisterFrom()
    context = {'form': form}
    return render(request, 'inscription.html', context)
 

# La fonction qui permet de se connecter
def connexion(request):
    if request.user.is_authenticated:
        messages.warning(request, "Hey vous etes déjà connecté !")
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            user = authenticate( request, username=username, password=password)

            if User is not None:
                login(request, user)
                messages.success(request, "Vous etes connecté !")
                return redirect('index')
            else:
                messages.warning(request, "Nom d'utilisateur ou mot de passe incorrect.")
        except:
            messages.warning(request, f"Le nom d'utilisateur {username} n'existe pas")

    form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'connexion.html', context)

     

# la fonction qui permet de se déconnecter
def deconnexion(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté.")
    return redirect('connexion')
    




    





