import PyPDF2

# encryt function


def encrypt(file_name, password):
    openFile = open(file_name, 'rb')
    pdfReader = PyPDF2.PdfFileReader(openFile)
    pdfWriter = PyPDF2.PdfFileWriter()
    for page in range(pdfReader.numPages):
        newPage = pdfReader.getPage(page)
        pdfWriter.addPage(newPage)
    pdfWriter.encrypt(password)
    outFile = open("encrypted.pdf", "wb")
    pdfWriter.write(outFile)
    openFile.close()
    outFile.close()


#encrypt('mod1.pdf', 'test123')
