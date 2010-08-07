Settings and settings_local.copy
--------------------------------

To set up your local development server, copy the file settings_local.copy to
settings_local.py. In settings_local.py, you can set whatever Django settings
you need to customize without affecting the global settings.py file, which
contains settings that will also be used in production.

There is a snippet of code at the bottom of settings.py that will check if your
settings_local.py is missing any settings defined in settings.py. It's to help
with the problem of repeating yourself in two places, in case you add an entry
to a list in settings.py and forget to add it to settings_local.py.

