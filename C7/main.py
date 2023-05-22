import webapp2
import urllib
import os
import json
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__),"index.html")
        context={}
        self.response.out.write(template.render(path,context))

    def post(self):
        dropdown = self.request.get("choices")
        if dropdown == "zip":
            pincode=str(self.request.get("zipcode"))
            url = "https://api.postalpincode.in/pincode/"+pincode
        else:
            branch = self.request.get("branchname")
            url = "https://api.postalpincode.in/postoffice/"+branch
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        status=data[0]['Status']
        if status!="Success":
            if(dropdown=="zip"):
                self.response.write("Invalid zip code")
            else:
                self.response.write("Invalid branch name")
        else:
            post_office = data[0]['PostOffice'][0]['State']
            name = data[0]['PostOffice'][0]['Name']
            district = data[0]['PostOffice'][0]['District']
            context={
                "post_office":post_office,
                "name":name,
                "district":district
            }
            path = os.path.join(os.path.dirname(__file__),"results.html")
            self.response.out.write(template.render(path,context))

app = webapp2.WSGIApplication([("/",MainPage)],debug=True)
