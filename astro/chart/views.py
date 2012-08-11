# -*- coding:utf-8 -*-

from astro.birth.models import *
from astro.common.calculator import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.forms.widgets import Select
from google.appengine.api import users
from google.appengine.api.datastore_errors import BadKeyError
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from utils import *
#from converters.readUnicode import readUnicode
from converters.Kaputa import *
from converters.readUnicode import *
from astro.chart import *
from astro.chart.models import *
from astro.chart.orbs import *
from astro.chart.templatetags.charttags import *
from collections import defaultdict
from converters.readUnicode import readUnicode
from converters.Kaputa import *
import datetime
import time
import canvas
#from reportlab.pdfgen import canvas
from astro.consts.planets import *
import sys

def polar2xy(r,th):
    return r*cos(deg2rad(th)),r*sin(deg2rad(th))

def index(request):
    data_list = Event.all().filter("added_by",users.get_current_user()).fetch(1000)#.order_by('-pub_date')[:5]
    return render_to_response(getHtmlPath(__name__,'index.html'), {'data_list': data_list})
def pvt_calc(event):
    if not "GMT" in event:
        event["GMT"]=event['time']-timedelta(seconds=event['timezone'])
    GetKendraNirayana(event)
    dlt=dict(event)
    dlt['GMT']+=datetime.timedelta(hours=1)
    GetKendraNirayana(dlt)
    for p in wheel.planets:
        event[p+".Speed"]=(dlt[p]-event[p])*24
    x=(event['Moon']/48000)%9
    event['Dasa Start']=event['GMT']-datetime.timedelta(days=(dasha_prama_acc[int(x)]+(x%1)*dasha_prama[int(x)])*365.256363)
    return event

def calc(key):
    db_event = Event.get(key)
    event = {}
    for k in db_event.properties():
        event[k]=getattr(db_event, k)
    for k in db_event.location.properties():
        event[k]=getattr(db_event.location, k)
    assert db_event.added_by==users.get_current_user()
    return pvt_calc(event)

def str2int(s):
    if type(s)==int:
        return s
    r=int(s[:-2])*3600
    sgn=r/abs(r)
    r+=sgn*int(s[-2:])*60
    return r

def calcGet(params,comp):
    event={'timezone':"+000000",'longitude':0,'latitude':0,'time':datetime.datetime.now().strftime("%Y%m%d%H%M%S")}
    for k in params:
        event[k.encode('utf-8')]=params[k].encode('utf-8')
    event['timezone']=3600*int(event['timezone'][1:3])+60*int(event['timezone'][3:5])+int(event['timezone'][5:])
    event['longitude'],event['latitude']=str2int(event['longitude']),str2int(event['latitude'])
    event['time']=datetime.datetime.strptime(event['time'], "%Y%m%d%H%M%S")
    if comp:
        event1=event.copy()
        if not "time1" in params:
            event1['time']=datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
            event1['timezone']="+000000"
            event1['name']='තත්කාල කේන්ද්‍රය'
        for k in params:
            if k.endswith("1"):
                event1[k[:-1].encode('utf-8')]=params[k].encode('utf-8')
        event1['timezone']=3600*int(event1['timezone'][1:3])+60*int(event1['timezone'][3:5])+int(event1['timezone'][5:])
        event1['longitude'],event1['latitude']=str2int(event1['longitude']),str2int(event1['latitude'])
        event1['time']=datetime.datetime.strptime(event1['time'], "%Y%m%d%H%M%S")
        return pvt_calc(event),pvt_calc(event1)
    else:
        r=pvt_calc(event)
        return r,r
    
def my_render(*args, **kwargs):
    httpresponse_kwargs = {'mimetype': kwargs.pop('mimetype', None)}
    content=loader.render_to_string(*args, **kwargs)
    return HttpResponse(content, **httpresponse_kwargs)

    rbody=re.compile("<body.*?>(?:.*)</body>", re.DOTALL|re.I)
    body=re.findall(rbody, content)[0]
    keeps=re.findall(r'[\x00-~]+', body)
    chgs=re.split('[\x00-~]+', body)
    body=""
    for i in range(len(keeps)):
        v=re.sub("([\x00-~]+)",r"<font face='kaputadotcom'>\1</font>",getKaputa(readUnicode(chgs[i])))
        body+=v#.decode('utf-8')
        body+=keeps[i]
    return HttpResponse(rbody.sub(body.replace("\\",r"\\"),content), **httpresponse_kwargs)


