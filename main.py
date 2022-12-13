from PyPDF2 import PdfFileWriter, PdfFileReader
from getpass import getpass

pdfwriter = PdfFileWriter()
pdfreader = PdfFileReader("название файла.pdf")

for page in range(pdfreader.numPages):
    pdfwriter.add_page(pdfreader.pages[page])

password = getpass(prompt="Введите пароль: ")
pdfwriter.encrypt(password)

with open("название зашифрованного файла.pdf", "wb") as file:
    pdfwriter.write(file)
