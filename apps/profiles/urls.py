from django.conf.urls.defaults import *

urlpatterns = patterns('profiles.views',
    url(r'^$', 'profile', name='profile'),
    url(r'^list/$', 'list_profiles', name='list_profiles'),
    url(r'^(?P<username>\w+)/$', 'view_profile', name='view_profile'),
    url(r'^(?P<profile_id>\d+)/skill/(?P<skill_id>\d+)/(?P<verb>\w+)/$', 'ajax_view', name='ajax-view'),
)
