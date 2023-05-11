from pdfminer.high_level import extract_text

input_pdf = input('pdf: ')
text = extract_text(input_pdf)
count = len(text.encode('utf-8'))
print(count)