from flask import Flask,render_template,url_for,request,redirect
app=Flask(__name__)
@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('help')),redirect(url_for('game'))     
    return render_template('home.html')
@app.route('/help', methods=['GET', 'POST'])
def help():
    if request.method == 'POST':
        return redirect(url_for('home')),redirect(url_for('game'))      
    return render_template('help.html')  
@app.route('/game', methods=['GET', 'POST'])
def game():  
    if request.method == 'POST':
        return redirect(url_for('home')),redirect(url_for('help'))        
    return render_template('game.html')       
if __name__=="__main__":
    app.run(debug=True)