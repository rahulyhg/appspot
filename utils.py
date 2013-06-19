from django.http import HttpResponsePermanentRedirect
from google.appengine.api import users

import re
def getHtmlPath(module,html):
    r=re.sub(r'\.','/',module)
    r=re.sub("[^/]*$",html,r)
    return r

def getParentPath(module):
    r=re.sub(r'\.','/',"/"+module)
    r=re.sub("[^/]*$",'',r)
    return r

def login_required(func):
    def redirect_to_login(request):
        return HttpResponsePermanentRedirect(users.create_login_url(request.get_full_path()))

    user = users.get_current_user()
    if user:
        return func
    else:
        return redirect_to_login
