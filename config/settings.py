"""
Django settings for config project.
Generated by 'django-admin startproject' using Django 4.0.
For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import json
import os
from pathlib import Path
from typing import List

import django_stubs_ext

from .my_settings import (
    EMAIL_SECRET_KEY,
    MY_DATABASES,
    MY_IAMPORT_KEY,
    MY_IAMPORT_SECRET,
    MY_SECRET,
    MY_SECRET_ACCESS_KEY,
    S3_BUCKET_NAME,
)

django_stubs_ext.monkeypatch()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = MY_SECRET["SECRET_KEY"]


DEBUG = True

# ALLOWED_HOSTS: List[str] = []
ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    # "corsheaders",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "order",
    "user",
    "plant",
    "product",
    "info",
    "feed",
    "cart",
    "crispy_forms",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.instagram",
    "allauth.socialaccount.providers.kakao",
    "allauth.socialaccount.providers.naver",
    "survey",
    "storages",
]

# password reset
CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = MY_DATABASES
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "ko-kr"
TIME_ZONE = "Asia/Seoul"
USE_I18N = True
USE_L10N = True
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_DIR = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [STATIC_DIR]

STATIC_ROOT = os.path.join(BASE_DIR, ".static_root")


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "user.Users"

CART_ID = "cart item"

# aws s3 setting
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

AWS_ACCESS_KEY_ID = MY_SECRET_ACCESS_KEY["ACCESS_KEY"]
AWS_SECRET_ACCESS_KEY = MY_SECRET["SECRET_KEY"]
AWS_STORAGE_BUCKET_NAME = S3_BUCKET_NAME["BUCKET_NAME"]

AWS_S3_REGION_NAME = "ap-northeast-2"
AWS_S3_SIGNATURE_VERSION = "s3v4"

AWS_DEFAULT_ACL = "public-read"  # its make read anybody

# =============== password reset email setting =============== #
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# gmail connect port
EMAIL_PORT = "587"
# Email host server
EMAIL_HOST = "smtp.gmail.com"
# use email
EMAIL_HOST_USER = "greendoor2203@gmail.com"
# use email password
EMAIL_HOST_PASSWORD = EMAIL_SECRET_KEY["EMAIL_SECRET_KEY"]
# TLS security method
EMAIL_USE_TLS = True
# site auto response setting
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of 'allauth'
    "django.contrib.auth.backends.ModelBackend",
    # 'allauth' specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1
LOGIN_REDIRECT_URL = "/"

# cors setting
# CORS_ORIGIN_ALLOW_ALL = True # <- 모든 호스트 허용
# CORS_ALLOW_CREDENTIALS = True
# CORS_ORIGIN_WHITELIST = ["http://127.0.0.1:8000", "http://localhost:8000"]  # it make white list that can access
# CORS_ALLOW_METHODS = (
#     'DELETE',
#     'GET',
#     'OPTIONS',
#     'PATCH',
#     'POST',
#     'PUT',
# )
# CORS_ALLOW_HEADERS = (
#     'accept',
#     'accept-encoding',
#     'authorization',
#     'content-type',
#     'dnt',
#     'origin',
#     'user-agent',
#     'x-csrftoken',
#     'x-requested-with',
# )
IAMPORT_KEY = MY_IAMPORT_KEY
IAMPORT_SECRET = MY_IAMPORT_SECRET


# eb 올리기 전에 수정할것
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
LOGIN_REDIRECT_URL = "/"
ACCOUNT_AUTHENTICATED_LOGOUT_REDIRECTS = True
ACCOUNT_LOGOUT_REDIRECT_URL = "/"

ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"
