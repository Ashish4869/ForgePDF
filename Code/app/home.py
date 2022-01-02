from tkinter import *
from tkinter import filedialog
import mysql.connector
from app import login, pdftoword,pdftoexcel,exceltopdf,wordtopdf,splitPdf,Scrapy,emailpdf,mergepdf,savedpdfs
from app.User import userDetails
from app.common import center
import os

class HomeWindow():
    def __init__(self):

        #variables that holds current UID
        uid = []

        #Button Functions
        def toLoginPage():
            # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the login up window class
            login.LogInWindow()

        def btn_clicked():
            print("ButtonClicked")

        def toPdfToWordPage():
             # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the pdf to word window class
            pdftoword.PdfToWordWindow()

        def toPdfToExcelPage():
             # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the pdf to excel window class
            pdftoexcel.PdfToExcelWindow()

        def toExcelToPdfPage():
             # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the excel to pdf window class
            exceltopdf.ExcelToPdfWindow()

        def toWordToPdfPage():
             # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the excel to pdf window class
            wordtopdf.WordToPdfWindow()

        def toSplitPdf():
             # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the splitPdf window class
            splitPdf.SplitPdfWIndow()

        def toScrapy():
             # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the scrapy window class
            Scrapy.ScrapyWindow()

        def toEmailPdf():
            # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the email pdf window class
            emailpdf.EmailPdfWindow()

        def toMergerPdf():
            # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the email pdf window class
            mergepdf.MergePdfWindow()

        def toSavedPdfs():
            # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the saved pdf window class
            savedpdfs.SavedPdfWindow()
            

        #Testing conditional rendering and file open
        # def showfile1():
        #     filename = filedialog.askopenfilename(initialdir= "D:\\Users\\ashis\\Desktop", title="Select a file" , filetypes=(("Pdf files","*.pdf*"),("all files","*.*")))
        #     print(filename)

        #     File1Button.pack()

        #     File1Button.place(
        #     x = 1057, y = 207,
        #     width = 156,
        #     height = 132)
            


        

        # Window config
        window = Tk()
        window.geometry("1280x720")
        window.title('Home Page')
        center(window)
        window.configure(bg = "#0b132b")

        # Creating a Canvas
        canvas = Canvas(
            window,
            bg = "#0b132b",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)


        # Adding the background
        background_img = PhotoImage(file = f"./images/home/HomeBG.png")
        background = canvas.create_image(
            640.0, 360.0,
            image=background_img)

        # Image for Log Out
        LogOutImage = PhotoImage(file = f"./images/home/LogOut.png")
        
        # Log Out button config
        LogOutButton = Button(
            image = LogOutImage,
            borderwidth = 0,
            highlightthickness = 0,
            activebackground= "#1C2541",
            command = toLoginPage,
            relief = "flat")

        # Logout button placement
        LogOutButton.place(
            x = 22, y = 29,
            width = 131,
            height = 48)

        # Image for Pdf to word
        PdfToWordImage = PhotoImage(file = f"./images/home/PdfToWord.png")
        
        # Pdf to word button config
        PdfToWordButton = Button(
            image = PdfToWordImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            activebackground="#0B132B",
            command = toPdfToWordPage,
            relief = "flat")


        # Pdf to word button placement
        PdfToWordButton.place(
            x = 140, y = 174,
            width = 159,
            height = 129)

        # Image for Pdf to excel
        PdfToExcelImage = PhotoImage(file = f"./images/home/PDFToExcel.png")
        
        # Pdf to excel button config
        PdfToExcelButton = Button(
            image = PdfToExcelImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            activebackground="#0B132B",
            command = toPdfToExcelPage,
            relief = "flat")

        # Pdf to excel button placement
        PdfToExcelButton.place(
            x = 424, y = 174,
            width = 159,
            height = 129)


        # Image for Scrap
        ScrapyImage = PhotoImage(file = f"./images/home/ScrapyImage.png")
        
        # Scrap button config
        ScrapyButton = Button(
            image = ScrapyImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            activebackground="#0B132B",
            command = toScrapy,
            relief = "flat")


        # Scrap button placement
        ScrapyButton.place(
            x = 710, y = 518,
            width = 158,
            height = 130)


        # Image for MergePdf
        MergePdfImage = PhotoImage(file = f"./images/home/MergePdf.png")
        
        # Merge Pdf button config
        MergePdfButton = Button(
            image = MergePdfImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            activebackground="#0B132B",
            command = toMergerPdf,
            relief = "flat")

        # MergePdf button placement
        MergePdfButton.place(
            x = 709, y = 346,
            width = 159,
            height = 129)


        # Image for SplitPDf
        SplitPdfImage = PhotoImage(file = f"./images/home/SplitPdf.png")
        
        # Split Pdf button config
        SplitPdfButton = Button(
            image = SplitPdfImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            activebackground="#0B132B",
            command = toSplitPdf,
            relief = "flat")

        # Split pdf  button placement
        SplitPdfButton.place(
            x = 709, y = 174,
            width = 160,
            height = 129)


        # Image for SavedPdf
        SavedPdfsImage = PhotoImage(file = f"./images/home/SavedPDF.png")
       
        # Saved Pdf button config
        SavedPdfsButton = Button(
            image = SavedPdfsImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            activebackground="#0B132B",
            command = toSavedPdfs,
            relief = "flat")


        # saved pdf button placement
        SavedPdfsButton.place(
            x = 424, y = 519,
            width = 159,
            height = 130)


        # Image for Email PDf
        EmailPdfImage = PhotoImage(file = f"./images/home/EmailPdf.png")
        
        # Email button config
        EmailPdfButton = Button(
            image = EmailPdfImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            activebackground="#0B132B",
            command = toEmailPdf,
            relief = "flat")


        # email pdf button placement
        EmailPdfButton.place(
            x = 142, y = 519,
            width = 158,
            height = 130)

        # Image for Word to pdf
        WordToPdfImage = PhotoImage(file = f"./images/home/WordToPdf.png")
        
        # word to pdf button config
        WordToPdfButton = Button(
            image = WordToPdfImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            activebackground="#0B132B",
            command = toWordToPdfPage,
            relief = "flat")


        # word to pdf button placement
        WordToPdfButton.place(
            x = 140, y = 346,
            width = 160,
            height = 130)

        # Image for Excel to pdf
        ExcelToPdfImage = PhotoImage(file = f"./images/home/ExcelToPdf.png")
        
        # Excel to pdf button config
        ExcelToPdfButton = Button(
            image = ExcelToPdfImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            activebackground="#0B132B",
            command = toExcelToPdfPage,
            relief = "flat")


        # excel to pdf button placement
        ExcelToPdfButton.place(
            x = 424, y = 346,
            width = 159,
            height = 130)


        uid.append(userDetails.getUID())
        
        # creating a mysql connection
        mydb = mysql.connector.connect(host=os.getenv('HOST'), user=os.getenv('USER'), password=os.getenv('PASSWORD'), database="forgepdf")
        mycursor = mydb.cursor()
        # getting all the user data from the database
        mycursor.execute("select file_address from files where user_id='" + str(uid[0]) + "' order by file_id desc")
        # selecting only the first row from the fetched data
        result = mycursor.fetchall()
        print(result)







        if len(result) > 0:
        # # Image for most recent Pdf in database
            Pdf1IconImage = PhotoImage(file = f"./images/home/Pdf1Icon.png")
        
            Pdf1IconLabel = Button(
                image = Pdf1IconImage,
                borderwidth = 0,
                highlightthickness = 0,
                background="#1C2541",
                activebackground="#1C2541",
                command = btn_clicked,
                relief = "flat")


            Pdf1IconLabel.place(
                x = 1057, y = 540,
                width = 156,
                height = 126)

            
            #PDF1 name box
            Pdf1TextBoxImage = PhotoImage(file = f"./images/home/TextBox1.png")
            Pdf1TextBox = canvas.create_image(
                1135.0, 648.0,
                image = Pdf1TextBoxImage)

            Pdf1Entry = Entry(
                bd = 0,
                bg = "#1c2541",
                font = 20,
                fg= "#5BC0BE",
                justify=CENTER,
                insertbackground= "#1C2541",
                highlightthickness = 0)

            Pdf1Entry.place(
                x = 1057, y = 633,
                width = 156,
                height = 28)

            Pdf1Entry.insert('0' , os.path.basename(result[0][0]))
            Pdf1Entry.bind("<Key>", lambda e: "break")

        
        if len(result) > 1:
        # # Image for 2nd most recent Pdf in database
            Pdf2IconImage = PhotoImage(file = f"./images/home/Pdf2Icon.png")
            
            Pdf2IconLabel = Button(
                image = Pdf2IconImage,
                borderwidth = 0,
                highlightthickness = 0,
                background="#1C2541",
                activebackground="#1C2541",
                command = btn_clicked,
                relief = "flat")

            Pdf2IconLabel.place(
                x = 1057, y = 374,
                width = 156,
                height = 126)

            #PDF2 name box
            Pdf2TextBoxImage = PhotoImage(file = f"./images/home/TextBox2.png")
            Pdf2TextBox = canvas.create_image(
                1135.0, 648.0,
                image = Pdf2TextBoxImage)

            Pdf2Entry = Entry(
                bd = 0,
                bg = "#1c2541",
                font = 20,
                fg= "#5BC0BE",
                justify=CENTER,
                insertbackground= "#1C2541",
                highlightthickness = 0)

            Pdf2Entry.place(
                x = 1057, y = 467,
                width = 156,
                height = 28)

            Pdf2Entry.insert('0' , os.path.basename(result[1][0]))
            Pdf2Entry.bind("<Key>", lambda e: "break")

            

        if len(result) > 2:
        # # Image for 3rd most recent Pdf in database
            Pdf3IconImage = PhotoImage(file = f"./images/home/Pdf3Icon.png")
            
            Pdf3IconLabel = Button(
                image = Pdf3IconImage,
                borderwidth = 0,
                highlightthickness = 0,
                background="#1C2541",
                activebackground="#1C2541",
                command = btn_clicked,
                relief = "flat")


            Pdf3IconLabel.place(
                x = 1057, y = 208,
                width = 156,
                height = 126)

            #PDF3 name box
            Pdf3TextBoxImage = PhotoImage(file = f"./images/home/TextBox3.png")
            Pdf2TextBox = canvas.create_image(
                1135.0, 648.0,
                image = Pdf3TextBoxImage)

            Pdf3Entry = Entry(
                bd = 0,
                bg = "#1c2541",
                font = 20,
                fg= "#5BC0BE",
                justify=CENTER,
                insertbackground= "#1C2541",
                highlightthickness = 0)

            Pdf3Entry.place(
                x = 1057, y = 301,
                width = 156,
                height = 28)

            Pdf3Entry.insert('0' , os.path.basename(result[2][0]))
            Pdf3Entry.bind("<Key>", lambda e: "break")



        if len(result) == 0:
            # Image for 3rd most recent Pdf in database
            NotFoundImage = PhotoImage(file = f"./images/home/notFound.png")
            
            NotFoundLabel = Button(
                image = NotFoundImage,
                borderwidth = 0,
                highlightthickness = 0,
                background="#1C2541",
                activebackground="#1C2541",
                command = btn_clicked,
                relief = "flat")


            NotFoundLabel.place(
                x = 1042, y = 250,
                width = 176,
                height = 231)

        

        window.resizable(False, False)
        window.mainloop()
    