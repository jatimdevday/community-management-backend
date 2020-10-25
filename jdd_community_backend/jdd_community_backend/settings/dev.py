from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', True)

# Django toolbar

INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
)

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost'
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@44vzh2g2a00$%&v$tqop)ex2jbwb46bx@o_q2*2#@(d+e$v%k'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
try:
    postgres_db = {
        # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
        'default': env.db(),
    }
    DATABASES = postgres_db
except:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

SOCIAL_AUTH_RAISE_EXCEPTIONS = True

try:
    from .local import *
except ImportError:
    pass

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}