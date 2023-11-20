import csv
import requests
from datetime import datetime
from bs4 import BeautifulSoup

start_date = datetime.strptime('2022-10-24', '%Y-%m-%d').date()
report_date = datetime.now().date()
days_between_reports = (report_date - start_date).days
report_path = r'O:\Документы\Книги\Отчеты' + f'\\report on {report_date}.csv'
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


def get_info(url_of_book):
    page = requests.get(url_of_book, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    try:
        title = soup.find('span', {'id': 'productTitle'}).text.strip()
    except AttributeError:
        title = ''
    try:
        rating_reviews = soup.find('div', {'id': 'averageCustomerReviews'}).text.strip()
        reviews_number = int(rating_reviews.split(' ')[-2].replace(',', ''))
    except AttributeError:
        reviews_number = ''
    return title, reviews_number


book_urls = []
books_info = []

with open(r'C:\Users\crisc\Desktop\MyProgs\book_project\amazon_parsing\get_info\all_book_links.txt',
          encoding='utf-8') as file:
    for book_url in file.readlines():
        book_urls.append(book_url)

with open(r'C:\Users\crisc\Desktop\MyProgs\book_project\amazon_parsing\get_info\project_book_links.txt',
          encoding='utf-8') as file:
    for book_url in file.readlines():
        book_urls.append(book_url)

for book_url in book_urls:
    books_info.append(get_info(book_url))

with open(report_path, 'x', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['title', f'reviews after {days_between_reports} days'])
    writer.writerows(books_info)