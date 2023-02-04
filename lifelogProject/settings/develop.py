from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]

INSTALLED_APPS += [
    'corsheaders',
]

MIDDLEWARE += [
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True