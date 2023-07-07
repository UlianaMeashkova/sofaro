"""
Django settings for sofaro project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", 'django-insecure-3$(j#!18wf=6nv9r8_5+6d98+9w(0ws$40-fvj!-+#nnkkqbsb')




DEBUG = os.getenv("DEBUG", "True") == "True"

ALLOWED_HOSTS = ["*"]

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "rest_framework",
    "rest_framework.authtoken",
    'crispy_forms',
    'crispy_bootstrap5',
    'sofaro',
    'products',
    'users',
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

ROOT_URLCONF = 'sofaro.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'sofaro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_NAME", "sofaro"),
        "USER": os.getenv("POSTGRES_USER", "sofaro"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "sofaro"),
        "HOST": os.getenv("POSTGRES_HOST", "localhost"),
        "PORT": 5432,
    }
}


LOGGING = {
   'version': 1,
   'disable_existing_loggers': False,
   'handlers': {
       'console': {
           'class': 'logging.StreamHandler',
           'formatter': 'simple',
       },
   },
   'formatters': {
       'simple': {'format': '%(levelname)s %(asctime)s %(message)s'},
   },
   'loggers': {
       '': {
           'handlers': ['console'],
           'level': 'INFO',
       },
       'django.db.backends': {
           'handlers': ['console'],
           'level': 'ERROR',
       }
   }
}

SECRET_KEY = "my-super-secret-key"



MY_CUSTOM_VARIABLE = 'ANY_TEXT_INFO'
MY_ENV_VARIABLE = os.getenv('MY_ENV_VARIABLE')


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



def _(x):
    return x

LANGUAGE_CODE = 'ru'



LANGUAGES = (
    ("en", _("English")),
    ("ru", _("Russian")),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LOCALE_PATH = (BASE_DIR/"locale",)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = os.environ.get("EMAIL_HOST", 'smtp.mail.ru')
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", 'sofaro.hotels@mail.ru')
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", 'GyJmc4m0qmXj9SXasSLG')
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", "587"))
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS", 'false') != "True"

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


