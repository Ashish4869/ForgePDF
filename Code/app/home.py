from tkinter import *
from app import login, pdftoword,pdftoexcel,exceltopdf,wordtopdf,splitPdf,Scrapy,emailpdf
from app.common import center

class HomeWindow():
    def __init__(self):
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

        #Testing conditional rendering
        def showfile1():
            File1Button.pack()

            File1Button.place(
            x = 1057, y = 207,
            width = 156,
            height = 132)
            


        

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
            command = showfile1,
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
            command = btn_clicked,
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

        # Image for most recent file in database
        File1Image = PhotoImage(file = f"./images/home/File1.png")
        
        # file1 button config
        File1Button = Button(
            image = File1Image,
            borderwidth = 0,
            highlightthickness = 0,
            background="#1C2541",
            activebackground="#1C2541",
            command = btn_clicked,
            relief = "flat")

        # file1 button placement
        File1Button.place(
            x = 1057, y = 207,
            width = 156,
            height = 132)

        #Putting the Element in pack and then immeadiatley hiding it 
        File1Button.pack()
        File1Button.pack_forget()

        # Image for second most recent file in database
        File2Image = PhotoImage(file = f"./images/home/File2.png")
        
        # File2 button config
        File2Button = Button(
            image = File2Image,
            borderwidth = 0,
            highlightthickness = 0,
            background="#1C2541",
            activebackground="#1C2541",
            command = btn_clicked,
            relief = "flat")

        # file2 button placement
        File2Button.place(
            x = 1057, y = 373,
            width = 156,
            height = 132)

        # Image for third most recent file in database
        File3Image = PhotoImage(file = f"./images/home/File3.png")
        
        # File3 button config
        File3Button = Button(
            image = File3Image,
            borderwidth = 0,
            highlightthickness = 0,
            background="#1C2541",
            activebackground="#1C2541",
            command = btn_clicked,
            relief = "flat")

        # file3 button placement
        File3Button.place(
            x = 1057, y = 539,
            width = 156,
            height = 132)

        window.resizable(False, False)
        window.mainloop()
    