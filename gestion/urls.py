from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_produits, name='produit_list'),
    path('create', views.produit_create, name='produit_create'),
    path('produits/<int:pk>/delete/', views.produit_delete, name='produit_delete'),
    path('produits/<int:pk>/update/', views.produit_update, name='produit_update'),

]

