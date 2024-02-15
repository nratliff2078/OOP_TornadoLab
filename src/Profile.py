import tornado.web, json

Dictionary={
    "alice":{
            "name" : "Alice Smith",
            "dob" : "Jan. 1",
            "email" : "alice@example.com",
            "pic" : "/static/Alice_pic.png"
        },
    "bob":{
            "name" : "Bob Jones",
            "dob" : "Dec. 31",
            "email" : "bob@bob.xyz",
            "pic" : "/static/Bob_pic.png"
        },
    "carol":{
            "name" : "Carol Ling",
            "dob" : "Jul. 27",
            "email" : "carol@example.com",
            "pic" : "/static/Carol_pic.png"
        },
    "dave":{
            "name" : "Dave N. Port",
            "dob" : "Mar. 14",
            "email" : "dave@dave.dave",
            "pic" : "/static/Dave_pic.png"
        },
}
    
class Handler(tornado.web.RequestHandler):
    def get(self):
        L = self.request.path.split("/")
        uname = L[2]
        info = Dictionary[uname]
        
        self.render("profilepage.html",
        name=info["name"], dateofbirth=info["dob"],
        email=info["email"],pic=info["pic"]
        )

    def post(self):
        J=json.loads(self.request.body)
        firstName = J["name"]
      #  ppic = base64.b64decode(J["pic"])
        print("WE GOT:",firstName)

        L = self.request.path.split("/")
        uname = L[2]
        info = Dictionary[uname]

        print("WE ALSO GOT:",info["name"])
        info["name"] = firstName
        print("NEW:",info["name"])
       

        resp={"ok": True}
        self.write( json.dumps(resp) )