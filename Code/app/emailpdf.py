from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo, WARNING
from app import login
from app import home
from app.FUNCTIONALITY import emailbot
from app.common import center
import os

class EmailPdfWindow():
    def __init__(self):

        #Variable to hold the attachment and csv address
        attachmentPath = []
        csvAddress = []

        #Button Functions
        def toHomePage():
            # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the login up window class
            home.HomeWindow()

        def btn_clicked():
            print("ButtonClicked")

        
        def getAttachment():
            #gets attachement from user
            attachmentPathvar = filedialog.askopenfilename(initialdir= "D:\\Users\\ashis\\Desktop", title="Select a file" , filetypes=(("Pdf files","*.pdf*"),("all files","*.*")))
            filename = os.path.basename(attachmentPathvar)

            #stores attachement in list
            attachmentPath.append(attachmentPathvar)
            print(attachmentPath)

            #adds the value in the textbox and displays it
            TextBoxAttachmentEntry.insert('0' , 'Attachment : ' + filename)
            TextBoxAttachmentEntry.bind("<Key>", lambda e: "break")
            showAttachment()



        def ImportCSV():
            #gets csv from user
            csvAddressvar = filedialog.askopenfilename(initialdir= "D:\\Users\\ashis\\Desktop", title="Select a file" , filetypes=(("CSV files","*.csv*"),("all files","*.*")))
            filename = os.path.basename(csvAddressvar)

            #stores csv in list
            csvAddress.append(csvAddressvar)
            print(csvAddress)

            #adds the value in the textbox and displays it
            TextBoxCSVEntry.insert('0' , 'CSV File : ' + filename)
            TextBoxCSVEntry.bind("<Key>", lambda e: "break")
            showCSVFile()

        
        def SendEmail():
            toaddress = EmailEntry.get()

            #checks if the attachment is added or not
            if len(attachmentPath) == 0:
                showinfo("ERROR" , "Please choose an attachment")
                return

            #doesntsend email if there is ambiguity
            if toaddress != '' and len(csvAddress) != 0 :
                showinfo("ERROR" , "Please choose any one way for email receipients.")
                EmailEntry.insert('0' , '')
                return

            #sends the email and shows that the email is sent
            showEmailSent()
            #giving priority on the csv emails then the ones typed
            if len(csvAddress) != 0 :
                emailbot.csvToStr(csvAddress[0] , attachmentPath[0])
            else:
                emailbot.emailbot(toaddress , attachmentPath[0])

            
        #shows the the atttachment in the text box
        def showAttachment():
            AddAttachmentButton.pack_forget()
            TextBoxAttachmentEntry.pack()

            TextBoxAttachmentEntry.place(
                 x = 50, y = 584,
            width = 536,
            height = 91)


        #shows thw csv filr selected in a text box
        def showCSVFile():
            CSVFileButton.pack_forget()
            TextBoxCSVEntry.pack()

            TextBoxCSVEntry.place(
            x = 750, y = 377,
            width = 440,
            height = 63)

        #shows message that email is sent
        def showEmailSent():
            SendEmailButton.pack_forget()
            EmailSentLabel.pack()

            EmailSentLabel.place(
            x = 702, y = 584,
            width = 536,
            height = 91)

            




        #Window Config
        window = Tk()

        window.geometry("1280x720")
        window.configure(bg = "#0b132b")
        center(window)


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


        #SendEmail Background image Config
        SendEmailBGImage = PhotoImage(file = f"./images/emailpdf/EmailPdfBG.png")
        SendEmailBG = canvas.create_image(
            640.0, 275.0,
            image=SendEmailBGImage)

        #Add Attachment config
        AddAttachmentImage = PhotoImage(file = f"./images/emailpdf/AddAttachmentBG.png")
        AddAttachmentButton = Button(
            image = AddAttachmentImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            activebackground="#0B132B",
            command = getAttachment,
            relief = "flat")

        AddAttachmentButton.pack()

        AddAttachmentButton.place(
            x = 50, y = 584,
            width = 536,
            height = 91)

        #Send email button config
        SendEmailImage = PhotoImage(file = f"./images/emailpdf/SendEmailBG.png")
        SendEmailButton = Button(
            image = SendEmailImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            activebackground="#0B132B",
            command = SendEmail,
            relief = "flat")

        SendEmailButton.pack()

        SendEmailButton.place(
            x = 702, y = 584,
            width = 536,
            height = 91)


        #back button config
        BackImage = PhotoImage(file = f"./images/emailpdf/Back.png")
        BackButton = Button(
            image = BackImage,
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


        #Import CSV file button config
        CSVFileImage = PhotoImage(file = f"./images/emailpdf/CSVFile.png")
        CSVFileButton = Button(
            image = CSVFileImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            activebackground="#0B132B",
            command = ImportCSV,
            relief = "flat")

        CSVFileButton.pack()

        CSVFileButton.place(
            x = 750, y = 377,
            width = 440,
            height = 63)

        #Email Entry Config
        EmailEntryBGImage = PhotoImage(file = f"./images/emailpdf/EmailEntryBG.png")
        EmailEntryBG = canvas.create_image(
            315.0, 408.5,
            image = EmailEntryBGImage)

        EmailEntry = Entry(
            bd = 0,
            bg = "#1c2541",
            font = 20,
            fg= "#5BC0BE",
            justify=CENTER,
            insertbackground= "#5BC0BE",
            highlightthickness = 0)

        EmailEntry.place(
            x = 95, y = 377,
            width = 440,
            height = 61)



        # Text Box for Attachment
        TextBoxAttachmentImage = PhotoImage(file = f"./images/emailpdf/TextboxBG.png")
        TextBoxAttachment = canvas.create_image(
            1124.5, 605.5,
            image = TextBoxAttachmentImage)

        TextBoxAttachmentEntry = Entry(
            bd = 0,
            bg = "#0B132B",
            font = 20,
            fg= "#5BC0BE",
            justify=CENTER,
            insertbackground= "#0B132B",
            highlightthickness = 0)

        TextBoxAttachmentEntry.pack()
        TextBoxAttachmentEntry.pack_forget()

       


        #Text Box for CSV File
        TextBoxCSVImage = PhotoImage(file = f"./images/emailpdf/TextboxBG.png")
        TextBoxCSV = canvas.create_image(
            1124.5, 605.5,
            image = TextBoxCSVImage)

        TextBoxCSVEntry = Entry(
            bd = 0,
            bg = "#0B132B",
            font = 20,
            fg= "#5BC0BE",
            justify=CENTER,
            insertbackground= "#0B132B",
            highlightthickness = 0)

        TextBoxCSVEntry.pack()
        TextBoxCSVEntry.pack_forget()

        #EmailSent Config
        EmailSentImage = PhotoImage(file = f"./images/emailpdf/Emailsent.png")
        EmailSent = canvas.create_image(
            1124.5, 605.5,
            image = TextBoxCSVImage)

        EmailSentLabel = Label(
            image = EmailSentImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#1C2541",
            activebackground="#1C2541",
            relief = "flat")

        EmailSentLabel.pack()
        EmailSentLabel.pack_forget()



      

        #Additional window config
        window.resizable(False, False)
        window.mainloop()
