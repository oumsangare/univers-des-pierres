# Guide de déploiement sur PythonAnywhere

## 📋 Étape 1 : Créer un compte PythonAnywhere

1. Allez sur [pythonanywhere.com](https://www.pythonanywhere.com/)
2. Créez un compte gratuit (Beginner account)
3. Vérifiez votre email

## 📋 Étape 2 : Configurer votre compte

1. Connectez-vous à PythonAnywhere
2. Allez dans l'onglet "Account"
3. Notez votre username (ex: monusername)
4. Votre site sera accessible à : `https://monusername.pythonanywhere.com`

## 📋 Étape 3 : Créer une base de données PostgreSQL

1. Allez dans l'onglet "Databases"
2. Cliquez sur "Start a new database"
3. Choisissez "PostgreSQL"
4. Notez :
   - Database name
   - Database username
   - Database password
   - Database host (généralement: username.postgres.database.azure.com)

## 📋 Étape 4 : Uploader votre code

### Option A : Via Git (recommandé)

1. **Créer un repository GitHub** :
   - Allez sur github.com
   - Créez un nouveau repository
   - Initialisez git dans votre projet local :
     ```bash
     cd "c:\Users\HP ELITEBOOK 830 G8\Desktop\site vente en ligne\vente"
     git init
     git add .
     git commit -m "Initial commit"
     git remote add origin https://github.com/votre-username/votre-repo.git
     git push -u origin main
     ```

2. **Sur PythonAnywhere** :
   - Allez dans l'onglet "Consoles"
   - Cliquez sur "Bash"
   - Clonez votre repository :
     ```bash
     git clone https://github.com/votre-username/votre-repo.git
     cd votre-repo
     ```

### Option B : Via upload manuel

1. Zippez votre dossier `vente`
2. Sur PythonAnywhere, allez dans "Files"
3. Uploadez le fichier zip
4. Décompressez-le

## 📋 Étape 5 : Configurer l'environnement virtuel

1. Dans la console Bash sur PythonAnywhere :
   ```bash
   cd votre-repo
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## 📋 Étape 6 : Configurer les variables d'environnement

1. Sur PythonAnywhere, allez dans l'onglet "Web"
2. Cliquez sur votre application web
3. Dans la section "Environment variables", ajoutez :
   - `DJANGO_SECRET_KEY` : Votre secret key sécurisé
   - `DB_NAME` : Votre nom de base de données
   - `DB_USER` : Votre utilisateur PostgreSQL
   - `DB_PASSWORD` : Votre mot de passe PostgreSQL
   - `DB_HOST` : Votre host PostgreSQL
   - `DB_PORT` : 5432

## 📋 Étape 7 : Modifier wsgi.py pour la production

Dans le fichier `vente/wsgi.py`, modifiez la ligne 14 :
```python
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vente.settings_production')
```

## 📋 Étape 8 : Exécuter les migrations

1. Dans la console Bash :
   ```bash
   cd votre-repo
   source venv/bin/activate
   python manage.py migrate --settings=vente.settings_production
   ```

## 📋 Étape 9 : Collecter les fichiers statiques

1. Dans la console Bash :
   ```bash
   python manage.py collectstatic --settings=vente.settings_production --noinput
   ```

## 📋 Étape 10 : Créer un superutilisateur

1. Dans la console Bash :
   ```bash
   python manage.py createsuperuser --settings=vente.settings_production
   ```

## 📋 Étape 11 : Configurer l'application Web sur PythonAnywhere

1. Allez dans l'onglet "Web"
2. Cliquez sur "Add a new web app"
3. Choisissez "Manual configuration"
4. Choisissez "Python 3.10"
5. Configurez :
   - **Source code** : `/home/votre-username/votre-repo`
   - **Working directory** : `/home/votre-username/votre-repo`
   - **WSGI configuration file** : `/home/votre-username/votre-repo/vente/wsgi.py`
   - **Virtualenv** : `/home/votre-username/votre-repo/venv`

## 📋 Étape 12 : Configurer les fichiers statiques

1. Dans l'onglet "Web" → "Static files"
2. Ajoutez :
   - URL : `/static/`
   - Directory : `/home/votre-username/votre-repo/staticfiles`

3. Ajoutez aussi pour les médias :
   - URL : `/media/`
   - Directory : `/home/votre-username/votre-repo/media`

## 📋 Étape 13 : Modifier settings_production.py

Dans le fichier `vente/settings_production.py`, remplacez :
- `votre-username.pythonanywhere.com` par votre vrai username PythonAnywhere
- Les informations de base de données par celles de votre PostgreSQL

## 📋 Étape 14 : Redémarrer l'application

1. Allez dans l'onglet "Web"
2. Cliquez sur le bouton "Reload"

## 📋 Étape 15 : Tester votre site

1. Allez sur `https://votre-username.pythonanywhere.com`
2. Votre site devrait être en ligne !

## 🔧 Dépannage

### Si vous avez une erreur 500 :
- Vérifiez les logs dans l'onglet "Web" → "Logs"
- Vérifiez que toutes les migrations sont appliquées
- Vérifiez que les fichiers statiques sont collectés

### Si les fichiers statiques ne s'affichent pas :
- Vérifiez la configuration des fichiers statiques
- Exécutez à nouveau `collectstatic`

### Si la base de données ne fonctionne pas :
- Vérifiez les variables d'environnement
- Vérifiez que PostgreSQL est actif sur PythonAnywhere

## 📝 Notes importantes

- Le compte gratuit PythonAnywhere a des limitations
- Pour un site professionnel, envisagez un compte payant (~5€/mois)
- N'oubliez pas de remplacer le secret key par défaut
- Configurez les emails si vous utilisez les notifications

## 🚀 Prochaines étapes

- Configurer un domaine personnalisé
- Mettre en place un backup automatique
- Configurer les notifications par email
- Optimiser les performances
- Mettre en place HTTPS (déjà activé sur PythonAnywhere)
