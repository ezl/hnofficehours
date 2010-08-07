from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^', 'profiles.views.skills_test', name='skills-test'),

)
