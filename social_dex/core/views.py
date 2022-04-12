from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from blog.views import Post 
from django.contrib.auth.decorators import login_required

import redis


# CONFIG FOR REDIS SERVER
SERVER_IP = '127.0.0.1'
SERVER_PORT = '6379'
PASSWORD = ''
DB = 0



def homepage(request):

    return render(request, 'core/homepage.html')


@login_required
def user_profile_view(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author = user)

    context={
        'user': user,
        'posts': posts,
    }
    return render(request, "core/profilo_giornalista.html", context)



class UserList(ListView):
    model = User
    template_name = "core/giornalisti.html"

# Create your views here.
