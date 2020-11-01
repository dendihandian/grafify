import os

APP_DEBUG = (os.getenv("APP_DEBUG") == 'true')
APP_SECRET_KEY = os.getenv("APP_SECRET_KEY")
