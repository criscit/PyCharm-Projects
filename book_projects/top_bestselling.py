import csv
import requests
from bs4 import BeautifulSoup

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

departments = {'Business & Money': 'n%3A283155%2Cn%3A3',
               'Education & Teaching': 'n%3A283155%2Cn%3A8975347011',
               'Health, Fitness & Dieting': 'n%3A283155%2Cn%3A10',
               'Medical Books': 'n%3A283155%2Cn%3A173514',
               'Parenting & Relationships': 'n%3A283155%2Cn%3A20',
               'Politics & Social Sciences': 'n%3A283155%2Cn%3A3377866011',
               'Science & Math': 'n%3A283155%2Cn%3A75',
               'Self-Help': 'n%3A283155%2Cn%3A4736',
               'Sports & Outdoors': 'n%3A283155%2Cn%3A26'
               }


def get_url(department):
    """generate an url from search term"""
    template = 'https://www.amazon.com/s?i=stripbooks&bbn=1000&rh={}&s=salesrank&dc'
    return template.format(department)


def get_info(url_of_search, index_of_data):
    page = requests.get(url_of_search, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    item = soup.find('div', {'data-index': str(index_of_data),
                             'data-component-type': 's-search-result'})
    try:
        title = item.find('h2').text.strip()
    except AttributeError:
        title = ''
    try:
        rating_reviews = item.find('div', {'class': 'a-row a-size-small'}).text.strip()
        reviews_number = rating_reviews.split()[-1]
    except AttributeError:
        reviews_number = ''
    return title + '|' + reviews_number + '\n'


books = []
search_urls = [get_url(department) for department in departments.values()]
for search_url in search_urls:
    for data_index in range(1, 17):
        books.append(get_info(search_url, data_index))

with open('top_bestselling.txt', 'a', encoding='utf-8') as file:
    file.writelines(books)

with open('top_bestselling.txt', encoding='utf-8') as file:
    books = file.readlines()

books = list(set(books))
books.sort()

with open('top_bestselling.txt', 'w', encoding='utf-8') as file:
    file.writelines(books)
