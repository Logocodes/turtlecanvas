import os

DEBUG = True

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.pardir, os.pardir, 'demo.db'))

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'turtlecanvas',
]

ROOT_URLCONF = 'turtlecanvas.urls.demo'

TEMPLATE_DIRS = []
