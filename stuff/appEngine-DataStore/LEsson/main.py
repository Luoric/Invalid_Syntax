#main.py
# the import section
import webapp2

# the handler section
class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
        self.response.write("""
        <html>
        <head>
        <style>
        .links{
        background-color : pink;
        padding 20px;
        display: flex;
        flex-direction: center;
        justify-content: space-around;
        font-family: sans-sarif;
        font-size: 30;
        }
        h1{
        text-align: center;
        text-size: 50;
        }
        </style>
        </head>
        <body>
        <h1>MainPage</h1>
        <br>
        <a href="http://localhost:8080/news" class = links>News</a>
        <br>
        <a href="http://localhost:8080/about" class = links>About</a>
        </body>
        </html>
        """)
class NewsPage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
        self.response.write("""
        <html>
        <head>
        <style>body{
            font-family:'Roboto', sans-serif;
          }

          h1 {
            background-color: black;
            color: white;
            text-align: center;
            padding: 20px 0px 20px 0px;
          }

          .clickableArea {
            border : 1px solid grey;
            background-color: black;
            width: fit-content;
            padding: 5px;
            color: white;
          }
          </style>
          <script src ="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.4/jquery.js"></script>
          <script>function converMsToDays(input){
            input = input/1000 / 60 /60 /24;
            return input;
          }


          let timeTotal = 0;

          function writeSummary() {
            let place1 = $("#where_1")[0].value;
            let time1 = converMsToDays($("#end1")[0].valueAsNumber - $("#start1")[0].valueAsNumber);
            timeTotal = timeTotal + time1;
            let text = "";
            text = place1 + " for " +time1 + " days";

            $("#summary").append(text+ ", ");
            $("#days").empty();
            $("#days").append("You will be gone for " + timeTotal + " days in total");
          }



          function initializeJs() {
            $("#summaryButton").click(writeSummary);
          }
          $(document).ready(initializeJs);
          </script>
        </head>
        <body>
          <h1> Vacation Planner </h1>

          <div id ="summary">
            Your vacation is to:

          </div>
          <br>
          <div id ="days">

          </div>

          <form>
            <div class = "destination">
              Where are you going?
              <input type = "text" name ="where" id ="where_1"></input>
              Start date <input type = "date" id = start1></input>
              End date <input type = "date" id = end1></input>
              <br>
          </form>
          <div class = "clickableArea" id = "summaryButton">
            Summarize My Trip
          </div>
        </body>
        </html>""")
# the app configuration section
class AboutPage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
        self.response.write("""
        <html>
        <head>
        </head>
        <body>
        HELLO THERE
        </body>
        </html>
        """)
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/about', AboutPage),
    ('/news', NewsPage)#this maps the root url to the Main Page Handler
], debug=True)
