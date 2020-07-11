from flask import Flask
app = Flask(__name__)
# ////////////////////////////////////////////

users = [{"id": 1, "name": "Nanachi"}, {"id": 2, "name": "nezuko"}]


@app.route('/')  #контролер
def nanachi():
    return "Hello World!"


@app.route('/users')  #контролер
def us():
    return users



# ////////////////////////////////////////////
if __name__ == '__main__':
    app.run()