from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path("utenti/", views.UserList.as_view(), name="giornalisti"),
    path('user/<username>', views.user_profile_view, name="profilo_giornalista"),
]