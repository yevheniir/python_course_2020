from flask import Flask
app = Flask(__name__)
# ////////////////////////////////////////////

users = [{"id": 1, "name"}]


@app.route('/')  #контролер
def nanachi():
    return "Hello World!"


@app.route('/users')  #контролер
def nanachi():
    return 



# ////////////////////////////////////////////
if __name__ == '__main__':
    app.run()