from flask import Flask
app = Flask(__name__)
# ////////////////////////////////////////////



@app.route('/')  #контролер   <domain>/
def nanachi():
    return "Hello World!"



# ////////////////////////////////////////////
if __name__ == '__main__':
    app.run()