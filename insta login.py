from selenium import webdriver
import time
class instagramBot():
 	"""docstring for instagramBot"""
 	def __init__(self, arg):
 		super(instagramBot, self).__init__()
 		self.arg = arg
 	    def __init__(self, username, password): 
    	self.opts = webdriver.ChromeOptions() 
    	self.opts.add_experimental_option("detach", True) 
    	self.driver  = webdriver.Chrome(options=self.opts)
    	self.username = scs_2005
    	self.password = shraddha
    	self.driver.get("https://instagram.com") 
    	time.sleep(2)
    	self.driver.find_element_by_xpath("//input[@name = 'username']").send_keys(self.username) 
    	self.driver.find_element_by_xpath("//input[@name = 'password']").send_keys(self.password) 
    	self.driver.find_element_by_xpath("//div[contains(text(), 'Log In')]").click() 
    	time.sleep(2) 
    	instagramBot('Sample Username','Sample Password') 