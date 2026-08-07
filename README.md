# Site de Vente en Ligne - Page d'Accueil Django

Projet e-commerce Django avec page d'accueil professionnelle et moderne.

## 🚀 Caractéristiques

### Page d'Accueil Complète
- **Header/Navigation** : Logo, menu, barre de recherche, icône panier
- **Hero Section** : Slider dynamique avec bannières
- **Catégories** : Affichage des catégories sous forme de cartes
- **Produits Populaires** : Produits mis en avant avec badges
- **Section Promotion** : Offres spéciales avec réduction
- **Nouveaux Produits** : Derniers arrivages
- **Avantages** : Pourquoi nous choisir
- **Statistiques** : Compteurs dynamiques
- **Témoignages** : Carousel d'avis clients
- **Contact Rapide** : Informations de contact
- **Footer** : Pied de page professionnel

### Technologies
- **Backend** : Django 6.0
- **Base de données** : SQLite (configuré pour MySQL)
- **Frontend** : HTML5, CSS3, Bootstrap 5, JavaScript
- **Design** : Moderne, responsive, professionnel

## 📋 Modèles Django

- **Banner** : Bannières du slider
- **Categorie** : Catégories de produits
- **Produit** : Produits avec prix, stock, badges
- **Promotion** : Offres promotionnelles
- **Avantage** : Avantages de la boutique
- **Temoignage** : Avis clients
- **Contact** : Informations de contact

## 🛠️ Installation

### Prérequis
- Python 3.8+
- pip

### Étapes

1. **Créer l'environnement virtuel**
```bash
python -m venv env
env\Scripts\activate
```

2. **Installer les dépendances**
```bash
pip install django pillow
```

3. **Appliquer les migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Créer un superuser**
```bash
python manage.py createsuperuser
```

5. **Démarrer le serveur**
```bash
python manage.py runserver
```

## 🌐 Accès

- **Site** : http://127.0.0.1:8000/
- **Administration** : http://127.0.0.1:8000/admin/

## 📝 Configuration

### Base de données MySQL (optionnel)

Modifier `vente/settings.py` :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'votre_base',
        'USER': 'votre_user',
        'PASSWORD': 'votre_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Installer le client MySQL :
```bash
pip install mysqlclient
```

## 🎨 Personnalisation

### Ajouter du contenu via l'administration

1. Connectez-vous à http://127.0.0.1:8000/admin/
2. Ajoutez des catégories, produits, bannières, etc.
3. Les données s'affichent automatiquement sur la page d'accueil

### Modifier le design

- **CSS** : `static/css/style.css`
- **JavaScript** : `static/js/main.js`
- **Templates** : `boutique/templates/boutique/`

## 📁 Structure du Projet

```
vente/
├── boutique/                  # Application principale
│   ├── models.py             # Modèles de données
│   ├── admin.py              # Administration Django
│   ├── views.py              # Vues
│   ├── urls.py               # URLs de l'app
│   └── templates/
│       └── boutique/
│           ├── base.html     # Template de base
│           └── accueil.html  # Page d'accueil
├── static/                   # Fichiers statiques
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── img/
├── media/                    # Images uploadées
├── vente/                    # Configuration Django
│   ├── settings.py
│   └── urls.py
└── manage.py
```

## ✨ Fonctionnalités

### Gestion via l'administration
- Créer/modifier/supprimer des bannières
- Gérer les catégories et produits
- Configurer les promotions
- Gérer les avantages
- Modérer les témoignages
- Configurer les informations de contact

### Interactions JavaScript
- Slider automatique des bannières
- Carousel des témoignages
- Animation des statistiques
- Effets hover sur les cartes
- Système de notifications
- Ajout au panier (placeholder)

## 🔐 Sécurité

Pour la production :
- Changer `SECRET_KEY` dans `settings.py`
- Configurer `ALLOWED_HOSTS`
- Utiliser HTTPS
- Configurer une base de données sécurisée
- Désactiver `DEBUG = False`

## 📞 Support

Pour toute question ou amélioration, contactez l'équipe de développement.

## 📄 Licence

Ce projet est créé à des fins éducatives et commerciales.
