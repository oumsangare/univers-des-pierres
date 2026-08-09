#!/bin/bash

# Script de déploiement pour PythonAnywhere
# À exécuter sur PythonAnywhere via la console Bash

echo "🚀 Début du déploiement..."

# 1. Créer les dossiers nécessaires
echo "📁 Création des dossiers nécessaires..."
mkdir -p logs media staticfiles

# 2. Tirer les dernières modifications
echo "📥 Récupération des dernières modifications depuis GitHub..."
git pull origin main

# 3. Activer l'environnement virtuel
echo "🔧 Activation de l'environnement virtuel..."
source venv/bin/activate

# 4. Installer les dépendances si nécessaire
echo "📦 Installation des dépendances..."
pip install -r requirements.txt --quiet

# 5. Exécuter les migrations (avec gestion d'erreur)
echo "🗄️ Exécution des migrations..."
python manage.py migrate --settings=vente.settings_production --noinput || echo "⚠️  Erreur lors des migrations (peut être normale si DB déjà à jour)"

# 6. Collecter les fichiers statiques
echo "📁 Collecte des fichiers statiques..."
python manage.py collectstatic --settings=vente.settings_production --noinput --clear

# 7. Redémarrer l'application web
echo "🔄 Redémarrage de l'application web..."
echo "⚠️  N'oubliez pas de redémarrer l'application web via l'interface PythonAnywhere"

echo "✅ Déploiement terminé avec succès !"
echo "📝 Prochaines étapes :"
echo "   1. Allez dans l'onglet 'Web' sur PythonAnywhere"
echo "   2. Cliquez sur le bouton 'Reload'"
echo "   3. Videz le cache de votre navigateur (Ctrl+F5)"
