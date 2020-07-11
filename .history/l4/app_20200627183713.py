from flask import Flask
app = Flask(__name__)
# ////////////////////////////////////////////



@app.route('/')  #контролер   <domain google.com nanachi.us/
def nanachi():
    return "Hello World!"



# ////////////////////////////////////////////
if __name__ == '__main__':
    app.run()