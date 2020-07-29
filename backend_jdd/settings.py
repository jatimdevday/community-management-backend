import environ
from .setting_base import *

# reading .env file - only in development
env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', default=False)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default='')

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