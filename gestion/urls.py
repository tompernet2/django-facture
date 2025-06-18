from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_produits, name='liste_produits'),
    path('produits/create/', views.produit_create, name='produit_create'),
    path('produits/<int:pk>/delete/', views.produit_delete, name='produit_delete'),
    path('produits/<int:pk>/update/', views.produit_update, name='produit_update'),
    
    path('factures/selection/', views.produits_facture, name='produits_facture'),
    path('factures/selection/create/', views.facture_create, name='facture_create'),
    path('factures/<int:pk>/', views.facture_detail, name='facture_detail'),
    path('factures/', views.liste_factures, name='liste_factures'),
]

