from flask import Flask
from flask import render_template

app = Flask(__name__)

scoreboard = [{"name": "test", "score": 10}, {"name": "test2", "score": 11}]

@app.route("/<name>")
def hello(name):
    for user in scoreboard:
        if user['name'] == name:
            user.score += 1
        
    return render_template("index.html", scoreboard=scoreboard)

@app.route("/game")
def game():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()