from flask import Flask
from flask import jsonify

app = Flask(__name__)
# ////////////////////////////////////////////

users_obj = [{"id": 1, "name": "Nanachi"}, {"id": 2, "name": "nezuko"}]


@app.route('/')  #контролер
def nanachi():
    return "Hello World!"


@app.route('/users')  #контролер
def users():
    return jsonify



# ////////////////////////////////////////////
if __name__ == '__main__':
    app.run()