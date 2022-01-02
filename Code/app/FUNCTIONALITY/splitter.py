import PyPDF2,os.path   

def spliter(start,end, file):# funtion to split


    #opening the input and output pdf files
    pdfFile=open(file,'rb')
    outputFile=open('output.pdf','wb')
  
    #creating the pdfreader and pdfwriter objects to read and write from and to pdf files
    pdfReader=PyPDF2.PdfFileReader(pdfFile)
    pdfWriter=PyPDF2.PdfFileWriter()

    #adding pages to the pdfwriter object
    for pageNo in range(start-1,end):
          page = pdfReader.getPage(pageNo)
          pdfWriter.addPage(page)

    #writing the pages stored in pdfwriter to output pdf
    pdfWriter.write(outputFile)      

    #closing the pdfs 
    outputFile.close()
    pdfFile.close()

# spliter(100,200, 'C:/Users/User/Desktop/Automate_the_Boring_Stuff_with_Python_Practical_Programming_for.pdf')