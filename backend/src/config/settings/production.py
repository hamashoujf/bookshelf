from .base import *

env.read_env(env_file=BASE_DIR / ".env.development", overwrite=True)
env.read_env(env_file=BASE_DIR / ".env.development.local", overwrite=True)

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = env("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = env.bool("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {"default": env.db()}
