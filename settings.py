# Django settings for hnofficehours project.
import os.path

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'hnoh.sqlite3',                # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/site_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'qlr90ew9v2lqzh3$24470#823!z8$txuy@v6w8^3v&(kuhx91!'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "hnofficehours.context_processors.output_timezone",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'hnofficehours.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',

    # third-party apps:
    'ajax_select',
    'django_extensions',
    'schedule',
    'timezones',

    # local apps:
    'officehours',
    'registration',
    'profiles',
)

USER_PROFILE_URL = "http://hnofficehours.com/profile/%s/" # the place holder is for the username

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
AUTH_PROFILE_MODULE = 'profiles.Profile'

AJAX_LOOKUP_CHANNELS = {
    'profile_skills' : dict(model='profiles.Skill', search_field='name'),
    # specifying the model Profile in the profiles app, and searching against the 'skills' field
}

GLOBAL_CALENDAR_SLUG = 'cal'
FIRST_DAY_OF_WEEK = 1 # Monday for USA


# ------------------------
# Deal with settings_local
# ------------------------
try:
    import types
    import settings_local
    # Make sure we don't have any synchronization problems between settings
    # files. This code will complain if, for example, you add an app to
    # INSTALLED_APPS in this settings.py file but forget to add it to
    # settings_local.py.
    for item_name in dir(settings_local):
        if item_name.startswith('__'):  # skip items in Python's namespace
            continue
        if item_name in locals().keys():
            local_setting = getattr(settings_local, item_name)
            entry_type = type(local_setting)
            # skip strings and other scalar values
            # (strings are iterable, which is why i'm not trying to cast to
            # iter and check for TypeError, which is usually the right way)
            if entry_type != types.ListType and entry_type != types.TupleType:
                continue
            original_setting = locals()[item_name]
            for item in original_setting:
                if item not in local_setting:
                    print("WARNING: local settings: '%s' missing item '%s'" %
                          (item_name, item))
    from settings_local import *    # overwrite items in local namespace
except ImportError:
    pass
