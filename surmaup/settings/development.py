from .base import *

DEBUG = True

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "surmaup_db",
        "USER": "postgres",
        "PASSWORD": "Mamun123",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

print('Loaded development environment.....!')
