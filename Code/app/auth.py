from tkinter import *
from tkinter.messagebox import showerror
from app.login import loadLogIn
from app.common import center
from app.FUNCTIONALITY import weatherapi

class AuthWindow():
    def __init__(self):
        window = Tk()
        window.geometry("1280x720")
        window.title('Auth Page')
        center(window)
        window.configure(bg = "#0b132b")

        # calling the weather api and storing the JSON object in tthe json file
        weatherapi.getWeatherData()

        # Call the loadLogIn function to load the login screen
        loadLogIn(window)
        # Additional window config
        window.resizable(False, False)
        window.mainloop()
