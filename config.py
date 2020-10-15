import os

class Config(object):
    TEMPLATES_AUTO_RELOAD = os.environ.get('TEMPLATES_AUTO_RELOAD') or 'True' # Makes sure the templates reload when we make a change in development
