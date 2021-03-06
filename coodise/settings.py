# -*- coding: utf-8 -*-

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l*aw1_q)q@*5_!+@d62zq%**!(tdub6s3#)f!irfl9pg=-qp6o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "192.168.1.100",
    "188.121.161.140",
    "127.0.0.1",
    "192.168.1.10",
    "localhost",
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'bootstrap3',
    'coodise',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'coodise.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['coodise/templates'],
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

WSGI_APPLICATION = 'coodise.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEFAULT_CHARSET = "utf-8"

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images);
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "coodise/static/"), )

###############################################################
# Coodise custom settings

# Put folder with MEDIA in here:
# e.g.
# MEDIA_DIR = "/mnt/media/extHDD"
MEDIA_DIR = 'Cloud'

MEDIA_ICONS = {
    "Picture": "glyphicon-picture",
    "Video": "glyphicon-facetime-video",
    "Folder": "glyphicon-folder-open",
    "Audio": "glyphicon-music",
    "Image": "glyphicon-floppy-disk",
    "Default": "glyphicon-file",
}

# watchout, tied to FILE_EXTENSIONS
MEDIA_TYPES = ["Picture", "Video", "Audio", "Text", "Image"]

# list of lowercase file extensions
FILE_EXTENSIONS = {
    "Image": [
        "iso",
        "img",
        "raw",
    ],
    "Video": [
        "webm",
        "avi",
        "mov",
        "mkv",
        "mp4",
        "3gp",
        "divx",
        "mpeg",
        "mpg",
    ],
    "Picture": [
        "png",
        "jpg",
        "jpeg",
        "tif",
        "tiff",
        "bmp",
        "gif",
    ],
    "Audio": [
        "mp3",
        "flac",
        "ogg",
        "wav",
        "wma",
    ],
    "Text": [
        "txt",
        "py",
        "pyw",
        "cpp",
        "log",
        "srt",
        "c",
        "m",
        "h",
        "hpp",
        "go",
        "mod",
        "js",
        "html",
        "xml",
        "yaml",
        "cmake",
        "java",
    ],
}  # TODO: extend this list
