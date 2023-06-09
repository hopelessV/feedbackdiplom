import os
from pathlib import Path
from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')

DEFAULT_FROM_EMAIL = 'admin@ms.permkrai.ru'  # замените на свою почту

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hipvwqv-36waz#lnkniy7tg73q^)j)nb8(*93s$+q^#j+b!90)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'startform.apps.StartformConfig',
    'user.apps.UserConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'feedbac.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'feedbac.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'user:login'
LOGIN_REDIRECT_URL = 'appeal:main_form'

COLOR_CHOICES = (
    ('Ведущий инспектор судебного участка № 8 Дзержинского судебного района г. Перми','Ведущий инспектор судебного участка № 8 Дзержинского судебного района г. Перми'),
    ('Делопроизводитель судебного участка № 1 Дзержинского судебного района г. Перми', 'Делопроизводитель судебного участка № 1 Дзержинского судебного района г. Перми'),
    ('Секретарь суда сектора делопроизводства судебных участков Дзержинского судебного района г. Перми','Секретарь суда сектора делопроизводства судебных участков Дзержинского судебного района г. Перми'),
    ('Заведующий сектором, секретарь суда сектора делопроизводства судебных участков Дзержинского судебного района г. Перми','Заведующий сектором, секретарь суда сектора делопроизводства судебных участков Дзержинского судебного района г. Перми'),
    ('Помощник мирового судьи судебного участка № 1 Индустриального судебного района г. Перми','Помощник мирового судьи судебного участка № 1 Индустриального судебного района г. Перми'),
)

TYPE_SELECT = (
('Да', 'Да'),
('Нет', 'Нет'),
)

QUESTION_SELECT = (
    ('Будет ли испытательный срок?', 'Будет ли испытательный срок?'),
    ('На время испытательного срока есть ли разница в заработной плате?', 'На время испытательного срока есть ли разница в заработной плате?'),
    ('Что является критерием прохождения испытательного срока?', 'Что является критерием прохождения испытательного срока?'),
    ('Что конкретно я буду делать на данной должности? Что будет входить в мои обязанности?', 'Что конкретно я буду делать на данной должности? Что будет входить в мои обязанности?'),
    ('C какими сложностями придется столкнуться?', 'C какими сложностями придется столкнуться?'),
    ('Какая скорость роста в компании? Как часто случаются повышения?', 'Какая скорость роста в компании? Как часто случаются повышения?'),
    ('Какие карьерные перспективы у меня на этой позиции? Куда дальше расти?', 'Какие карьерные перспективы у меня на этой позиции? Куда дальше расти?'),
    ('Какие еще будут этапы перед выходом на работу?', 'Какие еще будут этапы перед выходом на работу?'),
)