import re
def getHtmlPath(module,html):
    r=re.sub(r'\.','/',module)
    r=re.sub("[^/]*$",html,r)
    return r

def getParentPath(module):
    r=re.sub(r'\.','/',"/"+module)
    r=re.sub("[^/]*$",'',r)
    return r
