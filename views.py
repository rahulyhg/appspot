'''
Created on Dec 30, 2010

@author: Sandeva Goonetilleke
'''

from django.http import HttpResponse

from django.shortcuts import render_to_response
from utils import *

from google.appengine.api import users

import logging

logger = logging.getLogger(__name__)

def index(request):
    return render_to_response(getHtmlPath(__name__,'base.html'))

#class MyFile(file):
#    def __init__(self, pDownloadFile, pUser, *args, **kwargs):
#       self.downloadFile = pDownloadFile
#       self.user = pUser
#       lFilename = pDownloadFile
#       #print lFilename
#       super(MyFile, self).__init__(lFilename, *args, **kwargs)
#       logger.info("%s started downloading SriShell")
#
#    def close(self):
#       super(MyFile, self).close()
#       logger.info("%s ended downloading SriShell")
##       lDownloadLog = DownloadLog()
##       lDownloadLog.filename = self.downloadFile.file.name
##       lDownloadLog.lastChangedBy = self.user
##       lDownloadLog.owner = self.user
##       lDownloadLog.save()


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
