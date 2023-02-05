from .base import *

DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'lifelog.piechika.com']
CSRF_TRUSTED_ORIGINS = ['https://lifelog.piechika.com']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

STATIC_ROOT = os.getenv('STATIC_ROOT')
MEDIA_ROOT = os.getenv('MEDIA_ROOT')