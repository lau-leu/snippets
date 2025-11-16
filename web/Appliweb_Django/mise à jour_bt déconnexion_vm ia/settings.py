"""
Django settings for myproject project.
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2-j$hfqc9zzv8w@xbn#b&uffvkyr!s)j9y3l)br!5%l@z!jcn-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # IMPORTANT: Mettre False en production

ALLOWED_HOSTS = ['django.leumaire.fr', 'www.django.leumaire.fr', '192.168.1.58', 'localhost']

# Configuration pour reverse proxy
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_otp',
    'django_otp.plugins.otp_totp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_email',
    'two_factor',
    'authentication',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_app',
        'USER': 'django_user',
        'PASSWORD': 'LLPoste_Tsuchinshan25$',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Session configuration
SESSION_COOKIE_AGE = 1800  # 30 minutes
SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_SECURE = True  # Uniquement HTTPS
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'

# CSRF Protection
CSRF_COOKIE_SECURE = True  # Uniquement HTTPS
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SAMESITE = 'Lax'
CSRF_TRUSTED_ORIGINS = ['https://django.leumaire.fr', 'https://www.django.leumaire.fr']

# Security Headers
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT = True  # Rediriger HTTP vers HTTPS
SECURE_HSTS_SECONDS = 31536000  # 1 an
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Login URLs
LOGIN_URL = 'two_factor:login'
LOGIN_REDIRECT_URL = 'setup_2fa_choice'  # Notre page de choix personnalisée
LOGOUT_REDIRECT_URL = 'two_factor:login'

# Two-Factor Authentication Settings
TWO_FACTOR_PATCH_ADMIN = True
TWO_FACTOR_CALL_GATEWAY = None
TWO_FACTOR_SMS_GATEWAY = 'two_factor.gateways.twilio.gateway.Twilio'

# Activer l'authentification par email
OTP_EMAIL_SENDER = 'django-app-2fa@gmail.com'  # Votre email Gmail
OTP_EMAIL_SUBJECT = 'Code de vérification - Django App'
OTP_EMAIL_BODY_TEMPLATE_PATH = 'otp_email/token.txt'
OTP_EMAIL_TOKEN_VALIDITY = 300  # 5 minutes

# Twilio Configuration (pour SMS)
TWILIO_ACCOUNT_SID = 'votre_account_sid'  # À remplacer
TWILIO_AUTH_TOKEN = 'votre_auth_token'    # À remplacer
TWILIO_CALLER_ID = 'votre_numero_twilio'  # À remplacer

# Email Configuration (pour 2FA par email)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'django.app.2fa@gmail.com'  # À remplacer
EMAIL_HOST_PASSWORD = 'xumlcqfonblbuuin'  # À remplacer
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Ollama Configuration (VM IA voisine)
OLLAMA_API_URL = 'http://192.168.1.58:11434'  # IP de votre VM Ollama
OLLAMA_DEFAULT_MODEL = 'llama2'  # Modèle par défaut
