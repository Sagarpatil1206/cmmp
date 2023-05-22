import webapp2
# This line imports the webapp2 module, which is a lightweight web framework for Python used for creating web applications on Google App Engine.
class MainPage(webapp2.RequestHandler) :
#This line defines a class named MainPage that inherits from webapp2.RequestHandler. It represents a handler for incoming HTTP requests.
    def get(self):
        self.response.write("Hello World")
#This code block defines a get method within the MainPage class. The get method is executed when an HTTP GET request is made to the corresponding URL. In this case, it simply writes the string "Hello World" as the response to the request.
app = webapp2.WSGIApplication([("/",MainPage)],debug=True)
#The full form of webapp2.WSGIApplication is "Web Server Gateway Interface Application." It refers to the webapp2 class used to create a WSGI-compliant application in the webapp2 framework.
#The Web Server Gateway Interface (WSGI) is a specification that defines a standard interface between web servers and web applications or frameworks in the Python ecosystem. It allows web servers to communicate with web applications or frameworks and enables interoperability between different components of a web application stack.

#how its running 
#When you access a URL in your web browser, it automatically sends a GET request to the corresponding server. In your case, when you access localhost:8080 in your browser, the browser sends a GET request to the local development server running on localhost at port 8080.
# In the webapp2 framework, the get method within the MainPage class is responsible for handling incoming GET requests to the root URL ("/"). When you access localhost:8080 in your browser, the local development server routes the GET request to your MainPage handler, which then executes the get method and responds with the text "Hello World."
# So, in summary, it is your web browser that automatically sends the GET request when you access a URL, and the local development server running on localhost:8080 receives and routes that request to your MainPage handler.

# In summary, the role of Google Cloud in this context is to provide the local development server, tools, and infrastructure through the Google Cloud SDK, enabling you to develop and test your application locally before deploying it to the Google Cloud Platform.