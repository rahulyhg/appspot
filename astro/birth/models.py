from astro.location.models import Location
from django.forms import Select, ChoiceField, RadioSelect, CharField, SplitDateTimeField
from django.utils.safestring import mark_safe
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext.db import djangoforms
from misc.widgets import MyDateTimeWidget
import datetime


class Event(db.Model):
    name        = db.StringProperty(required=True)
    time        = db.DateTimeProperty(required=True,default=datetime.datetime(1999,12,31,23,59,59))
    sex         = db.StringProperty()
    location    = db.ReferenceProperty(Location)
    added_by    = db.UserProperty()
    refk   = db.SelfReferenceProperty()
    def __unicode__(self):
        return "%s"%(self.name())
    
datetimeformats=[
    '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30:59'
    '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
    '%Y-%m-%d',              # '2006-10-25'
    '%Y/%m/%d %H:%M:%S',     # '10/25/2006 14:30:59'
    '%Y/%m/%d %H:%M',        # '10/25/2006 14:30'
    '%Y/%m/%d',              # '10/25/2006'
]

class EventForm(djangoforms.ModelForm):
    country = ChoiceField(widget=Select({'class':"select_country"}))
    city = ChoiceField(widget=Select({'class':"select_city"}))
    sexs = ['ස්ත්‍රී','පුරුෂ']
    sex  = ChoiceField(choices=zip(sexs,sexs),widget=RadioSelect(), initial=0, required=False)
    sex.widget.renderer.render=lambda self:mark_safe('\n'.join([u'%s' % w for w in self]))
    sex.widget.renderer.safe=False
    name = CharField(label='නම',error_messages={'required': 'නම ඇතුළත් කරන්න'})
    time = SplitDateTimeField(widget=MyDateTimeWidget(),
                         error_messages={
                                         'required': 'වේලාව ඇතුළත් කරන්න',
                                         'invalid':'වලංගු දිනයක් හා වේලාවක් ඇතුළත් කරන්න (උදා : 1980-2-29 23:59:59)',
                                         })
    
    def __init__(self, data=None, instance=None, *args, **kwargs):
        super(EventForm, self).__init__(data=data,instance=instance, *args, **kwargs)
        self.fields['country'].choices=map(lambda country:(country,country), set(map(lambda loc:loc.country,Location.all().fetch(1000)))) 
        self.fields['country'].initial=instance and instance.location.country
        country = \
            (data and 'country' in data) and data['country'] \
            or (instance and instance.location.country) \
            or (self.fields['country'].choices[0][0] if self.fields['country'].choices else None) 
        if country:
            self.fields['city'].choices=[(loc.key(),loc.city) for loc in Location.all().filter('country =',country).fetch(1000)]
            self.fields['city'].initial=instance and instance.location.key()
    def save(self):
        if not self.is_valid():
            return
        self.cleaned_data['location'] = Location.get(self.cleaned_data['city'])
        entity = djangoforms.ModelForm.save(self,commit=False)
        entity.added_by = users.get_current_user()
        entity.put()

        
    class Meta:
        model = Event
        exclude = ['added_by']
