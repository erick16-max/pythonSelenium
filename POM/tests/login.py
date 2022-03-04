from cgi import print_directory
from selenium import webdriver
import time
import unittest

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # etting up the browser driver to use
        cls.driver = webdriver.Chrome(executable_path= "ChromeDrivers\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    
    def test_login_authentication(self):
        # Getting the website url to test
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        # Inputing values inside the form 
        username_textbox = self.driver.find_element_by_id("txtUsername")
        username_textbox.send_keys("Admin")

        password_textbox = self.driver.find_element_by_id("txtPassword")
        password_textbox.send_keys("admin123")

        #clicking the ligin button
        login_button = self.driver.find_element_by_id("btnLogin")
        login_button.click()

        #logging out of the web application
        self.driver.find_element_by_id("welcome").click()
        self.driver.find_element_by_link_text("Logout").click()

        #wait for 4 sec before browser quits to see results
        time.sleep(4)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")


if __name__ == '__main__':
    unittest.main()
        






