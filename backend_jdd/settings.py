import environ
from .settings_base import *

# reading .env file - only in development
env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', default=False)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default='')


# Static And Media
STATIC_ROOT = env( 'STATIC_ROOT',
                    default=os.path.join(BASE_DIR, "staticfiles")
                )

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

use_sqlite = env('USE_SQLITE', default=True)
sqlite_db = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
postgres_db = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    'default': env.db(),
}

DATABASES = sqlite_db if use_sqlite else postgres_db


# Python-Social-Auth
# https://python-social-auth.readthedocs.io/en/latest/configuration/django.html

SOCIAL_AUTH_GITHUB_KEY = env('GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = env('GITHUB_SECRET')
SOCIAL_AUTH_GITHUB_SCOPE = ['access_token']

# LOGIN_URL = ''
LOGIN_REDIRECT_URL = 'home'
# LOGOUT_URL = 'logout'
# LOGOUT_REDIRECT_URL = 'login'

#TODO: try psa google 
AUTHENTICATION_BACKENDS = (
    # 'social_core.backends.google.GoogleOpenId',
    # 'social_core.backends.google.GoogleOAuth2',
    # 'social_core.backends.google.GoogleOAuth',
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)