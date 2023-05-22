import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        for i in range(1,11):
            res = 5*i
            self.response.write("5 x "+str(i)+"="+str(res)+"<br>")

app = webapp2.WSGIApplication([("/",MainPage)],debug=True)