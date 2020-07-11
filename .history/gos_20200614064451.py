# # Імпорт фажливих бібліотек
# from BeautifulSoup import BeautifulSoup
# import urllib2
# import re

# # Створення функції пошуку силок
# def getLinks(url):
#     # отримання та присвоєння контенту сторінки в змінну
#     html_page = urllib2.urlopen(url)
#     # Перетворення контенту в обєкт бібліотеки BeautifulSoup
#     soup = BeautifulSoup(html_page)
#     # створення пустого масиву для лінків
#     links = []

#     # ЗА ДОПОМОГОЮ ЧИКЛУ ПРОХЛДИМСЯ ПО ВСІХ ЕЛЕМЕНТАХ ДЕ Є СИЛКА
#     for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
#         # Додаємо всі силки в список
#         links.append(link.get('href'))

#     # повертаємо список
#     return links
# -----------------------------------------------------------------------------------------------------------
# # # Імпорт фажливих бібліотек
# import subprocess

# # Створення циклу та використання функції range для генерації послідовних чисел
# for ping in range(1,10):
#     # генерування IP адреси базуючись на номері ітерації
#     address = "127.0.0." + str(ping)
#     # виклик функції call яка робить запит на IP адрес та запис відповіді в змінну
#     res = subprocess.call(['ping', '-c', '3', address])
    
#     # За допомогою умовних операторів перевіряємо відповідь та виводимо результат
#     if res == 0:
#         print "ping to", address, "OK"
#     elif res == 2:
#         print "no response from", address
#     else:
#         print "ping to", address, "failed!"
# -----------------------------------------------------------------------------------------------------------
# # Імпорт фажливих бібліотек
# import requests

# # Ітеруємося по масиву з адресами зображень
# for i, pic_url in enumerate(["http://x.com/nanachi.jpg", "http://x.com/nezuko.jpg"]):
#     # Відкриваємо файл базуючись на номері ітерації
#     with open('pic{0}.jpg'.format(i), 'wb') as handle:
#         # Отримуємо картинку
#         response = requests.get(pic_url, stream=True)

#         # Використовуючи умовний оператор перевіряємо чи успішно виконався запит
#         if not response.ok:
#             print(response)

#         # Ітеруємося по байтах картинки та записуємо батчаси в 1024 до файлу
#         for block in response.iter_content(1024):
#             # Якщо байти закінчилися, завершуємо алгоритм
#             if not block:
#                 break
#             # Записуємо байти в файл
#             handle.write(block)
# -----------------------------------------------------------------------------------------------------------
# # Створюємо клас для рахунку
# class Bank_Account: 
#     # В конструкторі ініціалізуємо рахунок як 0
#     def __init__(self): 
#         self.balance=0
#         print("Hello!!! Welcome to the Deposit & Withdrawal Machine") 
#     # В методі депозит, використовуючи функцію input() просимо ввести суму поповенння та додаємо цю суму до рахунку
#     def deposit(self): 
#         amount=float(input("Enter amount to be Deposited: ")) 
#         self.balance += amount 
#         print("\n Amount Deposited:",amount) 
#      # В методі депозит, використовуючи функцію input() просимо ввести суму отримання та віднімаємо цю суму від рахунку
#     def withdraw(self): 
#         amount = float(input("Enter amount to be Withdrawn: ")) 
#         # За допомогою умовного оператора перевіряємо чи достатнього грошей на рахунку
#         if self.balance>=amount: 
#             self.balance-=amount 
#             print("\n You Withdrew:", amount) 
#         else: 
#             print("\n Insufficient balance  ") 
  
#     # Виводимо бааланс на екран
#     def display(self): 
#         print("\n Net Available Balance=",self.balance) 
  
   
# # Створюємо рахунок 
# s = Bank_Account() 
   
# # Проводимо операції з рахунком
# s.deposit() 
# s.withdraw() 
# s.display() 
# -----------------------------------------------------------------------------------------------------------
# # Створюємо рекурсивну функцію яка приймає десяткове число
# def decimalToBinary(n):  
  
#     # перевіряємо чи число юільше 1
#     if(n > 1):  
#         # Якщо так, ділемо на 2 юез остачі та рекурсивно викликаємо функцію
#         decimalToBinary(n//2)  
  
#     # Якщо ні, виводимо на остачу ділення числа на 2
#     print(n%2, end=' ') 
  
# # Створюємо функцію яка приймає бінарне число
# def binaryToDecimal(binary): 
      
#     # Створюємо додаткову змінну
#     binary1 = binary 
    
#     # Ініціалізуємо ще 3 змінню даючи їм значення 0
#     decimal, i, n = 0, 0, 0
    
