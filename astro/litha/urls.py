from django.conf.urls.defaults import patterns
import re

urlpatterns = patterns(re.sub(r'[^.]*$', "views", __name__),
    (r'^$', 'index'),
)

