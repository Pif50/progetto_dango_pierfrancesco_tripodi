from django.urls import URLPattern, path
from . import views

urlpatterns =[
    path("nuovo_articolo", views.nuovo_articolo, name="nuovo_articolo"),
    path('hash_txid', views.hash_txid, name = 'hash_txid'), 
]