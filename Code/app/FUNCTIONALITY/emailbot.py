from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def emailbot():#used to send email
    
    web = webdriver.Chrome()
    web.maximize_window()
    web.get('https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Faccounts.google.com%2Fb%2F0%2FAddMailService&followup=https%3A%2F%2Faccounts.google.com%2Fb%2F0%2FAddMailService&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    email=web.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
    email.send_keys('adpproject69420@gmail.com')
    web.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
    web.implicitly_wait(5)
    pwd=web.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
    pwd.send_keys('project@adp69420')
    web.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()
    web.implicitly_wait(50)
    web.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div').click()
    toadd=web.find_element_by_xpath('/html/body/div[23]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[1]/td[2]/div/div/textarea')
    toadd.send_keys('adpproject69420@gmail.com')
    web.implicitly_wait(15)
    subject=web.find_element_by_xpath('/html/body/div[23]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[3]/div/input')
    subject.send_keys('FORGEPDF')    
    attachment=web.find_element_by_xpath('/html/body/div[23]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[4]/div/input')
    attachment.send_keys('C:\\Users\\avina\\AppData\\Local\\Programs\\Python\\Python39\\textbook (2).pdf')
    web.find_element_by_xpath('/html/body/div[23]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]').click()  
    web.implicitly_wait(30)
    web.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[1]/div[4]/div[1]/div/div[3]/div/div/div[2]/span/span[2]/span[2]')
    web.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[1]/div[3]/header/div[2]/div[3]/div[1]/div[2]/div/a').click()
    web.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[1]/div[3]/header/div[2]/div[4]/div[4]/a').click()
emailbot()

