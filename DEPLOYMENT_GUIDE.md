# Guide de déploiement rapide - PythonAnywhere

## 🚀 Déploiement automatique

### Option 1: Utiliser le script de déploiement

1. Connectez-vous à PythonAnywhere
2. Ouvrez une console Bash
3. Naviguez vers votre répertoire du projet
4. Exécutez le script :
   ```bash
   bash deploy.sh
   ```
5. Allez dans l'onglet "Web" et cliquez sur "Reload"

### Option 2: Déploiement manuel

1. **Connectez-vous à PythonAnywhere**
2. **Ouvrez une console Bash**
3. **Tirez les modifications** :
   ```bash
   cd votre-repo
   git pull origin main
   ```
4. **Activez l'environnement virtuel** :
   ```bash
   source venv/bin/activate
   ```
5. **Installez les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```
6. **Exécutez les migrations** :
   ```bash
   python manage.py migrate --settings=vente.settings_production
   ```
7. **Collectez les fichiers statiques** :
   ```bash
   python manage.py collectstatic --settings=vente.settings_production --noinput
   ```
8. **Redémarrez l'application web** :
   - Allez dans l'onglet "Web"
   - Cliquez sur le bouton "Reload"

## 🔍 Vérification du déploiement

Après le déploiement, vérifiez :

1. **Les fichiers statiques** :
   ```bash
   ls staticfiles/
   ```

2. **Les logs d'erreurs** :
   - Allez dans l'onglet "Web"
   - Cliquez sur "Logs"
   - Vérifiez les fichiers "error.log" et "server.log"

3. **Les modifications** :
   - Vérifiez que les boutons de favoris sont présents
   - Testez l'ajout au panier
   - Testez le triage dans la boutique

## 🐛 Dépannage

### Si les modifications ne s'affichent pas :

1. **Videz le cache du navigateur** (Ctrl+F5)

2. **Vérifiez que les fichiers statiques sont à jour** :
   ```bash
   python manage.py collectstatic --clear --noinput
   ```

3. **Redémarrez le serveur** :
   - Arrêtez l'application web
   - Attendez 10 secondes
   - Redémarrez l'application web

4. **Vérifiez les logs** pour les erreurs

### Si vous avez une erreur 500 :

1. Vérifiez les logs dans l'onglet "Web" → "Logs"
2. Vérifiez que toutes les migrations sont appliquées
3. Vérifiez que les fichiers statiques sont collectés

## 📝 Modifications récentes

Les modifications suivantes ont été déployées :

- ✅ Fix panier AJAX (ajout au panier fonctionne)
- ✅ Fix favoris (boutons et compteur)
- ✅ Fix triage boutique (conserve les paramètres de recherche)
- ✅ Fix position de défilement (page ne remonte pas lors du triage)
- ✅ Ajout des templates de connexion/déconnexion
- ✅ Configuration des URLs d'authentification
