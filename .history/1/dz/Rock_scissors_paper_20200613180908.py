import json
import random

print("Привет,это игра'Камень, ножницы, бумага'")
quest1=input("Ты хочешь сыграть?Да/Нет.")
c=True

def a():
    inp=input("Введи камень,ножницы или бумага.PS:С большой буквы.")
    list1=[]
    list1.append(inp)
    list2=['Бумага','Камень','Ножницы']
    rand=random.choice(list2)
    if(list1[0]==rand):
        print("Бот поставил  " + rand.lower()+".")
        print("Ничья!")
    if(list1[0]=='Бумага'and rand=='Камень'):
        print("Бот поставил  " + rand.lower()+".")
        print("Вы победили!")
    if(list1[0]=='Камень'and rand=='Бумага'):
        print("Бот поставил  " + rand.lower()+".")
        print("Вы проиграли!")
        print("Бот поставил "+rand)
    if(list1[0]=='Ножницы'and rand=='Камень'):
        print("Бот поставил  " + rand.lower()+".")
        print("Вы проиграли!")
    if(list1[0]=='Камень'and rand=='Ножницы'):
        print("Бот поставил  " + rand.lower()+".")
        print("Вы победили!")
    if(list1[0]=='Бумага'and rand=='Ножницы'):
        print("Бот поставил  " + rand.lower()+".")
        print("Вы проиграли!")
    if(list1[0]=='Ножницы'and rand=='Бумага'):
        print("Бот поставил  " + rand.lower()+".")
        print("Вы победили!")
if(quest1=="Да"):
    quest2=input("Ты знаешь правила игры?Да/Нет.")
    if(quest2=="Да"):
        a()
        while c==True:
            quest4=input("Ты хочешь ещё раз сыграть.Да/Нет.")
            if(quest4=="Да"):
                a()
            elif(quest4=="Нет"):
                с=False
                print("Игра завершена")
                print("Выход из игры...")
                break
    if(quest2=="Нет"):
        print("_____________________________________________________________________________________________________________________________________________________________________________________________________________________________")
        print("|Вот правила игры:\n")
        print("|Игроки считают вместе вслух «Камень… Ножницы… Бумага… Раз… Два… Три», одновременно качая кулаками.\n")
        print("|Существуют и другие варианты счёта, распространённость которых различается в разных городах и регионах, например, «Рас(е)л-двас(е)л-трис(е)л!», «Эна-бена-цо!», «Су-ли-фа», «Ю-зе-фа», «Бу-це-фа», «Аль… ман… джуз!» и др.\n")
        print("|На счёт «Три» они одновременно показывают при помощи руки один из трёх знаков: камень, ножницы или бумагу.\n ")
        print("|Победитель определяется по следующим правилам: \n\n")
        print("|Бумага побеждает камень («бумага обёртывает камень»).\n")
        print("|Ножницы побеждают бумагу («ножницы разрезают бумагу»).\n")
        print("|Камень побеждает ножницы («камень затупляет или ломает ножницы»).\n")
        print("|Если игроки показали одинаковый знак, то засчитывается ничья и игра переигрывается.")
        print("|_____________________________________________________________________________________________________________________________________________________________________________________________________________________________")
        a()
        while c==True:
            quest4=input("Ты хочешь ещё раз сыграть.Да/Нет.")
            if(quest4=="Да"):
                a()
            elif(quest4=="Нет"):
                с=False
                print("Игра завершена")
                print("Выход из игры...")
                break
elif(quest1=="Нет"):
    print("Выход из игры...")
else:
    pass
input()
