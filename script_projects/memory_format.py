import docx
import re
import os

file = r'C:\Users\crisc\Desktop\Сценарий.docx'
direct = os.path.dirname(file)


def get_text(filename):
    doc = docx.Document(filename)
    return '\n'.join([p.text for p in doc.paragraphs])


txt_full = get_text(file)
paragraphs = txt_full.split('\n')
words = []
for paragraph in paragraphs:
    words.append(paragraph.split())
print(words)

first_letters = []

for paragraph in paragraphs:
    words = paragraph.split()
    for word in words:
        first_letters.append(word[0].upper() + ' ')
        if re.findall(r'\W', word[-1]):
            first_letters.append(word[-1] + ' ')
    first_letters[-1] += '\n'

txt = ''
for index, character in enumerate(first_letters):
    if index < len(first_letters)-1 and re.findall(r'\W', character[0]) and character == first_letters[index + 1]:
        print(character)
        continue
    txt += character
for paragraph in paragraphs:
    words = paragraph.split()
    if len(words) > 3:
        for i in range(3):
            txt += words[i] + ' '
        txt += '\n'

with open(os.path.join(direct, "first_letters.txt"), "w", encoding='utf-8') as file:
    file.write(txt)