def getChoices():
    r=[(e.key(),e.name) for e in Event.all().filter('added_by =',users.get_current_user()).fetch(1000)]
    r=[('0','තත්කාලය')]+r
    return r
YEAR=365.256363
from django.template import loader
def simplechart(request):
    #event=calc(key) if key else 
    event,event1=calcGet(request.GET,True)
    canEdit=str(users.get_current_user()).encode('utf-8') =='sandeva' or \
            users.get_current_user()==Event.get(request.GET['key']).added_by if 'key' in request.GET else False
    x=(event['Moon']/48000)%9
    strt=(event['GMT']-datetime.timedelta(days=(x%1)*dasha_prama[int(x)]*YEAR)).date()
    end=strt+timedelta(days=120*YEAR)
    res = my_render(getHtmlPath(__name__,"simplechart.html"), 
                              {'event': event,
                               'event1': event1,
                               'events':Event.all().filter('added_by =',users.get_current_user()).fetch(1000),
                               'eventselect':Select().render(
                                    "eventselect",
                                    request.GET['key1'] if 'key1' in request.GET else '0',
                                    [('onChange','document.getElementById("form"+this.value).submit()')],
                                    choices=getChoices()),
                               'dasa':{"p":x, "strt":strt, "end":end}, 
                               'request':request,
                               'canEdit':canEdit,
                               },
                               context_instance=RequestContext(request))
    return res

sinhala_rashis=[
"meesha","vrshabha","mitxhuna",
"kataka","si/nha","kanyaa",
"txulaa","vrsxcika","dxhanu",
"makara","kumbha","miina"]

sinhala_nakshatra_short=[
"as(kee)","bera(sxu)",
"kaetxi(ra)","re(ca)","muvasi(ku)","adxa(raa)","punaava(gu)","pusha(sxa)","asli(bu)","maa(kee)","puvapa(sxu)",
"utxrapa(ra)","hatxa(ca)","sitxa(ku)","saa(raa)","visaa(gu)","anura(sxa)","dxeta(bu)","mula(kee)","puvasa(sxu)",
"utxrasa(ra)","suvana(ca)","dxena(ku)","siyaa(raa)","puvapu(gu)","utxrapu(sxa)","reevatxii(bu)"]

xxx=["අස්(කේ)","බෙර(ශු)",
"කැති(ර)","රෙ(ච)","මුවසි(කු)","අද(රා)","පුනාව(ගු)","පුෂ(ශ)","අස්ලි(බු)","මා(කේ)","පුවප(ශු)",
"උත්‍රප(ර)","හත(ච)","සිත(කු)","සා(රා)","විසා(ගු)","අනුර(ශ)","දෙට(බු)","මුල(කේ)","පුවස(ශු)",
"උත්‍රස(ර)","සුවන(ච)","දෙන(කු)","සියා(රා)","පුවපු(ගු)","උත්‍රපු(ශ)","රේවතී(බු)"]
 

def call(object,lst,reverse=True):
    rvs=[]
    for l in lst:
        if type(l)==list:
            call(object,l)
        else:
            getattr(object, l[0])(*l[1])
            if reverse and l[0] in ('rotate','translate'):
                rvs.append((l[0],tuple(map(lambda x:-x,l[1]))))
    if reverse:
        rvs.reverse()
        call(object, rvs, False)


def ifDownHalf(i):
    downhalf = i % 360 >= 180
    downhalf = downhalf * 2 - 1
    return downhalf

def funcOn(i):
    i = i %360
    if i<45 or i > 315:
        return "drawRightString"
    if i<135 or i > 225:
        return "drawCentredString"
    return "drawString"

