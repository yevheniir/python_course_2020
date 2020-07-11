import random
 
print("---Гра---")
print("Камінь/Ножиці/Папір")
app = random.randint(1, 3)
if app == 1:
    gg = "Камінь"
elif app == 2:
    gg = "Ножиці"
else:
    gg = "Папір"
print("1)Камінь")
print("2)Ножиці")
print("3)Папір")
try:
    x = int(input("Напиши вибрану цифру: "))
    if x == 1:
        print("")
        print("Ти вибрав: Камінь")
        print("Абонент вибрав: " + str(gg))
        print("")
        if app == 1:
            print("Ніч'я :/")
        elif app == 2:
            print("Ти вийграв!!!")
        else:
            print("Ти програв! :(")
            print("")
    elif x == 2:
        print("")
        print("Ти вибрав: Ножиці")
        print("Абонент вибрав: " + str(gg))
        print("")
        if app == 1:
            print("Ти програв! :(")
        elif app == 2:
            print("Ніч'я :/")
        else:
            print("Ти вийграв!!!")
            print("")
    elif x == 3:
        print("")
        print("Ти вибрав: Папір")
        print("Абонент вибрав: " + str(gg))
        print("")
        if app == 1:
            print("Ти вийграв!!!")
        elif app == 2:
            print("Ти програв! :(")
        else:
            print("Ніч'я :/")
        print("")
    else:
        print("Можна писати тільки цифри: 1/2/3!")
except ValueError:
    print("ERROR: Write only INT numbers!")
