from google.appengine.ext import ndb

class User(ndb.Model):
    user_name = ndb.StringProperty(required = True)
    user_story= ndb.StringProperty(required = True)

    date_string = ndb.StringProperty(required = True)
