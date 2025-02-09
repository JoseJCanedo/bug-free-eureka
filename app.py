from flask import Flask, render_template     #import flask framework
import requests
app = Flask(__name__)       #create app instance

@app.route("/")             #decorator defines routes in app, in this case home '/'
def home():
    URL = "https://xkcd.com/info.0.json"
    req = requests.get(url = URL)
    data = req.json()
    return render_template("index.html", data = data)

@app.route("/pastComic/<comicNum>")             #decorator defines routes in app, in this case home '/'
def pastComic(comicNum):
    if(comicNum.isdigit() and int(comicNum) <= 3000):
        URL = "https://xkcd.com/" + comicNum + "/info.0.json"
        req = requests.get(url = URL)
        data = req.json()
        return render_template("pastComic.html", data = data)
    else:
        return render_template("errorPage.html")

@app.route("/who/<name>/who")  #second route with query parameter called name
def hello_pathParam(name):
    return {"name": name}

if __name__=="__main__":
    app.run(debug=True)

# path parameters -> part of the url
# query params -> ?foo=bar&foo1=bar1

# 127.0.0.1:5000
# path parameter/variable Part of the URL
# query parameter/variable Not a part of the URL necessary for navigation /who?name=jose