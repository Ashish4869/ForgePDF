from tkinter import *
from app import login
from app import home
from app.common import center

class SplitPdfWIndow():
    def __init__(self):
        #Button Functions
        def toHomePage():
            # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the login up window class
            home.HomeWindow()

        def btn_clicked():
            print("ButtonClicked")

        window = Tk()

        #Window Config
        window.geometry("1280x720")
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
            command = btn_clicked,
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
            command = btn_clicked,
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

        window.resizable(False, False)
        window.mainloop()
