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
        name = self.request.get("map_name")
        tuo = TwitterUserOrder(name)
        ts = TwitterSearch(
            consumer_key = 'dKu6bH3B6kzjjQx8SQOZix1zm',
            consumer_secret = '0JeXDLbdGApPxoGc7X3KKDHfLSfz9nLtrfcnRNvMCQwW3MVYG1',
            access_token = '3659983230-oAz1ASVWPfp9tA6rMKmLUy9KIbt01WEvqCwwf6z',
            access_token_secret = 's4S30z2lb7TNy6UqULkfSnz1lJiAxvlaDTyECjFfIq27Z'
         )

        i = 5
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
        r = requests.post(
            'https://stevesie.com/cloud/api/v1/endpoints/3cd58c09-c547-481e-a011-180097f61f49/executions',
            headers={
                'Token': '04e4dc3c-481c-462f-875d-4e8202874ec7',
            },
            json={
                'inputs': {
                    'session_id': '2229053416%3AERftJLIFsesnIt%3A5',
                    'username': name,
                    'max_id': '',
                },
                'proxy': {
                  'type': 'shared',
                  'location': 'nyc3',
                }
            },
        )

        response_json = r.json()
        img_url = response_json['object']['response']['response_text']
        img_url = str(img_url)
        json_acceptable_string = img_url.replace('''"''', "\"")
        url = json.loads(json_acceptable_string)
        url = url['items'][0]['image_versions2']['candidates'][0]['url']

        template_var  = {
            'tsts': tsts,
            'url' : url,
            'list_url': list_url
        }
        result_template = the_jinja_env.get_template('templates/results2.html')
        self.response.write(result_template.render(template_var))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/results', ResultHandler),
    ('/map', MapHandler),
],debug=True)
