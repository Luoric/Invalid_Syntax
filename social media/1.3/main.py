import webapp2
from google.appengine.api import urlfetch
import json
import jinja2
import os
import requests
import ssl
from TwitterSearch import *
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.appengine.api import urlfetch


scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


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
        api_key = 'AIzaSyBOrP8QroOlqPw0bdOFjhXnEKB0ITXRX4o'
        search_name = self.request.get("map_name")
        search_name = search_name.replace(" ", "_")
        endpoint_url = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=5&q="+ search_name+"&safeSearch=strict&type=video&key="+ api_key


        response = urlfetch.fetch(endpoint_url)
        content = response.content

        response_as_json = json.loads(content)
        print(response_as_json)
        list_url = []

        for thing in response_as_json["items"]:
            list_url.append(thing["id"]["videoId"])
        template_var  = {
            'list_url': list_url
        }
        result_template = the_jinja_env.get_template('templates/results2.html')
        self.response.write(result_template.render(template_var))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/results', ResultHandler),
    ('/map', MapHandler),
],debug=True)
