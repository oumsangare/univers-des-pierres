# Progressive Web App (PWA) - Univers des Pierres

## ✅ Fonctionnalités PWA ajoutées

Votre site est maintenant une Progressive Web App (PWA) qui peut être installée comme une application native sur mobile.

### 📱 Fonctionnalités incluses :

1. **Installation hors-ligne** : Le site peut être installé sur l'écran d'accueil
2. **Mode hors-ligne** : Fonctionne sans connexion internet
3. **Cache intelligent** : Les pages sont mises en cache pour un chargement rapide
4. **Notifications push** : Support pour les notifications (à configurer)
5. **Raccourcis d'app** : Accès direct à Boutique et Panier
6. **Thème personnalisé** : Couleur de thème rose (#e91e63)
7. **Écran de démarrage** : Splash screen avec logo
8. **Mode plein écran** : Interface sans barre d'adresse

### 🔧 Fichiers créés/modifiés :

- `boutique/static/manifest.json` : Configuration PWA
- `boutique/static/js/service-worker.js` : Service Worker pour le cache
- `boutique/static/images/icons/icon-192x192.svg` : Icône d'installation
- `boutique/templates/boutique/base.html` : Meta tags et JavaScript PWA
- `vente/urls.py` : Configuration des fichiers statiques
- `boutique/static/css/style.css` : Styles du bouton d'installation

### 🧪 Comment tester la PWA :

#### Sur Chrome (Desktop) :
1. Ouvrez le site dans Chrome
2. Ouvrez les DevTools (F12)
3. Allez dans l'onglet "Application"
4. Vérifiez "Manifest" et "Service Workers"
5. Cliquez sur "Add to home screen" dans DevTools

#### Sur Android (Chrome) :
1. Ouvrez le site dans Chrome
2. Un bouton "Installer l'app" apparaîtra en bas à droite
3. Cliquez sur "Installer"
4. L'application sera ajoutée à l'écran d'accueil

#### Sur iOS (Safari) :
1. Ouvrez le site dans Safari
2. Appuyez sur le bouton "Partager"
3. Sélectionnez "Sur l'écran d'accueil"
4. L'application sera ajoutée

### 📊 Vérification PWA :

Utilisez l'outil Lighthouse dans Chrome DevTools :
1. Ouvrez DevTools (F12)
2. Allez dans l'onglet "Lighthouse"
3. Sélectionnez "Progressive Web App"
4. Cliquez sur "Analyze page load"

### 🔧 Configuration requise pour production :

Pour un déploiement en production, vous aurez besoin de :

1. **HTTPS obligatoire** : Les PWA nécessitent HTTPS
2. **Domaine propre** : Pas de localhost en production
3. **Icônes PNG** : Convertir les SVG en PNG pour meilleure compatibilité
4. **Notifications** : Configurer un serveur de notifications push

### 🎨 Personnalisation :

Vous pouvez modifier :
- Couleur de thème : Dans `manifest.json` (`theme_color`)
- Nom de l'app : Dans `manifest.json` (`name`, `short_name`)
- Icônes : Remplacer les fichiers SVG par des PNG
- Raccourcis : Modifier la section `shortcuts` dans `manifest.json`

### 📱 Installation sur mobile :

1. Ouvrez le site sur votre mobile
2. Le bouton "Installer l'app" apparaîtra automatiquement
3. Cliquez pour installer
4. L'application sera disponible sur votre écran d'accueil

### 🚀 Prochaines étapes :

Pour améliorer la PWA :
- Ajouter des notifications push réelles
- Créer des icônes PNG pour meilleure compatibilité
- Ajouter un écran de chargement personnalisé
- Implémenter la synchronisation hors-ligne
- Ajouter des analytics pour suivre l'utilisation

### 📞 Support :

Si vous avez des questions sur la PWA, consultez :
- [Documentation PWA Google](https://web.dev/progressive-web-apps/)
- [Documentation MDN](https://developer.mozilla.org/fr/docs/Web/Progressive_web_apps)
