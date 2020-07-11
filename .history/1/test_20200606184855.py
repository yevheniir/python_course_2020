import os
import json

people = []

with open(os.path.dirname(os.path.realpath(__file__)) + "/save.json", 'r') as file:
    people = json.load(file)

while True:
    name = input()
    
    if name == "stop":
        break
    elif name == "show all":
        print(people)
    else:
        name
        try:
            name, game = name.split(', ')
        except Exception as er:
            print(er)
        
        people.append({"name": name, "game": game})
    

with open(os.path.dirname(os.path.realpath(__file__)) + "/save.json", 'w') as file:
    json.dump(people, file)
    
# print("STOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOP")

# for name in people:
#     if name != "JoJo":
#         print(name) 