def circlechart(request,key=None):
    event =calc(key) if key else calcGet(request.GET)
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=Horoscope.pdf'#%re.sub(r'\s',"_",event['name']))#.encode('utf-8','ignore')
    p = canvas.Canvas(response)#MyCanvas(response)#
    mx,my=0,0
    p.translate(298,600)
    R=200
    
    p.setStrokeColorRGB(1,0,0)
    p.setLineWidth(0.5)
    p.circle(mx,my,R)
    p.setStrokeColorRGB(0,0,0)
    p.circle(mx,my,1.01*R)
    p.circle(mx,my,0.15*R)
    p.circle(mx,my,0.85*R)
    p.circle(mx,my,0.7*R)
    
    pdfmetrics.registerFont(TTFont('kaputa', r"astro/chart/kaputa.ttf"))#r'D:\kendra-python\workspace\mysitedjando_101226\mysite\astro\chart\kaputa.ttf'))
    p.setFont('kaputa', 12)
    for b in bhavas:
        i = int(((event[b] - event["I"]) / 3600 + 450) % 360)
        p.rotate(i)
        p.line(0.15 * R, 0, 0.7 * R, 0)
        p.rotate(-i)

    for a in range(0,360,30):
        i = a + 90 - event["I"] / 3600
        call(p,[
            ("rotate",(i,)),
            ("line",(0.7 * R, 0, 0.85 * R, 0,)),
            ("rotate",(15,)),
            ('translate',(0.775 * R + 3 * ifDownHalf(i+15), 0)),
            [('rotate',(90*ifDownHalf(i+15),)),('drawCentredString',(0, 0, getKaputa(sinhala_rashis[a / 30])))],
            ])
    for a in range(108):
        i = a * 10.0 / 3 + 90 - event["I"] / 3600
        call(p,[
            ("rotate",(i,)),
            ("line",(0.85 * R, 0, (0.9 + (a%4==0 and 0.1)) * R, 0,)),
            ])
        if not a%4==0:
            continue
        call(p,[
            ("rotate",(i+20.0/3,)),
            ('translate',(0.95 * R + 3 * ifDownHalf(i+20.0/3), 0)),
            [('rotate',(90*ifDownHalf(i),)),('drawCentredString',(0, 0, getKaputa(sinhala_nakshatra_short[a/4])))],
            ])
            
    p.setStrokeColor(colors.blue)
    p.setLineWidth(1)
    for plnt in sinhala_planets_short:
        i=(event[plnt]-event["I"])/3600+90
        call(p,[
            ("rotate",(i,)),
            ("line",(0.8 * R, 0, 0.85 * R, 0,)),
            #("rotate",(ifLeftHalf(i)*5,)),
            ('translate',(0.65 * R  , 0)),#+ 3 * ifDownHalf(i)
            ("rotate",(-i,)),
            (funcOn(i),(0, funcOn(i)!="drawCentredString" and -4, getKaputa(readUnicode(sinhala_planets_short[plnt]))))
            ])
        
    p.setLineWidth(0.75)
    for p1 in range(len(sinhala_planets_short)):
        for p2 in range(p1+1,len(sinhala_planets_short)):
            ps=sinhala_planets_short.keys()[p1],sinhala_planets_short.keys()[p2]
            a=abs(event[ps[0]]-event[ps[1]])/3600.00
            clr=seiyo.getAspectColor(ps[0],ps[1],a)
            if len(clr):
                p.setStrokeColor(getattr(colors, clr))
                pp = map(lambda ps:polar2xy(0.6 * R, (event[ps]-event["I"])/3600+90),ps)
                p.line(pp[0][0], pp[0][1], pp[1][0], pp[1][1])

    p.showPage()
    p.save()
    return response

#t0=datetime.datetime.now()
#def timer():
#    global t0
#    print >>sys.stderr,datetime.datetime.now()-t0
#    t0=datetime.datetime.now()

def bmp2(request):
    return bmp(request,True)
    
