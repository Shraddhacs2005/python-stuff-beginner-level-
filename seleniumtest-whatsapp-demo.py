from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys 

import datetime

urlToUse = 'https://web.whatsapp.com/'
lastSeenElementXPath = '//span[contains(@class, "_3-cMa _3Whw5")]'
searchNameXPath = '//div[contains(@class, "_3FRCZ copyable-text selectable-text")]' 

friend_name = 'Vinton'

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
driver = webdriver.Chrome(options=options)
driver.get(urlToUse)

try:
	print("Scan the code to login.")
	x_arg = searchNameXPath
	input_box = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, x_arg))) 

finally:
	print("Yes. Logged In.")
	logInLoadTime = 7
	for k in range(logInLoadTime):
		time.sleep(1)
		print(str(logInLoadTime - k) + "s to start searching names.")

	input_box = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, x_arg))) 
	input_box = driver.find_elements_by_xpath(x_arg)[0]
	input_box.send_keys(friend_name) 
	time.sleep(2)
	input_box.send_keys(Keys.ENTER)

	lastseenX = lastSeenElementXPath
	time.sleep(1)
	try:
		lastXelement = driver.find_elements_by_xpath(lastseenX)[0]
		textinfo = lastXelement.text
	except:
		textinfo = 'Not found.'

	print(friend_name + " : " + textinfo)
#help credits : https://github.com/prajwalsouza

		
