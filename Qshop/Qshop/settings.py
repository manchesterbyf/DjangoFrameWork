"""
Django settings for Qshop project.

Generated by 'django-admin startproject' using Django 2.1.8.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^brypt@6in!9u2ah=elv!(_6q(7@s2+x$gvkb&22kyu097=-wr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Seller',
    'Buyer',
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

ROOT_URLCONF = 'Qshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Qshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,"static"),
)

# STATIC_ROOT = os.path.join(BASE_DIR,"static")
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR,"static")

alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwWL7j8vs1nlbBBImiyRZM8mPJuBUvxsMclZoYkOzbpU6dis66u3i66ndAqpLFz1KnIaNZhd9kVjkW4jnQ4ViQoBKFturq8d9UdgOez+5H58xlv98A4jLG/1yqD4J4HFRCSSZvPzz4YWIhLfl/C+gSbnTQjpd3aStqVBAhSrXxvH2xlLJWvhNp/4msc4+rLfdUZatfjMrjwikpW780grbC0eKBrXtDsn3PSKgp+PR64I7AokXKvyKJ0okaghkeLn2VnPrsFY3ajb0Llt2WgSgtzbxb1ajDPX0JQQSCUzhXfA8M+oofnWQKEPcYW12d56QFu22J+9mdOV7uftSTJhq5wIDAQAB
-----END PUBLIC KEY-----"""

alipay_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAwWL7j8vs1nlbBBImiyRZM8mPJuBUvxsMclZoYkOzbpU6dis66u3i66ndAqpLFz1KnIaNZhd9kVjkW4jnQ4ViQoBKFturq8d9UdgOez+5H58xlv98A4jLG/1yqD4J4HFRCSSZvPzz4YWIhLfl/C+gSbnTQjpd3aStqVBAhSrXxvH2xlLJWvhNp/4msc4+rLfdUZatfjMrjwikpW780grbC0eKBrXtDsn3PSKgp+PR64I7AokXKvyKJ0okaghkeLn2VnPrsFY3ajb0Llt2WgSgtzbxb1ajDPX0JQQSCUzhXfA8M+oofnWQKEPcYW12d56QFu22J+9mdOV7uftSTJhq5wIDAQABAoIBAAkToEMLiz41y/PQ9kYpmpY3q6RjexbNKjRjodqa2t0h2/CX7tf/+lqdSmZJn+SjV9Eo75IPIDGmPnGdZ11f8VC1vMR94vzZDCS/Q069mu7FBgrUSvnPfdj+eFc1Mjl6mBcZxK1+IeQ/5Dx2dTD0+0z6j9PX8Xfptszvm1ekvyPzOnpv6qK0K0V+Rw/td84Y56PVJhlxo5enZn7G5fID9IH+mjqBkMF+fM1r21ZgrTCO5JwwXHpYrELiAhxrecQS82ift876LLNcN3JvTJNuoAD/PKdowL57JN1zdi2YcihBb6bmKVkMku4pvACQowtwwX0DILSvLwK6hvs/xTakM0ECgYEA62bMnyX9KTn55myTWNzh6UkW+9s8cmra/mxsbf/oSFHtwZVSzBkc28QN/b3zC7wbOVrXDFxPFJYvfLssVZNFzcFwS2S2WB6Db8DA/qONuERy0H42YQXjUJQI4spntoVL1kfh3USWCcV+Gf2RYF4LpzcCPdL9WC1onEBuZuYpbn8CgYEA0k8DPvYplXo0ea23bKwoCPHLxGVmKI4f0lEyGjrXILXDSy4omYw1vO/e+fKYQkEKB7lCIeKOSFRT1MFetLfJbIdwHZMIbftlYpWn3a+KQ1yGZ6Ec6onpaezVmQUVypRued47ijW36Vy5mEDaHxTuDAPSXA0MYVhWcnf9ZrSMH5kCgYEAhSemEVP8yugniobaJkbzZvFYFejiXVpCO+56uxIpg1cMpRbhOd/uqgVRYLmklHu37o6K3EwO03dMr0J1BocC0itcaNk0J85CzOD8ik1bqeLWC0eJXQJmnbrO9/JEDkOCLViF05KrSCW1eeAr7pXkA5cjJnOFqO4uoUv05zHEN+MCgYBCvn66OaeC3/DNeRtQauadyBcyMjgUwN5KgihTeL8Ti3v6XSDXck8PslTioGJADKIhR2M8m8kqHVEpoWDsG7PaNLWZPTOcq/9GJVbMHUzVCgVB2Dj0GmawjlBPqvR6gVb6aFQfDeNbNWlVb6eJ27ucpo3ZVu7J6h4tX/VU5hHeaQKBgC0KZYErxe/3KUuVdD5wsm20fiLvUE+D4m2i/xdq7aFurB3LgVswTMZ1aL+9HCETHzFDFH1dJVuA8ntT5KRJK9RRPPMFMTqZj5fG0AESZt3rxNsLb8P2ssz9vHJOXznDaZoPh61Txyc7SIHM4wMArVWVIheEZ1AtchC7+nu8m86c
-----END RSA PRIVATE KEY-----"""

DING_URL = "https://oapi.dingtalk.com/robot/send?access_token=d1e8b271ee11da2a3f4f1a9bf35f1613b422a7af74552c8e510b968d53333474"
