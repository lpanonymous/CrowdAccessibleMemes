from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

#DATABASES = {
#    'sqlite': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    },
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'memesaccesibles',
#        'USER': 'root',
#        'PASSWORD': '',
#        'HOST': 'localhost',
#        'PORT': '3306',
#        'OPTIONS': {
#            'sql_mode': 'traditional',
#        }
#    }
#}
import dj_database_url
from decouple import config
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}