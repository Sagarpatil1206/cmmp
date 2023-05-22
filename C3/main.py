import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        i=0
        while i<10 :
            self.response.write("Dept:IT<br>")
            i=i+1

app = webapp2.WSGIApplication([("/",MainPage)],debug=True)     