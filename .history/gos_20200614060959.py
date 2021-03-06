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
# Створюємо рекурсивну функцію яка приймає десяткове число
def decimalToBinary(n):  
  
    # перевіряємо чи число юільше 1
    if(n > 1):  
        # Якщо так, ділемо на 2 юез остачі та рекурсивно викликаємо функцію
        decimalToBinary(n//2)  
  
    # Якщо ні, виводимо на остачу ділення числа на 2
    print(n%2, end=' ') 
  
# Створюємо функцію яка приймає бінарне число
def binaryToDecimal(binary): 
      
    # Створюємо додаткову змінну
    binary1 = binary 
    
    # Ініціалізуємо ще 3 змінню даючи їм значення 0
    decimal, i, n = 0, 0, 0
    
    # Ітеруємося до тих пір поки передане нами число не буде 0
    while(binary != 0): 
        # Отримуємо остачу від ділення нашого чила на 10 на записуємо в змінну
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    print(decimal)     
      
