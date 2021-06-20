# Done at 3/1/2019 11:12 PM. Now, this is pretty extreme. finally a use of a library like selenium. Not sure if its complete tho.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
browser = webdriver.Chrome()

browser.get('https://www.instagram.com/accounts/login/')

time.sleep(2)
emailInput = browser.find_elements_by_css_selector('form input')[0]
passwordInput = browser.find_elements_by_css_selector('form input')[1]

emailInput.send_keys("example")
passwordInput.send_keys("example")
passwordInput.send_keys(Keys.ENTER)
time.sleep(2)
browser.get("https://www.instagram.com/explore/")
time.sleep(2)

explore = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div[1]/div/div[1]/div[1]/a/div/div[2]')
explore.click()
browser.refresh()
while True:
	time.sleep(2)
	comment_input = browser.find_element_by_css_selector('form  textarea')
	comment_input.click()
	comment_input.send_keys("Hello World")
	comment_input.send_keys(Keys.ENTER)

	next0 = browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/a[2]').click()

	time.sleep(2)


