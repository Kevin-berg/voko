# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from unipath import Path

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = Path(__file__).ancestor(3)
MEDIA_ROOT = PROJECT_DIR.child("media")
STATIC_ROOT = PROJECT_DIR.child("static")
STATICFILES_DIRS = (
    PROJECT_DIR.child("assets"),
)
TEMPLATE_DIRS = (
    PROJECT_DIR.child("templates"),
)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Application definition

INSTALLED_APPS = (
    'flat',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_nose',
    'tinymce',
    'django_extensions',
    'braces',
    'bootstrap3',
    "django_cron",
    "captcha",

    'mailing',
    'accounts',
    'log',
    'finance',
    'ordering',
    'docs',
    'hijack',
    'compat'  # Requirement of hijack

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'vokou.middleware.OrderRoundMiddleware',
)

CRON_CLASSES = [
    "ordering.cron.MailOrderLists",
]

ROOT_URLCONF = 'vokou.urls'
WSGI_APPLICATION = 'vokou.wsgi.application'

# Internationalization

LANGUAGE_CODE = 'nl-nl'
TIME_ZONE = 'Europe/Amsterdam'
USE_I18N = True
USE_L10N = False
USE_TZ = True
DECIMAL_SEPARATOR = ','


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

AUTH_USER_MODEL = "accounts.VokoUser"
MEMBER_FEE = 20.0
LOGIN_REDIRECT_URL = "/"

EMAIL_SUBJECT_PREFIX = "[Voko Admin] "

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

MOLLIE_API_KEY = "SETME"

BASE_URL = "https://leden.vokoutrecht.nl"

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,xhtmlxtras,paste,searchreplace",
    'theme': "advanced",
    "theme_advanced_buttons3_add" : "cite,abbr",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'forced_root_block': False,
    "width": "75%",
    "height": "500px",
}

HIJACK_DISPLAY_ADMIN_BUTTON = False  # Because of custom user model

RECAPTCHA_PUBLIC_KEY = os.getenv("RECAPTCHA_SITE_KEY")
RECAPTCHA_PRIVATE_KEY = os.getenv("RECAPTCHA_SECRET_KEY")
NOCAPTCHA = True
