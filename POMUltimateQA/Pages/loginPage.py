from POMUltimateQA.Locators.locators import Locators


class LoginPage():

    def __init__(self, driver):  # constructor
        self.driver = driver

        self.email_textbox_id = Locators.email_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.sign_in_button_id = Locators.sign_in_button_id
        self.new_acc_linkText = Locators.new_acc_linkText
        self.forgot_password_linkText = Locators.forgot_password_linkText
        self.incorrect_credentials_classText = Locators.incorrect_credentials_classText
        # self.invalidUsername_message_id = "spanMessage"

    def enter_username(self, useremail):
        self.driver.find_element_by_id(self.email_textbox_id).clear()
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(useremail)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_sign_in(self):
        self.driver.find_element_by_id(self.sign_in_button_id).click()

    def click_new_acc_link(self):
        self.driver.find_element_by_classText(self.new_acc_linkText).click()

    def click_forgot_password_link(self):
        self.driver.find_element_by_linkText(self.forgot_password_linkText).click()


    def incorrect_credentials_message(self):
        self.driver.find_element_by_classText(self.incorrect_credentials_classText)





    # def check_invalid_username_message(self):
    #     msg = self.driver.find_element_by_id(self.invalidUsername_message_id).text
    #     return msg
