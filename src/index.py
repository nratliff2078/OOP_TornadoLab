import tornado.web

class Handler(tornado.web.RequestHandler):
    def get(self):
        self.write("<center>")
        self.write("<body style=\"background-color:#363535;\">")
        self.write("<font color= #FFFFFF>")
        self.write('<a href="/Profile/alice">Alice</a><br>')
        self.write('<a href="/Profile/bob">Bob</a><br>')
        self.write('<a href="/Profile/carol">Carol</a><br>')
        self.write('<a href="/Profile/dave">Dave</a><br>')
        self.write("<br>")
        self.write("<footer>Profile Pictures Obtained from OpenGameArt.org</footer>")
        self.write("</center></font></body")