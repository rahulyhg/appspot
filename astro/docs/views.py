# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import QueryDict
from django.utils.http import urlencode
from django.utils.datastructures import MultiValueDict


from google.appengine.api.datastore_errors import BadKeyError
from google.appengine.api import users

from collections import defaultdict
from utils import *

def names(request):
    return render_to_response('astro/docs/names.html')
    
