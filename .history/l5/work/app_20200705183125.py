from flask import Flask
from flask import render_template
import random
#from app import app

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/game")
def game():
    return render_template("index.html")



if __name__ == "__main__":
    app.run()