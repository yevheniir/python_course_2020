from flask import Flask
from flask import render_template
import random 

app = Flask(__name__)

def get_computer_move():
    options = ["камень", "paper", "scissors"]
    return options[random.randint(0,2)]

def get_winner(player_choice, computer_choice):
    winner = "компьютер"

    if player_choice == computer_choice:
        winner = "Ничья"
    if player_choice == "камень" and computer_choice == "scissors":
        winner = "Игрок"
    if player_choice == "scissors" and computer_choice == "paper":
        winner = "Игрок"
    if player_choice == "paper" and computer_choice == "камень":
        winner = "Игрок"

    return winner

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/rps/<choice>')
def rps(choice):
    player_choice = choice.lower()    
    computer_choice = get_computer_move()
    winner = get_winner(player_choice, computer_choice)
    
    return winner
    
    # return render_template("rps.html", winner=winner, player_choice=player_choice, computer_choice=computer_choice)

if __name__ == "__main__":
    app.run()