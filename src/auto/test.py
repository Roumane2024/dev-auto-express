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
