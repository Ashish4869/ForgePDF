import PyPDF2

def decrypt(file,password):#function to the Pdf file decrypt

    #opening the encrypted file and decrypted file in read and write mode respectively
    efile = open(file, 'rb')
    defile= open('decrypted.pdf', 'wb')

    #the reader and writer objects
    pdfReader = PyPDF2.PdfFileReader(efile)
    pdfWriter = PyPDF2.PdfFileWriter()

    #decrypting the Pdf file
    pdfReader.decrypt(password)
    
    #copying the pages from the encrypted file to the writer object
    for pageNo in range(pdfReader.numPages):
        Page = pdfReader.getPage(pageNo)
        pdfWriter.addPage(Page)

    #copying the pages from the writer object to the decrypted file
    pdfWriter.write(defile)

    #saving the changes and closing the files
    efile.close()
    defile.close()

# decrypt('encrypted.pdf','lol')