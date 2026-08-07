from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('boutique/', views.boutique, name='boutique'),
    path('produit/<slug:slug>/', views.detail_produit, name='detail_produit'),
    path('contact/', views.contact, name='contact'),
    path('panier/ajouter/<int:produit_id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('panier/', views.panier, name='panier'),
    path('panier/modifier/<int:item_id>/', views.modifier_quantite, name='modifier_quantite'),
    path('panier/supprimer/<int:item_id>/', views.supprimer_du_panier, name='supprimer_du_panier'),
    path('commande/', views.commande, name='commande'),
    path('commande/<int:produit_id>/', views.commande, name='commande_produit'),
    path('recherche/', views.recherche, name='recherche'),
    path('favoris/', views.favoris, name='favoris'),
    path('favoris/ajouter/<int:produit_id>/', views.ajouter_favori, name='ajouter_favori'),
    path('favoris/supprimer/<int:favori_id>/', views.supprimer_favori, name='supprimer_favori'),
    path('gestion-commandes/', views.admin_commandes, name='admin_commandes'),
    path('gestion-commandes/<int:commande_id>/', views.admin_commande_detail, name='admin_commande_detail'),
]
