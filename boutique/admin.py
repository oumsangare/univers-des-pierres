from django.contrib import admin
from .models import Banner, Categorie, Produit, Promotion, Avantage, Temoignage, Contact, PanierItem, Commande, CommandeItem, Favori


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['titre', 'sous_titre', 'active', 'ordre', 'date_creation']
    list_filter = ['active', 'date_creation']
    search_fields = ['titre', 'sous_titre']
    list_editable = ['active', 'ordre']


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['nom', 'slug', 'active', 'date_creation']
    list_filter = ['active', 'date_creation']
    search_fields = ['nom']
    prepopulated_fields = {'slug': ('nom',)}


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ['nom', 'categorie', 'prix', 'ancien_prix', 'stock', 'est_populaire', 'est_nouveau', 'meilleure_vente', 'date_creation']
    list_filter = ['categorie', 'est_populaire', 'est_nouveau', 'meilleure_vente', 'date_creation']
    search_fields = ['nom', 'description']
    prepopulated_fields = {'slug': ('nom',)}
    list_editable = ['prix', 'ancien_prix', 'stock', 'est_populaire', 'est_nouveau', 'meilleure_vente']


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['titre', 'reduction', 'date_debut', 'date_fin', 'active', 'date_creation']
    list_filter = ['active', 'date_debut', 'date_fin']
    search_fields = ['titre', 'description']


@admin.register(Avantage)
class AvantageAdmin(admin.ModelAdmin):
    list_display = ['icone', 'titre', 'ordre']
    list_editable = ['ordre']


@admin.register(Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    list_display = ['nom', 'note', 'active', 'date_creation']
    list_filter = ['active', 'note', 'date_creation']
    search_fields = ['nom', 'commentaire']
    list_editable = ['active']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['telephone', 'whatsapp', 'email']
    fieldsets = (
        ('Téléphone', {
            'fields': ('telephone', 'whatsapp')
        }),
        ('Email et Adresse', {
            'fields': ('email', 'adresse')
        }),
        ('Réseaux sociaux', {
            'fields': ('facebook', 'instagram', 'tiktok')
        }),
    )


@admin.register(PanierItem)
class PanierItemAdmin(admin.ModelAdmin):
    list_display = ['produit', 'quantite', 'session_key', 'date_ajout']
    list_filter = ['date_ajout']
    search_fields = ['produit__nom', 'session_key']


@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'email', 'telephone', 'total', 'mode_paiement', 'statut', 'date_creation']
    list_filter = ['statut', 'mode_paiement', 'date_creation']
    search_fields = ['nom', 'email', 'telephone']
    list_editable = ['statut']
    readonly_fields = ['date_creation']


@admin.register(CommandeItem)
class CommandeItemAdmin(admin.ModelAdmin):
    list_display = ['commande', 'produit', 'quantite', 'prix']
    list_filter = ['commande']
    search_fields = ['produit__nom']


@admin.register(Favori)
class FavoriAdmin(admin.ModelAdmin):
    list_display = ['utilisateur', 'produit', 'date_ajout']
    list_filter = ['date_ajout']
    search_fields = ['utilisateur__username', 'produit__nom']
