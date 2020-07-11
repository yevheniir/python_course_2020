from flask import Flask
from flask import render_template

app = Flask(__name__)

scoreboard 

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/game")
def game():
    return render_template("index.html")



if __name__ == "__main__":
    app.run()