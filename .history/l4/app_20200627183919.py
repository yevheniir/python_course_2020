from flask import Flask
app = Flask(__name__)
# ////////////////////////////////////////////

users = [{"id": 1, "name": "Nanachi"}, {"id": 2, "name": "ne"}]


@app.route('/')  #контролер
def nanachi():
    return "Hello World!"


@app.route('/users')  #контролер
def nanachi():
    return 



# ////////////////////////////////////////////
if __name__ == '__main__':
    app.run()