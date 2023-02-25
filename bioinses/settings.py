from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-carq2!&zn!%=w$ogz_*-nfxdm^-+j^ne+0uub)k9m7wlm9owy"

DEBUG = True

ROOT_URLCONF = "bioinses.urls"

INSTALLED_APPS = [
  "django.contrib.staticfiles",
  "fontawesomefree",
]

MIDDLEWARE = [
  "django.middleware.common.CommonMiddleware",
]

TEMPLATES = [
  {
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": ["bioinses/templates"]
  },
]

STATIC_URL = "static/"

STATICFILES_DIRS = [
  "bioinses/static"
]

MEDIA_URL = "media/"

MEDIA_ROOT = "bioinses/media"

TIME_ZONE = "Asia/Bangkok"