def bmp(request,comp=False):
    event,event1 = calcGet(request.GET,comp)
    response = HttpResponse(mimetype='image/bmp')
    p=canvas.Canvas(response)
    
    mx,my=0,0
    p.translate(375,375)
    R=360
    
    p.pen=p.pens[1.5]
    p.setStrokeColorRGB(1,0,0)
    #p.setLineWidth(0.5)
    p.circle(mx,my,R)
    p.setStrokeColorRGB(0,0,0)
    p.circle(mx,my,1.01*R)
    p.circle(mx,my,0.15*R)
    p.circle(mx,my,0.85*R)
    p.circle(mx,my,0.7*R)

    for b in bhavas:
        i = int(((event[b] - event["I"]) / 3600 + 450) % 360)
        p.rotate(i)
        p.line(0.15 * R, 0, 0.7 * R, 0)
        p.rotate(-i)

    h=35
    tp=820
    bits=open("astro/chart/words.bmp",'rb').read()
    rashiw=[canvas.readBits(bits, 0, tp-(y+1)*h, 120, tp-y*h) for y in range(12)]
    h=26.5
    tp=400
    grahaw=[canvas.readBits(bits, 0, tp-(y+1)*h, 80, tp-y*h) for y in range(12)]
    tp=815
    h=24
    nktw=[canvas.readBits(bits, 130, tp-(y+1)*h, 300, tp-y*h) for y in range(27)]


    for a in range(0,360,30):
        i = a + 90 - event["I"] / 3600
        call(p,[
            ("rotate",(i,)),
            ("line",(0.7 * R, 0, 0.85 * R, 0,)),
            ("rotate",(15,)),
            ('translate',(0.75 * R , 0)),
            [('rotate',(90*ifDownHalf(i+15),)),('addPoints',(rashiw[a / 30],))],
            ])
    for a in range(108):
        i = a * 10.0 / 3 + 90 - event["I"] / 3600
        call(p,[
            ("rotate",(i,)),
            ("line",(0.85 * R, 0, (0.9 + (a%4==0 and 0.1)) * R, 0,)),
            ])
        if not a%4==0:
            continue
        call(p,[
            ("rotate",(i+20.0/3,)),
            ('translate',(0.95 * R + 3 * ifDownHalf(i+20.0/3), 0)),
            [('rotate',(90*ifDownHalf(i),)),('addPoints', (nktw[a/4],))],
            ])


    p.setStrokeColorRGB(0,0,1)
    p.pen=p.pens[3]
    for ndx,plnt in enumerate(wheel.planets):
        i=(event[plnt]-event["I"])/3600+90
        call(p,[
            ("rotate",(i,)),
            ("line",(0.8 * R, 0, 0.85 * R, 0,)),
            ('translate',(0.65 * R  , 0)),#+ 3 * ifDownHalf(i)
            ("rotate",(-i,)),
            ('addPoints',(grahaw[ndx],)),
            ])


    if comp:
        p.setStrokeColorRGB(1,0,0)
        p.pen=p.pens[3]
        for ndx,plnt in enumerate(wheel.planets):
            i=(event1[plnt]-event["I"])/3600+90
            call(p,[
                ("rotate",(i,)),
                ("line",(0.8 * R, 0, 0.85 * R, 0,)),
                ('translate',(0.65 * R  , 0)),#+ 3 * ifDownHalf(i)
                ("rotate",(-i,)),
                ('addPoints',(grahaw[ndx],)),
                ])

    p.pen=p.pens[2]
    if 'orb' in event:
        orb=eval(event['orb'])
    else:
        orb=seiyo_trans if comp else seiyo
    f=orb.getAspectColor
    #f=seiyo.getAspectColor
    for p1 in range(len(sinhala_planets_short)):
        for p2 in range(p1+1,len(sinhala_planets_short)):
            ps=sinhala_planets_short.keys()[p1],sinhala_planets_short.keys()[p2]
            a=abs(event[ps[0]]-event1[ps[1]])/3600.00
            clr=f(ps[0],ps[1],a)
            if len(clr):
                CC=getattr(colors, clr)
                p.setStrokeColorRGB(*CC.rgb())
                pp = polar2xy(0.6 * R, (event[ps[0]]-event["I"])/3600+90), \
                     polar2xy(0.6 * R, (event1[ps[1]]-event["I"])/3600+90)
                p.line(pp[0][0], pp[0][1], pp[1][0], pp[1][1])


    p.save()
    return response
