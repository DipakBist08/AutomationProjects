import time
import os
from selenium import webdriver
driver=webdriver.Chrome()
PATH="C:\CHOME\AppData\Local\Programs\Python\ChromeDriver\chromedriver.exe"
driver.get("https://youtube.com")
print(driver.title)
driver.save_screenshot('seleniumss.png')
time.sleep(3)
driver.close()


