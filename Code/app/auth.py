from tkinter import *
from app.login import loadLogIn
from app.common import center

class AuthWindow():
    def __init__(self):
        window = Tk()
        window.geometry("1280x720")
        window.title('Log In Page')
        center(window)
        window.configure(bg = "#0b132b")

        # Call the loadLogIn function to load the login screen
        loadLogIn(window)
        # Additional window config
        window.resizable(False, False)
        window.mainloop()
    
    
