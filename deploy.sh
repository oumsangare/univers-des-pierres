#!/bin/bash

# Script de déploiement pour PythonAnywhere
# À exécuter sur PythonAnywhere via la console Bash

echo "🚀 Début du déploiement..."

# 1. Tirer les dernières modifications
echo "📥 Récupération des dernières modifications depuis GitHub..."
git pull origin main

# 2. Activer l'environnement virtuel
echo "🔧 Activation de l'environnement virtuel..."
source venv/bin/activate

# 3. Installer les dépendances si nécessaire
echo "📦 Installation des dépendances..."
pip install -r requirements.txt

# 4. Exécuter les migrations
echo "🗄️ Exécution des migrations..."
python manage.py migrate --settings=vente.settings_production

# 5. Collecter les fichiers statiques
echo "📁 Collecte des fichiers statiques..."
python manage.py collectstatic --settings=vente.settings_production --noinput

# 6. Redémarrer l'application web
echo "🔄 Redémarrage de l'application web..."
# Sur PythonAnywhere, vous devez le faire manuellement via l'interface web

echo "✅ Déploiement terminé !"
echo "📝 N'oubliez pas de redémarrer l'application web via l'interface PythonAnywhere"
