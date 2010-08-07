from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^hnofficehours/', include('hnofficehours.foo.urls')),
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'homepage.html'}),
    (r'^tagging_autocomplete/', include('tagging_autocomplete.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    url(r'^officehours/', include('officehours.urls')),
    url(r'^register/$', 'registration.views.register', name='register'),
    url(r'^register/finish/$', 'registration.views.set_password', name='set_password'),	
    #url(r'^profile/$', include('profiles.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        (r'^raw_template/(?P<template>.*)', 'django.views.generic.simple.direct_to_template'),
    )
