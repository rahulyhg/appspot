# Copyright 2008 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls.defaults import *


urlpatterns = patterns('',
    (r'^location/', include('astro.location.urls')),
    (r'^birth/', include('astro.birth.urls')),
    (r'^chart/', include('astro.chart.urls')),
    (r'^docs/', include('astro.docs.urls')),

    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)

#from django.conf.urls.defaults import *
#from polls.models import Poll
#
#info_dict = {
#    'queryset': Poll.objects.all().fetch(1000),
#}
#
#
#urlpatterns = patterns('',
#    (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
#    (r'^(?P<object_id>\w+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
#    url(r'^(?P<object_id>\w+)/results/$', 'django.views.generic.list_detail.object_detail', dict(info_dict, template_name='polls/results.html'), 'poll_results'),
#    (r'^(?P<poll_id>\w+)/vote/$', 'polls.views.vote'),
#)
