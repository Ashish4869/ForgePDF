#Stores the current users id here
uid = []

#function to SET the UID of the user who logged in
def setUID(useruid):
    if len(uid) == 0:
        uid.append(useruid)
    else:
        uid[0] = useruid


#fucntion to get the UID of the user who is already logged in
def getUID():
    return uid[0]

