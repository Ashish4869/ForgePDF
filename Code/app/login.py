from tkinter import *
from tkinter.messagebox import showinfo, WARNING
import mysql.connector
from app import signup
from app import home
from app.common import center

class LogInWindow():
    def __init__(self):
        # Button functions 
        def toSignUpPage():
            # Destroy the current window instance (LogInWindow)
            window.destroy()
            # Call the sign up window class
            signup.SignUpWindow()

        def SubmitDetails():
            # TODO: Implement input validation
            
            # storing the values from the entry fields
            name = NameEntry.get()
            pasword = PasswordEntry.get()
            # creating a mysql connection
            mydb = mysql.connector.connect(host="localhost", user="root", password="Ashishkishorekumar321", database="forgepdf")
            mycursor = mydb.cursor()
            # getting all the user data from the database
            mycursor.execute("select name, password from users where name='" + name + "'")
            # selecting only the first row from the fetched data
            result = mycursor.fetchone()

            # checking if the 'name' exists in the database
            if result == None:
                showinfo('Error', 'Name not found.', icon=WARNING)
            # checking if the 'password' matches the one in the database
            elif pasword != result[1]:
                showinfo('Error', 'Invalid Password!.', icon=WARNING)
            # else, successfull login
            else:
                showinfo('Successfull', 'You have successfully logged in!')
                 # destroy the current window instance (SignUpWindow)
                window.destroy()
                # call the Home window class
                home.HomeWindow()
            mydb.close()
        
        def btn_clicked():
            print("Button Clicked")

        # Window config
        window = Tk()
        window.geometry("1280x720")
        window.title('Log In Page')
        center(window)
        window.configure(bg = "#0b132b")

        # Creating a Canvas and setting its configuration
        canvas = Canvas(
            window,
            bg = "#0b132b",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        # Adding the background
        background_img = PhotoImage(file = "./images/login/WindowBG.png")
        background = canvas.create_image(
            640.0, 328.0,
            image=background_img)


        # Image for the Submit Button
        SubmitButtonImage = PhotoImage(file = f"./images/login/Submit.png")

        # Submit button Configuration
        SubmitButton = Button(
            image = SubmitButtonImage,
            borderwidth = 0,
            highlightthickness = 2,
            background= "#0b132b",
            activebackground= "#0b132b",
            command = SubmitDetails,
            relief = "flat")

        # Placement of submit button
        SubmitButton.place(
            x = 265, y = 557,
            width = 192,
            height = 58)

        # Image for Sign up
        SignUpButtonImage = PhotoImage(file = f"./images/login/SignUp.png")

        # Sign up button config
        SignUpButton = Button(
            image = SignUpButtonImage,
            borderwidth = 0,
            highlightthickness = 0,
            background= "#1c2541",
            activebackground= "#1c2541",
            command = toSignUpPage,
            relief = "flat")

        # Sign up button placement
        SignUpButton.place(
            x = 11, y = 20,
            width = 141,
            height = 65)

        # Image for Log In button
        LogInButtonImage = PhotoImage(file = f"./images/login/LogIn.png")

        # Log In button Configuration
        LogInButton = Button(
            image = LogInButtonImage,
            borderwidth = 0,
            highlightthickness = 0,
            background= "#1c2541",
            activebackground= "#1c2541",
            command = btn_clicked,
            relief = "flat")


        # Placement of LogIn button
        LogInButton.place(
            x = 168, y = 20,
            width = 113,
            height = 65)


        # Image for User name input box 
        NameBgImage = PhotoImage(file = f"./images/login/NameBG.png")
        NameBG = canvas.create_image(
            453.5, 378.0,
            image = NameBgImage)

        # Name Entry Configuration
        NameEntry = Entry(
            bd = 0,
            bg = "#1c2541",
            font = 20,
            fg= "#5BC0BE",
            insertbackground= "#5BC0BE",
            highlightthickness = 0)


        # Name Entry placement
        NameEntry.place(
            x = 263, y = 357,
            width = 381,
            height = 40)

        # Image for Password input box 
        PasswordBgImage = PhotoImage(file = f"./images/login/PasswordBG.png")
        PasswordBG = canvas.create_image(
            453.5, 483.0,
            image = PasswordBgImage)

        # Password Entry Configuration
        PasswordEntry = Entry(
            bd = 0,
            bg = "#1c2541",
            font = 20,
            fg= "#5BC0BE",
            insertbackground= "#5BC0BE",
            show="*",
            highlightthickness = 0)

        # Password Entry placement
        PasswordEntry.place(
            x = 263, y = 462,
            width = 381,
            height = 40)

        # Additional window config
        window.resizable(False, False)
        window.mainloop()
    
    
