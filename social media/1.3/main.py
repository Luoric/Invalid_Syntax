import webapp2
from google.appengine.api import urlfetch
import json
import jinja2
import os
import requests
import ssl
from TwitterSearch import *
import googleapiclient.discovery
import googleapiclient.errors
import google_auth_oauthlib.flow


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
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_console()
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

        request = youtube.search().list(
            part="snippet",
            maxResults=3,
            q="surfing",
            type="video",
            videoEmbeddable="true"
        )
        response = request.execute()

        print(response)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/results', ResultHandler),
    ('/map', MapHandler),
],debug=True)
