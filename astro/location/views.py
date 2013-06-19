# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext

from google.appengine.api.datastore_errors import BadKeyError

from models import *

from collections import defaultdict
from utils import * 

from django import forms
from django.utils import simplejson
from django.http import HttpResponse

def to_int(s):
    return len(s) and int(s) or 0

countries = lambda:map(lambda c:(c,c), set([loc.country for loc in Location.all().fetch(1000)]))
class CountryForm(forms.Form):
    def __init__(self, *args, **kwargs):
        forms.Form.__init__(self, *args, **kwargs)
        self.errors['country']=''
    country = forms.ChoiceField(countries(),label='රට',widget=widgets.Select({'onChange':"submit()"}))

def index(request):
    form = CountryForm(data=request.POST)
    data_list = Location.all()
    if 'country' in request.POST:
        data_list=data_list.filter('country',request.POST['country'])
    return render_to_response(getHtmlPath(__name__,'index.html'), 
                              {'data_list': data_list,
                               'country':form.as_table()
                               })

def edit(request,key=None):
    loc = LocationForm(data = len(request.POST) and request.POST or None,
                      instance=key and Location.get(key))
    if loc.is_valid():
        loc_db = Location.all()\
            .filter('country',loc.cleaned_data['country']) \
            .filter('city',loc.cleaned_data['city']).fetch(1)
        loc_db = len(loc_db) and loc_db[0] or None
        loc = LocationForm(data=request.POST, instance=loc_db)
        loc.save()
        return redirect(getParentPath(__name__))
    return render_to_response('astro/location/edit.html', {'location': loc},
                               context_instance=RequestContext(request))
    
def ajax_cities(request):
    country = request.GET.get('country')
    cities = Location.all().filter('country =',country).fetch(1000)
    return HttpResponse(simplejson.dumps(dict([(str(loc.key()),loc.city) for loc in cities]))) 

