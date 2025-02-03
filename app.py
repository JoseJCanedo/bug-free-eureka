from flask import Flask, render_template     #import flask framework
import requests
app = Flask(__name__)       #create app instance

@app.route("/")             #decorator defines routes in app, in this case home '/'
def home():
    URL = "https://xkcd.com/info.0.json"
    req = requests.get(url = URL)
    data = req.json()
    return render_template("index.html", data = data)

@app.route("/pastComic")             #decorator defines routes in app, in this case home '/' 
def pastComic():
    URL = "https://xkcd.com/info.0.json"
    req = requests.get(url = URL)
    data = req.json()
    return render_template("index.html", data = data)

@app.route("/who/<name>/who")  #second route with query parameter called name
def hello_pathParam(name):
    return {"name": name}

if __name__=="__main__":
    app.run(debug=True)

# 127.0.0.1:5000
# path parameter/variable Part of the URL
# query parameter/variable Not a part of the URL necessary for navigation /who?name=jose