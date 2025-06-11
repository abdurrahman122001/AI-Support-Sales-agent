"""
Django settings for telnyx_project project.
"""

from pathlib import Path

# ─── BASE DIRECTORY ─────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

# ─── SECRET KEY & DEBUG ─────────────────────────────────────────────────────────
SECRET_KEY = "django-insecure-please-replace-with-your-own-secret"
DEBUG = True

# ─── ALLOWED HOSTS ──────────────────────────────────────────────────────────────
# For local dev, "*" is fine.
ALLOWED_HOSTS = ["http://localhost:8080"]

# ─── INSTALLED APPS ─────────────────────────────────────────────────────────────
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Our custom app
    "calls",
]

# ─── MIDDLEWARE ─────────────────────────────────────────────────────────────────
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ─── ROOT URLCONF ────────────────────────────────────────────────────────────────
ROOT_URLCONF = "telnyx_project.urls"

# ─── TEMPLATES ──────────────────────────────────────────────────────────────────
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # We rely on app-level templates
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

# ─── WSGI APPLICATION ───────────────────────────────────────────────────────────
WSGI_APPLICATION = "telnyx_project.wsgi.application"

# ─── DATABASES ──────────────────────────────────────────────────────────────────
# Using SQLite for simplicity
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ─── PASSWORD VALIDATION ─────────────────────────────────────────────────────────
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

# ─── INTERNATIONALIZATION ────────────────────────────────────────────────────────
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ─── STATIC FILES (CSS, JavaScript, Images) ──────────────────────────────────────
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "calls" / "static",
]

# ─── DEFAULT AUTO FIELD ─────────────────────────────────────────────────────────
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
