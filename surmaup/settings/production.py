from .base import *


DEBUG = False

STATIC_ROOT = (
    os.path.join(BASE_DIR, "statics"),
)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "charlicoder_db",
        "USER": "charlidbuser",
        "PASSWORD": "Mamun123",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

print('Loaded production environment.....!')
