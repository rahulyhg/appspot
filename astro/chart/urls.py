from django.conf.urls.defaults import patterns
import re

urlpatterns = patterns(re.sub(r'[^.]*$', "views", __name__),
    (r'^$', 'index'),
    (r'^simplechart/$', 'simplechart'),
    (r'^((?P<key>.*?)/)?circlechart/$', 'circlechart'),
    (r'^bmp/$', 'bmp'),
    (r'^bmp2/$', 'bmp2'),
)

