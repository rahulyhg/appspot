# -*- coding:utf-8 -*-

from django import template
from astro.chart import *
import datetime

register = template.Library()

@register.filter
def rashi(value):
    return sinhala_rashi[int(value/108000)]

@register.filter
def navamshaka(value):
    return sinhala_rashi[int(value/12000)%12]

@register.filter
def house(value, arg):
    r=[]
    for k in ["Sun","Moon","Mars","Mercury","Jupiter","Venus","Saturn","Moon_Node","Moon_S_Node","Uranus","Neptune","Pluto"]:
        if int(arg)-1==(int(value[k]/108000)-int(value['I']/108000))%12:
            r.append(sinhala_planets_short[k])
    return len(r) and " ".join(r) or arg

@register.filter
def navamshaka_house(value, arg):
    r=[]
    for k in ["Sun","Moon","Mars","Mercury","Jupiter","Venus","Saturn","Moon_Node","Moon_S_Node","Uranus","Neptune","Pluto"]:
        if int(arg)-1==(int(value[k]/12000)-int(value['I']/12000))%12:
            r.append(sinhala_planets_short[k])
    return len(r) and " ".join(r) or arg

rashi_lords=['Mars','Venus','Mercury','Moon','Sun','Mercury','Venus','Mars','Jupiter','Saturn','Saturn','Jupiter']

@register.filter
def shadvarga(value, arg):
    arg = int(arg)
    if arg == 1:
        return int(value / 108000)
    if arg == 2:
        return int((value + 162000) / 108000) % 2 + 3
    if arg == 3:
        return (int(value / 108000) + 4 * int(value / 36000)) % 12
    if arg == 9:
        return int(value / 12000) % 12
    if arg == 12:
        return (int(value / 108000) + int(value / 9000)) % 12
    thrin=[0]*5+[10]*5+[8]*8+[2]*7+[6]*5+ \
              [1]*5+[5]*7+[11]*8+[9]*5+[7]*5
    return thrin[int(value / 3600)%60]


@register.filter
def shubha_varga(value):
    return "%d / 6"%(sum(map(lambda x:x in [1, 2, 3, 5, 6, 8, 11], map(shadvarga,[value]*6,[1,2,3,9,12,30]))))

@register.filter
def pyeval(value,arg=tuple()):
    return eval(value%arg)

@register.filter
def get_sinhala_planet(value):
    return sinhala_planets[value]

@register.filter
def attr(value, atr):
    if type(value) in [list,tuple]:
        atr=int(atr)
    return value[atr]

@register.filter
def nakshatra(value):
    return int(value/48000)

@register.filter
def nakshatra_lord(value):
    return nakshatra_lords[value]

@register.filter
def thithi(value):
    return int(value['Moon']-value['Sun'])/43200

@register.filter
def sinhala(value,dec=None):
    dec = dec.encode('utf-8')
    if dec == "nakshatra":
        return sinhala_nakshatra[value]
    if dec == "nakshatra_lord":
        return sinhala_planets[nakshatra_lords[value]]
    if dec == "thithi":
        return sinhala_thithi[value]
    if dec == "රාශි":
        return sinhala_rashi[value]
    if dec == "ග්‍රහ":
        return sinhala_planets[value]
    if dec == "ග්‍රහ(කෙටි)":
        return sinhala_planets_short[value]
    return dec,"ග්‍රහ(කෙටි)",dec == "ග්‍රහ(කෙටි)"

@register.filter
def rashi_lord(value):
    return rashi_lords[int(value)]

@register.filter
def bhava_occupant(value,arg):
    bhv="I II III IV V VI VII VIII IX X XI XII I".split()
    x,y=value[arg],value[bhv[bhv.index(arg)+1]]
    r=[]
    for k in ["Sun","Moon","Mars","Mercury","Jupiter","Venus","Saturn","Moon_Node","Moon_S_Node"]:
        v=value[k]
        if x<v<y or y<x<v or v<y<x:
            r.append(k)
    return r

@register.filter
def nakshtra_occupants(event,pl):
    r=[]
    for k in ["Sun","Moon","Mars","Mercury","Jupiter","Venus","Saturn","Moon_Node","Moon_S_Node"]:
        if pl==nakshatra_lords[int(event[k]/48000)]:
            r.append(k)
    return r


#@register.simple_tag
#def current_time(context, format_string):
#    return "test",context
