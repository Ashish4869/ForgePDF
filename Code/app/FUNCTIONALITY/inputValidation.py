import re

def signupVal(name,email,phone,password):
    nameRe=re.compile(r'([a-z A-Z]{1,})(\s[a-z A-Z]{1,})*')
    emailRe=re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    phoneRe=re.compile(r'((\+*)((0[ -]*)*|((91 )*))((\d{12})+|(\d{10})+))|\d{5}([- ]*)\d{6}')
    passwordRe=re.compile(r'.{8,20}')
    if len(nameRe.findall(name.strip()))>=1 and name.isdecimal()!=True:
        print(name.isdecimal())
        print('Success')
    else: 
        print(name.isnum())
        print(len(nameRe.findall(name.strip())))
        print('Invalid Name!!!')
    print(nameRe.findall(name.strip()))

    if len(emailRe.findall(email))>=1:
        print('Success')
    else:
        print('Invalid Email!!!')

    if len(phoneRe.findall(phone))>=1:
        print('Success')
    else:
        print('Invalid Phone!!!')
    
    if len(passwordRe.findall(password))>=1:
        print('Success')
    else:
        print('Invalid Password!!!')
signupVal('Adithya K Shetty','4s019cc@sjec.ac.in','3242432422','asdfl213_$#22b ?')

def toaddrrValid(toaddress):
    emailRe=re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    
    if len(emailRe.findall(toaddress))>=1:
        print('Success')
    else:
        print('Invalid Email!!!')