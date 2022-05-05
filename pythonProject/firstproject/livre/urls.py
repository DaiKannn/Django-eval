from django.urls import path
from . import views
urlpatterns = [
    path('formulaire', views.formulaire, name='formulaire'),
    path('traitement/', views.traitement),
    path("",views.index),
    path("affiche/<int:id>/",views.affiche),
    path("update/<int:id>/",views.update),
    path("updatetraitement/<int:id>/",views.updatetraitement),
    path("delete/<int:id>/",  views.delete),
    path("accueil/", views.accueil),
    path("formulairebibliothèque/", views.formulairebibliothèque),
    path("affichebibliotheque/<int:id>/", views.affichebibliotheque)
]

