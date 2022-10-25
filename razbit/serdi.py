from  PyPDF2 import PdfFileWriter, PdfFileReader
 
input_PDF = PdfFileReader(open('1.pdf', 'rb'))
 
for i in range(input_PDF.getNumPages()):
    output = PdfFileWriter()    
    new_File_PDF = input_PDF.getPage(i)
    output.addPage(new_File_PDF)
    output_Name_File = "serdi"+str(i+1)+".pdf"
    outputStream = open(output_Name_File, 'wb')
    output.write(outputStream)
    outputStream.close()
