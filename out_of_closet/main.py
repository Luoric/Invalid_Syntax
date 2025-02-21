import webapp2
import jinja2
import os
import time
from time import gmtime, strftime, mktime, localtime
from datetime import datetime
import meme_model

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

        template_var  = {
            'users': users
        }

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
        meme_line2 = self.request.get("userStory")
        meme_date = strftime("%a, %d %b %Y", localtime())
        meme_date = str(meme_date)

        user = meme_model.User(
        user_name = meme_line1,
        user_story = meme_line2,
        date_string = meme_date,
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

app = webapp2.WSGIApplication([
    ('/', ShowStarter),
    ('/welcome', EnterInfoHandler),
    ('/memeresult', ShowMemeHandler),
    ('/library', ShowLibrary),
    ('/comingsoon', ComingSoon),
    ('/about', About)
], debug=True)
