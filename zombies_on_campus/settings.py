"""
Django settings for zombies_on_campus project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# These will be needed when the project goes live
# from django.conf import settings
# from django.conf.urls.static import static

# This as well
# if not settings.DEBUG:
#         urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n#isjueba2@d1pwttf#8ic!w@=8gm&0x^3h8=^t=@6r1)8@)t7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# Will need to set this when the project goes live.
ALLOWED_HOSTS = []


# Application definition
# If we change anything here, we need to run 'python manage.py migrate'
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'zombies',
    # Registration add-on. We don't have to do hard-lifting
    'registration',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'zombies_on_campus.urls'

WSGI_APPLICATION = 'zombies_on_campus.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Templates' directory
# Template path: to avoid hardcoding the directory
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
# Add any other directories where templates may be
# Absolute paths should be used.
TEMPLATE_DIRS = (
    TEMPLATE_PATH,
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
# Requires absolute path
STATIC_PATH = os.path.join(BASE_DIR, 'static')
# Where static files (JavaScript, images, etc) will be found.
# IMPOTANT: do not remove the slashes.
STATIC_URL = '/static/'
# Directories where we keep our static files
STATICFILES_DIRS = (
    STATIC_PATH,
)


# Media paths
# Where user uploaded files will reside
MEDIA_URL = '/media/'
# Where the files that were uplaoded will be stored on a disk.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Required stuff for registration add-on
REGISTRATION_OPEN = True
ACCOUNT_ACTIVATION_DAYS = 7  # Do we need this?
REGISTRATION_AUTO_LOGIN = True
LOGIN_REDIRECT_URL = '/zombies/'
LOGIN_URL = '/accounts/login/'