from django.conf.urls.defaults import *

urlpatterns = patterns('profiles.views',
    url(r'^(?P<username>\w+)/$', 'userprofile', name='userprofile'),
    url(r'^$', 'profile', name='profile'),
    url(r'^(?P<profile_id>\d+)/skill/(?P<skill_id>\d+)/(?P<verb>\w+)/$', 'ajax_view', name='ajax-view'),
)
