from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

os.environ['PATH'] += r"C:\src\SeleniumChromeDrivers"
driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Welcome" in driver.title
elem = driver.find_element(by=By.NAME, value='q')
elem.clear()
elem.send_keys("variables")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.quit()