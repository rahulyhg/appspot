'''
Created on Dec 30, 2010

@author: Sandeva Goonetilleke
'''

from django.http import HttpResponse

from django.shortcuts import render_to_response
from utils import getHtmlPath

import logging
from django.template.context import RequestContext

logger = logging.getLogger(__name__)

def index(request):
    return render_to_response(
         getHtmlPath(__name__,'base.html'), 
         context_instance=RequestContext(request))

def srishell_download(request):
    """
    Download file to browser
    """
    
    print "\r\n"*2
    print "O"*100

    print \
    """Content-Type:application/octet-stream
Content-Disposition:attachment; filename=SriShell_setup.exe
"""
    print open("templates/srishell/download/setup.exe",'rb').read()
    exit()
#    lFile = MyFile("templates/srishell/download/setup.exe", users.get_current_user())
    lResponse = HttpResponse(open("templates/srishell/download/setup.exe","rb").read(), mimetype='application/octet-stream')
    lResponse['Content-Disposition'] = 'attachment; filename=SriShell_setup.exe' 
    return lResponse
