import site
site.addsitedir('/home/hnofficehours/env/lib/python2.6/site-packages')

import sys
sys.path.append('/home/hnofficehours')
sys.path.append('/home/hnofficehours/hnofficehours')
sys.path.append('/home/hnofficehours/hnofficehours/apps')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'hnofficehours.production-settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
