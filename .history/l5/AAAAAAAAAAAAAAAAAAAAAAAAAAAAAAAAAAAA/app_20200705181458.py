import random
from flask import Flask
from flask import render_template
#######################################
choose = ['rock', 'paper', 'scisors']

app = Flask(__name__)

#######################################
def winners():
	if winner == 'compucter':
		return render_template('2.html')
	else:
		return render_template('3.html')


def random2():
	choose = random.choice(choose)
def game():
	if (choose == 'rock' and player == 'paper') or (choose == 'paper' and player == 'scisors') or (choose == 'scisors' and player == 'rock'):
		winner = 'player'
#######################################
	elif (choose == 'paper' and player == 'rock') or (choose == 'scisors' and player == 'paper') or (choose == 'rock' and player == 'scisors'):
		winner = 'compucter'
	else:
		winner = 'Tie'


@app.route('/')
def home():
   return render_template('index.html')
#######################################
@app.route('/rock')

def rock():
	random2()
	player = "rock"
	game()
#######################################
@app.route('/paper')

def paper():
	random2()
	player = "paper"
	game()
#######################################
@app.route('/scisors')

def scisors():
	random2()
	player = "scisors"
	game()
#######################################
@app.route('/tie')

def tie():
	winner = 'Tie'
	return render_template('1.html')
#######################################
if __name__ == '__main__':
   app.run()