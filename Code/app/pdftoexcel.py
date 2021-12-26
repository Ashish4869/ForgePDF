from tkinter import *
from app import login
from app import home
from app.common import center

class PdfToExcelWindow():
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

        #Creating a Canvas
        canvas = Canvas(
            window,
            bg = "#0b132b",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        #background Config
        PdfToExcelBGImage = PhotoImage(file = f"./images/pdftoexcel/pdftoexcelBG.png")
        PdfToExcelBG = canvas.create_image(
            640.0, 134.0,
            image=PdfToExcelBGImage)


        #Choose File Config
        ChooseFileImage = PhotoImage(file = f"./images/pdftoexcel/ChooseFile.png")
        ChooseFileButton = Button(
            image = ChooseFileImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            activebackground="#0B132B",
            command = btn_clicked,
            relief = "flat")

        ChooseFileButton.place(
            x = 372, y = 336,
            width = 536,
            height = 100)



        #BackImage config
        BackImage = PhotoImage(file = f"./images/pdftoexcel/Back.png")
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

        window.resizable(False, False)
        window.mainloop()
