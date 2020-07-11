from flask import Flask
from flask import render_template

app = Flask(__name__)

scoreboard = []

@app.route("/game/<name>")
def hello(name):
    user_exist = False
    for user in scoreboard:
        if user['name'] == name:
            user_exist = True
            user['score'] += 1
            
    if not user_exist:
        scoreboard.append({"name": name, "score": 0})
        
    return render_template("index.html", scoreboard=scoreboard)

if __name__ == "__main__":
    app.run()