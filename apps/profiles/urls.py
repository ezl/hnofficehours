from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^', 'profiles.views.profile', name='profile'),

)
