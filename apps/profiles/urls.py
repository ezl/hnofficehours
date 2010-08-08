from django.conf.urls.defaults import *

urlpatterns = patterns('profiles.views',
    url(r'^$', 'profile', name='profile'),
    url(r'^(?P<username>\w+)/$', 'view_profile', name='view_profile'),
)
