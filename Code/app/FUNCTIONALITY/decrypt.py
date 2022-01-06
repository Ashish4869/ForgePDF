import PyPDF2

def decrypt(file,password):#function to the Pdf file decrypt

    #opening the encrypted file and decrypted file in read and write mode respectively
    efile = open(file, 'rb')
    defile= open('decrypted.pdf', 'wb')

    #the reader and writer objects
    pdfReader = PyPDF2.PdfFileReader(efile)
    pdfWriter = PyPDF2.PdfFileWriter()

    #decrypting the Pdf file and storing the condition
    # the condition is 1 if the password is correct
    # and 0 if the password is incorrect
    # also, if it's 0 it creates a corrupted file which needs to be blocked
    condition = pdfReader.decrypt(password)
    # here we control that condition
    if condition == 0:
        efile.close()
        defile.close()
        return False
    
    
    #copying the pages from the encrypted file to the writer object
    for pageNo in range(pdfReader.numPages):
        Page = pdfReader.getPage(pageNo)
        pdfWriter.addPage(Page)

    #copying the pages from the writer object to the decrypted file
    pdfWriter.write(defile)

    #saving the changes and closing the files
    efile.close()
    defile.close()

    # returning true if the pdf was succesfully decrypted
    return True
