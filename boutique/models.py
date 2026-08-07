from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Banner(models.Model):
    titre = models.CharField(max_length=200)
    sous_titre = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='banners/')
    texte_bouton = models.CharField(max_length=100, default='Acheter maintenant')
    lien_bouton = models.CharField(max_length=200, blank=True)
    active = models.BooleanField(default=True)
    ordre = models.IntegerField(default=0)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordre', '-date_creation']

    def __str__(self):
        return self.titre


class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    image = models.ImageField(upload_to='categories/')
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nom']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='produits/')
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    ancien_prix = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(default=0)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='produits', null=True, blank=True)
    est_populaire = models.BooleanField(default=False)
    est_nouveau = models.BooleanField(default=True)
    meilleure_vente = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_creation']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

    @property
    def reduction_pourcentage(self):
        if self.ancien_prix and self.ancien_prix > self.prix:
            return int(((self.ancien_prix - self.prix) / self.ancien_prix) * 100)
        return 0

    def __str__(self):
        return self.nom


class Promotion(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='promotions/')
    reduction = models.IntegerField(help_text='Pourcentage de réduction')
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    active = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_creation']

    def __str__(self):
        return f"{self.titre} - {self.reduction}%"


class Avantage(models.Model):
    icone = models.CharField(max_length=100, help_text='Nom de l\'icône (ex: fa-truck, fa-shield)')
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    ordre = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordre']

    def __str__(self):
        return self.titre


class Temoignage(models.Model):
    nom = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='temoignages/', blank=True)
    commentaire = models.TextField()
    note = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    active = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_creation']

    def __str__(self):
        return f"{self.nom} - {self.note}/5"


class Contact(models.Model):
    telephone = models.CharField(max_length=20, blank=True)
    whatsapp = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    adresse = models.TextField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    tiktok = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Informations de contact'
        verbose_name_plural = 'Informations de contact'

    def __str__(self):
        return 'Informations de contact'


class PanierItem(models.Model):
    session_key = models.CharField(max_length=255, null=True, blank=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='panier_items')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)
    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_ajout']

    def __str__(self):
        return f"{self.produit.nom} x {self.quantite}"

    @property
    def total(self):
        return self.produit.prix * self.quantite


class Commande(models.Model):
    nom = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    telephone = models.CharField(max_length=20)
    adresse = models.TextField()
    ville = models.CharField(max_length=100)
    pays = models.CharField(max_length=100, default="Côte d'Ivoire")
    mode_paiement = models.CharField(max_length=50, choices=[
        ('wave', 'Wave'),
        ('orange', 'Orange Money'),
        ('especes', 'Paiement à la livraison')
    ])
    notes = models.TextField(blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    session_key = models.CharField(max_length=255)
    statut = models.CharField(max_length=50, default='en_attente', choices=[
        ('en_attente', 'En attente'),
        ('confirmee', 'Confirmée'),
        ('en_cours', 'En cours de livraison'),
        ('livree', 'Livrée'),
        ('annulee', 'Annulée')
    ])
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_creation']
        verbose_name = 'Commande'
        verbose_name_plural = 'Commandes'

    def __str__(self):
        return f"Commande #{self.id} - {self.nom}"


class CommandeItem(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name='items')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Article de commande'
        verbose_name_plural = 'Articles de commande'

    def __str__(self):
        return f"{self.produit.nom} x {self.quantite}"

    @property
    def total(self):
        return self.prix * self.quantite


class Favori(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favoris')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='favoris')
    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Favori'
        verbose_name_plural = 'Favoris'
        unique_together = ('utilisateur', 'produit')

    def __str__(self):
        return f"{self.utilisateur.username} - {self.produit.nom}"
