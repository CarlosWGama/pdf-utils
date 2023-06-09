#pip install aspose-words
from docx2pdf import convert
import os


DIR_ORIGINAL = './original'
DIR_FINAL = './final'

convert(DIR_ORIGINAL, DIR_FINAL)

# docs = os.listdir(DIR_ORIGINAL)

# # Imprimir os nomes dos arquivos
# for doc in docs:
#     if (doc == '.gitignore'): continue

#     #Cria o nome do arquivo
#     pdf = doc.split('.')
#     pdf = pdf[:-1]
#     pdf = ' '.join(pdf) + '.pdf'

#     #Recupera e salva como pdf
#     convert(DIR_ORIGINAL+'/'+doc, DIR_FINAL+'/'+pdf)