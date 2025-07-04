"""
Django settings for Oh_Wow_wow_pair project.

Generated by 'django-admin startproject' using Django 5.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
import logging
import environ
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 讀取 Oh_Wow_wow_pair/.env（專案根目錄）
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR.parent, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')
RECAPTCHA_SECRET_KEY = env('RECAPTCHA_SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
SIMPLE_JWT = {
    'USER_ID_FIELD': 'username',  #告訴 SimpleJWT 你不是用 id，而是 username 當 primary key
    'USER_ID_CLAIM': 'user_id',   #token 裡存的是哪個 key，可以留 user_id
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition

UNFOLD = {
    "SITE_TITLE": "喔哇哇配！管理後台",  # 瀏覽器標籤頁標題
    "SITE_HEADER": "娃娃社交網站管理系統",      # 頁面頂部標題
}

INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.filters",  # 可選
    "unfold.contrib.forms",    # 可選
    "unfold.contrib.inlines",  # 可選
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',  # CORS headers
    'core',  #確保有加入core app
    'post',
    'search',
]

#每次 API 請求都會檢查 HTTP Header 裡的 token（Authorization: Bearer ...），用 SimpleJWT 驗證使用者身份。
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    # 不全域啟用 throttle，僅在個別 view 設定
}
AUTH_USER_MODEL = 'core.User' #自定義 User 模型
'''
刪除資料方法
rm db.sqlite3
find core/migrations -name "*.py" -not -name "__init__.py" -delete
find core/migrations -name "*.pyc" -delete
建立 migration
python manage.py makemigrations
python manage.py migrate
'''
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # CORS middleware
    'django.middleware.locale.LocaleMiddleware', # 啟用語言判斷
]

ROOT_URLCONF = 'wowpair.urls'

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:5173",  # 前端的開發伺服器 URL
    "http://localhost:5173",  # 前端的開發伺服器 localhost URL OK
]

# 圖片上傳相關
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.parent / 'media'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wowpair.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hant'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}