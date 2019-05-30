"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from configurations import Configuration

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Base(Configuration):
    """Base configuration for django app."""
    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

    # Configuring email from enviorenment and setting mailhog as default
    EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
    EMAIL_HOST = os.environ.get('EMAIL_HOST', 'mail')
    EMAIL_PORT = os.environ.get('EMAIL_PORT', 1025)
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
    EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
    EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL')

    EMAIL_FROM = 'Lalita <lalita@ac.python.org.ar>'
    EMAIL_MANAGER = 'presidencia@ac.python.org.ar'

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'svz&bkp-k(zydvn+v9$kqmds=ncl8w8(i-sp^1u280vez=g-zj'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True
    ALLOWED_HOSTS = ['*']

    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django_extensions',
        'members.apps.MembersConfig',
        'crispy_forms',
        'events.apps.EventsConfig',
        'reversion',
        'reversion_compare',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'events.middleware.CurrentUserMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'website.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

    WSGI_APPLICATION = 'website.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/2.0/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    # Password validation
    # https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
    # https://docs.djangoproject.com/en/2.0/topics/i18n/

    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
    DATE_INPUT_FORMATS = ('%d/%m/%Y', '%d-%m-%Y')
    LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]

    CRISPY_TEMPLATE_PACK = 'bootstrap3'

    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR

    LOGIN_URL = '/cuentas/login/'

    AFIP = {
        'url_wsaa': "https://wsaahomo.afip.gov.ar/ws/services/LoginCms?wsdl",
        'url_wsfev1': "https://wswhomo.afip.gov.ar/wsfev1/service.asmx?WSDL",
        'selling_point': 4000,
        'cuit': 20267565393,
        'auth_cert_path': '/tmp/reingart.crt',
        'auth_key_path': '/tmp/reingart.key',
    }

    INVOICES_GDRIVE = {
        'credentials_filepath': "",
        'folder_id': "",
    }

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'DEBUG',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            },
            '': {
                'handlers': ['console'],
                'propagate': True,
                'level': 'INFO',
            },
        },
    }

    # Azure blob-storage
    AZURE_ACCOUNT_KEY = os.environ.get("AZURE_ACCOUNT_KEY")
    AZURE_ACCOUNT_NAME = os.environ.get("AZURE_ACCOUNT_NAME")
    AZURE_CONTAINER = os.environ.get("AZURE_CONTAINER")
    AZURE_SSL = os.environ.get("AZURE_SSL", True)
    AZURE_QUERYSTRING_AUTH = os.environ.get("AZURE_QUERYSTRING_AUTH", False)


# try to import the local settings; if the file is not there just create a stub class
# for the inheritance later
try:
    from local_settings import LocalSettings
except ModuleNotFoundError:
    class LocalSettings:
        pass


class Dev(LocalSettings, Base):
    """Development configuration."""


class Staging(Base):
    """Staging configuration."""
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('POSTGRES_DB', "memberships"),
            'USER': os.environ.get('POSTGRES_USER', "postgres"),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD', "secret"),
            'HOST': os.environ.get('POSTGRES_HOST', "localhost"),
            'PORT': os.environ.get('POSTGRES_PORT', 5432),
        }
    }

    DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
    STATICFILES_STORAGE = "storages.backends.azure_storage.AzureStorage"


class Prod(Base):
    """Production configuration."""
    DEBUG = False
    TEMPLATE_DEBUG = False
    SECRET_KEY = os.getenv(
        'SECRET_KEY',
        '!a44%)(r2!1wp89@ds(tqzpo#f0qgfxomik)a$16v5v@b%)ecu')
    ALLOWED_HOSTS = [os.getenv('APP_DOMAIN')]
    # Database
    # https://docs.djangoproject.com/en/2.0/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('POSTGRES_DB', "memberships"),
            'USER': os.environ.get('POSTGRES_USER', "postgres"),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD', "secret"),
            'HOST': os.environ.get('POSTGRES_HOST', "localhost"),
            'PORT': os.environ.get('POSTGRES_PORT', 5432),
        }
    }

    EMAIL_HOST = os.environ.get('EMAIL_HOST')
    EMAIL_PORT = os.environ.get('EMAIL_PORT', '587')
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
    EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
    EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', True)
    EMAIL_TIMEOUT = int(os.environ.get('EMAIL_TIMEOUT', '10'))
    EMAIL_FROM = os.environ.get('EMAIL_FROM', 'do_not_reply@python.org.ar')

    AFIP = {
        'url_wsaa': "https://wsaa.afip.gov.ar/ws/services/LoginCms?wsdl",
        'url_wsfev1': "https://servicios1.afip.gov.ar/wsfev1/service.asmx?WSDL",
        'selling_point': 7,
        'cuit': 30715639129,
        'auth_cert_path': '/tmp/afip_pyar.crt',
        'auth_key_path': '/tmp/afip_pyar.key',
    }

    DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
    STATICFILES_STORAGE = "storages.backends.azure_storage.AzureStorage"

    sentry_sdk.init(
        dsn=os.environ.get('SENTRY_DSN'),
        integrations=[DjangoIntegration()]
    )
