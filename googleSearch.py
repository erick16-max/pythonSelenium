from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner

class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="ChromeDrivers\chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        
    

    def test_search_name_in_serachTextbox (self):
        self.driver.get("https://www.google.com/")
        search_box = self.driver.find_element_by_name('q')
        search_box.send_keys("erick gege")
        search_box.send_keys(Keys.RETURN)
    
    def test_search_tutorial_in_serachTextbox (self):
        self.driver.get("https://www.google.com/")
        search_box = self.driver.find_element_by_name('q')
        search_box.send_keys("Python programming")
        search_box.send_keys(Keys.RETURN)
    
    def tearDown(self):
        self.driver.implicitly_wait(10)
        self.driver.quit()
        print("test completed")

if __name__ == '__main__' :
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Html_Reports'))


        




