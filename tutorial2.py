from pathlib import Path
# Page Navigation and Clicking Elements

from selenium import webdriver
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


os.environ['PATH'] += r"C:\src\SeleniumChromeDrivers"
driver = webdriver.Chrome()
driver.get("https://www.techwithtim.net/")

link = driver.find_element_by_link_text("Python Programming")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Get Started"))
    )
    element.click()

    driver.back()
    driver.back()
    driver.back()

except:
    driver.quit()
