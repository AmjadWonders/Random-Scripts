# Done at 3/11/2019 8:43 PM. an updated version of the old one! This is going to be legendary!

# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException
import time
import sys

user = "thekingamjad" #enter your username right here
password = "if you know it, you get it." # your pass goes here
driver = webdriver.Chrome()
usr2change = "theksas" # and a user to start this turbo at
clicks = 0


driver.get("https://www.instagram.com/accounts/login")

time.sleep(2)

userfield = driver.find_elements_by_css_selector('form input')[0]
passwordfield = driver.find_elements_by_css_selector('form input')[1]

userfield.send_keys(user)
passwordfield.send_keys(password)
passwordfield.send_keys(Keys.ENTER)

time.sleep(3)

url = driver.current_url

if url == "https://www.instagram.com/":
    print("logged in successfully!")
else:
    print("There is a problem with your credientials, Try Hard!")
    sys.exit(1)

driver.get("https://www.instagram.com/accounts/edit/")

time.sleep(2)

userfield = driver.find_element_by_xpath('//*[@id="pepUsername"]')
enter = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/form/div[10]/div/div/button[1]')

userfield.clear()
userfield.send_keys(usr2change)

if userfield == usr2change:
    print("username entered !")
else:
    userfield.clear()
    userfield.send_keys(usr2change)
    print("username entered !")
    time.sleep(2)

while True:
    try:
        enter.click()
        clicks += 1
        print("ok, clicks:", clicks)
        time.sleep(1)
    except WebDriverException:
        print("Done!, username = ", usr2change)
        break
