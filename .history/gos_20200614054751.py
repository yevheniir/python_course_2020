# Імпорт фажливих бібліотек
from BeautifulSoup import BeautifulSoup
import urllib2
import re

# Створення функції пошуку силок
def getLinks(url):
    # отримання та присвоєння контенту сторінки в змінну
    html_page = urllib2.urlopen(url)
    # Перетворення контенту в обєкт бібліотеки BeautifulSoup
    soup = BeautifulSoup(html_page)
    # створення пустого масиву для лінків
    links = []

    # ЗА ДОПОМОГОЮ ЧИКЛУ ПРОХЛДИМСЯ ПО ВСІХ ЕЛЕМЕНТАХ ДЕ Є СИЛКА
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        # Додаємо всі силки
        links.append(link.get('href'))

    return links