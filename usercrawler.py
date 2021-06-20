# done at 3/5/2019 9:41 PM. You will see alot of these. I think its due to the fact that I pretty much liked user crawling.

# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time
import sys

user = "thekingamjadll"
password = "if you know it, you get it"
driver = webdriver.Chrome()

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

user_input = input("Enter wanted username: ")
user_insta = ("https://www.instagram.com/" + user_input)

driver.get(user_insta)

followers_num = driver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(2) > a > span').text
followers_btn = driver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(2) > a')

followers_btn.click()


#WebDriverWait(driver,10).until(EC.visibility_of_any_elements_located((By.XPATH,'/html/body/div[2]/div/div[2]/ul/div/li[1]/div/div[1]/div[2]/div[1]/a')))
anelement = driver.find_elements_by_css_selector('body > div.RnEpo.Yx5HN > div > div.isgrP > ul > div > li:nth-child(1) > div > div.t2ksc > div.enpQJ > div.d7ByH > a')

print(anelement)
