
# -*- coding: utf-8 -*-
from .base import *
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
SITE_ID = 3
ALLOWED_HOSTS_ = ['taskbuster-project.herokuapp.com']
DATABASES['default'] = dj_database_url.config(conn_max_age=500)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
