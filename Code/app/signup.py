from tkinter import *
from tkinter.messagebox import showinfo
import mysql.connector
from app import login
from app.FUNCTIONALITY import inputValidation
from app.User import userDetails
from app.common import executeQuery
import os

def loadSignUp(window):
        # Button functions
    def toLoginPage():
        # call the loadlogin function to swap the frame to login screen
        login.loadLogIn(window)

    def SubmitDetails():
        # storing the values from the entry fields
        name = NameEntry.get()
        email = EmailEntry.get()
        phone = PhoneEntry.get()
        password = PasswordEntry.get()

    # condition = inputValidation.signupVal(name, email, phone, password)
    # if condition != True:
    #     showinfo('Error', condition['error'])
    # else:
        # creating a query and checking if there exist a account before signing up
        mydb = mysql.connector.connect(host=os.getenv('HOST'), user=os.getenv('USER'), password=os.getenv('PASSWORD'), database="forgepdf")
        mycursor = mydb.cursor()
        # getting all the user data from the database
        mycursor.execute("select name, password from users where name='" + name + "'")
        # selecting only the first row from the fetched data
        result = mycursor.fetchone()

        
            
        # creating a query to insert the user details into the database
        query = "insert into users (name, email, phone, password) values('" + name + "','" + email + "','" + phone + "','" + password + "')"
        executeQuery(query)

        # TODO: Display status message (success/failure)
        if result == None:
            showinfo('Successfull','You have successfully registered an account! Please login to continue!')
            
            userDetails.setUID('')
            # call the Home window class
            login.loadLogIn(window)

        elif result != None:
            showinfo("ERROR" , "A user with this name already exist, please choose a new one!")

        

    def btn_clicked():
        print("Button Clicked")


    signup_frame=Frame(window,width=1280,height=720,bg='#0b132b')
    signup_frame.place(x=0,y=0)
    # Creating a Canvas
    signup_canvas = Canvas(
        signup_frame,
        bg = "#0b132b",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    signup_canvas.place(x = 0, y = 0)

    # Adding the background
    background_img = PhotoImage(file = f"./images/signup/WindowBG.png")
    background_label = Label(image=background_img)
    background_label.image = background_img
    background = signup_canvas.create_image(
        640.0, 326.5,
        image=background_img)

        # Image for Sign up
    SignUpImage = PhotoImage(file = f"./images/signup/SignUp.png")
    SignUpLabel = Label(image=SignUpImage)
    SignUpLabel.image = SignUpImage
    # Sign up button config
    SignUpButton = Button(
        signup_canvas,
        image = SignUpImage,
        borderwidth = 0,
        highlightthickness = 0,
        background= "#1C2541",
        activebackground= "#1C2541",
        command = btn_clicked,
        relief = "flat")


    # Sign up button placement
    SignUpButton.place(
        x = 11, y = 19,
        width = 150,
        height = 65)


    # Image for Log In button
    LogInImage = PhotoImage(file = f"./images/signup/LogIn.png")
    LogInLabel = Label(image=LogInImage)
    LogInLabel.image = LogInImage
    # Log In button Configuration
    LogInButton = Button(
        signup_canvas,
        image = LogInImage,
        borderwidth = 0,
        highlightthickness = 0,
        background= "#1C2541",
        activebackground= "#1C2541",
        command = toLoginPage,
        relief = "flat")


    # Placement of LogIn button
    LogInButton.place(
        x = 162, y = 20,
        width = 125,
        height = 65)

    # Image for the Submit Button
    SubmitImage = PhotoImage(file = f"./images/signup/Submit.png")
    SubmitLabel = Label(image=SubmitImage)
    SubmitLabel.image = SubmitImage
    # Submit button Configuration
    SubmitButton = Button(
        signup_canvas,
        image = SubmitImage,
        borderwidth = 0,
        highlightthickness = 0,
        background= "#0b132b",
        activebackground= "#0b132b",
        command = SubmitDetails,
        relief = "flat")

    # Placement of submit button
    SubmitButton.place(
        x = 252, y = 614,
        width = 205,
        height = 55)

    # Image for User name input box
    NameBgImage = PhotoImage(file = f"./images/signup/NameBG.png")
    NameEntry = signup_canvas.create_image(
        454.0, 306.0,
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
        x = 251, y = 286,
        width = 406,
        height = 38)

    # Image for Email input box
    EmailBgImage = PhotoImage(file = f"./images/signup/EmailBG.png")
    EmailEntry = signup_canvas.create_image(
        454.0, 392.0,
        image = EmailBgImage)


    # Email Entry Configuration
    EmailEntry = Entry(
        bd = 0,
        bg = "#1c2541",
        font = 20,
        fg= "#5BC0BE",
        insertbackground= "#5BC0BE",
        highlightthickness = 0)


    # Email Entry placement
    EmailEntry.place(
        x = 251, y = 372,
        width = 406,
        height = 38)


    # Phone for User name input box 
    PhoneBgImage = PhotoImage(file = f"./images/signup/PhoneBG.png")
    PhoneEntry = signup_canvas.create_image(
        454.0, 475.5,
        image = PhoneBgImage)

    # Name Entry Configuration
    PhoneEntry = Entry(
        bd = 0,
        bg = "#1c2541",
        font = 20,
        fg= "#5BC0BE",
        insertbackground= "#5BC0BE",
        highlightthickness = 0)


    # Name Entry placement
    PhoneEntry.place(
        x = 251, y = 455,
        width = 406,
        height = 39)


    # Image for Password input box
    PasswordBgImage = PhotoImage(file = f"./images/signup/PasswordBG.png")
    PasswordEntry = signup_canvas.create_image(
        454.0, 551.0,
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
        x = 251, y = 531,
        width = 406,
        height = 38)
    
    signup_canvas.pack()

    # Additional window config
    # window.resizable(False, False)
    # window.mainloop()

    


