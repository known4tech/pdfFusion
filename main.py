import PyPDF2

# Officially Created by Yatin Kumar (With the help of Google :-) )

pdfFiles = ["1.pdf", "2.pdf", "n.pdf"]
merger = PyPDF2.PdfMerger()

for filename in pdfFiles:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)  # Use PdfReader instead of PdfFileReader
    merger.append(pdfReader)
    pdfFile.close()

with open('merged.pdf', 'wb') as merged_pdf:
    merger.write(merged_pdf)