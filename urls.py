from django.conf.urls.defaults import patterns
import re

urlpatterns = patterns(re.sub(r'[^.]*$', "views", __name__),
    (r"^(?:srishell/)?$", 'index'),
    (r"^srishell/download/$", 'srishell_download'),
    (r'^srishell/', include('srishell.urls')),
    (r'^astro/', include('astro.urls')),
)
