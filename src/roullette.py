import tornado.web, tornado.websocket

activeClients=[]

class Handler(tornado.web.RequestHandler):
    def get(self):
        
        self.render( "/static/roullette.html")
