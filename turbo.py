# Done at 3/2/2019 12:50 AM. Finally, the use of comments with a good library. Bravo! to my old self.

# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import sys

#options = Options()
#options.add_argument("--headless") # Runs Chrome in headless mode.
#options.add_argument('--no-sandbox') # # Bypass OS security mode
#chromedriver_path = "/usr/local/bin/chromedriver"
#browser = webdriver.Chrome(chromedriver_path, chrome_options=options)


# variables
browser = webdriver.Chrome()
nmbr_clicks = 0
status = ""
user = input("Enter username: ")
password = input("Enter Password: ")
delay = 5
url = browser.current_url

# to get into a specific page
browser.get('https://www.instagram.com/accounts/login/')
print("Logging in!, please wait...")
time.sleep(2)

# fields to manipulate
emailInput = browser.find_elements_by_css_selector('form input')[0]
passwordInput = browser.find_elements_by_css_selector('form input')[1]

# Def 
def getstatus():
	pass

def runcheck():
	if userfield == usr2change:
		print("username entered !")
	else:
		userfield.clear()
		userfield.send_keys(usr2change)
		print("username entered !")
		time.sleep(3)

def login():
	emailInput.send_keys(user)
	passwordInput.send_keys(password)
	passwordInput.send_keys(Keys.ENTER)

login()

time.sleep(2)

if url == "https://www.instagram.com":
	print("Logged in!")
elif url == "https://www.instagram.com/accounts/login/?source=auth_switcher":
	print("Invaild user or password, please try again")


browser.get("https://www.instagram.com/accounts/edit/")

time.sleep(4)

# more fields to manipulate!
#try:
userfield = browser.find_element_by_xpath('//*[@id="pepUsername"]')
#enter = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/form/div[10]/div/div/button[1]')
print("successfully Logged in!")
#except:
#print("Invaild user or password, please try again")
#sys.exit(1)

usr2change = input("user to crawl: ")
userfield.clear()
userfield.send_keys(usr2change)
#enter = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/article/form/div[10]/div/div/button[1]')))
#enter = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/form/div[10]/div/div/button[1]')
runcheck()

# Loop to Start the Turbo!
while True:
	try:
		enter.click()
		nmbr_clicks += 1
		print("=> OK, Number of clicks: ", nmbr_clicks)
	except:
		if enter.is_displayed():
			print("==> Done!, USER =",usr2change)
			break
		else:
			print("an error have encountred, please try again later.")