import requests, json

def getEmailValidate(email):
    try:
        response = requests.get('http://localhost:5000/emailvalidate?email='+email)
        emailData = json.loads(response.text)
    except:
        emailData = json.dumps({"error": "Could not connect to the server, please run the server first"})
        emailData = json.loads(emailData)
    return emailData
    
    