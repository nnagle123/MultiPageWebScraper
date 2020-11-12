import requests
from bs4 import BeautifulSoup as bs

URL = 'https://thegreatestbooks.org/?page='

for page in range(1, 53):

    req = requests.get(URL + str(page))
    soup = bs(req.text, 'html.parser')
    container = soup.find('div', attrs={'class', 'container'})
    books = container.find_all('h4')

    for book in books:
        links = book.find_all('a')
        title = links[0].text
        author = ''
        try:
            author = links[1].text
        except:
            pass
        print('title: %s \n author: %s' %(title, author))

