import random

users = ["Власюк Владислав Володимирович",
"Степаненко Юрій",
"Редько Аліна Олександрівна",
"Станкевич Дарій-Сергій",
"Гурін Ілля Валентинович",
"Яромир Юрченко",
"Маценко Володимир Володимирович",
"Осачій Роман Олексанрович",
"Оліщук Олександр Олександрович",
"Нечко Дмитро Васильович",
"Яковенко Даніель",
"Тетьора Ілля Сергійович ",
"Стрижов Кіріл",
"Іван"]

random.shuffle(users)

for i in range(len(users) // 2):
    print(users[i] + " : " + users[-i])