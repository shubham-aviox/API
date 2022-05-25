import PyPDF2
import textract
import re

file = open('Diario_J_TST.pdf', 'rb')
read_file = PyPDF2.PdfFileReader(file)
# print(read_file.getDocumentInfo())
total_pages = read_file.numPages

text_page1 = read_file.getPage(0).extractText()
# print(text_page1)

txt_file = open('txt_pdf.txt', 'a')
for i in range(0, total_pages):
	# word = re.findall('perícia', read_file.getPage(i).extractText())
	# if word:
	# 	print(word, i+1)
	ext_text = read_file.getPage(i).extractText()
	# print(i+1)

	results = re.findall(r'([P]rocesso.*)(.*?)([P]rocesso.*)', ext_text, re.DOTALL)
	for x, data in enumerate(results):
		# search_count = '\nsearch:' + ' ' + str(x) + '>>>>>>>>>>>>\n\n'
		# txt_file.write(search_count)
		# txt_file.write(data)
		search = ''
		for y, i in enumerate(data):
			search = i
			if 'perícia médica' in search or 'perícia\nmédica' in search:
				if 'Complemento' in search:
					res = re.findall(r'Complemento(.*?)Relator', search, re.DOTALL)
					# Complemento = res
					# print('Complemento', Complemento)
				if 'Relator' in search:
					res = re.findall(r'Relator(.*?)Embargante|Agravante(s)', search, re.DOTALL)
					Relator = res
					print('Relator', Relator)
				# print('search\n', search)