from flask import Flask, render_template  # import flask framework
import requests
import logging
app = Flask(__name__)  # create app instance

@app.route("/")  # decorator defines routes in app, in this case home '/'
def home():
    try:
        URL = "https://xkcd.com/info.0.json"
        response = requests.get(url=URL)
        if (response.status_code != 200):
            raise ValueError("Error connecting to XKCD please check back later.")
        return render_template("index.html", data=response.json())
    except ValueError as e:
        logging.error(f"ValueError with home: {e}")
        return render_template("errorPage.html", errorMessage = e)

@app.route("/pastComic/<comicNum>")             #decorator defines routes in app, in this case home '/'
def pastComic(comicNum):
    try:
        logging.info(f"Past Comic URL with value: {comicNum}")
        if not comicNum.isdigit():
            raise ValueError(f"The requested comic should be a integer. Received '{comicNum}' instead")
        if(int(comicNum) > 3000):
            raise ValueError(f"No comic available for '{comicNum}'. Please try another number smaller than 3001")
        URL = "https://xkcd.com/" + comicNum + "/info.0.json"
        response = requests.get(url = URL)
        if (response.status_code != 200):
            raise ValueError("Error connecting to XKCD please check back later.")
        return render_template("pastComic.html", data = response.json())
    except ValueError as e:
        logging.error(f"ValueError with pastComic: {e}")
        return render_template("errorPage.html", errorMessage = e)
    except Exception as e:
        logging.error(f"Exception with pastComic: {e}")
        return render_template("errorPage.html", errorMessage = e)

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