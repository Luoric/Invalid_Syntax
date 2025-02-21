import webapp2
import jinja2
import os
import time
from time import gmtime, strftime, mktime, localtime
from datetime import datetime
import meme_model
from google.appengine.api import urlfetch
import json
import requests
import ssl
from TwitterSearch import *
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.appengine.api import urlfetch

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# the handler section
class ShowStarter(webapp2.RequestHandler):
    def get(self):  # for a get request
        welcome_template = the_jinja_env.get_template('templates/start.html')
        self.response.write(welcome_template.render())

class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        welcome_template = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(welcome_template.render())
    def post(self):  # for a get request
        welcome_template = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(welcome_template.render())

class ShowLibrary(webapp2.RequestHandler):
    def get(self):  # for a get request
        library_template = the_jinja_env.get_template('templates/library.html')

        users = meme_model.User.query().fetch()
        length = len(users)
        print(length)
        rpt = length/3
        breaks = []
        breaks2 = ["","","<br>"]
        for i in range(rpt):
            breaks.extend(breaks2)

        template_var  = {
            'users': users,
            'breaks':breaks
        }
        print(breaks)
        self.response.write(library_template.render(template_var))


class ShowMemeHandler(webapp2.RequestHandler):
    def get(self):
        dd = {'img_url': 'https://pics.me.me/other-people-whats-so-funny-my-brain-shalomander-44416997.png',
        'line1': 'A',
        'line2': "Shalomander"
        }
        results_template = the_jinja_env.get_template('templates/results.html')
        self.response.write(results_template.render(dd))  # the response

    def post(self):
        results_template = the_jinja_env.get_template('templates/results.html')
        meme_line1 = self.request.get("userName")
        if meme_line1 == '':
            meme_line1 = "anonymous"
        meme_line2 = self.request.get("userStory")
        meme_date = strftime("%a, %d %b %Y", localtime())
        meme_date = str(meme_date)
        meme_email = self.request.get("userEmail")

        users = meme_model.User.query().fetch()
        usercount = 1
        for user in users:
            usercount = usercount + 1
        print(usercount)

        user = meme_model.User(
        user_name = meme_line1,
        user_story = meme_line2,
        date_string = meme_date,
        user_email = meme_email,
        user_count = usercount
        )
        dic = {
        'user_name': meme_line1,
        'user_story': meme_line2,
        'date': meme_date,
        }
        self.response.write(results_template.render(dic))
        user.put()

class ComingSoon(webapp2.RequestHandler):
    def get(self):  # for a get request
        welcome_template = the_jinja_env.get_template('templates/comingSoon.html')
        self.response.write(welcome_template.render())

class About(webapp2.RequestHandler):
    def get(self):  # for a get request
        welcome_template = the_jinja_env.get_template('templates/about.html')
        self.response.write(welcome_template.render())

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):

        result_template = the_jinja_env.get_template('templates/media.html')
        self.response.write(result_template.render())

class MapHandler(webapp2.RequestHandler):
    def get(self):
        api_key = "AIzaSyBOrP8QroOlqPw0bdOFjhXnEKB0ITXRX4o"
        url = "https://maps.googleapis.com/maps/api/staticmap?center=Google+Seattle&size=600x300&key=" + api_key

        self.response.write('<html><body><img src=' + url + '></body></html>')

    def post(self):
        api_key = 'AIzaSyBOrP8QroOlqPw0bdOFjhXnEKB0ITXRX4o'
        search_name = self.request.get("map_name")
        search_name = search_name.replace(" ", "_")
        endpoint_url = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=6&order=relevance&q="+ search_name+"&safeSearch=strict&type=video&key="+ api_key


        response = urlfetch.fetch(endpoint_url)
        content = response.content

        response_as_json1 = json.loads(content)
        print(response_as_json1)
        list_url = []

        for thing in response_as_json1["items"]:
            list_url.append(thing["id"]["videoId"])
        name = self.request.get("map_name")
        tuo = TwitterUserOrder(name)
        ts = TwitterSearch(
            consumer_key = 'dKu6bH3B6kzjjQx8SQOZix1zm',
            consumer_secret = '0JeXDLbdGApPxoGc7X3KKDHfLSfz9nLtrfcnRNvMCQwW3MVYG1',
            access_token = '3659983230-oAz1ASVWPfp9tA6rMKmLUy9KIbt01WEvqCwwf6z',
            access_token_secret = 's4S30z2lb7TNy6UqULkfSnz1lJiAxvlaDTyECjFfIq27Z'
         )

        i = 6
        tsts = []
        if i > 0:
            for tweet in ts.search_tweets_iterable(tuo):
                result = tweet['user']['screen_name'] + ": "+ tweet['text']
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
            'list_url': list_url,
        }
        result_template = the_jinja_env.get_template('templates/results2.html')
        self.response.write(result_template.render(template_var))


app = webapp2.WSGIApplication([
    ('/', ShowStarter),
    ('/welcome', EnterInfoHandler),
    ('/memeresult', ShowMemeHandler),
    ('/library', ShowLibrary),
    ('/comingsoon', ComingSoon),
    ('/about', About),
    ('/media', MainHandler),
    ('/result', MapHandler)
], debug=True)
