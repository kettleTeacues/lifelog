from .base import *

DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'lifelog.piechika.com']
CSRF_TRUSTED_ORIGINS = ['https://lifelog.piechika.com']

STATIC_ROOT = '/usr/share/nginx/html/static'
MEDIA_ROOT = '/usr/share/nginx/html/media'