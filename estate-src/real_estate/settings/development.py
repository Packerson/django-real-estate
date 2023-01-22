from .base import *

EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_USE_TLS = True
EMAIL_PORT = env("EMAIL_PORT")
# EMAIL_HOST_USER = 'apikey' # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = env("SENDGRID_API_KEY")
DEFAULT_FROM_EMAIL = 'info@sharpmind.club'
SITE_NAME = "Real Estate"
SENDGRID_SANDBOX_MODE_IN_DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': env("POSTGRES_ENGINE"),
        'NAME': env("POSTGRES_DB"),
        'USER': env("POSTGRES_USER"),
        'PASSWORD': env("POSTGRES_PASSWORD"),
        'HOST': env("POSTGRES_HOST"),
        'PORT': env("POSTGRES_PORT"),
    }
}
