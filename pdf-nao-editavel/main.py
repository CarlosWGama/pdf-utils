#instalar nas variavies de ambiente o poppler
#https://blog.alivate.com.au/poppler-windows/

from pdf2image import convert_from_path 
import os
from PIL import Image

DIR_ORIGINAL = './original'
DIR_FINAL = './final'

pdfs = os.listdir(DIR_ORIGINAL)

# Imprimir os nomes dos arquivos
for pdf in pdfs:
    if (pdf == '.gitignore'): continue
    images = convert_from_path(f'{DIR_ORIGINAL}/{pdf}') 
    im1 = images[0]
    images.pop(0)

    pdf1_filename = DIR_FINAL+"/"+pdf

    im1.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=images)