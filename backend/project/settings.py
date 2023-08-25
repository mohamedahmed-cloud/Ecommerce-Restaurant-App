"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@-dzrsy)95d^f57oxd)m5-j$m1--*6y7!2%$=&^cf7e(b1p*l9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'accounts',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'corsheaders',  # cors headers
    'accounts.apps.AccountsConfig',
    'products',
    'restaurants',
    'orders',
    # 'drf-spectacular',
    'drf_yasg',
    
    

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CORS middleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#*******************************
import datetime 

AUTH_USER_MODEL = 'accounts.CustomUser'
AUTHENTICATION_BACKENDS = ['accounts.auth_backends.EmailBackend']
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    # 'DEFAULT_TOKEN_EXPIRATION': {
    #     'rest_framework.authentication.TokenAuthentication': timedelta(days=7),
    # }
}

from django.conf import settings

# AUTH_TOKEN_VALIDITY = getattr(settings, 'AUTH_TOKEN_VALIDITY', timedelta(days=1))

# Emailing settings


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_FROM = 'pythonlessons0@gmail.com'
EMAIL_HOST_USER = 'backendbackend90@gmail.com'
EMAIL_HOST_PASSWORD = 'fkgkonllykbobfin'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# PASSWORD_RESET_TIMEOUT = 14400
# SIMPLE_JWT = {
#     'ROTATE_REFRESH_TOKENS': False,
#     'BLACKLIST_AFTER_ROTATION': False,
#     'UPDATE_LAST_LOGIN': False,
# }
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=15),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=15),
}

# SESSION_EXPIRE_AT_BROWSER_CLOSE=True
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CORS_ORIGIN_ALLOW_ALL = True

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('POSTGRES_NAME'),
#         'USER': os.environ.get('POSTGRES_USER'),
#         'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
#         'HOST': 'db',
#         'PORT': 5432,
#     }
# }
# WSGI_APPLICATION = 'vercel_app.wsgi.app'