import os

people = []

while True:
    name = input()
    
    if name == "stop":
        break
    if name == "show all":
        print(people)
    
    people.append({"name": name})
    

with open(os.path.dirname(os.path.realpath(__file__)) + "/save.json"):
    print("hi")
    
# print("STOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOP")

# for name in people:
#     if name != "JoJo":
#         print(name) 