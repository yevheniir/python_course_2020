from flask import Flask
from flask import render_template
import random 

app = Flask(__name__)

def get_computer_move():
    options = ["камень", "бумага", "ножницы"]
    return options[random.randint(1,3)]

def get_winner(player_choice, computer_choice):
    winner = "компьютер"

    if player_choice == computer_choice:
        winner = "Ничья"
    if player_choice == "камень" and computer_choice == "ножницы":
        winner = "Игрок"
    if player_choice == "ножницы" and computer_choice == "бумага":
        winner = "Игрок"
    if player_choice == "бумага" and computer_choice == "камень":
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
    
    return render_template("rps.html", users=["nanachi", "nezuko"] winner=winner, player_choice=player_choice, computer_choice=computer_choice)

if __name__ == "__main__":
    app.run()