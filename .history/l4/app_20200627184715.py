from flask import Flask
from flask import jsonify
from flask import render_template

app = Flask(__name__)
# ////////////////////////////////////////////

users_obj = [{"id": 1, "name": "Nanachi"}, {"id": 2, "name": "nezuko"}]


@app.route('/')  #контролер
def nanachi():
    return "<h1>Hello World!<!h1>"


@app.route('/users')  #контролер
def users():
    return jsonify(users_obj)



# ////////////////////////////////////////////
if __name__ == '__main__':
    app.run()