#     # Ітеруємося до тих пір поки передане нами число не буде 0
#     while(binary != 0): 
#         # Отримуємо остачу від ділення нашого чила на 10 на записуємо в змінну
#         dec = binary % 10
        
#         # Додаємо до результату суму попереднього результату та добуток від dec та піднесення 2 до степеня номеру ітерації
#         decimal = decimal + dec * pow(2, i) 
#         # Змінюємо binary
#         binary = binary//10
#         # Додаємо 1 до кількості ітерацій
#         i += 1
#     # Виводимо результат
#     print(decimal)     
# -----------------------------------------------------------------------------------------------------------
# # Імпорт фажливих бібліотек
# import re

# # В умовному операторі перевіряємо чи підходить введена пошта під знайдений з інтернету regex
# if re.match(r"[^@]+@[^@]+\.[^@]+", "nanachi@gmail.com"):
#   # Якщо так, виводиму valid 
#   print("valid")
# -----------------------------------------------------------------------------------------------------------
# # Створення функції яка приймає текст для шифрування та здвиг
# def encrypt(text,s):
#    # Створення змінної для результату    
#    result = ""
#    # Ітеруємося по тексту використовуючи range та довжину тексту
#    for i in range(len(text)):
#       # Беремо літеру базуючись на номері ітерації    
#       char = text[i]
      
#       # Перевіряємо чи ця літера велика
#       if (char.isupper()):
#          # Кодуємо літеру базуючись на її номері 
#          result += chr((ord(char) + s-65) % 26 + 65)
#       else:
#          # Кодуємо літеру базуючись на її номері 
#          result += chr((ord(char) + s - 97) % 26 + 97)
#       # Повертаємо результат   
#       return result
# -----------------------------------------------------------------------------------------------------------
# # Створення списку з телефонами
# numbers = ["0502342349", "0500897897", "0992342349"]

# # Ініціалізація змінної з результатом
# result = {}

# # Ітерації по телефонах для ініціалізації клічів результата
# for num in numbers:
#     # Створення ключа бузуючись на номері оператора та присвоєння йому пустого масиву
#     result[num[:3]] = []

# # Ітерації по телефонах
# for num in numbers:
#     # Додавання телефону до відповідного оператора
#     result[num[:3]].append(num)
    
# # Вивід результатту
# print(result)
# -----------------------------------------------------------------------------------------------------------
# # Імпорт фажливих бібліотек
# import unittest

# # Створення класу з тестами наслідуючись від unittest.TestCase
# class TestStringMethods(unittest.TestCase):

#     # Створення методу з тестом
#     def test_upper(self):
#         # перевірка чи буде результат виконання першого аргументу дорівнювати другому
#         self.assertEqual('foo'.upper(), 'FOO')

# # Запуск скрипта
# if __name__ == '__main__':
#     unittest.main()
# -----------------------------------------------------------------------------------------------------------
# # Імпорт фажливих бібліотек
# import math 

# # створення функції яка приймає 2 точки
# def distance(x1, y1, z1, x2, y2, z2):  
       
#     # Знаходження відстані за шкільної формулою використовуючи функції з модулю math
#     d = math.sqrt(math.pow(x2 - x1, 2) +
#                 math.pow(y2 - y1, 2) +
#                 math.pow(z2 - z1, 2)* 1.0) 
    
#     # Вивід результату
#     print("Distance is ") 
#     print(d) 
# -----------------------------------------------------------------------------------------------------------
# # Відкриваємо файл для запису
# file1 = open("myfile.txt","w") 
  
# # Записуємо Hello в файл
# file1.write("Hello") 
# # Закриваємо файл
# file1.close() 
  
# # Відкриваємо файл для зчитування
# file1 = open("myfile.txt","r+")  
# # Виводимо в консоль вміст файлу
# print(file1.read()) 
# -----------------------------------------------------------------------------------------------------------
# Python program to find the k most frequent words 
# from data set 
from collections import Counter 
  
data_set = "Welcome to the world of Geeks " \ 
"This portal has been created to provide well written well" \ 
"thought and well explained solutions for selected questions " \ 
"If you like Geeks for Geeks and would like to contribute " \ 
"here is your chance You can write article and mail your article " \ 
" to contribute at geeksforgeeks org See your article appearing on " \ 
"the Geeks for Geeks main page and help thousands of other Geeks. " \ 
  
# split() returns list of all the words in the string 
split_it = data_set.split() 
  
# Pass the split_it list to instance of Counter class. 
Counter = Counter(split_it) 
  
# most_common() produces k frequently encountered 
# input values and their respective counts. 
most_occur = Counter.most_common(4) 
  
print(most_occur) 