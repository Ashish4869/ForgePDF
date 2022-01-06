from tkinter import *
from tkinter.messagebox import showinfo, showwarning, showerror
from app import signup, home
import mysql.connector
from app.FUNCTIONALITY import inputValidation
from app.User import userDetails
import os

def loadLogIn(window):
     # Button functions 
    def toSignUpPage():
        # call the loadsignup function to swap the frame to signup screen
        signup.loadSignUp(window)

    def SubmitDetails(name, password):
        try:
            # storing the values from the entry fields
            condition = inputValidation.loginVal(name, password)
            if condition != True:
                showwarning('Error', condition['error'])
            else:
                # creating a mysql connection
                mydb = mysql.connector.connect(host=os.getenv('HOST'), user=os.getenv('USER'), password=os.getenv('PASSWORD'), database="forgepdf")
                mycursor = mydb.cursor()
                # getting all the user data from the database
                mycursor.execute("select name, password, user_id from users where name='" + name + "'")
                # selecting only the first row from the fetched data
                result = mycursor.fetchone()

                # checking if the 'name' exists in the database
                if result == None:
                    showwarning('Error', 'Name not found.')
                # checking if the 'password' matches the one in the database
                elif password != result[1]:
                    showwarning('Error', 'Invalid Password!.')
                # else, successfull login
                else:
                    showinfo('Successfull', 'You have successfully logged in!')
                        # destroy the current window instance (SignUpWindow)
                    
                    #Stores the UID in a py file
                    userDetails.setUID(result[2])
                    userDetails.setUsername(name)
                    # print(result)

                    window.destroy()
                    # call the Home window class
                    home.HomeWindow()
                mydb.close()
        except:
            showerror('Error', 'An error has occurred.')
    
    frame=Frame(window,width=1280,height=720,bg='#0b132b')
    frame.place(x=0,y=0)
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
    background_label = Label(image=background_img)
    background_label.image = background_img
    background = canvas.create_image(
        640.0, 328.0,
        image=background_img)


    # Image for the Submit Button
    SubmitButtonImage = PhotoImage(file = f"./images/login/Submit.png")
    SubmitLabel = Label(image=SubmitButtonImage)
    SubmitLabel.image = SubmitButtonImage
    # Submit button Configuration
    SubmitButton = Button(
        canvas,
        image=SubmitButtonImage,
        borderwidth = 0,
        highlightthickness = 2,
        background= "#0b132b",
        activebackground= "#0b132b",
        command = lambda: SubmitDetails(NameEntry.get(), PasswordEntry.get()),
        relief = "flat")
    

    # Placement of submit button
    SubmitButton.place(
        x = 265, y = 557,
        width = 192,
        height = 58)

    # Image for Sign up
    SignUpButtonImage = PhotoImage(file = f"./images/login/SignUp.png")
    SignUpLabel = Label(image=SignUpButtonImage)
    SignUpLabel.image = SignUpButtonImage
    # Sign up button config
    SignUpButton = Button(
        canvas,
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
    LogInLabel = Label(image=LogInButtonImage)
    LogInLabel.image = LogInButtonImage
    # Log In button Configuration
    LogInButton = Button(
        canvas,
        image = LogInButtonImage,
        borderwidth = 0,
        highlightthickness = 0,
        background= "#1c2541",
        activebackground= "#1c2541",
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
