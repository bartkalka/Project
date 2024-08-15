import requests
from bs4 import BeautifulSoup

def scrape_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = []
    for book_elem in soup.find_all('article', class_='product_pod'):
        title = book_elem.h3.a['title'].strip()
        price = book_elem.find('p', class_='price_color').text.strip()
        books.append({'title': title, 'price': price})

    return books
