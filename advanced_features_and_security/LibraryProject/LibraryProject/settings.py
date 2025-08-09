# settings.py

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hs1f6=s^z$(3qxxp2jtm^wdr&fk0rg3meugtmqfbmn%&908z='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # Turn off debug mode in production to avoid leaking sensitive info

# Define allowed hosts for your application
ALLOWED_HOSTS = ['yourdomain.com', 'localhost', '127.0.0.1']  # Change 'yourdomain.com' to your real domain

# Application definition
INSTALLED_APPS = [
    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your custom app
    'bookshelf',

    # django-csp app for Content Security Policy headers
    'csp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'csp.middleware.CSPMiddleware',  # Middleware to add Content Security Policy headers

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF protection middleware
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Protects against clickjacking
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # You can add project-level template directories here if needed
        'APP_DIRS': True,  # Looks for templates inside each app's 'templates' folder
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

WSGI_APPLICATION = 'LibraryProject.wsgi.application'

# Database configuration (SQLite example)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation - default Django validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# ----------------------
# SECURITY SETTINGS
# ----------------------

# Enables the browser's XSS filtering and protection
SECURE_BROWSER_XSS_FILTER = True

# Prevents the site from being displayed in a frame to protect against clickjacking
X_FRAME_OPTIONS = 'DENY'

# Prevents the browser from guessing content types, reducing MIME type sniffing attacks
SECURE_CONTENT_TYPE_NOSNIFF = True

# Ensures the CSRF cookie is only sent over HTTPS
CSRF_COOKIE_SECURE = True

# Ensures the session cookie is only sent over HTTPS
SESSION_COOKIE_SECURE = True

# Redirect all HTTP requests to HTTPS (make sure you have SSL configured)
SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security settings (enforces HTTPS for a duration)
SECURE_HSTS_SECONDS = 31536000  # Enforce HTTPS for 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS to all subdomains
SECURE_HSTS_PRELOAD = True  # Allow your site to be included in browsers’ preload lists

# ----------------------
# Content Security Policy (CSP) SETTINGS
# ----------------------

# Default sources allowed for content loading (self = your own domain)
CSP_DEFAULT_SRC = ("'self'",)

# Allowed sources for stylesheets (including Google Fonts example)
CSP_STYLE_SRC = ("'self'", 'https://fonts.googleapis.com')

# Allowed sources for scripts
CSP_SCRIPT_SRC = ("'self'",)

# Allowed sources for images (including inline base64 images via 'data:')
CSP_IMG_SRC = ("'self'", 'data:')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
