with open('book_projects/amazon_parsing/get_info/all_book_list.txt', 'r', encoding='utf-8') as file:
    books = []
    for row in file:
        books.append('00' + row)
books.sort(reverse=True)

with open('book_projects/amazon_parsing/get_info/search_terms.txt', 'w', encoding='utf-8') as file:
    file.writelines(books)

"""
Переименование файлов
directory = 'O:\\Документы\\Книги\\ru\\'

for root, dirs, files in os.walk(directory):
    for file in files:
        dst = os.path.join(root, re.sub(r'\d+,\d+\. ', '', file))
        src = os.path.join(root, file)
        os.rename(src, dst)"""