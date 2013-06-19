# -*- coding:utf-8 -*-

from astro.chart.views import calcGet
from django.shortcuts import render_to_response
from utils import getHtmlPath
import datetime

def index(request):
    data_list = [datetime.datetime.now() + datetime.timedelta(days=i) for i in range(1000)]
    data_list = [calcGet(dict(time=dt.strftime("%Y%m%d000000")), False)[0] for dt in data_list]
    return render_to_response(getHtmlPath(__name__,'index.html'), {'data_list': data_list})
