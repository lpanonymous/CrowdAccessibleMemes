from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['crowdmemes.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'daqnvnd2g43pck',
        'USER':'qwynfjgrvwofbb',
        'PASSWORD':'1b8f9d9ffe76f185c4b1abf3617300143caf5bd1178dcad69739be9d3730cfbb',
        'HOST':'ec2-50-17-255-120.compute-1.amazonaws.com',
        'PORT':5432,
        
    }
}

#DATABASES={
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        
#    }
#}

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

#import dj_database_url
#from decouple import config
#DATABASES = {
#    'default': dj_database_url.config(
#        default=config('DATABASE_URL')
#    )
#}

STATIC_DIRS = (BASE_DIR, 'static')