import re
import csv
import requests
import time
import datetime
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


# with open(r'O:\Документы\Книги\Проект\список книг.txt', encoding='utf-8') as file:
#     search_terms = ''
#     for row in file:
#         if re.findall(':', row):
#             row = row.split(':')[0] + (' by' + row.split(':')[1].split('by')[1] + '\n' if 'by' in row else '\n')
#         search_terms += row
#
# search_terms = search_terms.lower()
# search_terms = re.sub(" – ", " by ", search_terms)
# search_terms = re.sub(" - ", " by ", search_terms)
# search_terms = re.sub(r"\d", "", search_terms)
# search_terms = re.sub(r"[^a-zA-Z'\n ]", " ", search_terms)
# search_terms = re.sub(r"\W+\n", "\n", search_terms)
# search_terms = re.sub(r"\n\W+", "\n", search_terms)
# search_terms = re.sub(r"^\W+|\W+$", "", search_terms)
# search_terms = re.sub("'", "%27", search_terms)
# while re.findall("  ", search_terms):
#     search_terms = re.sub("  ", " ", search_terms)
#
#
# def get_url(search_term):
#     """generate an url from search term"""
#     template = 'https://www.amazon.com/s?k={}&i={}&ref=nb_sb_noss_1'
#     search_term = search_term.replace(' ', '+')
#     search_department = 'stripbooks-intl-ship'
#     return template.format(search_term, search_department)
#
#
# search_urls = [get_url(url) for url in search_terms.split('\n')]
#
#
# def get_info(search_url):
#     amazon_url = 'https://www.amazon.com'
#     page = requests.get(search_url, headers=headers)
#     soup = BeautifulSoup(page.text, 'html.parser')
#     item = soup.find('div', {'data-index': '1',
#                              'data-component-type': 's-search-result'})
#     try:
#         reference = amazon_url + item.find('h2').find('a').get('href')
#     except AttributeError:
#         reference = '0'
#     try:
#         title = item.find('h2').text.strip()
#     except AttributeError:
#         title = '0'
#     try:
#         author_row = item.find('div', {'class': 'a-size-base'}).text
#         author_row = author_row.split('by')[1]
#     except AttributeError:
#         author_row = '0 0'
#     except IndexError:
#         author_row = '0 0'
#     if '|' in author_row:
#         author = author_row.split('|')[0].strip()
#     else:
#         author = author_row.strip()
#     try:
#         rating_reviews = item.find('div', {'class': 'a-row a-size-small'}).text.strip()
#     except AttributeError:
#         rating_reviews = '0 0'
#     rating = rating_reviews.split(' ')[0].replace('.', ',')
#     reviews_number = int(rating_reviews.split(' ')[-1].replace(',', ''))
#     return search_url, reference, title, author, rating, reviews_number
#
#
# books = []
# for url in search_urls:
#     books.append(get_info(url))
#
# with open('check_links.csv', 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow(['url search', 'reference', 'title', 'author', 'rating', 'reviews_number', 'nothing'])
#     writer.writerows(books)


"""Удаление лишних частей ссылки"""
with open('project_book_links.txt', encoding='utf-8') as file:
    book_links = []
    for link in file.readlines():
        if link.count('/') > 5:
            while link.count('/') != 5:
                link = link[0:link.rindex('/')]
                book_links.append(link+'\n')
        else:
            book_links.append(link+'\n')

with open('links.txt', 'w', encoding='utf-8') as file:
    file.writelines(book_links)


def get_kindle_url(book_url):
    page = requests.get(book_url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    item = soup.find('li', {'class': 'swatchElement selected'})
    amazon_url = 'https://www.amazon.com'
    type_of_book = item.text.strip().split()[0]
    reference = ''
    if type_of_book != 'Kindle' or type_of_book != 'eTextbook':
        for item in soup.find_all('li', {'class': 'swatchElement unselected'}):
            type_of_book = item.text.strip().split()[0]
            reference = amazon_url + item.find('a').get('href') + '\n'
            if type_of_book == 'Kindle' or type_of_book == 'eTextbook':
                break

    else:
        reference = book_url
    return reference


# with open('project_book_links.txt', encoding='utf-8') as file:
#     book_links = []
#     for link in file.readlines():
#         book_links.append(get_kindle_url(link))
#
# with open('links.txt', 'w', encoding='utf-8') as file:
#     file.writelines(book_links)
# print(get_kindle_url('https://www.amazon.com/Influence-Psychology-Persuasion-Robert-Cialdini/dp/006124189X/ref=tmm_pap_swatch_0?_encoding=UTF8&qid=&sr='))