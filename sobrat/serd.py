from PyPDF2 import PdfFileMerger


pdfs = []

t=1
for i in range(13):
    f=str(t)+".pdf"
    pdfs.append(f)
    t=t+1
print(pdfs)
merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
