from django.conf.urls.defaults import *

urlpatterns = patterns('profiles.views',
    url(r'^$', 'profile', name='profile'),
    url(r'^list/$', 'list_profiles', name='list_profiles'),
    url(r'^(?P<username>\w+)/$', 'view_profile', name='view_profile'),
)
