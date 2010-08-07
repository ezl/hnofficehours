from django.conf.urls.defaults import *

urlpatterns = patterns('profiles.views',
    url(r'^(?P<username>\w+)/$', 'userprofile', name='userprofile'),
    url(r'^', 'profile', name='profile'),
)
