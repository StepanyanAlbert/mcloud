import os
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import  reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bnk99hg#5*v@dr7wl6auw7hd$8)81mjv!ivr*s4!y_!8k!6_d5'

# SECURITY WARNING: don't run with debug turned on in production!
<<<<<<< HEAD
DEBUG = False

ALLOWED_HOSTS = ['*']
=======
DEBUG = True

ALLOWED_HOSTS = []
>>>>>>> 48a22e972706e483092587876eb19290600e8f8d

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'custom',
	'languages',
	'password_reset',
	'music',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mcloud.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mcloud.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

<<<<<<< HEAD
AUTH_USER_MODEL='custom.MyUser'
LOGIN_URL=reverse_lazy('custom:login')
=======

>>>>>>> 48a22e972706e483092587876eb19290600e8f8d
# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/


LANGUAGES=(
				('en',_('ENGLISH')),
				('fr',_('FRENCH')),
			    ('cs', _('czech')),
			    ('hy', _('ARMENIAN')),
			    ('ru', _('RUSSIAN')),
				)
LOCALE_PATHS = (
					    os.path.join(BASE_DIR, 'locale'),

					)
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Yerevan'

USE_I18N = True

USE_L10N = True

USE_TZ = True

<<<<<<< HEAD
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
=======
>>>>>>> 48a22e972706e483092587876eb19290600e8f8d

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

<<<<<<< HEAD
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'
=======
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/' 
>>>>>>> 48a22e972706e483092587876eb19290600e8f8d
STATICFILES_DIRS = (
				    os.path.join(PROJECT_ROOT, 'static'),

				)

<<<<<<< HEAD
=======

>>>>>>> 48a22e972706e483092587876eb19290600e8f8d
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'
