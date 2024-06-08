from dbpt.core.utils.collections import deep_update
from dbpt.core.utils.settings import get_settings_from_envirionment
from. import ENVVAR_SETTINGS_PREFIX

'''
This takes the env variables with a matching prefix, strips out the ptrfix, and adds it to the global settings

eg.

export DBPTSETTINGS_DATABASES_DEFAULT_ENGINE=django.db.backends.postgresql

will add the following to the global settings:
DATABASES_DEFAULT_ENGINE = 'django.db.backends.postgresql'
'''

# globals() is a dictionary that holds all the global variables in the current scope

deep_update(globals(), get_settings_from_envirionment(ENVVAR_SETTINGS_PREFIX))