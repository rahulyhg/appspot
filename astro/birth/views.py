# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import QueryDict
from django.utils.http import urlencode
from django.utils.datastructures import MultiValueDict


from google.appengine.api.datastore_errors import BadKeyError
from google.appengine.api import users

from models import *

from collections import defaultdict
from utils import *

def index(request,admin='',user=None):
    if admin:
        assert 'sandeva'==str(users.get_current_user()).encode('utf-8')
        user=users.User(user)
    else:
        user=users.get_current_user()
    data_list = Event.all().filter("added_by",user).filter("sex !=",None).fetch(1000)#.order_by('-pub_date')[:5]
    return render_to_response(getHtmlPath(__name__,'index.html'), {'data_list': data_list})

@login_required
def editPureEvent(request,ref_key,event_key=None):
    return edit(request, event_key, True,ref_key=ref_key)

@login_required
def edit(request,event_key=None,pureEvent=False,ref_key=None):
    db_event=None
    if event_key:
        db_event=Event.get(event_key)
        assert db_event.added_by==users.get_current_user() or \
            'sandeva'==str(users.get_current_user()).encode('utf-8')
    event = EventForm(data = len(request.POST) and request.POST or None,
                      instance=db_event )
    #event.fields['sex'].required=not ref_key
    if 'control_submit' in request.POST and event.is_valid():
        if ref_key:
            event.cleaned_data['refk']=Event.get(ref_key)
        event.save()
        return redirect(getParentPath(__name__))
    return render_to_response(getHtmlPath(__name__,"edit.html"), 
                              {'event': event, 
                               'pureEvent':pureEvent,
                               #"action":"/astro/birth/%sedit/%s"%(event_key+'/' if event_key else '','event/' if pureEvent else ''),
                               },
                               context_instance=RequestContext(request))
    
