from django.conf.urls.defaults import patterns, include


urlpatterns = patterns('',
    (r'^location/', include('astro.location.urls')),
    (r'^birth/', include('astro.birth.urls')),
    (r'^chart/', include('astro.chart.urls')),
    (r'^litha/', include('astro.litha.urls')),
    (r'^docs/', include('astro.docs.urls')),
)
