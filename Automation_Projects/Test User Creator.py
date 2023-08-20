# Test User create Code
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("https://testapp.pnpl.com.np/home")
time.sleep(5)
sign_in=driver.find_element()
