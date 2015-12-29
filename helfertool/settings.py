"""
Django settings for helfertool project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'CHANGE-ME-AFTER-INSTALL'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

ADMINS = (('Admin Name', 'admin@localhost'), )

CONTACT_MAIL = 'helfertool@localhost'

PRIVACY_URL = 'https://fs.tum.de/datenschutz/'
IMPRINT_URL = 'https://fs.tum.de/impressum/'
CODE_URL = 'https://git.fs.tum.de/helfertool/helfertool'

GROUP_ADDUSER = "registration_adduser"
GROUP_ADDEVENT = "registration_addevent"

# HTML sanitization for textfields
BLEACH_ALLOWED_TAGS = ['p', 'b', 'i', 'u', 'em', 'strong', 'a', 'br', 'ul',
                       'ol', 'li']
BLEACH_ALLOWED_ATTRIBUTES = ['href', 'style']
BLEACH_ALLOWED_STYLES = ['font-weight', 'text-decoration']
BLEACH_STRIP_TAGS = True

# badges: path to pdflatex
BADGE_PDFLATEX = '/usr/bin/pdflatex'

# badge creation
BADGE_IMAGE_DIR = os.path.join(BASE_DIR, 'badgeupload')

# copy generated latex code for badges to this file, disable with None
BADGE_TEMPLATE_DEBUG_FILE = "/tmp/badge.tex"

# file permissions for newly uploaded files
FILE_UPLOAD_PERMISSIONS = 0o640

# for e-mail debugging
#EMAIL_HOST = 'localhost'
#EMAIL_PORT = 1025

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

# Logging
#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#    'handlers': {
#        'file': {
#            'level': 'DEBUG',
#            'class': 'logging.FileHandler',
#            'filename': os.path.join(BASE_DIR, 'django.log'),
#        },
#        'mail_admins': {
#            'level': 'ERROR',
#            'class': 'django.utils.log.AdminEmailHandler',
#        },
#    },
#    'loggers': {
#        #'django.request': {
#        #    'handlers': ['file'],
#        #    'level': 'DEBUG',
#        #    'propagate': True,
#        #},
#        'django.request': {
#            'handlers': ['mail_admins'],
#            'level': 'ERROR',
#            'propagate': False,
#        },
#    },
#}

# Application definition

INSTALLED_APPS = (
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'badges',
    'registration',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'helfertool.urls'

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
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'helfertool.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('de', _('German')),
    ('en', _('English')),
)

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files and media (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'  # must end with '/' !
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
