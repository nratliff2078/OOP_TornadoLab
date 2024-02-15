import asyncio
import os, os.path
import tornado.web
import roullette, Profile, index, Sock, Quote       

HTMLDIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..","html"
    )
)

class IndexPage(tornado.web.RequestHandler):
    def get(self):
        self.write("<a href='/static/roullette.html'>Visit the casino</a>")



def makeApp():
    endpoints=[


        #("/",roullette.Handler),
        ("/",index.Handler),
        ("/Profile/.*",Profile.Handler)
        #("/", IndexPage),
       # ("/sock", Sock.Handler)
    ]
    app = tornado.web.Application(
        endpoints,
        static_path=HTMLDIR
    )
    app.listen(8000)
    return app

if __name__ == "__main__":
    app = makeApp()
    asyncio.get_event_loop().run_forever()




