import os
from pathlib import Path
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = bool(int(os.environ.get('DEBUG', 0)))

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(' ')
CSRF_TRUSTED_ORIGINS =  os.environ.get('CSRF_TRUSTED_ORIGINS').split(' ')

DJANGO_CORE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_cotton',

]

UNFOLD_APPS = [
    "unfold",  # before django.contrib.admin
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.inlines",  # optional, if special inlines are needed
]

WAGTAIL_APPS = [
   "wagtail_localize",
    "wagtail_localize.locales",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail',
    'taggit',
    'modelcluster',
]

THRID_PARTY_APPS = [
    'django_htmx',
    'django_filters',
    'django_extensions',
    'allauth',
    'allauth.account',
    'rest_framework',
    'rosetta',
]

MY_APPS = [
    'blog',
    'core',
    'api',
    'wg_blog',
    'my_templatetags',
]

INSTALLED_APPS = WAGTAIL_APPS +  UNFOLD_APPS +  DJANGO_CORE_APPS + THRID_PARTY_APPS + MY_APPS

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
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'allauth_templates',
            BASE_DIR / 'templates',

        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                # 'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]



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

LANGUAGE_CODE = 'es'

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
    PRIVATE_ENDPOINT = f"https://{os.getenv('R2_ACCOUNT_ID')}.r2.cloudflarestorage.com"
    PUBLIC_ENDPOINT = os.getenv('R2_CUSTOM_DOMAIN')
    
    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
            "OPTIONS": {
                "secret_key": os.getenv('R2_SECRET_ACCESS_KEY'),
                "access_key": os.getenv('R2_ACCESS_KEY_ID'),
                "bucket_name": os.getenv('R2_BUCKET_NAME'),
                "location": "media",
                "default_acl": "public-read",
                "signature_version":"s3v4",
                "endpoint_url": PRIVATE_ENDPOINT,
                "custom_domain":PUBLIC_ENDPOINT,

            },
        },
        "staticfiles":{
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
            "OPTIONS": {
                "secret_key": os.getenv('R2_SECRET_ACCESS_KEY'),
                "access_key": os.getenv('R2_ACCESS_KEY_ID'),
                "bucket_name": os.getenv('R2_BUCKET_NAME'),
                "location": "static",
                "default_acl": "public-read",
                "signature_version":"s3v4",
                "endpoint_url": PRIVATE_ENDPOINT,
                "custom_domain":PUBLIC_ENDPOINT,

            },
        },
    }

    # Django’s STATIC_URL must end in a slash and this must not. It is best to set this variable independently of STATIC_URL.
    # SEE  https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
    STATIC_URL = f"{PUBLIC_ENDPOINT}/static/"
    MEDIA_URL = f"{PUBLIC_ENDPOINT}/media/"

else:
    
    STATIC_URL = 'static/'
    STATIC_ROOT = BASE_DIR / 'static/'
    MEDIA_URL = 'media/'
    MEDIA_ROOT = BASE_DIR / 'media/'

STATICFILES_DIRS = [
    BASE_DIR / 'staticfiles'
]



ADMINS = [
    ('Keiner Mendoza', 'keienrmendoza.pagos@gmail.com'),
]

MANAGERS = ADMINS


# Email
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')
USE_EMAIL = bool(int(os.environ.get('USE_EMAIL', 0)))
if USE_EMAIL:
    EMAIL_HOST = os.environ.get('EMAIL_HOST')
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 0))
    EMAIL_USE_TLS = bool(int(os.environ.get('EMAIL_USE_TLS', 0)))

    SERVER_EMAIL = 'servidor@example.com'  # Correo que aparecerá como remitente
    ADMINS = [('Admin', 'admin@example.com')]  # Correo al que se enviarán los errores


#Loggin
    

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(levelname)s - %(asctime)s - %(name)s - %(message)s"
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'  # Filtro para no enviar emails en modo DEBUG
        }
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "filters": [],
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
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
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}



# Celery
CELERY_BROKER_URL = 'amqp://guest:guest@rabbitmq:5672/'

# # Url
ROOT_URLCONF = os.environ.get('ROOT_URLCONF', 'config.urls')

WHATSAPP_NUMBER = os.environ.get('WHATSAPP_NUMBER')


# wagtail


# This is the human-readable name of your Wagtail install
# which welcomes users upon login to the Wagtail admin.
WAGTAIL_SITE_NAME = 'My Project'
WAGTAIL_I18N_ENABLED = USE_I18N
WAGTAIL_CONTENT_LANGUAGES = LANGUAGES

# Replace the search backend
#WAGTAILSEARCH_BACKENDS = {
#  'default': {
#    'BACKEND': 'wagtail.search.backends.elasticsearch8',
#    'INDEX': 'myapp'
#  }
#}

# Wagtail email notifications from address
# WAGTAILADMIN_NOTIFICATION_FROM_EMAIL = 'wagtail@myhost.io'

# Wagtail email notification format
# WAGTAILADMIN_NOTIFICATION_USE_HTML = True

# Allowed file extensions for documents in the document library.
# This can be omitted to allow all files, but note that this may present a security risk
# if untrusted users are allowed to upload files -
# see https://docs.wagtail.org/en/stable/advanced_topics/deploying.html#user-uploaded-files
WAGTAILDOCS_EXTENSIONS = ['csv', 'docx', 'key', 'odt', 'pdf', 'pptx', 'rtf', 'txt', 'xlsx', 'zip']

# Reverse the default case-sensitive handling of tags
TAGGIT_CASE_INSENSITIVE = True


# WAGTAIL PIGMENTS
WAGTAIL_CODE_BLOCK_LANGUAGES = (
    ('cpp', 'C++'),
    ('java', 'Java'),
    ('python3', 'Python 3'),
    ('bash', 'Bash/Shell'),
    ('javascript', 'Javascript'),
    ('css', "CSS"),
    ('html', "HTML"),
    ('julia', "Julia"),
    ('nginx', "Nginx configuration file"),
    ('numpy', "NumPy"),
    ('django', "Django"),
    ('jinja', "Jinja"),
    ('docker', "Docker"),
    ('jinja', "Jinja"),
    ('yaml', "YAML"),
    ('json', "JSON"),
    ('plpgsql', "PL/pgSQL"),
    ('psql', "PostgreSQL console (psql)"),
)