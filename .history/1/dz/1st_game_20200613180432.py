import time


print("Вітаю у грі камінь, ножиці, бумага!")
time.sleep(2)
відповідь_до_початку_гри=input("Хочете зіграти?(Відповідати Так або Ні)")
if відповідь_до_початку_гри=="Так":
    print("Чудово")
else:
    print("Шкода")
    time.sleep(9999999999999999999999999999999999999999999999999999999999999999999999999999999)
time.sleep(2)
input("Обирайте предмет.(Камінь-1st-1, Ножиці-2nd-2, чи Бумага-3d-3)")
import random
first=Камінь=1
second=Ножиці=2
third=Бумага=3
ваша_відповідь = 1 or 2 or 3
1 < 3
2 > 1
3 < 2
відповідь_бота=(random.randint(1,3))
if ваша_відповідь<відповідь_бота:
    print("Упс. Ви програли")
    print(відповідь_бота)
else:
    print("Ура ви виграли!")
    print(відповідь_бота)
