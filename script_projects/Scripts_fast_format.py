import docx
import re
import os

file = r'O:\Affirmations\Scenarios\0. No more mr nice guy\Robert_Glover_-_No_More_Mr_Nice_Guy_id353324692_size612.docx'
direct = os.path.dirname(file)


def get_text(filename):
    doc = docx.Document(filename)
    return '\n'.join([p.text for p in doc.paragraphs])


txt = get_text(file)
list_start = txt.split('\n')
txt = re.sub(r"\d", "", txt)
txt = re.sub(r"\W+\n", "\n", txt)
txt = re.sub(r"\n\W+", "\n", txt)
txt = re.sub(r"^\W+|\W+$", "", txt)
txt = re.sub(r"\n", ".\n", txt)
txt = re.sub(r"$", "..", txt)
list_end = txt.split('\n')
if len(list_start) != len(list_end):
    print('error', len(list_start), len(list_end))
with open(os.path.join(direct, "003 Google.txt"), "w", encoding='utf-8') as file:
    file.write(txt)
