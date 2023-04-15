from .base import *


"""set settings for sending email in celery"""
EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

SENDGRID_SANDBOX_MODE_IN_DEBUG = False
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")

EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "apikey"
SENDGRID_API_KEY = env("SENDGRID_API_KEY")
EMAIL_PORT = env("EMAIL_PORT")
DOMAIN = env("DOMAIN")

SITE_NAME = "Real Estate"


DATABASES = {
    "default": {
        "ENGINE": env("POSTGRES_ENGINE"),
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
}

"""Can use CELERY AS an namespace because in celery.py CELERY 
is set as a nampespace"""

CELERY_BROKER_URL = env("CELERY_BROKER")
CELERY_RESULT_BACKEND = env("CELERY_BACKEND")
CELERY_TIMEZONE = "UTC"
