import webapp2
from google.appengine.api import urlfetch
import json
import jinja2
import os
import requests
import ssl
#from lib import requests
from TwitterSearch import *


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):

        result_template = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(result_template.render())

class ResultHandler(webapp2.RequestHandler):
    def post(self):
        giphy_key = 'eJe7EvyU11b9fqcIAphGSxsSJP36EIt2'
        gif_name = self.request.get("gif_name")
        gif_name = gif_name.replace(" ", "_")
        endpoint_url = "https://api.giphy.com/v1/gifs/search?q=" +  gif_name + "&api_key="+ giphy_key

        response = urlfetch.fetch(endpoint_url)
        content = response.content

        response_as_json = json.loads(content)
        list_url = []
        for thing in response_as_json["data"]:
            list_url.append(thing["images"]["original"]["url"])
        template_var  = {
            'list_url': list_url
        }
        result_template = the_jinja_env.get_template('templates/results.html')
        self.response.write(result_template.render(template_var))

class MapHandler(webapp2.RequestHandler):
    def get(self):
        api_key = "AIzaSyBOrP8QroOlqPw0bdOFjhXnEKB0ITXRX4o"
        url = "https://maps.googleapis.com/maps/api/staticmap?center=Google+Seattle&size=600x300&key=" + api_key

        self.response.write('<html><body><img src=' + url + '></body></html>')

    def post(self):
        try:
            #tso = TwitterSearchOrder() # create a TwitterSearchOrder object
            #tso.set_keywords(['Taylor']) # let's define all words we would like to have a look for
            #tso.set_language('en') # we want to see German tweets only
            #tso.set_include_entities(False) # and don't give us all those entity information
            tuo = TwitterUserOrder('elonmusk') # create a TwitterUserOrder
        # it's about time to create a TwitterSearch object with our secret tokens
            ts = TwitterSearch(
                consumer_key = 'dKu6bH3B6kzjjQx8SQOZix1zm',
                consumer_secret = '0JeXDLbdGApPxoGc7X3KKDHfLSfz9nLtrfcnRNvMCQwW3MVYG1',
                access_token = '3659983230-oAz1ASVWPfp9tA6rMKmLUy9KIbt01WEvqCwwf6z',
                access_token_secret = 's4S30z2lb7TNy6UqULkfSnz1lJiAxvlaDTyECjFfIq27Z'
             )

             # this is where the fun actually starts :)
            i = 3
            tsts = []
            if i > 0:
                for tweet in ts.search_tweets_iterable(tuo):
                    result = tweet['user']['screen_name'] + tweet['text']
                    tsts.append(result)
                    print(tsts)
                    i = i -1
                    if i == 0:
                        break
                    print(i)
            template_var  = {
                'tsts': tsts
            }
            result_template = the_jinja_env.get_template('templates/results2.html')
            self.response.write(result_template.render(template_var))
        except TwitterSearchException as e: # take care of all those ugly errors if there are some
            print(e)



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/results', ResultHandler),
    ('/map', MapHandler),
],debug=True)
