import os

class Config(object):
    FREEZER_DESTINATION = os.environ.get('FREEZER_DESTINATION') or '../'
    FREEZER_REMOVE_EXTRA_FILES = os.environ.get('FREEZER_REMOVE_EXTRA_FILES') or False
    FREEZER_DEFAULT_MIMETYPE = os.environ.get('FREEZER_DEFAULT_MIMETYPE') or 'text/html'
