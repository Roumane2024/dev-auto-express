from django.contrib import admin
from . models import Categorie, Voiture, Location, Vente

#Enregistrement des tables
class AdminCategorie(admin.ModelAdmin):
    list_display= ["nom", "description"]

class AdminVoiture(admin.ModelAdmin):
    list_display= ["marque", "categorie", "annee_fabrication", "type_de_carburant", "couleur"]

class AdminLocation(admin.ModelAdmin):
    list_display= ["voiture", "nom", "prenom", "date_debut", "total_jours", "permit_conduit", "statut"] 

class AdminVente(admin.ModelAdmin):
    list_display= ["nom", "prenom", "adresse", "telephone", "email", "ville", "voiture"]  


admin.site.register(Categorie, AdminCategorie)
admin.site.register(Voiture, AdminVoiture)
admin.site.register(Location, AdminLocation)
admin.site.register(Vente, AdminVente)
