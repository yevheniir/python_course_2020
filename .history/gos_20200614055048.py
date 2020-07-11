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

# # Імпорт фажливих бібліотек
import subprocess

# Створення циклу та використання функції range для генерації послідовних чисел
for ping in range(1,10):
    # генерування IP адреси базуючись на номері ітерації
    address = "127.0.0." + str(ping)
    # виклик функції call яка 
    res = subprocess.call(['ping', '-c', '3', address])
    if res == 0:
        print "ping to", address, "OK"
    elif res == 2:
        print "no response from", address
    else:
        print "ping to", address, "failed!"