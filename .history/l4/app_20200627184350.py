from flask import Flask
app = Flask(__name__)
# ////////////////////////////////////////////

users_obj = [{"id": 1, "name": "Nanachi"}, {"id": 2, "name": "nezuko"}]


@app.route('/')  #контролер
def nanachi():
    return "Hello World!"


@app.route('/users')  #контролер
def users():
    return json



# ////////////////////////////////////////////
if __name__ == '__main__':
    app.run()