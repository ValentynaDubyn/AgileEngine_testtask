from POMUltimateQA.Locators.locators import Locators
class ForgotPasswordPage():

    class LoginPage():

        def __init__(self, driver):  # constructor
            self.driver = driver

            self.forgot_password_textbox_id = Locators.forgot_password_textbox_id
            self.submit_name = Locators.submit_nameText

        def enter_exist_email(self, existemail):
            self.driver.find_element_by_id(self.forgot_password_textbox_id).clear()
            self.driver.find_element_by_id(self.forgot_password_textbox_id).send_keys(existemail)

        def click_submit(self):
            self.driver.find_element_by_nameText(self.submit_name).click()

