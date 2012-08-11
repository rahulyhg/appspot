import os
import urllib

from google.appengine.ext import blobstore
from google.appengine.ext import webapp
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users

class MainHandler(webapp.RequestHandler):
  def get(self):
    upload_url = blobstore.create_upload_url('/srishell/download/upload/')
    self.response.out.write('<html><body>')
    self.response.out.write('<form action="%s" method="POST" enctype="multipart/form-data">' % upload_url)
    self.response.out.write("""Upload File: <input type="file" name="file"><br> <input type="submit"
        name="submit" value="Submit"> </form></body></html>""")

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
  def post(self):
    if not 'sandeva'==str(users.get_current_user()).encode('utf-8'):
        return
    upload_files = self.get_uploads('file')  # 'file' is file upload field in the form
    blob_info = upload_files[0]
    self.response.out.write('/srishell/download/serve/%s' % blob_info.key())

class ServeHandler(blobstore_handlers.BlobstoreDownloadHandler):
  def get(self, resource):
    resource = str(urllib.unquote(resource))
    blob_info = blobstore.BlobInfo.get(resource)
    self.send_blob(blob_info)

class ServeSriShell(blobstore_handlers.BlobstoreDownloadHandler):
  def get(self):
    blob_info = blobstore.BlobInfo.all().fetch(1)
    self.send_blob(blob_info[0],save_as='SriShell_setup.exe')

def main():
  application = webapp.WSGIApplication(
    [('/srishell/download/form/', MainHandler),
     ('/srishell/download/upload/', UploadHandler),
     ('/srishell/download/serve/([^/]+)?', ServeHandler),
     ('/srishell/download/', ServeSriShell),
    ], debug=True)
  run_wsgi_app(application)

if __name__ == '__main__':
  main()