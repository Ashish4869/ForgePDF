#Stores the current users id  and name here
uid = []
username = []

#function to SET the UID of the user who logged in
def setUID(useruid):
    if len(uid) == 0:
        uid.append(useruid)
    else:
        uid[0] = useruid


#fucntion to get the UID of the user who is already logged in
def getUID():
    return uid[0]



#function to SET the name of the user who logged in
def setUsername(userName):
    if len(username) == 0:
        username.append(userName)
    else:
        username[0] = userName


#function to get the UID of the user who is already logged in
def getUsername():
    return username[0]

