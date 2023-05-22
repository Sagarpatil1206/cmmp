import webapp2
import json
import os
import urllib
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__),"index.html")
        context={}
        self.response.out.write(template.render(path,context))

    def post(self):
        
        uni_name = self.request.get("university")
        url = "http://universities.hipolabs.com/search?name="+uni_name
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        country = data[0]['country']
        name = data[0]['name']
        context={
            "country":country,
            "name":name
        }
        path = os.path.join(os.path.dirname(__file__),"result.html")
        self.response.out.write(template.render(path,context))

app = webapp2.WSGIApplication([("/",MainPage)],debug=True)