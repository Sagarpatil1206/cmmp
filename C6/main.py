import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        a = 0
        b = 1
        self.response.write(str(a)+" "+str(b)+" ")
        for i in range(0,6):
            ans = a+b
            self.response.write(str(ans)+" ")
            a = b
            b = ans

app = webapp2.WSGIApplication([("/",MainPage)],debug=True)
        