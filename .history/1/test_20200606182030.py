people = {Єname: "Ваня"}

for i in range(3):
    name = input()
    people.append(name)

for name in people:
    if name != "JoJo":
        print(name) 