from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^search/$', 'search.views.search', name='search'),
)
