from flask import Flask
app = Flask(__name__)
# ////////////////////////////////////////////



@app.route('/')  #контролер
def nanachi():
    return "Hello World!"


@app.route('/use')  #контролер
def nanachi():
    return "Hello World!"



# ////////////////////////////////////////////
if __name__ == '__main__':
    app.run()