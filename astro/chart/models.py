from appengine_django.models import BaseModel
from google.appengine.ext import db
from google.appengine.ext.db import djangoforms,GqlQuery
from django.forms import *
from astro.location.models import Location 
from google.appengine.api import users


#class Event(db.Model):
#    name        = db.StringProperty(required=True)
#    time        = db.DateTimeProperty()
#    isMale      = db.BooleanProperty()
#    location    = db.ReferenceProperty(Location)
#    added_by    = db.UserProperty()
#    def __unicode__(self):
#        return "%s"%(self.name())
#
#class EventForm(djangoforms.ModelForm):
#    country = ChoiceField(widget=widgets.Select({'onChange':"submit()"}))
#    city = ChoiceField()
#    
#    def __init__(self, data=None, instance=None, *args, **kwargs):
#        super(EventForm, self).__init__(data=data,instance=instance, *args, **kwargs)
#        self.fields['country'].choices=[(loc.country,loc.country) for loc in Location.all().fetch(1000)] 
#        country = \
#            (data and 'country' in data) and data['country'] \
#            or (instance and instance.location.country) \
#            or self.fields['country'].choices[0][0]
#        self.fields['city'].choices=[(loc.key(),loc.city) for loc in Location.all().filter('country =',country).fetch(1000)]
#    def save(self):
#        if not self.is_valid():
#            return
#        self.cleaned_data['location'] = Location.get(self.cleaned_data['city'])
#        entity = djangoforms.ModelForm.save(self,commit=False)
#        entity.added_by = users.get_current_user()
#        entity.put()
#
#        
#    class Meta:
#        model = Event
#        exclude = ['added_by']
