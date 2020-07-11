from flask import Flask
app = Flask(__name__)
# ////////////////////////////////////////////



@app.route('/')  #контролер
def nanachi():
    return "Hello World!"


@app.route('/users')  #контролер
def nanachi():
    return 



# ////////////////////////////////////////////
if __name__ == '__main__':
    app.run()