"""
Django settings for production on PythonAnywhere.
"""

from .settings import *

# SECURITY WARNING: keep the secret key used in production secret!
# Vous devrez définir cette variable d'environnement sur PythonAnywhere
import os
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-h_!@eap=&pg#o98#77_-7h4)j#p&o)-i2_j!5$85z)ti$9epw+')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ALLOWED_HOSTS pour PythonAnywhere
# Remplacez 'votre-username.pythonanywhere.com' par votre vrai domaine
ALLOWED_HOSTS = [
    'votre-username.pythonanywhere.com',
    'www.votre-username.pythonanywhere.com',
]

# Si vous avez un domaine personnalisé, ajoutez-le ici
# ALLOWED_HOSTS.append('votre-domaine.com')

# Configuration de la base de données PostgreSQL sur PythonAnywhere
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'votre_db_name'),
        'USER': os.environ.get('DB_USER', 'votre_db_user'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'votre_db_password'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Configuration des fichiers statiques pour PythonAnywhere
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configuration des médias
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Sécurité supplémentaire pour la production
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Email configuration (optionnel)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'noreply@universdespierre.com')

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
