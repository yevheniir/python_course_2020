import os
import json

people = []

with open(os.path.dirname(os.path.realpath(__file__)) + "/save.json", 'r') as file:
    people = json.load(people, file)

while True:
    name = input()
    
    if name == "stop":
        break
    if name == "show all":
        print(people)
    
    people.append({"name": name})
    

with open(os.path.dirname(os.path.realpath(__file__)) + "/save.json", 'w') as file:
    json.dump(people, file)
    
# print("STOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOP")

# for name in people:
#     if name != "JoJo":
#         print(name) 