from selenium import webdriver
import random
import time

while True:

	driver = webdriver.Firefox()
	driver.get('http://www.porngifs.xyz/')

	driver.switch_to.window(driver.window_handles[1])
	driver.close()

	driver.switch_to.window(driver.window_handles[0])
	time.sleep(10)
	driver.close()