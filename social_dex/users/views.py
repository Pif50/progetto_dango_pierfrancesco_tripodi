from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from users.forms import FormRegistrazione

# Create your views here.

def registrazione_view(request):
    if request.method == "POST": #Controlliamo se il metodo della richiesta sia o meno POST
        form = FormRegistrazione(request.POST)
        if form.is_valid(): #Controlliamo se il form è valido
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            User.objects.create_user( 
                username=username,
                password=password,
                email=email
            )
            user = authenticate(username=username, password=password) #Autenticazione dell'user
            login(request, user)
            return HttpResponseRedirect("/") #Reindirizzamento nella home page
    else: 
        form = FormRegistrazione()
    context = {'form': form}
    return render (request, "users/registrazione.html", context)
