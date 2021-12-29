from tkinter import *
from app import login
from app import home
from app.common import center

class EmailPdfWindow():
    def __init__(self):
        #Button Functions
        def toHomePage():
            # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the login up window class
            home.HomeWindow()

        def btn_clicked():
            print("ButtonClicked")


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
            command = btn_clicked,
            relief = "flat")

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
            command = btn_clicked,
            relief = "flat")

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
            command = btn_clicked,
            relief = "flat")

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

        #Additional window config
        window.resizable(False, False)
        window.mainloop()
