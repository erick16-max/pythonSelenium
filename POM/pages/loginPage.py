from locators import Locators

class Login ():
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_id = Locators.login_button_id
        self.invalid_login_message_id = "spanMessage"

    def enter_username (self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password (self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login_button (self,):
        self.driver.find_element_by_id(self.login_button_id).click()
    
    def login_invalid(self):
        mssg = self.driver.find_element_by_id(self.invalid_login_message_id).text()
        return mssg
        