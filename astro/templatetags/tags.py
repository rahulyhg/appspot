from django import template

register = template.Library()

@register.filter
def p(value,arg):
    return arg.split("/")[value<0]

@register.filter
def sgn(value,dec=None):
    if dec:
        return dec[value>=0]
    return "-" if value<0 else ""

@register.filter
def dd(value,mod=None):
    if mod:
        return "%02d"%((value/3600)%eval(mod))
    return "%02d"%(abs(value)/3600)

@register.filter
def mm(value):
    return "%02d"%((abs(value)/60)%60)

@register.filter
def ss(value):
    return "%02d"%(abs(value)%60)

@register.filter
def sub(value1,value2):
    return value1-value2

good={
      'Sun':[2,5,9,10],
      'Moon':[0,2,5,6,9,10],
      'Mars':[2,5,9,10],
      'Mercury':[0,1,3,5,7,9,10],
      'Jupiter':[1,4,6,8,10],
      'Venus':[0,1,2,3,4,7,8,10,11],
      'Saturn':[2,5,10],
      "Moon_Node":[2,5,10],
      "Moon_S_Node":[2,5,10]
      }

@register.filter
def gochara(house,planet):
    return 2*(house%12 in good[planet])-1
