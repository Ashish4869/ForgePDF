from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo, WARNING
from app.Functionality import splitter
from app import login
from app import home
from app.User import userDetails
import os
from app.common import center

class SplitPdfWIndow():
    def __init__(self):


        #Variable to hold the address of the pdf to be split
        PdfToSplit = []

        #Button Functions
        def toHomePage():
            #makes the selectpdf false so that we can start fresh
            userDetails.NotSelectPdfBool()
            # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the login up window class
            home.HomeWindow()

        def btn_clicked():
            print("ButtonClicked")
        

        #gets the pdf the split
        def getPdf():
            if len(PdfToSplit) != 0:
                showinfo("ERROR" , "You can split only one pdf at a time")
                return

            #gets attachement from user
            attachmentPathvar = filedialog.askopenfilename(initialdir= "D:\\Users\\ashis\\Desktop", title="Select a file" , filetypes=(("Pdf files","*.pdf*"),("all files","*.*")))
            filename = os.path.basename(attachmentPathvar)
            
            #stores attachement in list
            PdfToSplit.append(attachmentPathvar)

            #adds the value in the textbox and displays it
            PDFTextBoxEntry.insert('0' , filename)
            PDFTextBoxEntry.bind("<Key>", lambda e: "break")
            showSplitPdf()


        #checks the condition and splits the pdf
        def SplitPdf():
            startRange = int(StartingRange.get())
            endRange = int(EndingRange.get())
            
            #if starting range is greater than endingrange
            if(startRange > endRange):
                showinfo("ERROR" , "Starting range cannt be greater than ending range!!")
                return

            showPdfSplitMessage()

            splitter.spliter(startRange , endRange , PdfToSplit[0])

       
        #shows the selected pdf along with the name
        def showSplitPdf():
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

            #if case we have routed from options page , then make neccessary arrangments
            if userDetails.GetselectedPdfBool() == True:
                PDFTextBoxEntry.insert('0' , os.path.basename(userDetails.getSelectPdf()))
                PDFTextBoxEntry.bind("<Key>", lambda e: "break")

                PdfToSplit.append(userDetails.getSelectPdf())



        #shows the message that pdf is split
        def showPdfSplitMessage():
            SplitPdfSubmitButton.pack_forget()
            PdfSplitLabel.pack()

            PdfSplitLabel.place(
            x = 1022, y = 604,
            width = 206,
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


        #SplitPdf  background Config
        splitpdfBGImage = PhotoImage(file =  f"./images/splitpdf/splitpdfBG.png")
        splitpdfBG = canvas.create_image(
            640.0, 360.0,
            image=splitpdfBGImage)


        #ChooseFile BG
        ChooseFileImage = PhotoImage(file = f"./images/splitpdf/ChooseFile.png")
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
        BackButtonImage = PhotoImage(file = f"./images/splitpdf/BackButton.png")
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


        #Split pdf button config
        SplitPdfImage = PhotoImage(file = f"./images/splitpdf/SplitPdf.png")
        SplitPdfSubmitButton = Button(
            image = SplitPdfImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#1C2541",
            activebackground="#1C2541",
            command = SplitPdf,
            relief = "flat")

        SplitPdfSubmitButton.place(
            x = 1022, y = 604,
            width = 206,
            height = 46)



        #Starting Range Entry Config
        StartingRangeEntryImage = PhotoImage(file = f"./images/splitpdf/TextBox1.png")
        StartingRangeEntryButton = canvas.create_image(
            1124.5, 337.0,
            image = StartingRangeEntryImage)

        StartingRange = Entry(
            bd = 0,
            bg = "#0b132b",
            font = 20,
            fg= "#5BC0BE",
            justify=CENTER,
            insertbackground= "#5BC0BE",
            highlightthickness = 0)

        StartingRange.place(
            x = 1033, y = 304,
            width = 183,
            height = 64)

        #Ending Range Entry Config
        EndingRangeEntryImage = PhotoImage(file = f"./images/splitpdf/TextBox2.png")
        EndingRangeEntry = canvas.create_image(
            1122.5, 487.0,
            image = EndingRangeEntryImage)

        EndingRange = Entry(
            bd = 0,
            bg = "#0b132b",
            font = 20,
            fg= "#5BC0BE",
            justify=CENTER,
            insertbackground= "#5BC0BE",
            highlightthickness = 0)

        EndingRange.place(
            x = 1031, y = 454,
            width = 183,
            height = 64)

        
        #PdfTextBox
        PDFTextBoxImage = PhotoImage(file = f"./images/splitpdf/TextBoxBG.png")
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
        PdfSplitImage = PhotoImage(file = f"./images/splitpdf/PdfSplit.png")
        PdfSplitLabel = Label(
            image = PdfSplitImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#1C2541",
            relief = "flat")

        PdfSplitLabel.pack()
        PdfSplitLabel.pack_forget()



        #PdfImage Config
        PdfImage = PhotoImage(file = f"./images/splitpdf/pdfImage.png")
        PdfImageIcon = Label(
            image = PdfImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            relief = "flat")

        PdfImageIcon.pack()
        PdfImageIcon.pack_forget()

        #if we have routed from options page then set the pdf to be split
        if userDetails.GetselectedPdfBool() == True:
            showSplitPdf()


        window.resizable(False, False)
        window.mainloop()
