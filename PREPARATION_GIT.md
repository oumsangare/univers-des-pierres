# Préparation du projet pour GitHub

## 📋 Étape 1 : Initialiser Git

Ouvrez un terminal dans votre dossier projet :
```bash
cd "c:\Users\HP ELITEBOOK 830 G8\Desktop\site vente en ligne\vente"
git init
```

## 📋 Étape 2 : Créer un repository GitHub

1. Allez sur [github.com](https://github.com)
2. Connectez-vous ou créez un compte
3. Cliquez sur "+" → "New repository"
4. Nommez-le : `univers-des-pierre`
5. Cochez "Public" ou "Private" selon votre préférence
6. Cliquez sur "Create repository"

## 📋 Étape 3 : Connecter votre projet local à GitHub

```bash
git remote add origin https://github.com/votre-username/univers-des-pierre.git
```

Remplacez `votre-username` par votre vrai username GitHub.

## 📋 Étape 4 : Ajouter les fichiers et committer

```bash
git add .
git commit -m "Initial commit - Univers des Pierres"
```

## 📋 Étape 5 : Push sur GitHub

```bash
git branch -M main
git push -u origin main
```

## 📋 Étape 6 : Vérifier sur GitHub

1. Allez sur votre repository GitHub
2. Vous devriez voir tous vos fichiers

## 🔧 Si vous avez des erreurs

### Erreur "remote origin already exists" :
```bash
git remote remove origin
git remote add origin https://github.com/votre-username/univers-des-pierre.git
```

### Erreur d'authentification :
- Configurez GitHub avec votre token d'authentification
- Ou utilisez SSH au lieu de HTTPS

## 📝 Fichiers ignorés par Git

Le fichier `.gitignore` empêche l'upload de :
- Le dossier `venv/` (environnement virtuel)
- Le fichier `db.sqlite3` (base de données locale)
- Les fichiers `__pycache__/`
- Les fichiers `.log`

## 🚀 Une fois sur GitHub

Vous pourrez suivre le guide `DEPLOIEMENT_PYTHONANYWHERE.md` pour déployer votre site.
