import random
e=0
while(e==0):
    player=int(input("1.Камень 2.Ножницы 3.Бумага"))
    if player==1 or player==2 or player==3:
        e=1
if player==1:
    print("Ви обрали камінь")
if player==2:
    print("Ви обрали ножиці")
if player==3:
    print("Ви обрали бумагу")
    
c=random.randint(1,3)
if c==1:
    print("Комп'ютер обрав камінь")
if c==2:
    print("Комп'ютер обрав ножиці")
if c==3:
    print("Комп'ютер обрав бумагу")
    
if player==c:
    win=0
if player==1 and c==3:
    win=2
if player==1 and c==2:
    win=1
if player==2 and c==1:
    win=2
if player==2 and c==3:
    win=1
if player==3 and c==2:
    win=2
if player==3 and c==1:
    win=1
if win==0:
    print("Нічия")
if win==1:
    print("Ви перемогли")
if win==2:
    print("Переміг комп'ютер")
    
    
