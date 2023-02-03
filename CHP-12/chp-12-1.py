import pyinputplus as pyip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

usr=input("Enter your username: ")
pws=pyip.inputPassword("Enter your password: ")
sem=input("Enter reciever's mail id")
sub=input("Type the subject")
body=input("Type the body of mail")

brw = webdriver.Firefox()
brw.get('https://outlook.office365.com')
time.sleep(5)
eml=brw.find_element_by_name('loginfmt')
eml.send_keys(usr)
next=brw.find_element_by_id('idSIButton9')
next.click()
time.sleep(3)
passw=brw.find_element_by_name('passwd')
passw.send_keys(pws)
sign=brw.find_element_by_id('idSIButton9')
sign.click()
time.sleep(10)
#text=brw.find_element_by_tag_name('div')
#text.send_keys('c')
#text.send_keys(Keys.TAB)
#text.send_keys(Keys.TAB)
# text.send_keys(Keys.TAB)

#text.send_keys(Keys.RETURN)