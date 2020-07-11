from flask import Flask
from flask import render_template

app = Flask(__name__)

scoreboard = [{"name": "Tester", "score": 10}, {"name": "Tester", "score": 11}]

def x(user)


@app.route("/<name>")
def hello(name):
    if name in map(lambda user: user.name == name ,scoreboard):
        
    return render_template("index.html", scoreboard=scoreboard)

@app.route("/game")
def game():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()