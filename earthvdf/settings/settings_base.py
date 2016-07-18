import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

ADMINS = ()
MANAGERS = ADMINS

TIME_ZONE = 'America/New_York'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'

USE_I18N = True
USE_L10N = True

STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.locale.LocaleMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'earthvdf.middleware.crossdomainxhr.XsSharingMiddleware',
)

ROOT_URLCONF = 'earthvdf.urls'

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.admin',
	'django.contrib.admindocs',
	'django.contrib.gis',
	'sekizai',
	'core',
)

DEFAULT_LON = -81.669722
DEFAULT_LAT = 41.482222
