from django.db import models    
from django.contrib.auth.models import AbstractUser

#Creation de la table des utilisateurs
class User(AbstractUser):
    ROLES = (
        ("CLIENT", "Client"),
        ("ADMIN", "Admin")
    )
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=20)
    role = models.CharField(choices=ROLES,default='CLIENT', max_length=100)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username



#Creation de la table Categorie
class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.nom 

# Creation de la table voiture
class Voiture(models.Model):
    ETAT_VOITURES = (
        ("neuf", "Neuf"),
        ("ocasion", "Ocasion"),
        ("louer", "Louer"),
        ("vendu", "Vendu"),
        ("maintenance", "Maintenance"),
    )
    marque = models.CharField(max_length=100)
    prix_location = models.FloatField()
    prix_vente = models.FloatField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    annee_fabrication = models.DateField()
    type_de_carburant = models.CharField(max_length=100)
    couleur = models.CharField(max_length=100)
    disponibilite = models.BooleanField(default=True)
    etat = models.CharField(max_length=100,choices=ETAT_VOITURES)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.marque 

#Creation de la table location
class Location(models.Model):
    STATUT = (
        ("en-attente","En Attente"),
        ("confirmer","Confirmer"),
        ("annuler","Annuler"),
    )
    nom = models.CharField(max_length=100, default='')
    prenom = models.CharField(max_length=100, default='')
    adresse = models.CharField(max_length=100, default='')
    telephone = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=100, default='')
    ville = models.CharField(max_length=100, default='')
    permit_conduit =models.ImageField(upload_to='documents/', default='')
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE)
    date_debut = models.DateField()
    total_jours = models.CharField(max_length=50, default='')
    statut = models.CharField(max_length=100,choices=STATUT, default='en-attente')

    def __str__(self):
        return self.nom + self.prenom 

#Creation de la table Vente
class Vente(models.Model): 
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    telephone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom + self.prenom
