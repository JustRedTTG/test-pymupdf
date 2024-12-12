import fitz, os

pdf = fitz.open('test.pdf', filetype='pdf')

pdf_page = pdf[0]

pixmap = pdf_page.get_pixmap()
pixmap.save('test.png')

if not os.path.exists('test.png'):
    raise Exception("Image wasn't created")