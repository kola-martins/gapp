
# this file simply contains methods that perform a number of actions related 
# to the functionality of GApp

from model import GappUser
from google.appengine.ext import db
from google.appengine.api import images

onlineusers  = [] # list of online users

#adds a new user to the datastore
def addnewuser(phone, uname, lat, lon): # done
  location  = db.GeoPt(lat,lon) #create the geopt object from lat and long supplied
  if(numberexists(phone) != True and usernameexists(uname) != True):
    user = GappUser(username  = uname, phonenumber = phone, location  = location)
    user.put()
# create the user and .put()
    #this method assumes that the app on the client has  validated user input and whats 
    #being submitted is in the correct format
 
def uploadpix(userpix, phone): 
   
#   user = model.GappUser(username = uname, phonenum = phone)
#   user.displaypix = userpix

#  user.put()
  g_user = GappUser.gql("WHERE phonenumber == :1",phone).get() # get user with the phone number in question
  currentuser = db.get(g_user.key().id()) 
  avatar = images.resize(userpix, 32, 32) # resize to ana avatar size - 32 X 32
  currentuser.avatar = db.Blob(avatar) # set the avatra to the resized img
  currentuser.displaypix = db.Blob(userpix) #set he display pix to the uploaded pix
  currentuser.put()

def getusers():
  return GappUser.all()
# checks if a user already exists with teh details supplied

def getuserkey(phone):
  g_user = GappUser.gql("WHERE phonenumber == :1",phone).get() # get user with the phone number in question
  currentuser = db.get(g_user.key().id()) # gets the id of the user having the phone.
  return currentuser
  
def userexists(n_user): #done
  users = GappUser.all()
  for user in users:
    if user == n_user:
      return True
    else:
      return False
# users = db.GqlQuery("SELECT username FROM GappUser")
# note: thsi method will be 
    
def usernameexists(username): #done
#get the list of existing usernames
# check if the username exists
    #if yes:
        #return yes
    #if no
        #return no 
  users = GappUser.all()
  for user in users:
    if user.username == username:
      status = True
    else:
      status = False
    return status
    
def numberexists(number): #done
  users = GappUser.all()
  for user in users:
    if user.phonenumber == number:
      status = True
    else:
     status = False
    return status
# gets a list of users within the location of the user   
def viewusersaround(location, perimeter):
  usersaround  = GappUser.gql('WHERE location = :1', location)
  return
# gets the list of all the users around the current location of the client

# send a message to the specified user...use GCM
def sendmessage(sender, receiver, msgbody, timesent):
    #create a message instance 
    # .put() the message
    # return succes message 
  return 
# send a friendrequest to the speciifed user
# this doesnt persist any data...just pops up a notice to the recipient whoaccepts or rejects
def sendfriendrequest():
    #create a friend reqest instance
    # .put() the instance
    # return succes message 
# allows user to update a status message
  return
def updatestatus(phone, newstatus):  
    #create and update instance 
    # .put() the instance
    
  return
def addfriend(guser, new_friend):
  currentUser  = GappUser.all().filter('key = ', guser.key().id_or_name())
    
#gets the details for a given userid
def getuserdetails(phone):
    #get user where userid == id
  return 
#gets the current activity for the clients contacts
def getcontactsactivity():
    #get all the contacts for the client
    # get the statuses of the clients
    #return teh ststauses as a lsit
# pools the datastore for messages intended for a user
  return
def getmessages():
    #get all the message instances intended for the client
    # retrun the messages ...the client wil crunch teh data and spread it according to teh contacts of 
    # the user
  return
# pools the datastore for requests intended for the specific user
def getrequests():
    #get all requests
    # filter request by the id of the client
    #return te request meant fro teh cleint
  return 
# allows user to respond to a friendrequest
def respondtorequest(repsonse):
    #check what the response is
    # if 
    # yes - accept
    #elif 
    # no - reject
    #elif
    # ignore - ignore
  return 
# indicates that the user is online i.e. actively using the app
def login(phone):
  currentuser = getuserkey(phone)
  onlineusers.append(currentuser)
  return 
def logout(phone):
  currentuser = getuserkey(phone) 
  onlineusers.remove(currentuser)
    
def getusersonline():
  return onlineusers