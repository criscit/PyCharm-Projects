import csv
import requests
from datetime import datetime
from bs4 import BeautifulSoup

start_date = datetime.now().date()
headers = {
    "Accept": "text/html,application/xhtml+xml,application"
              "/xml;q=0.9,image/avif,image/webp,image/apng,*"
              "/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Dnt": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
                  "/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "connection": "close"
}
with open(r'C:\Users\crisc\Desktop\MyProgs\book_project\amazon_parsing\get_info\all_book_links.txt',
          encoding='utf-8') as file:
    book_urls = []
    for book_url in file.readlines():
        book_urls.append(book_url)


def get_info(url_of_book):
    page = requests.get(url_of_book, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    try:
        title = soup.find('span', {'id': 'productTitle'}).text.strip()
    except AttributeError:
        title = ''
    authors = ''
    try:
        for author in soup.find_all('a', {'class': 'a-link-normal contributorNameID'}):
            authors += author.text + ', '
        authors = authors.rstrip(', ')
    except AttributeError:
        authors = ''
    publication_year = ''
    print_length = ''
    try:
        for list_item in soup.find_all('li', {'class': 'a-carousel-card rpi-carousel-attribute-card'}):
            if list_item.text.strip().split()[0] == 'Print':
                print_length = list_item.text.strip().split()[-2]
            if list_item.text.strip().split()[0] == 'Publication':
                publication_year = list_item.text.strip().split()[-1]
    except AttributeError:
        publication_year = ''
        print_length = ''
    try:
        rating_reviews = soup.find('div', {'id': 'averageCustomerReviews'}).text.strip()
        rating = rating_reviews.split()[0].replace('.', ',')
        reviews_number = int(rating_reviews.split(' ')[-2].replace(',', ''))
    except AttributeError:
        rating = ''
        reviews_number = ''
    return title, authors, publication_year, print_length, rating, reviews_number


books_info = []
for book_url in book_urls:
    books_info.append(get_info(book_url))

with open(r'C:\Users\crisc\Desktop\MyProgs\book_project\amazon_parsing\all_book_info.csv', 'x', newline='',
          encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['title', 'author', 'publication date, year',
                     'print length, pages', 'rating', f'reviews on {start_date}'])
    writer.writerows(books_info)

with open(r'C:\Users\crisc\Desktop\MyProgs\book_project\amazon_parsing\get_info\project_book_links.txt',
          encoding='utf-8') as file:
    book_urls = []
    for book_url in file.readlines():
        book_urls.append(book_url)

books_info = []
for book_url in book_urls:
    books_info.append(get_info(book_url))

with open(r'C:\Users\crisc\Desktop\MyProgs\book_project\amazon_parsing\project_book_info.csv', 'x', newline='',
          encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['title', 'author', 'publication date, year',
                     'print length, pages', 'rating', f'reviews on {start_date}'])
    writer.writerows(books_info)
