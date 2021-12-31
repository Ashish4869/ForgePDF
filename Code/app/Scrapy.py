from tkinter import *
from tkinter.messagebox import showinfo, WARNING
from app import login , home
from app.FUNCTIONALITY import scrapping
from app.common import center
import threading

class ScrapyWindow  ():
    def __init__(self):
        #Button Functions
        def toHomePage():
            # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the login up window class
            home.HomeWindow()

        def ScrapIt():
            #getting the input from the text box
            itemToScrap = InputEntry.get()
            
            #this doesnt work cause threads are messing things up
            #Checking if the input box in empty , if so prevent from scrapping
            # if itemToScrap.strip() == '':
            #     showinfo('Error' , 'Something went wrong')
            #     home.HomeWindow()
            #     window.destroy()

            #call the scrapping function and scrap the details
            scrapping.main(itemToScrap)

        def btn_clicked():
            print("ButtonClicked")

        #Shows the loading label when the button is pressed
        def showLoading():
            # ScrapItButton.pack_forget()
            ScrapItLoadingLabel.pack()
            ScrapItLoadingLabel.place(  
            x = 362, y = 557,
            width = 536,
            height = 100)
        
        #shows the done label 5 seconds after the button is pressed
        def showDone():
            # ScrapItLoadingButton.pack_forget()
            ScrapItDoneLabel.pack()
            ScrapItDoneLabel.place(  
            x = 362, y = 557,
            width = 536,
            height = 100)

            



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

            #creating 3 threads to run the scraping , and show the 2 labels at some fixed time
            command= lambda: [threading.Timer(0.1, ScrapIt).start(), threading.Timer(0.1, showLoading).start(), threading.Timer(5.0, showDone).start()],
            relief = "flat")

        ScrapItButton.place(
            x = 362, y = 557,
            width = 536,
            height = 100)


        

        #Loading Image Config
        ScrapItLoadingImage = PhotoImage(file = f"./images/Scrapy/LoadingImage.png")
        ScrapItLoadingLabel = Label(
            image = ScrapItLoadingImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            activebackground="#0B132B",
            relief = "flat")
   
        #packing the label and hiding it 
        ScrapItLoadingLabel.pack()
        ScrapItLoadingLabel.pack_forget()



        #Done Image Config
        ScrapItDoneImage = PhotoImage(file = f"./images/Scrapy/DoneImage.png")
        ScrapItDoneLabel = Label(
            image = ScrapItDoneImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            activebackground="#0B132B",
            relief = "flat")


        ScrapItDoneLabel.place(  
            x = 362, y = 557,
            width = 536,
            height = 100)
        
        #packing the label and hiding it 
        ScrapItDoneLabel.pack()
        ScrapItDoneLabel.pack_forget()



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
