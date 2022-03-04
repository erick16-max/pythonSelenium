
from email import message
from selenium import webdriver
import time
import unittest
import HtmlTestRunner
from loginPage import Login
from homePage import Home

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # etting up the browser driver to use
        cls.driver = webdriver.Chrome(executable_path= "ChromeDrivers\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    
    def test_login_authentication(self):
        driver = self.driver
        # Getting the website url to test
        driver.get("https://opensource-demo.orangehrmlive.com/")

        #instance of the Login Class and its methods
        login = Login(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login_button()

        #instantition of Home class and its method 
        home = Home(driver)
        home.click_welcome()
        home.click_logout()

        #wait for 4 sec before browser quits to see results
        time.sleep(4)

    def test_login_invalid(self):
        driver = self.driver
        # Getting the website url to test
        driver.get("https://opensource-demo.orangehrmlive.com/")

        #instance of the Login Class and its methods
        login = Login(driver)
        login.enter_username("Admin")
        login.enter_password("admin1")
        login.click_login_button()

        message = driver.find_element_by_id("").text
        mssg = login.login_invalid()
        self.assertEqual(message, mssg)
       

        #wait for 4 sec before browser quits to see results
        time.sleep(4)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("ovaral test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Html_Reports"))
        






