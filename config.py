import os

class Config(object):
    TEMPLATES_AUTO_RELOAD = os.environ.get('TEMPLATES_AUTO_RELOAD') or 'True' # Makes sure the templates reload when we make a change in development
    FREEZER_DESTINATION = os.environ.get('FREEZER_DESTINATION') or '../'
    FREEZER_REMOVE_EXTRA_FILES = os.environ.get('FREEZER_REMOVE_EXTRA_FILES') or 'False'
