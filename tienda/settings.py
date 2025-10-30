from .settings import *  # Importa todo del settings principal (producción)

# Configuración local (desarrollo)
DEBUG = True

ALLOWED_HOSTS = []

# Base de datos local (usa SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
