import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        for i in range(5):
            self.response.write("Name:Sagar Patil<br>")
            self.response.write("Seat Number: T190058665<br>")
            self.response.write("Dept:IT<br>")

app = webapp2.WSGIApplication([("/",MainPage)],debug=True)