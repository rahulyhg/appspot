from django.conf.urls.defaults import patterns, url
import re

urlpatterns = patterns(re.sub(r'[^.]*$', "views", __name__),
    (r'^$', 'index'),
    (r'^((?P<key>.+?)/)?edit/$', 'edit'),
    url(r'^ajax_cities', 'ajax_cities', name='ajax_cities'),
)

