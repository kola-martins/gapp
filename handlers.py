#!/usr/bin/env python
#
# scripts for ksw-gapp----the connect2share app
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from django.utils import simplejson
import datamethods
import cgi 

class adduser(webapp.RequestHandler):
  def post(self):
    self.response.headers['Content-type'] = "application/json"
    data = simplejson.loads(self.request.body) #the json data will be in the body of the request
        # check if the data aint empty
    if(len(data)):
      userphone = data['phone'] # get the phone number from json data in request
      name = data['name'] # get the name from json data in request
      datamethods.addnewuser(userphone, name, "45.66", "-34.56")
      self.response.out.write("success")

class userexists(webapp.RequestHandler):
  def get(self):
    return
    
class updatestatus(webapp.RequestHandler):
  def post(self):
    return 
    
class getusers(webapp.RequestHandler):
  def get(self):
    users = []
    data = datamethods.getusers()
    for user in data:
      person = {"name": user.username, "phone":user.phonenumber, "lat":user.location.lat, "long":user.location.lon,"displaypix":user.displaypix}
      #add to the list and encode with json
      users.append(person)
    users_json = simplejson.dumps(users)
    self.response.headers['Content-type'] = "application/json"
    self.response.out.write(users_json)
         
class sendmessage(webapp.RequestHandler):
  def post(self):
    return
    
class logout(webapp.RequestHandler):
  def post(self):
    data = simplejson.loads(self.request.body) 
    if len(data):
      phone = data["phone"]
      datamethods.login(phone)
    return simplejson.dumps('{"status": True}')

class welcome(webapp.RequestHandler):
  def get(self):
    self.response.out.write("you are welcome to connect2share do av a great time using this awesome platform") 

class login(webapp.RequestHandler):
  def post(self):
    data = simplejson.loads(self.request.body) 
    if len(data):
      phone = data["phone"]
      datamethods.login(phone)
    return simplejson.dumps('{"status": True}')
                            

# end of the handlers                          







#mapping urls to method calls
app = webapp.WSGIApplication([('/',welcome),
  ('/adduser', adduser),
  ('/sign', updatestatus),
  ('/login',login),
  ('/getusers', getusers)
], debug=True)


def main():
    run_wsgi_app(app)

if __name__ == "__main__":
    main()