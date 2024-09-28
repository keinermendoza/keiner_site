import os
from pathlib import Path
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR.parent / '.env.dev')
SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = bool(int(os.environ.get('DEBUG', 0)))

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(' ')
CSRF_TRUSTED_ORIGINS =  os.environ.get('CSRF_TRUSTED_ORIGINS').split(' ')

INSTALLED_APPS = [
    "unfold",  # before django.contrib.admin
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.inlines",  # optional, if special inlines are needed
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_cotton',

    'blog',
    'core',
    'api',
    'django_htmx',
    'django_filters',
    'django_extensions',

    'allauth',
    'allauth.account',
    'rest_framework',
    'rosetta',

]
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    "django_htmx.middleware.HtmxMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "allauth.account.middleware.AccountMiddleware",
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'allauth_templates',
            BASE_DIR / 'components',

        ],
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


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(levelname)s - %(asctime)s - %(name)s - %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "filters": [],
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
    },
}


WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', _('English')),
    ('es', _('Spanish')),
    ('pt', _('Portuguese'))
]

TIME_ZONE = 'America/Manaus'

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ]
}

# ALL AUTH
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_MAX_EMAIL_ADDRESSES = 1
ACCOUNT_PRESERVE_USERNAME_CASING = False
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
LOGIN_REDIRECT_URL = reverse_lazy('core:home')
ACCOUNT_ADAPTER = 'core.adapter.AccountAdapterEmailAsync'

# Database
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE', 'django.db.backends.sqlite3'),
        'HOST': os.environ.get('SQL_HOST'),
        'USER': os.environ.get('USER'),
        'NAME': os.environ.get('NAME', BASE_DIR / 'db.sqlite3'),
        'PASSWORD': os.environ.get('PASSWORD'),
        'PORT': os.environ.get('SQL_PORT'),
    }
}

# Statics
USE_S3 = bool(int(os.environ.get('USE_S3', 1)))

if USE_S3:
    AWS_S3_ACCESS_KEY_ID = os.getenv('AWS_S3_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_BUCKET_NAMESPACE = os.getenv('AWS_BUCKET_NAMESPACE')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_BUCKET_REGION = os.getenv('AWS_S3_BUCKET_REGION')
    
    AWS_S3_ENDPOINT_URL = f'https://{AWS_BUCKET_NAMESPACE}.compat.objectstorage.{AWS_S3_BUCKET_REGION}.oraclecloud.com'

    # AWS_QUERYSTRING_EXPIRE = 1800
    AWS_LOCATION = f'{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}'
    
    STATICFILES_STORAGE = 'core.custom_storages.StaticStorage'
    DEFAULT_FILE_STORAGE = 'core.custom_storages.MediaStorage'

    STATIC_URL = f"{AWS_LOCATION}/static/"
    STATIC_ROOT = 'static/'
    
    MEDIA_URL = f"{AWS_LOCATION}/media/"
    MEDIA_ROOT = 'media/'
else:
    
    STATIC_URL = 'static/'
    STATIC_ROOT = BASE_DIR / 'static/'
    MEDIA_URL = 'media/'
    MEDIA_ROOT = BASE_DIR / 'media/'

STATICFILES_DIRS = [
    BASE_DIR / 'staticfiles'
]

# Email
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')
USE_EMAIL = bool(int(os.environ.get('USE_EMAIL', 0)))
if USE_EMAIL:
    EMAIL_HOST = os.environ.get('EMAIL_HOST')
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 0))
    EMAIL_USE_TLS = bool(int(os.environ.get('EMAIL_USE_TLS', 0)))

# Celery
CELERY_BROKER_URL = 'amqp://guest:guest@rabbitmq:5672/'

# # Url
ROOT_URLCONF = os.environ.get('ROOT_URLCONF', 'config.urls')

WHATSAPP_NUMBER = os.environ.get('WHATSAPP_NUMBER')