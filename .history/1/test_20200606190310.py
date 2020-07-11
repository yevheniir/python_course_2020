import os
import json

people = ['rfdfdf', 'sdsd', 'dsdsd']

with open(os.path.dirname(os.path.realpath(__file__)) + "/save.json", 'r') as file:
    people = json.load(file)

while True:
    msg = input().encode('ascii')
    
    if msg == "stop":
        break
    elif msg == "show all":
        print(people)
    else:
        name = ""
        game = ""
        try:
            name, game = msg.split(', ')
        except Exception as er:
            print("Err, try again with 2 params separated by ', '")
        
        people.append({"name": name, "game": game})
    

with open(os.path.dirname(os.path.realpath(__file__)) + "/save.json", 'w') as file:
    json.dump(people, file)
    
# print("STOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOP")

# for name in people:
#     if name != "JoJo":
#         print(name) 