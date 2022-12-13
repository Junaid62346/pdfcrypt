from PyPDF2 import PdfFileWriter, PdfFileReader
from getpass import getpass

pdfwriter = PdfFileWriter()
pdfreader = PdfFileReader("english-for-it-specialists.pdf")

for page in range(pdfreader.numPages):
    pdfwriter.add_page(pdfreader.pages[page])

password = getpass(prompt="Введите пароль: ")
pdfwriter.encrypt(password)

with open("protected.pdf", "wb") as file:
    pdfwriter.write(file)
