import PyPDF2
from io import StringIO
import re

file = open('Diario_J_TST_new.pdf', 'rb')
read_file = PyPDF2.PdfFileReader(file)
pages = read_file.numPages
search_text = 'perícia médica'
search_text_from = 'Processo Nº'
search_text_from = r'^Processo Nº.*[0-9]$'
which_not_search = r'Processo Nº.*66$'
f = open('dummy.txy', 'w')
for i in range(pages):
    
    page = read_file.getPage(i)
    
    data = page.extractText()
# print(data)
# li = []
# if search_text_from in data:
#     li.append(search_text)

# print(li)
    # for line in StringIO(data):
    #     # print(line)
    #     if re.match(search_text_from, line):
            
    #         f.write(line)
            # print(line, i+1)

print(re.match(r'^Processo.*Processo$', read_file.getPage(75).extractText()))
