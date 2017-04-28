"""
Django settings for guestbook project.

Generated by "django-admin startproject" using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
import os
import sys


SOURCE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SOURCE_DIR)
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
sys.path.append(os.path.join(SOURCE_DIR, "apps"))
sys.path.append(os.path.join(SOURCE_DIR, "external_apps"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "(82_c00@_&adfy6!34bt!0*x%p$^)d23u8*t14hs&4!ih+t1un"

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

ADMINS = (
    ("Alexander Melnik", "heretic.alex@gmail.com"),

)
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "guestbook",
    "oauth2_provider",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("DB_ENV_DB_NAME"),
        "USER": os.environ.get("DB_ENV_DB_USER"),
        "PASSWORD": os.environ.get("DB_ENV_DB_USER_PASSWORD"),
        "HOST": os.environ.get("DB_PORT_5432_TCP_ADDR"),
        "PORT": os.environ.get("DB_PORT_5432_TCP_PORT"),
        "SCHEMA": os.environ.get("DB_ENV_DB_SCHEMA"),
    }
}
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyLibMCCache",
        "LOCATION": [
            os.environ.get("MEMCACHED_PORT_11211_TCP_ADDR") + ":" + os.environ.get("MEMCACHED_PORT_11211_TCP_PORT"),
        ]
    }
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        },
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        },
        "logfile_common": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "logs", "common.log"),
            "maxBytes": 1024 * 1024 * 20,  # 20 Mb
            "backupCount": 5,
            "formatter": "standard",
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "project_common": {
            "handlers": ["logfile_common"],
            "level": "DEBUG",
            "propagate": True,
        }
    }
}
# DEBUG Toolbar
if DEBUG:
    INTERNAL_IPS = ("192.168.99.1", )

    DEBUG_TOOLBAR_PATCH_SETTINGS = False
    MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE
    INSTALLED_APPS += ["debug_toolbar"]
    DEBUG_TOOLBAR_PANELS = [
        "debug_toolbar.panels.versions.VersionsPanel",
        "debug_toolbar.panels.timer.TimerPanel",
        "debug_toolbar.panels.request.RequestPanel",
        "debug_toolbar.panels.sql.SQLPanel",
        "debug_toolbar.panels.cache.CachePanel",
        "debug_toolbar.panels.signals.SignalsPanel",
        "debug_toolbar.panels.logging.LoggingPanel",
    ]
    DEBUG_TOOLBAR_CONFIG = {"RENDER_PANELS": True}


AUTH_USER_MODEL = "guestbook.CustomUser"

OAUTH2_PROVIDER = {
    "SCOPES": {"read": "Read scope", "write": "Write scope"}
}
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
        # "oauth2_provider.ext.rest_framework.IsAuthenticatedOrTokenHasScope"
    ],
    "PAGE_SIZE": 5,
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "oauth2_provider.ext.rest_framework.OAuth2Authentication",
    ),
}
