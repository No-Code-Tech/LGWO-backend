
from pathlib import Path
# from dotenv import load_dotenv,find_dotenv
import os 
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent
# load_dotenv(find_dotenv())

from decouple import config





SECRET_KEY = config("DJANGO_SECRET_KEY")
DATABASE_KEY = config("DATABASE_URL")


DEBUG = True
ALLOWED_HOSTS = ['.railway.app']

if DEBUG:
    ALLOWED_HOSTS = ["127.0.0.1","localhost"]

# if os.environ.get("DATABASE")=="POSTGRES":
#     SECRET_KEY = os.environ.get('SECRET_KEY')
#     NAME = os.environ.get("NAME")
#     USER = os.environ.get("USER")
#     PASSWORD = os.environ.get("PASSWORD")
#     HOST = os.environ.get("HOST")
#     PORT = os.environ.get("PORT")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_extensions',
    'client',
    'employee',
    'finance',
    'supplier',
    'user',
    'drf_yasg',
    "corsheaders",

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'src.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# if os.environ.get("DATABASE")=="SQLITE":


DATABASES = {'default':dj_database_url.config(
    default=DATABASE_KEY,
    conn_max_age=600,
    conn_health_checks=True,
)}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# if os.environ.get("DATABASE")=="POSTGRES":
    # DATABASES = {
    #     "default": {
    #         "ENGINE" : "django.db.backends.postgresql",
    #         "NAME":NAME,
    #         "USER":USER,
    #         "PASSWORD":PASSWORD,
    #         "HOST":HOST,
    #         "PORT":PORT,
    #     }
    # }



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'user.CustomUser'



MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'uploads'


CORS_ALLOWED_ORIGINS = [
        "http://localhost:5173",
]



AUTH_USER_MODEL = "user.CustomUser"


GOFILE_API_TOKEN = config("GOFILE_API_TOKEN")