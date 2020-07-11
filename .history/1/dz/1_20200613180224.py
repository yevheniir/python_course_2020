import random
player_score = 0
compucter_score = 0
choose = ["paper", "rock", "scissors"]

print("You can choose paper/rock/scissors")
n = int(input("How many rounds do you want? "))
print('Start!')
while n > 0:
    x = input()
    y = random.choice(choose)
    print(y)
    if(x == "paper" and y == "scissors") or (x == "rock" and y == "paper") or (x == "scissors" and y == "rock"):
        print("Lose")
        compucter_score = compucter_score+1
    elif x == y:
        print("Draw")
    else:
        print("Win")
        player_score = player_score+1
    n = n-1
print(player_score, compucter_score)
if player_score > compucter_score:
    print('You win compucter! Nice work :3')
else:
    print("Yes compucter win! Stuped human! HAHAHAHAHA")
