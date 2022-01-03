from tkinter import *
from tkinter import filedialog
from app import home
from app.common import center
import os

class encryptWindow():
    def __init__(self):


        #Button Functions
        def toHomePage():
            # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the login up window class
            home.HomeWindow()
        

        #gets the pdf to encrypt
        def getPdf():

            #gets attachement from user
            attachmentPathvar = filedialog.askopenfilename(initialdir= "D:\\Users\\ashis\\Desktop", title="Select a file" , filetypes=(("Pdf files","*.pdf*"),("all files","*.*")))
            filename = os.path.basename(attachmentPathvar)

            #adds the value in the textbox and displays it
            PDFTextBoxEntry.insert('0' , filename)
            PDFTextBoxEntry.bind("<Key>", lambda e: "break")
            showEncryptPdf()


        # function to encrypt the pdf
        def EncryptPdf():
            # TODO: encrypt the pdf
            # TODO: Input validation
            showPdfEncryptMessage()

       
        #shows the selected pdf along with the name
        def showEncryptPdf():
            PDFTextBoxEntry.pack()

            PDFTextBoxEntry.place(
            x = 100, y = 600,
            width = 800,
            height = 87)

            PdfImageIcon.pack()

            PdfImageIcon.place(
            x = 100, y = 525,
            width = 800,
            height = 87)


        #shows the message that pdf is encypted
        def showPdfEncryptMessage():
            EncryptPdfSubmitButton.pack_forget()
            PdfEncryptLabel.pack()

            PdfEncryptLabel.place(
            x = 1012, y = 604,
            width = 230,
            height = 46)



        window = Tk()

        #Window Config
        window.geometry("1280x720")
        center(window)
        window.configure(bg = "#0b132b")



        #Canvas Config
        canvas = Canvas(
            window,
            bg = "#0b132b",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)


        #EncryptPdf  background Config
        encryptpdfBGImage = PhotoImage(file =  f"./images/encryptpdf/encryptpdfBG.png")
        encryptpdfBG = canvas.create_image(
            640.0, 360.0,
            image=encryptpdfBGImage)


        #ChooseFile BG
        ChooseFileImage = PhotoImage(file = f"./images/encryptpdf/ChooseFile.png")
        ChooseFileButton = Button(
            image = ChooseFileImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            activebackground="#0B132B",
            command = getPdf,
            relief = "flat")

        ChooseFileButton.place(
            x = 243, y = 344,
            width = 536,
            height = 100)



        #BackButton Config
        BackButtonImage = PhotoImage(file = f"./images/encryptpdf/BackButton.png")
        BackButton = Button(
            image = BackButtonImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#1C2541",
            activebackground="#1C2541",
            command = toHomePage,
            relief = "flat")

        BackButton.place(
            x = 17, y = 21,
            width = 139,
            height = 58)


        #Encrypt pdf button config
        EncryptPdfImage = PhotoImage(file = f"./images/encryptpdf/Encrypt.png")
        EncryptPdfSubmitButton = Button(
            image = EncryptPdfImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#1C2541",
            activebackground="#1C2541",
            command = EncryptPdf,
            relief = "flat")

        EncryptPdfSubmitButton.place(
            x = 1022, y = 604,
            width = 206,
            height = 46)



        

        #Ending Range Entry Config
        passwordEntryImage = PhotoImage(file = f"./images/encryptpdf/TextBox.png")
        PasswordEntryCanvasImage = canvas.create_image(
            1124.0, 443.0,
            image = passwordEntryImage)

        PasswordEntry = Entry(
            bd = 0,
            bg = "#0b132b",
            font = 20,
            fg= "#5BC0BE",
            justify=CENTER,
            insertbackground= "#5BC0BE",
            highlightthickness = 0)

        PasswordEntry.place(
            x = 987, y = 410,
            width = 274,
            height = 66)

        
        #PdfTextBox
        PDFTextBoxImage = PhotoImage(file = f"./images/encryptpdf/TextboxBG.png")
        PDFTextBox = canvas.create_image(
            1124.5, 605.5,
            image = PDFTextBoxImage)

        PDFTextBoxEntry = Entry(
            bd = 0,
            bg = "#0B132B",
            font = 20,
            fg= "#5BC0BE",
            justify=CENTER,
            insertbackground= "#0B132B",
            highlightthickness = 0)

        PDFTextBoxEntry.pack()
        PDFTextBoxEntry.pack_forget()


        #PdfMerged Message
        PdfEncryptImage = PhotoImage(file = f"./images/encryptpdf/Encrypted.png")
        PdfEncryptLabel = Label(
            image = PdfEncryptImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#1C2541",
            relief = "flat")

        PdfEncryptLabel.pack()
        PdfEncryptLabel.pack_forget()



        #PdfImage Config
        PdfImage = PhotoImage(file = f"./images/encryptpdf/pdfImage.png")
        PdfImageIcon = Label(
            image = PdfImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            relief = "flat")

        PdfImageIcon.pack()
        PdfImageIcon.pack_forget()


        window.resizable(False, False)
        window.mainloop()