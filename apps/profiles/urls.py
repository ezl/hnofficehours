from django.conf.urls.defaults import *

urlpatterns = patterns('profiles.views',
    url(r'^$', 'profile', name='profile'),
    url(r'^list/$', 'list_profiles', name='list_profiles'),
    url(r'^ajax_toggle_availability/$', 'ajax_toggle_availability',
        name='ajax_toggle_availability'),
    url(r'^set_availability/(?P<set_status>\d)/$', 'set_availability',
        name='set_availability'),
    url(r'^skills/(?P<skill>\w+)/$', 'list_profiles_by_skill',
       name='list_profiles_by_skill'),
    url(r'^(?P<username>\w+)/$', 'view_profile', name='view_profile'),
    url(r'^(?P<profile_id>\d+)/skill/(?P<skill_id>\d+)/(?P<verb>\w+)/$', 'ajax_view', name='ajax-view'),
)
