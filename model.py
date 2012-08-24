from google.appengine.ext import webapp
import cgi
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db


class GappUser(db.Model):
  username = db.StringProperty(required=True)
  phonenumber = db.PhoneNumberProperty(required=True)
  displaypix = db.BlobProperty()
  location = db.GeoPtProperty()
  lastseen  = db.DateTimeProperty()
  friends = db.ListProperty(db.Key) # list of friends
  avatar = db.BlobProperty()
  email = db.EmailProperty()
  status = db.StringProperty()

class Status(db.Model):
    userid = db.ReferenceProperty(GappUser, collection_name= 'status_updates',required= True)
    statusmsg = db.StringProperty();
    statustime = db.DateTimeProperty(auto_now = True)
  
class Message(db.Model):
  sender = db.ReferenceProperty(GappUser, collection_name='sent_msgs')
  receiver = db.ReferenceProperty(GappUser, collection_name='received_msgs')
  message = db.StringProperty(required = True)
  timesent = db.DateTimeProperty(auto_now = True)


# not sure hwo to omdel this yet ...no storage of friend requests
#class FriendRequests(db.Model):
 # tobefriend = db.ReferenceProperty(GappUser)
 # sender = db.ReferenceProperty(GappUser)



