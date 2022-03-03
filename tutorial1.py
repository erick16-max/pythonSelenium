# Locating Html elements in a web app
from email.quoprimime import header_check
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"C:\src\SeleniumChromeDrivers"
driver = webdriver.Chrome()
driver.get("https://www.techwithtim.net/")
search = driver. find_element(by=By.NAME, value='s')
search.send_keys("test")
search.send_keys(Keys.RETURN)
#main = driver.find_element_by_id('main')
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_elements_by_tag_name('article')
    for article in articles:
        header = article.find_element_by_class_name('entry-summary')
        print(header.text)
        print("-----Next Article------------")
    
finally:
    driver.quit()



