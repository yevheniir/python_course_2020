# Імпорт фажливих бібліотек
from BeautifulSoup import BeautifulSoup
import urllib2
import re

# Створення функції пошуку силок
def getLinks(url):
    # отримання та присвоєння контенту сторінки в змінну
    html_page = urllib2.urlopen(url)
    # Перетворення 
    soup = BeautifulSoup(html_page)
    links = []

    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        links.append(link.get('href'))

    return links