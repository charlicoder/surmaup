from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "surmaup_db",
#         "USER": "postgres",
#         "PASSWORD": "Mamun123",
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }
print('At development.py ' + BASE_DIR)

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

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# print(STATICFILES_DIRS)
