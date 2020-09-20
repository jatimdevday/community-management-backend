from .base import *

DEBUG = False

SOCIAL_AUTH_RAISE_EXCEPTIONS = False

try:
    from .local import *
except ImportError:
    pass
