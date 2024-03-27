"""
Django settings for versatile_app project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import sentry_sdk

# from sentry_sdk.integrations.django import DjangoIntegration


# sentry_sdk.init(
#     dsn="https://1525381614cb88bff4fdcedf4147af56@o4506834851921920.ingest.sentry.io/4506834853298176",
#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for performance monitoring.
#     traces_sample_rate=1.0,
    
#     # Set profiles_sample_rate to 1.0 to profile 100%
#     # of sampled transactions.
#     # We recommend adjusting this value in production.
#     profiles_sample_rate=1.0,
#     # integrations=[DjangoIntegration()]
# )

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zx3)yr=p&xq%1mylcvz!*svame%3+1x%8o4q91@ehs&na+ma@0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['https://dd99-2001-44c8-4742-8616-7909-28f0-14b-937b.ngrok-free.app', '127.0.0.1', 'localhost']
# CSRF_TRUSTED_ORIGINS = ['https://15dd-2001-44c8-4742-8616-7909-28f0-14b-937b.ngrok-free.app.ngrok.io']
# ALLOWED_HOSTS = ['127.0.0.1']    # For Sentry

# Application definition
INSTALLED_APPS = [
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',    # ต้องวางก่อน app ตัวอื่น

    'widget_tweaks',
    'django_recaptcha',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    
    'todo',
    'weather',
    'poll',
    'user_example',
    'dashboard',
    'omise_payment',
    'diary',
    'beginner',
    'ToDo2'

]

SITE_ID = 1
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#Sign-up allauth
ACCOUNT_EMAIL_REQUIRED = True  
ACCOUNT_EMAIL_VERIFICATION = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'versatile_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': [BASE_DIR/'templates'], # for allauth
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

WSGI_APPLICATION = 'versatile_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators



AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]


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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR /'media' # When user upload anythings go to media folder

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# LOGIN_REDIRECT_URL = '/user_example'    # สำหรับ user example
# LOGOUT_REDIRECT_URL = '/user_example'   # สำหรับ user example

RECAPTCHA_PUBLIC_KEY = '6LeVzYApAAAAAMVcFTcCIiXM9mI9EMz2c_DV6t6b'
RECAPTCHA_PRIVATE_KEY = '6LeVzYApAAAAAPtJVc1UgWOZwy8gE0_eJquMzDo7'
# RECAPTCHA_REQUIRED_SCORE  = '9.0'

# Custom recaptcha to allauth 
ACCOUNT_FORMS = {
    'signup': 'versatile_app.form.CustomSignupForm'
}
# ACCOUNT_SIGNUP_FORM_CLASS = 'versatile_app.forms.AllauthSignupForm'


# STATICFILES_STORAGE = "storages.backends.s3.S3Storage"
# DEFAULT_FILE_SOTRAGE = "storages.backends.s3.S3Storage" 
AWS_STORAGE_BUCKET_NAME = "django-s3-images"
AWS_ACCESS_KEY_ID = "AKIATCKASNHHBMAMZUPA"
AWS_SECRET_ACCESS_KEY = "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"
AWS_QUERYSTRING_AUTH = False