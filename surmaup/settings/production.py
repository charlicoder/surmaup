from .base import *


DEBUG = False

ALLOWED_HOSTS = ['*']

STATIC_ROOT = (
    os.path.join(BASE_DIR, "statics"),
)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "surmaup_demo",
        "USER": "surmaup_user",
        "PASSWORD": "Mamun123",
        "HOST": "localhost",
        "PORT": "5432",
    }
}


print('Loaded production environment.....!')
