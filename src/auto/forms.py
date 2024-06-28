from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserResgisterFrom(UserCreationForm):
    username = forms.CharField(
        widget= forms.TextInput(attrs={"placeholder": "Nom d'utilisateur", "class":"form-control"})
    )
    email = forms.EmailField(
        widget= forms.EmailInput(attrs={"placeholder": "Adresse Email", "class":"form-control"})
    )
    phone = forms.CharField(
        widget= forms.TextInput(attrs={"placeholder": "Numero de telephone", "class":"form-control"})

    )
    password1 = forms.CharField(
        widget= forms.PasswordInput(attrs={"placeholder": "Mot de passe","class":"form-control"})
    )
    password2 = forms.CharField(
        widget= forms.PasswordInput(attrs={"placeholder": "confirmer le mot de passe","class":"form-control"})

    )

    class Meta:
        model = User
        fields = ['username', 'email', 'phone']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Nom d\'utilisateur', widget=forms.TextInput(attrs={"placeholder":"Saisir votre nom d'utilisateur", "class":"form-control"}))
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={"placeholder":"Saisir votre mot de passe", "class":"form-control"}))