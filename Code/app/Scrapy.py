from tkinter import *
from app import login
from app import home
from app.common import center

class ScrapyWindow  ():
    def __init__(self):
        #Button Functions
        def toHomePage():
            # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the login up window class
            home.HomeWindow()

        def btn_clicked():
            print("ButtonClicked")


        #Window config
        window = Tk()

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



        #Scrapy Background config
        ScrapyBGImage = PhotoImage(file = f"./images/Scrapy/ScrapyBG.png")
        ScrapyBG = canvas.create_image(
            640.0, 155.5,
            image=ScrapyBGImage)

        #Scrapy Button Config
        ScrapitImage = PhotoImage(file = f"./images/Scrapy/Scrapit.png")
        ScrapItButton = Button(
            image = ScrapitImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            activebackground="#0B132B",
            command = btn_clicked,
            relief = "flat")

        ScrapItButton.place(
            x = 362, y = 557,
            width = 536,
            height = 100)

        #back button config
        BackImage = PhotoImage(file = f"./images/Scrapy/Back.png")
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

        #Input entry config
        InputEntryImage = PhotoImage(file = f"./images/Scrapy/TextBox.png")
        InputEntry = canvas.create_image(
            639.5, 391.5,
            image = InputEntryImage)

        InputEntry = Entry(
            bd = 0,
            bg = "#1c2541",
            font = 30,
            fg= "#5BC0BE",
            justify=CENTER,
            insertbackground= "#5BC0BE",
            highlightthickness = 0)

        InputEntry.place(
            x = 282, y = 360,
            width = 715,
            height = 61)

        window.resizable(False, False)
        window.mainloop()