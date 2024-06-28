from django.urls import path

from .views import index, detail, location, achat, categorie, apropos, contact, confirmationLocation, confirmationVente, inscription, connexion, deconnexion

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:id>/', detail, name='detail'),
    path('location/<int:id>/', location, name='location'),
    path('achat/<int:id>/', achat, name='achat'),
    path('categorie/<slug:nom_categorie>/', categorie, name='categorie'),
    path('apropos/', apropos, name='apropos'),
    path('contact', contact, name='contact'),
    path('confirmation-location', confirmationLocation, name='confirmation-location'),
    path('confirmation-achat', confirmationVente, name='confirmation-achat'),
    path('inscription/', inscription, name='inscription'),
    path('connexion/', connexion, name='connexion'),
    path('deconnexion/', deconnexion, name='deconnexion')
]
