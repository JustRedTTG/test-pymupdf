import fitz
from fitz import Pixmap

pdf = fitz.open('test.pdf', filetype='pdf')

pdf_page = pdf[0]

pixmap: Pixmap = pdf_page.get_pixmap()
pixmap.save('test.png')
