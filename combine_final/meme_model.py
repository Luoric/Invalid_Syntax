from google.appengine.ext import ndb

class User(ndb.Model):
    user_name = ndb.StringProperty(required = True)
    user_story= ndb.StringProperty(required = True)
    user_email= ndb.StringProperty(required = False)
    user_count= ndb.IntegerProperty(required = False)
    date_string = ndb.StringProperty(required = True)
