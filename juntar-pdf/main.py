import PyPDF2, os


DIR_ORIGINAL = './arquivos'
ARQUIVO_FINAL = 'merged.pdf'

pdfs = os.listdir(DIR_ORIGINAL)

# Imprimir os nomes dos arquivos
pdfMerge = PyPDF2.PdfMerger()
for pdf in pdfs:
        if (pdf == '.gitignore'): continue
        pdfFile = open(DIR_ORIGINAL+'/'+pdf, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFile)
        pdfMerge.append(pdfReader)
pdfFile.close()
pdfMerge.write(ARQUIVO_FINAL)