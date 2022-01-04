import re

# function to validate the inputs from the signup page
def signupVal(name, email, phone, password):
    count = 0
    # re for checking if the name is valid or not
    nameRe = re.compile(r'([a-z A-Z]{1,})(\s[a-z A-Z]{1,})*')
    # re for checking if the email is valid or not
    emailRe = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    # re for checking if the phone no. is valid or not
    phoneRe = re.compile(r'\d{10}')
    # re for checking if the password is valid or not
    passwordRe = re.compile(r'.{8,20}')
    # checking if the name doesnt contain numbers and is valid
    if len(nameRe.findall(name.strip()))>=1 and name.strip().isalpha() == True:
        count+=1           
    else:
        return {"error": "Please enter your name in the correct format"}
    # checking if the email is valid
    if len(emailRe.findall(email)) >= 1:
        count += 1
    else:
        return {"error": "Please enter your email in the correct format"}
    # checking if the phone no. valid
    if len(phoneRe.findall(phone)) >= 1:
        count += 1
    else:
        return {"error": "Please enter your phone number in the correct format"}
    # checking if the password is valid
    if len(passwordRe.findall(password)) >= 1:
        count += 1
    else:
        return {"error": "Please enter your password"}
    if count==4:
        return True
    else:
        return {"error": "Something went wrong"}


# function tto validate the input from send email page
def emailVal(toaddress):  
    # re to check if the to address is valid or not
    emailRe = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    # checking if the to address is valid or not
    if len(emailRe.findall(toaddress)) >= 1:
        return True
    else:
        return {"error": "Please enter your email in the correct format"}


#input validation for login
def loginVal(name, password):
    nameRe = re.compile(r'([a-z A-Z]{1,})(\s[a-z A-Z]{1,})*')
    passwordRe = re.compile(r'.{8,20}')
    loginCounter = 0
    if len(nameRe.findall(name.strip())) >= 1 and name.isdecimal() != True:
        loginCounter = loginCounter + 1
    else:
        return {"error": "Please enter your name in the correct format"}
    if len(passwordRe.findall(password)) >= 1:
        loginCounter = loginCounter + 1
    else:
        return {"error": "Please enter your password"}
    if loginCounter == 2:
        return True

# the input validations below will cause the program to go back to Home window

# input validation for scrappy
def scrappyVal(product_name):
    product_name = product_name.strip()
    productRe = re.compile(r'[A-Za-z0-9-]')
    productNameList = productRe.findall(product_name)
    numCounter = 0
    for name in productNameList:
        if name.isdecimal() == True:
            numCounter = numCounter + 1
        else:
            continue
    if numCounter == len(productNameList):
        return {"error": "Please enter a valid product name"}
    else:
        return True


# function to check whether the string given is containing only numbers
def splitVal(start, end):
    #if starting range is greater than endingrange
    if(start > start):
        return ("error" , "Starting range cannt be greater than ending range!!")
    if start.isdecimal()==False and end.isdecimal()==False:
        return {"error": "Please enter a valid range"}
    else:
        return True


# function for validating the inputs from encrypt pdf page
# validates the password field
def encryptVal(password):
    # if the password is empty
    if len(password) == 0:
        return {"error": "Please enter a valid password"}
    # if the password is less than 8 characters
    elif len(password) < 6:
        return {"error": "Please enter a password of atleast 6 characters"}
    else:
        return True

# function for validating the inputs from decrypt pdf page
# validates the password field
def decryptVal(password):
    # if the password is empty
    if len(password) == 0:
        return {"error": "Please enter a valid password"}
    # if the password is less than 8 characters
    elif len(password) < 6:
        return {"error": "Please enter a password of atleast 6 characters"}
    else:
        return True

# function for validating the inputs from extract pdf page
# validates the pdf_path which is the absolute path of the pdf file
def extractVal(pdf_path):
    # if the password is empty
    if len(pdf_path) == 0:
        return {"error": "Please input a valid pdf path"}
    else:
        return True