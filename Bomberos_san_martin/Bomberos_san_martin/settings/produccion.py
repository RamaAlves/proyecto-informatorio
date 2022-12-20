from .base import *

ALLOWED_HOSTS = ['info2022.pythonanywhere.com']

DATABASES={
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'info2022$blogdb',
        'USER': 'info2022',
        'PASSWORD': 'etapa2info',
        'HOST': 'info2022.mysql.pythonanywhere-services.com',
    },
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False