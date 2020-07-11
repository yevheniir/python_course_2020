from flask import Flask
from flask import jsonify
from flask import render_template

app = Flask(__name__)
# ////////////////////////////////////////////

users_obj = [{"id": 767867867, "name": "Nanachi"}, {"id": 6786787, "name": "nezuko"}]


@app.route('/')  #контролер
def nanachi():
    return render_template("index.html", users=users_obj)


@app.route('/users')  #контролер
def users():
    return jsonify(users_obj)


@app.route('/choise/<choise>')  #контролер
def users():
    user_choise = choise
    bot_coise  = "камін"
    return "Win or не він"



# ////////////////////////////////////////////
if __name__ == '__main__':
    app.run()